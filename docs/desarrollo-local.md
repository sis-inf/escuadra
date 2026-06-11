# Desarrollo local

Esta guía explica cómo configurar el entorno de desarrollo local del proyecto para poder trabajar correctamente en nuevas funcionalidades, correcciones o documentación.

---

# Requisitos previos

Antes de comenzar, es recomendable tener instalado:

- Python 3
- pip
- Git

También se recomienda trabajar dentro de un entorno virtual para evitar conflictos entre dependencias de distintos proyectos.

---

# 1. Crear entorno virtual

Para crear el entorno virtual se utiliza el siguiente comando:

```bash
python -m venv venv
```

Este comando crea una carpeta llamada `venv` que contendrá todas las dependencias necesarias del proyecto.

# 2. Activar entorno virtual

Una vez creado el entorno virtual, es necesario activarlo.

## Linux / macOS

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

Cuando el entorno virtual está activo, normalmente aparecerá `(venv)` al inicio de la terminal.

# 3. Instalar dependencias del proyecto

## Instalar el proyecto en modo editable

```bash
pip install -e .
```

El modo editable permite realizar cambios en el proyecto sin necesidad de reinstalar el paquete después de cada modificación.

---

## Instalar dependencias de desarrollo

```bash
pip install -r requirements-dev.txt
```

Este archivo contiene herramientas necesarias para el desarrollo y pruebas del proyecto.

## Configurar pre-commit

Después de instalar las dependencias de desarrollo, es obligatorio configurar los hooks de **pre-commit**.

### Instalar los hooks

```bash
pre-commit install
```

Este comando registra los hooks configurados por el proyecto para que se ejecuten automáticamente antes de cada `git commit`.

Los hooks ayudan a detectar problemas de formato, calidad de código y configuración antes de que los cambios sean enviados al repositorio.

### Verificar que los hooks funcionan

```bash
pre-commit run --all-files
```

Este comando ejecuta todos los hooks sobre todos los archivos del proyecto y permite verificar que la configuración es correcta.

## ¿Qué hace cada hook?

Actualmente el proyecto tiene configurados los siguientes hooks:

### Ruff

Este hook ejecuta validaciones de calidad de código utilizando Ruff.

Detecta problemas como:

* Imports no utilizados
* Variables no utilizadas
* Problemas de estilo
* Errores comunes detectados por las reglas configuradas en el proyecto

La configuración actual utiliza la opción `--fix`, por lo que Ruff intentará corregir automáticamente algunos problemas cuando sea posible.

### Ruff Format

Este hook aplica automáticamente el formato definido por Ruff para mantener un estilo consistente en todo el proyecto.

Su objetivo es evitar diferencias de formato entre colaboradores y reducir cambios innecesarios en los Pull Requests.

### Check YAML

Este hook verifica que todos los archivos YAML del proyecto tengan una sintaxis válida.

Ayuda a detectar errores de:

* Indentación incorrecta
* Estructura inválida
* Errores de formato
* Configuraciones YAML mal definidas

Es especialmente útil para archivos como:

```text
.pre-commit-config.yaml
.github/workflows/*.yml
```

Si encuentra errores, el commit será rechazado hasta que el problema sea corregido.

# 4. Verificar instalación

Para comprobar que todo funciona correctamente, ejecutar:

```bash
pytest
```

Si la configuración es correcta, pytest ejecutará las pruebas del proyecto sin errores.

También es recomendable ejecutar:

```bash
pre-commit run --all-files
```

para verificar que todos los hooks funcionan correctamente.

## Resultado esperado

Al finalizar todos los pasos:

* El entorno virtual estará configurado correctamente.
* Las dependencias del proyecto estarán instaladas.
* El proyecto podrá ejecutarse en modo de desarrollo.
* Las pruebas podrán ejecutarse usando pytest.
* Los hooks de pre-commit estarán configurados y funcionando.

## Problemas comunes con pre-commit

### `pre-commit: command not found`

La herramienta no está instalada en el entorno actual.

Instálala mediante:

```bash
pip install pre-commit
```

Verifica posteriormente la instalación:

```bash
pre-commit --version
```

### Los hooks fallan al ejecutar `pre-commit run --all-files`

Lee cuidadosamente el mensaje mostrado en la terminal para identificar el problema.

En muchos casos basta con ejecutar:

```bash
ruff check . --fix
ruff format .
```

Después vuelve a ejecutar:

```bash
pre-commit run --all-files
```

hasta que todos los hooks finalicen correctamente.

### Ruff modifica archivos automáticamente

Es normal que el hook `ruff` corrija algunos archivos durante la ejecución.

Si esto ocurre:

```bash
git status
```

mostrará archivos modificados.

Simplemente vuelve a agregarlos:

```bash
git add .
git commit -m "mensaje del commit"
```

### Error en archivos YAML

Si el hook `check-yaml` falla, revisa:

* Indentación incorrecta
* Mezcla de espacios y tabulaciones
* Estructuras YAML incompletas
* Caracteres inválidos

Corrige el archivo indicado y vuelve a ejecutar:

```bash
pre-commit run --all-files
```

### Reinstalar los hooks

Si existe algún problema con la instalación, puedes reinstalarlos:

```bash
pre-commit uninstall
pre-commit install
```

Esto suele resolver problemas relacionados con configuraciones dañadas o cambios recientes en el proyecto.

# Notas adicionales

Si ocurre algún problema con las dependencias, se recomienda:

- Verificar la versión de Python instalada
- Actualizar pip
- Volver a crear el entorno virtual

Comando para actualizar pip:

```bash
python -m pip install --upgrade pip
```