import argparse
from pathlib import Path
from tasktagger.core import scan_file

def print_results(results, only_tag=None):
    if only_tag:
        results = [r for r in results if r[0].upper() == only_tag.upper()]

    if not results:
        print("No task tags found.")
        return

    print(f"Found {len(results)} task tag(s):\n")
    for tag, file, line, msg in results:
        print(f"[{tag}] {file}:{line} – {msg}")

def main():
    parser = argparse.ArgumentParser(
        description="Scan a single file for TODO, FIXME, or HACK-style tags."
    )
    parser.add_argument("path", type=str, help="Path to a file")
    parser.add_argument("--only", type=str, help="Only show a specific tag (e.g. TODO)")

    args = parser.parse_args()
    target_path = Path(args.path)

    if not target_path.exists():
        print(f"Path not found: {args.path}")
        return

    if not target_path.is_file():
        print("Directories are not supported yet.")
        return

    results = scan_file(target_path)
    print_results(results, only_tag=args.only)
