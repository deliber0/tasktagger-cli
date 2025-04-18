from pathlib import Path
import re
from typing import List, Tuple

SUPPORTED_TAGS = ["TODO", "FIXME", "HACK"]

def scan_file(file_path: Path) -> List[Tuple[str, Path, int, str]]:
    """Scan a single file for TODO/FIXME/HACK-style tags."""
    results = []
    try:
        with file_path.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                for tag in SUPPORTED_TAGS:
                    if tag in line:
                        match = re.search(f"{tag}[:]?(.*)", line, re.IGNORECASE)
                        message = match.group(1).strip() if match else ""
                        results.append((tag, file_path, i, message))
    except (UnicodeDecodeError, PermissionError):
        pass  # Skip unreadable or binary files
    return results
