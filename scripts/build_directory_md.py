#!/usr/bin/env python3

import os
from collections.abc import Iterator
import logging
logger = logging.getLogger(__name__)


def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    logger.error(">>> Entering good_file_paths(top_dir=%s)", top_dir, extra={"event.action": "good_file_paths", "logrite.top_dir": top_dir})
    for dir_path, dir_names, filenames in os.walk(top_dir):
        dir_names[:] = [
            d
            for d in dir_names
            if d != "scripts" and d[0] not in "._" and "venv" not in d
        ]
        for filename in filenames:
            if filename == "__init__.py":
                continue
            if os.path.splitext(filename)[1] in (".py", ".ipynb"):
                yield os.path.join(dir_path, filename).lstrip("./")
                logger.warning("<<< Exiting good_file_paths(top_dir=%s)", top_dir, extra={"event.action": "good_file_paths", "logrite.top_dir": top_dir})


def md_prefix(indent: int) -> str:
    """
    Markdown prefix based on indent for bullet points

    >>> md_prefix(0)
    '\\n##'
    >>> md_prefix(1)
    '  *'
    >>> md_prefix(2)
    '    *'
    >>> md_prefix(3)
    '      *'
    """
    logger.error(">>> Entering md_prefix(indent=%s)", indent, extra={"event.action": "md_prefix", "logrite.indent": indent})
    logger.warning("<<< Exiting md_prefix(indent=%s)", indent, extra={"event.action": "md_prefix", "logrite.indent": indent})
    return f"{indent * '  '}*" if indent else "\n##"


def print_path(old_path: str, new_path: str) -> str:
    logger.error(">>> Entering print_path(old_path=%s,new_path=%s)", old_path, new_path, extra={"event.action": "print_path", "logrite.old_path": old_path, "logrite.new_path": new_path})
    old_parts = old_path.split(os.sep)
    logger.error("print_path(old_path=%s,new_path=%s): old_parts → %s", old_path, new_path, old_parts, extra={"event.action": "print_path", "logrite.old_path": old_path, "logrite.new_path": new_path})
    for i, new_part in enumerate(new_path.split(os.sep)):
        if (i + 1 > len(old_parts) or old_parts[i] != new_part) and new_part:
            print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")
    logger.warning("<<< Exiting print_path(old_path=%s,new_path=%s)", old_path, new_path, extra={"event.action": "print_path", "logrite.old_path": old_path, "logrite.new_path": new_path})
    return new_path


def print_directory_md(top_dir: str = ".") -> None:
    logger.error(">>> Entering print_directory_md(top_dir=%s)", top_dir, extra={"event.action": "print_directory_md", "logrite.top_dir": top_dir})
    old_path = ""
    logger.error("print_directory_md(top_dir=%s): old_path → %s", top_dir, old_path, extra={"event.action": "print_directory_md", "logrite.top_dir": top_dir})
    for filepath in sorted(good_file_paths(top_dir)):
        filepath, filename = os.path.split(filepath)
        if filepath != old_path:
            old_path = print_path(old_path, filepath)
        indent = (filepath.count(os.sep) + 1) if filepath else 0
        logger.error("print_directory_md(top_dir=%s): indent → %s", top_dir, indent, extra={"event.action": "print_directory_md", "logrite.top_dir": top_dir})
        url = f"{filepath}/{filename}".replace(" ", "%20")
        logger.error("print_directory_md(top_dir=%s): url → %s", top_dir, url, extra={"event.action": "print_directory_md", "logrite.top_dir": top_dir})
        filename = os.path.splitext(filename.replace("_", " ").title())[0]
        logger.error("print_directory_md(top_dir=%s): filename → %s", top_dir, filename, extra={"event.action": "print_directory_md", "logrite.top_dir": top_dir})
        print(f"{md_prefix(indent)} [{filename}]({url})")
        logger.warning("<<< Exiting print_directory_md(top_dir=%s)", top_dir, extra={"event.action": "print_directory_md", "logrite.top_dir": top_dir})


if __name__ == "__main__":
    print_directory_md(".")
