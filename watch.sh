#!/usr/bin/env sh

if [ ! command -v pytest ]; then
  echo "`pytest` not found"
  exit 1
fi

while true; do
  find . -type f \
    -not -path './.git/*' \
    -not -path './.venv/*' \
    -not -path './.pytest_cache/*' \
    -not -path '*/__pycache__/*' \
  | entr -d -c pytest -q
done
