#!/usr/bin/env bash

set -euo pipefail

if ! command -v git-cliff >/dev/null 2>&1; then
    echo "Error: git-cliff no está instalado."
    echo "Instálelo desde: https://git-cliff.org/"
    exit 1
fi

git-cliff --output CHANGELOG.md
echo "CHANGELOG.md generado correctamente."