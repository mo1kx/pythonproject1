#!/usr/bin/env python3
import argparse
import re
from datetime import date


def parse_version(v: str) -> tuple[int, int, int]:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", v.strip())
    if not m:
        raise ValueError("version.txt malformed")
    return tuple(map(int, m.groups()))  # type: ignore[return-value]


def format_version(t: tuple[int, int, int]) -> str:
    return f"{t[0]}.{t[1]}.{t[2]}"


def bump(kind: str, v: str) -> str:
    major, minor, patch = parse_version(v)
    if kind == "feature":
        minor += 1
        patch = 0
    elif kind == "hotfix":
        patch += 1
    else:
        raise ValueError("kind must be 'feature' or 'hotfix'")
    return format_version((major, minor, patch))


def update_changelog(new_version: str, branch: str, message: str) -> None:
    today = date.today().isoformat()
    header = f"## [{new_version}] - {today}\n"
    details = f"- {branch}: {message}\n"
    with open("CHANGELOG.md", "r", encoding="utf-8") as f:
        old = f.read()
    with open("CHANGELOG.md", "w", encoding="utf-8") as f:
        f.write("# Changelog\n\n")
        f.write(header)
        f.write(details)
        f.write("\n")
        f.write(old.split("\n", 1)[1] if "\n" in old else old)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("kind", choices=["feature", "hotfix"])
    p.add_argument("--branch", default="unknown")
    p.add_argument("--message", default="update")
    args = p.parse_args()

    with open("version.txt", "r", encoding="utf-8") as f:
        current = f.read().strip()
    new = bump(args.kind, current)
    with open("version.txt", "w", encoding="utf-8") as f:
        f.write(new + "\n")
    update_changelog(new, args.branch, args.message)
    print(new)


if __name__ == "__main__":
    main()

