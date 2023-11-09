package environment

import (
	"crypto/md5"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"os"

	"github.com/robocorp/robo/cli/config"
	"github.com/robocorp/robo/cli/config/conda"
	"github.com/robocorp/robo/cli/environment/cache"
	"github.com/robocorp/robo/cli/paths"
	"github.com/robocorp/robo/cli/rcc"
)

type Environment struct {
	Variables map[string]string
	Capabilities
}

func (e Environment) FindExecutable(name string) string {
	if pathvar, ok := e.Variables["PATH"]; ok {
		if f, err := paths.FindExecutable(name, pathvar); err == nil {
			return f
		}
	}

	return name
}

func (e Environment) ToSlice() []string {
	env := make([]string, 0)
	for k, v := range e.Variables {
		env = append(env, fmt.Sprintf("%v=%v", k, v))
	}
	return env
}

func TryCache(cfg config.Config) (Environment, bool) {
	condaYaml := conda.NewFromConfig(cfg)
	digest := digest(cfg.Dir, condaYaml)

	if entry, ok := cache.Get(digest); ok {
		return Environment{
			Variables:    merge(entry.Variables),
			Capabilities: Capabilities(entry.Capabilities),
		}, true
	} else {
		return Environment{}, false
	}
}

func Create(
	cfg config.Config,
	onProgress func(*rcc.Progress),
) (Environment, error) {
	condaPath := paths.CreateTempFile(cfg.Dir, ".conda-*.yaml")
	defer os.Remove(condaPath)

	condaYaml := conda.NewFromConfig(cfg)
	if err := condaYaml.SaveAs(condaPath, true); err != nil {
		return Environment{}, err
	}

	key := digest(cfg.Dir, condaYaml)
	space := fmt.Sprintf("robo-%v", key)

	vars, err := rcc.HolotreeVariables(condaPath, space, onProgress)
	if err != nil {
		return Environment{}, err
	}

	// Parse supported features from new environment
	env := Environment{Variables: merge(vars)}
	cap := probeCapabilities(env)
	env.Capabilities = cap

	// Cache ht variables result, not merged environment
	entry := cache.CacheEntry{}
	entry.Variables = vars
	entry.Capabilities.Tasks = cap.Tasks
	entry.Capabilities.Server = cap.Server

	if err := cache.Add(key, entry); err != nil {
		return env, err
	}

	return env, nil
}

func merge(holotree map[string]string) map[string]string {
	env := environ()

	delete(env, "PYTHONPATH")
	delete(env, "PYTHONHOME")
	delete(env, "PYTHONSTARTUP")
	delete(env, "PYTHONEXECUTABLE")

	for k, v := range holotree {
		env[k] = v
	}

	return env
}

func digest(projectPath string, condaYaml conda.CondaYaml) string {
	condaContent, err := json.Marshal(condaYaml)
	if err != nil {
		panic(err)
	}

	hash := md5.New()
	hash.Write([]byte(projectPath))
	hash.Write(condaContent)

	checksum := hex.EncodeToString(hash.Sum(nil))
	return checksum[:16]
}
