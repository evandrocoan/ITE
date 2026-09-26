"""Exercise retention without launching Sublime Text."""

import io
import json
import os
import runpy
import sys
import tempfile
import types
import unittest


class RotationTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_dir = os.path.join(self.temp_dir.name, "Data")
        user_dir = os.path.join(self.data_dir, "Packages", "User")
        os.makedirs(user_dir)
        with open(os.path.join(user_dir, "ConsoleCapture.json"), "w") as config:
            json.dump({"max_files": 3, "max_bytes": 200}, config)

        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.original_sublime = sys.modules.get("sublime")
        self.console_out = io.StringIO()
        self.console_err = io.StringIO()
        sys.stdout = self.console_out
        sys.stderr = self.console_err
        sublime = types.ModuleType("sublime")
        sublime.executable_path = lambda: os.path.join(self.temp_dir.name,
                                                        "sublime_text.exe")
        sys.modules["sublime"] = sublime
        self.plugin = None

    def tearDown(self):
        if self.plugin is not None:
            self.plugin["plugin_unloaded"]()
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
        if self.original_sublime is None:
            del sys.modules["sublime"]
        else:
            sys.modules["sublime"] = self.original_sublime
        self.temp_dir.cleanup()

    def load_plugin(self):
        path = os.path.join(os.path.dirname(__file__), "ConsoleCapture.py")
        self.plugin = runpy.run_path(path)

    def test_rotation_and_console_mirror(self):
        self.load_plugin()
        for number in range(20):
            print("entry {:02d}: {}".format(number, "x" * 45))
        print("stderr entry", file=sys.stderr)
        self.assertIn("entry 19", self.console_out.getvalue())
        self.assertIn("stderr entry", self.console_err.getvalue())

        log_path = os.path.join(self.data_dir, "Log", "ConsoleCapture.log")
        paths = [log_path, log_path + ".1", log_path + ".2"]
        self.assertTrue(all(os.path.isfile(path) for path in paths))
        self.assertFalse(os.path.exists(log_path + ".3"))
        with open(log_path, "r", encoding="utf-8") as current:
            self.assertIn("stderr entry", current.read())
        contents = []
        for path in paths:
            with open(path, "r", encoding="utf-8") as log:
                contents.append(log.read())
        self.assertNotIn("entry 00", "".join(contents))

        self.plugin["plugin_unloaded"]()
        self.plugin = None
        self.load_plugin()
        with open(log_path, "r", encoding="utf-8") as current:
            self.assertIn("ConsoleCapture started", current.read())
        self.assertFalse(os.path.exists(log_path + ".3"))


if __name__ == "__main__":
    unittest.main()
