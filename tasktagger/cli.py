import argparse
from pathlib import Path
from tasktagger.core import scan_file, scan_directory

def print_results(results, only_tag=None):
    if only_tag:
        results = [r for r in results if r[0].upper() == only_tag.upper()]

    if not results:
        print("No task tags found.")
        return

    print(f"Found {len(results)} task tag(s):\n")
    for tag, file, line, msg, due in results:
        due_str = f" (due: {due})" if due else ""
        print(f"[{tag}] {file}:{line} - {msg}{due_str}")

def scan_path(path: Path):
    if not path.exists():
        print(f"Path not found: {path}")
        return []
    
    if path.is_file():
        return scan_file(path)
    elif path.is_dir():
        return scan_directory(path)
    else:
        print("Invalid path.")
        return[]

def main_menu():
    print("Welcome to TaskTagger Interactive Mode\n")
    path_input = input ("Enter the path to the file to scan: ").strip()
    path = Path(path_input)

    only = input("Filter by tag (TODO/FIXME/HACK) or leave blank: ").strip()
    
    results = scan_path(path)
    
    print_results(results, only_tag=only if only else None)

def main():
    parser = argparse.ArgumentParser(description="Scan a single file for TODO, FIXME, or HACK tags.")
    parser.add_argument("path", nargs="?", help="Path to a file")
    parser.add_argument("--only", type=str, help="Only show a specific tag (e.g. TODO)")
    parser.add_argument("--menu", action="store_true", help="Launch interactive menu")

    args = parser.parse_args()

    if args.menu:
        main_menu()
        return
    
    if not args.path:
        print("You must provide a path or use --menu.")
        return
    
    target_path = Path(args.path)
    results = scan_path(target_path)
    print_results(results, only_tag=args.only)