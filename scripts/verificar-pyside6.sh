#!/usr/bin/env bash

set -e

if grep -R --include="*.py" --exclude-dir=.git --exclude-dir=.venv --exclude-dir=venv "PyQt6" src tests; then
    echo ""
    echo "ERROR: Se encontraron imports de PyQt6."
    echo "Este proyecto utiliza PySide6. Reemplace PyQt6 por PySide6."
    exit 1
fi

echo "OK: No se encontraron imports de PyQt6."