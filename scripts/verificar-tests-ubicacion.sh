#!/usr/bin/env bash

set -e

echo "Verificando ubicación de tests..."

# Buscar tests fuera de la carpeta tests/
INVALID_TESTS=$(find src -type f -name "test_*.py" | grep -v "^tests/" || true)

if [ -n "$INVALID_TESTS" ]; then
  echo ""
  echo "ERROR: Se encontraron tests fuera de la carpeta tests/"
  echo ""
  echo "$INVALID_TESTS"
  echo ""
  echo "Regla del proyecto:"
  echo "Todos los tests deben estar dentro de tests/"
  echo "Ejemplo correcto: tests/test_algo.py"
  echo ""
  exit 1
fi

echo "Ubicación de tests correcta"