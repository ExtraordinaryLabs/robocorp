package run

import (
	"fmt"
	"os"

	"github.com/robocorp/robo/cli/config"
	"github.com/robocorp/robo/cli/environment"
	"github.com/robocorp/robo/cli/tasks"
	"github.com/robocorp/robo/cli/ui"
)

var (
	bold = ui.DefaultStyles().Bold.Render
)

func RunTask(dir, name string) (tasks.Result, error) {
	cfg, err := config.FromPath(dir)
	if err != nil {
		return tasks.Result{}, err
	}

	env, err := environment.EnsureWithProgress(cfg)
	if err != nil {
		return tasks.Result{}, err
	}

	fmt.Println("")
	if name == "" {
		fmt.Println("Parsing tasks")
		name, err = selectTask(cfg, env)
		if err != nil {
			return tasks.Result{}, err
		}
	}

	if err := clearOutput(cfg); err != nil {
		return tasks.Result{}, err
	}

	fmt.Println("Running task: " + bold(name))
	return tasks.Run(cfg, env, name)
}

func clearOutput(cfg config.Config) error {
	if err := os.RemoveAll(cfg.OutputDir); err != nil {
		return err
	}
	if err := os.MkdirAll(cfg.OutputDir, 0o755); err != nil {
		return err
	}

	return nil
}
