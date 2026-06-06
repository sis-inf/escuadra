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

---

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

---

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

---

# 4. Verificar instalación

Para comprobar que todo funciona correctamente, ejecutar:

```bash
pytest
```

Si la configuración es correcta, pytest ejecutará las pruebas del proyecto sin errores.

---

# Resultado esperado

Al finalizar todos los pasos:

- El entorno virtual estará configurado correctamente.
- Las dependencias del proyecto estarán instaladas.
- El proyecto podrá ejecutarse en modo de desarrollo.
- Las pruebas podrán ejecutarse usando pytest.

---

# Notas adicionales

Si ocurre algún problema con las dependencias, se recomienda:

- verificar la versión de Python instalada
- actualizar pip
- volver a crear el entorno virtual

Comando para actualizar pip:

```bash
python -m pip install --upgrade pip
```