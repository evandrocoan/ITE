"""Build the early-loading Sublime package at the specified path."""

import os
import sys
import zipfile


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python build.py OUTPUT.sublime-package")
    directory = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile(sys.argv[1], "w", zipfile.ZIP_DEFLATED) as archive:
        for name in (".python-version", "ConsoleCapture.py"):
            archive.write(os.path.join(directory, name), name)


if __name__ == "__main__":
    main()
