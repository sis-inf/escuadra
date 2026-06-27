.DEFAULT_GOAL := help

PYTHON ?= python3
PIP ?= pip3

.PHONY: help install test lint format build run clean

help:
	@echo "Targets disponibles:"
	@echo "  install       Instalar el proyecto con dependencias de desarrollo"
	@echo "  test          Ejecutar la suite de pruebas"
	@echo "  lint          Ejecutar Ruff"
	@echo "  format        Formatear con Ruff"
	@echo "  build         Generar distribuciones del paquete"
	@echo "  run           Ejecutar la GUI localmente"
	@echo "  clean         Limpiar archivos temporales"

install:
	$(PIP) install -e ".[dev]"

test:
	$(PYTHON) -m pytest

lint:
	ruff check .

format:
	ruff format .

build:
	$(PYTHON) -m build

run:
	$(PYTHON) -m escuadra.app

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov
