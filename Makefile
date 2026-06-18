.DEFAULT_GOAL := help

help:
	@echo "Targets disponibles:"
	@echo "  install       Instalar dependencias"
	@echo "  test          Ejecutar pruebas"
	@echo "  test-cov      Ejecutar pruebas con cobertura"
	@echo "  lint          Ejecutar flake8"
	@echo "  format        Aplicar black e isort"
	@echo "  format-check  Verificar formato con black"
	@echo "  clean         Limpiar archivos temporales"

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

test-cov:
	pytest --cov=src/escuadra tests/

lint:
	flake8 src/ tests/

format:
	black src/ tests/
	isort src/ tests/

format-check:
	black --check src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov
	