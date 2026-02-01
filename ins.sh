#!/usr/bin/env bash
set -e

if command -v python3 >/dev/null 2>&1; then
    echo "Python 3 found"
else
    echo "Python 3 not found. Please install Python 3."
    exit 1
fi

if python3 -m pip --version >/dev/null 2>&1; then
    echo "pip found"
else
    echo "pip not found. Please install pip."
    exit 1
fi

if ! command -v fusermount3 >/dev/null 2>&1; then
    echo "FUSE3 not found. Please install it."
    exit 1
fi

echo "Environment check passed."
echo "You can now run: python3 main.py <arguments>"
