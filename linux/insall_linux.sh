#!/usr/bin/env bash
set -e

# ------------------------------
# Check FUSE3
# ------------------------------
command -v fusermount3 >/dev/null 2>&1 || { echo "FUSE3 not found. Please install fuse3."; exit 1; }

# ------------------------------
# Start Python-file
# ------------------------------
curl -L -o appimageInstaller \
https://github.com/yyyumeniku/HyPrism/releases/latest/download/appimageInstaller
chmod +x appimageInstaller
./appimageInstaller --yes

echo "Done! HyPrism should now run."
