import { PythonTraceback } from '~/treebuild/protocols';

export type FormatType = 'auto' | 'raw' | 'pretty';

export type ViewSettings = {
  columns: {
    duration: boolean;
    location: boolean;
  };
  theme: 'dark' | 'light';
  format: FormatType;
};

export enum StatusLevel {
  error = 3,
  warn = 2,
  info = 1,
  success = 0,
  unset = -1,
}

export enum Type {
  task = 1 << 0, // 1
  variable = 1 << 1, // 2
  method = 1 << 2, // 4
  exception = 1 << 3, // 8
  generator = 1 << 4, // 16
  untrackedGenerator = 1 << 5, // 32
  resumeYieldFrom = 1 << 6, // 64
  resumeYield = 1 << 7, // 128
  suspendYieldFrom = 1 << 8, // 256
  suspendYield = 1 << 9, // 512
  log = 1 << 10, // 1024
  threadDump = 1 << 11, // 2048
  processSnapshot = 1 << 12, // 4096

  unhandled = 1 << 13,
}

export enum ConsoleMessageKind {
  unset = 0,
  regular = 1 << 1, // 1
  stdout = 1 << 2, // 2
  stderr = 1 << 3, // 4
  important = 1 << 5, // 8
  task_name = 1 << 6, // 16
  error = 1 << 7, // 32
  traceback = 1 << 8, // 64
  processSnapshot = 1 << 9, // 128
}

export interface EntryBase {
  id: string;
  type: Type;
  entriesIndex: number;
}

export interface EntryWithLocationBase extends EntryBase {
  source: string;
  lineno: number;
}

export interface EntryTask extends EntryWithLocationBase {
  type: Type.task;
  name: string;
  libname: string;
  status: StatusLevel;
  startDeltaInSeconds: number | -1 | undefined;
  endDeltaInSeconds: number | -1 | undefined;
}

export interface EntryProcessSnapshot extends EntryBase {
  type: Type.processSnapshot;
  startDeltaInSeconds: number | -1 | undefined;
  endDeltaInSeconds: number | -1 | undefined;
}

export interface Argument {
  name: string;
  type: string;
  value: string;
}

export interface EntryMethodBase extends EntryWithLocationBase {
  name: string;
  libname: string;
  status: StatusLevel;
  startDeltaInSeconds: number | -1 | undefined;
  endDeltaInSeconds: number | -1 | undefined;
  arguments: Argument[] | undefined;
}

export interface EntryMethod extends EntryMethodBase {
  type: Type.method;
}

export interface EntryGenerator extends EntryMethodBase {
  type: Type.generator;
}

export interface EntryUntrackedGenerator extends EntryMethodBase {
  type: Type.untrackedGenerator;
}

export interface EntryResumeYield extends EntryMethodBase {
  type: Type.resumeYield;
}

export interface EntryResumeYieldFrom extends EntryMethodBase {
  type: Type.resumeYieldFrom;
}

export interface EntrySuspendYield extends EntryMethodBase {
  type: Type.suspendYield;
  value: string; // the yielded value
  varType: string;
}

export interface EntrySuspendYieldFrom extends EntryMethodBase {
  type: Type.suspendYieldFrom;
}

export interface EntryException extends EntryWithLocationBase {
  tb: PythonTraceback;
  excType: string;
  excMsg: string;
}

export interface EntryThreadDump extends EntryWithLocationBase {
  tb: PythonTraceback;
  threadName: string;
  threadDetails: string;
}

export interface EntryVariable extends EntryWithLocationBase {
  type: Type.variable;
  name: string;
  value: string;
  varType: string;
}

export interface EntryLog extends EntryWithLocationBase {
  type: Type.log;
  status: StatusLevel;
  isHtml: boolean;
  message: string;
}

export type Entry =
  | EntryTask
  | EntryMethod
  | EntryVariable
  | EntryLog
  | EntryException
  | EntryGenerator
  | EntryResumeYield
  | EntryResumeYieldFrom
  | EntrySuspendYield
  | EntrySuspendYieldFrom
  | EntryUntrackedGenerator
  | EntryThreadDump
  | EntryProcessSnapshot;
