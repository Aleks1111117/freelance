#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    if sys.argv[1] == "test":
        print("NOTE: Running black formation:")
        print(os.popen(f"black --config {Path(__file__).resolve().parent.parent}/.black.toml .").read())
        print(os.popen("isort .").read())


if __name__ == "__main__":
    main()
