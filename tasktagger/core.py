from pathlib import Path
import re
from typing import List, Tuple, Optional

SUPPORTED_TAGS = ["TODO", "FIXME", "HACK"]

def scan_file(file_path: Path) -> List[Tuple[str, Path, int, str, Optional[str]]]:
    """Scan a single file for TODO/FIXME/HACK-style tags, with optional due dates."""
    results = []
    tag_pattern = re.compile(r"(TODO|FIXME|HACK)(?:\(due:\s*(.*?)\))?:?(.*)")

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                match = tag_pattern.search(line)
                if match:
                    tag, due, message = match.groups()
                    results.append((tag.upper(), file_path, i, message.strip(), due))                    
    except (UnicodeDecodeError, PermissionError):
        pass  # Skip unreadable or binary file
    return results

def scan_directory(path: Path) -> List[Tuple[str, Path, int, str, Optional[str]]]:
    """"Recursively scan a directory for task tags in supported file types."""
    results = []
    supported_exts = [".py", ".js", ".ts", ".sh", ".c", ".cpp", ".java", ".rb"]

    for file in path.rglob("*"):
        if file.is_file() and file.suffix.lower() in supported_exts:
            results.extend(scan_file(file))

    return results