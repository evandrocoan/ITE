#!/usr/bin/env python3

import configparser
from pathlib import Path
import subprocess
import sys
from typing import List, Optional


SCRIPT_DIRECTORY = Path(__file__).resolve().parent


def find_project_root() -> Path:
    """Find .gitmodules in the current, script, or a parent directory."""
    directories = (
        Path.cwd().resolve(),
        *Path.cwd().resolve().parents,
        SCRIPT_DIRECTORY,
        *SCRIPT_DIRECTORY.parents,
    )

    for directory in dict.fromkeys(directories):
        if (directory / ".gitmodules").is_file():
            return directory

    raise SystemExit(
        "ERROR: .gitmodules was not found in the current directory, "
        "the script directory, or any parent directory."
    )


ROOT = find_project_root()

TEXT_TO_FIND = """\
    > [!WARNING]
    > Placing this custom channel before the default channel changes Package Control's resolution globally. Packages from this channel with the same name will override versions from the default channel.
    >
    > You can review the channel contents here:
    > https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
"""

TEXT_TO_REPLACE = """\
    > [!WARNING]
    > Placing this custom channel before the default channel changes Package Control's resolution globally.
    > Packages from this channel with the same name will override versions from the default channel.
    >
    > You can review the channel contents here:
    > https://raw.githubusercontent.com/evandrocoan/StudioChannel/master/channel.json
"""

WARNING_SIGNATURE = (
"""\
Placing this custom channel before the default channel changes Package Control's resolution globally. Packages from
"""
)

COMMIT_SUBJECT = (
"""\
Fix README.md line wrap"
"""
)

COMMIT_BODY = (
"""\
"""
)


def read_submodule_paths() -> List[str]:
    """Read paths safely, including submodule names and paths with spaces."""
    config = configparser.ConfigParser(interpolation=None)
    config.read(ROOT / ".gitmodules", encoding="utf-8")

    paths = []
    for section in config.sections():
        if section.startswith('submodule "') and config.has_option(section, "path"):
            path = config.get(section, "path").strip()

            # ConfigParser preserves quotes around values such as
            # path = "Packages/C#". They delimit the Git configuration value
            # and are not part of the directory name.
            if len(path) >= 2 and path[0] == path[-1] and path[0] in ('"', "'"):
                path = path[1:-1]

            paths.append(path)
    return paths


def print_process_output(result: subprocess.CompletedProcess) -> None:
    if result.stdout:
        print("----- stdout -----")
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print("----- stderr -----", file=sys.stderr)
        print(result.stderr, end="" if result.stderr.endswith("\n") else "\n", file=sys.stderr)


def print_command(command: List[str]) -> None:
    print(f"\n$ {subprocess.list2cmdline(command)}")
    sys.stdout.flush()


def has_readme_changes(repository: Path) -> Optional[bool]:
    command = [
        "git",
        "-C",
        str(repository),
        "status",
        "--porcelain",
        "--",
        "README.md",
    ]
    print_command(command)
    result = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # This command is captured so the script can inspect its output, but both
    # streams are still printed completely.
    print_process_output(result)

    if result.returncode != 0:
        print(
            f"ERROR: command failed with exit status {result.returncode}: "
            f"{subprocess.list2cmdline(command)}",
            file=sys.stderr,
        )
        return None

    return bool(result.stdout.strip())


def commit_readme(repository: Path, relative_path: str) -> bool:
    command = [
        "git",
        "-C",
        str(repository),
        "commit",
        "--only",
        "-m",
        COMMIT_SUBJECT,
        "-m",
        COMMIT_BODY,
        "--",
        "README.md",
    ]

    print(f"\nCommit for {relative_path}:")
    print_command(command)

    # Do not capture either stream: Git prints its complete stdout and stderr
    # directly in the terminal.
    result = subprocess.run(command, text=True)
    if result.returncode != 0:
        print(
            f"ERROR: git commit failed in {relative_path} with exit status "
            f"{result.returncode}. README.md was left modified so you can "
            "inspect it and retry.",
            file=sys.stderr,
        )
        return False

    return True


def main() -> int:
    modules = read_submodule_paths()
    print(f"Project root: {ROOT}")
    print(f"Submodules found: {len(modules)}")

    committed = 0
    failures = 0

    for relative_path in modules:
        repository = ROOT / relative_path
        readme = repository / "README.md"

        if not readme.is_file():
            print(f"SKIP: {relative_path}/README.md does not exist")
            continue

        text = readme.read_text(encoding="utf-8")

        if WARNING_SIGNATURE not in text:
            if TEXT_TO_FIND not in text:
                print(f"SKIP: text not found in {relative_path}/README.md")
                continue

            updated_text = text.replace(TEXT_TO_FIND, TEXT_TO_REPLACE, 1)
            readme.write_text(updated_text, encoding="utf-8")
            print(f"UPDATED: {relative_path}/README.md")
        else:
            print(f"INFO: {relative_path}/README.md already has the warning")

        changed = has_readme_changes(repository)
        if changed is None:
            failures += 1
            continue
        if not changed:
            print(f"SKIP: {relative_path}/README.md has nothing to commit")
            continue

        if commit_readme(repository, relative_path):
            committed += 1
            print(f"COMMITTED: {relative_path}/README.md")
        else:
            failures += 1

    print(f"\nFinished: {committed} commit(s), {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
