"""Capture Sublime plugin output in a small set of rotating log files.

This package installs its stream wrappers at import time so it can capture
errors from packages loaded later in the same Python plugin host.
"""

import json
import os
import sys
import threading
from datetime import datetime

import sublime


DEFAULT_MAX_FILES = 5
DEFAULT_MAX_BYTES = 2 * 1024 * 1024
_stdout = None
_stderr = None


def _positive_int(value, default):
    if isinstance(value, bool):
        return default
    try:
        value = int(value)
    except (TypeError, ValueError):
        return default
    return value if value > 0 else default


def _configuration(data_dir):
    path = os.path.join(data_dir, "Packages", "User", "ConsoleCapture.json")
    try:
        with open(path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
    except (OSError, ValueError):
        config = {}
    if not isinstance(config, dict):
        config = {}
    return (
        min(_positive_int(config.get("max_files"), DEFAULT_MAX_FILES), 100),
        _positive_int(config.get("max_bytes"), DEFAULT_MAX_BYTES),
    )


class _RotatingLog:
    def __init__(self, path, max_files, max_bytes):
        self.path = path
        self.max_files = max_files
        self.max_bytes = max_bytes
        self.lock = threading.RLock()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self._remove_excess_backups()
        if os.path.isfile(path) and os.path.getsize(path):
            self._rotate()
        self.write("[ConsoleCapture started {} | pid {} | files {} | bytes {}]\n".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            os.getpid(), max_files, max_bytes))

    def _backup_path(self, number):
        return "{}.{}".format(self.path, number)

    def _remove_excess_backups(self):
        directory = os.path.dirname(self.path)
        prefix = os.path.basename(self.path) + "."
        for name in os.listdir(directory):
            if name.startswith(prefix) and name[len(prefix):].isdigit():
                if int(name[len(prefix):]) >= self.max_files:
                    try:
                        os.remove(os.path.join(directory, name))
                    except OSError:
                        pass

    def _rotate(self):
        if self.max_files == 1:
            if os.path.exists(self.path):
                os.remove(self.path)
            return
        for number in range(self.max_files - 1, 0, -1):
            source = self.path if number == 1 else self._backup_path(number - 1)
            if os.path.exists(source):
                os.replace(source, self._backup_path(number))

    def write(self, message):
        if not message:
            return
        data = message.encode("utf-8", "replace")
        with self.lock:
            try:
                size = os.path.getsize(self.path) if os.path.exists(self.path) else 0
                if size and size + len(data) > self.max_bytes:
                    self._rotate()
                with open(self.path, "ab") as log:
                    log.write(data)
            except OSError:
                # File logging must never stop plugins or their console output.
                pass


class _Tee:
    def __init__(self, original, log):
        self.original = original
        self.log = log

    def write(self, message):
        try:
            return self.original.write(message)
        finally:
            self.log.write(message)

    def flush(self):
        self.original.flush()

    def __getattr__(self, name):
        return getattr(self.original, name)


def _install():
    global _stdout, _stderr
    if _stdout is not None:
        return
    data_dir = os.path.join(os.path.dirname(sublime.executable_path()), "Data")
    max_files, max_bytes = _configuration(data_dir)
    try:
        log = _RotatingLog(os.path.join(data_dir, "Log", "ConsoleCapture.log"),
                           max_files, max_bytes)
    except OSError:
        return
    _stdout, _stderr = sys.stdout, sys.stderr
    sys.stdout = _Tee(_stdout, log)
    sys.stderr = _Tee(_stderr, log)
    print("[ConsoleCapture] capturing Python plugin output")


def plugin_unloaded():
    global _stdout, _stderr
    if isinstance(sys.stdout, _Tee) and sys.stdout.original is _stdout:
        sys.stdout = _stdout
    if isinstance(sys.stderr, _Tee) and sys.stderr.original is _stderr:
        sys.stderr = _stderr
    _stdout = _stderr = None


_install()
