# Guía de instalación de la suite Escuadra

## Requisitos previos

Antes de instalar la suite Escuadra, asegúrate de tener instalado lo siguiente:

- **Sistema operativo:** Linux (Ubuntu/Debian recomendado), macOS o Windows (con WSL2)
- **Python:** Versión 3.10 o superior
- **pip:** Versión 22 o superior
- **Git:** Para clonar el repositorio
- **make** (opcional): Para usar los atajos del Makefile

### Verificar versiones instaladas

```bash
python --version   # debe ser v3.10 o superior
pip --version      # debe ser v22 o superior
git --version      # debe estar instalado
```

### Actualizar pip (recomendado)

```bash
python -m pip install --upgrade pip
```

---

## Instalación rápida (usuarios)

Si solo quieres usar Escuadra como librería en tu propio proyecto:

```bash
# Opción 1: instalar desde PyPI (cuando esté publicado)
pip install escuadra

# Opción 2: instalar desde el repositorio
pip install git+https://github.com/sis-inf/escuadra.git
```

Verifica la instalación:

```bash
python -c "import escuadra; print(escuadra.__version__)"
```

---

## Instalación de desarrollo (colaboradores)

Si planeas contribuir al proyecto, clona el repositorio y configura un entorno aislado.

### 1. Haz un fork y clona tu fork

```bash
# Reemplaza TU-USUARIO por tu nombre de usuario de GitHub
git clone https://github.com/TU-USUARIO/escuadra.git
cd escuadra
git remote add upstream https://github.com/sis-inf/escuadra.git
```

### 2. Crea un entorno virtual

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instala el proyecto en modo editable con dependencias de desarrollo

```bash
pip install -e ".[dev]"
```

Esto instala:

- El paquete `escuadra` apuntando a tu clon local
- Dependencias de desarrollo: `pytest`, `pytest-cov`, `ruff`, `mypy`, `pre-commit`, etc.

### 4. Configura los hooks de pre-commit

```bash
pre-commit install
```

Los hooks se ejecutarán automáticamente en cada `git commit` para verificar formato, linting y otros chequeos.

### 5. Sincroniza con upstream periódicamente

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## Verificación de la instalación

Después de instalar, ejecuta las pruebas para confirmar que todo funciona:

```bash
# Ejecutar toda la suite de tests
pytest

# Con cobertura
pytest --cov=escuadra --cov-report=term-missing

# Solo tests rápidos (excluir lentos)
pytest -m "not slow"
```

Salida esperada si todo va bien:

```
===================== test session starts =====================
collected 42 items

tests/test_unit.py ..........                              [ 23%]
tests/test_integration.py ...........                     [ 50%]
tests/test_cli.py ..............                           [ 83%]
tests/test_matematicas.py .......                          [100%]

===================== 42 passed in 2.34s =====================
```

### Verificación manual rápida

```python
from escuadra.modulos.matematicas.estadisticas import media

assert media([1, 2, 3, 4, 5]) == 3.0
print("Escuadra funciona correctamente")
```

---

## Solución de problemas

### Error: `ModuleNotFoundError: No module named 'escuadra'`

Asegúrate de haber activado el entorno virtual y de haber ejecutado `pip install -e ".[dev]"`.

### Error: `pip install` falla por permisos

Usa un entorno virtual (ver paso 2) o instala en modo usuario:

```bash
pip install --user escuadra
```

### Error: `pre-commit` no encontrado

Instálalo manualmente:

```bash
pip install pre-commit
pre-commit install
```

### Windows: problemas con scripts `.ps1`

Si PowerShell bloquea la activación del entorno:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## Próximos pasos

- Lee la [guía de contribución](CONTRIBUTING.md) para saber cómo enviar tu primer PR.
- Revisa el [README](../README.md) para ver ejemplos de uso.
- Ejecuta `pytest --cov` para ver el estado actual de la cobertura de tests.

¿Encontraste un error en esta guía? [Abre un issue](https://github.com/sis-inf/escuadra/issues/new).
