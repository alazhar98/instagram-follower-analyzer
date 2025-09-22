#!/bin/sh
set -e

# Package the Pro distribution into a zip
OUT=instagram-follower-analyzer-pro.zip
rm -f "$OUT"

zip -r "$OUT" \
  instagram_follower_analyzer.py \
  license_config.py \
  COMMERCIAL_EULA.md \
  README.md \
  requirements.txt \
  connections/followers_and_following/followers_1.html \
  connections/followers_and_following/following.html \
  -x "venv/*" \
  -x ".git/*" \
  -x "*.pyc" \
  -x "__pycache__/*" \
  -x ".env*" \
  -x "LICENSE_KEY.txt"

echo "Packaged $OUT"


