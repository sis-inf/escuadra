# Guía de Despliegue

Esta guía describe el proceso de instalación y ejecución de Escuadra en sistemas Windows, Linux y macOS. Incluye la configuración del entorno virtual, la instalación del proyecto mediante pip y la verificación del funcionamiento de la interfaz de línea de comandos (CLI).

---

# Prerrequisitos

Antes de instalar Escuadra, asegúrese de tener instalado:

* Python 3.10 o superior
* pip (incluido con Python)
* Git

> Escuadra requiere Python 3.10 o superior. Versiones anteriores no están soportadas.

Verificar las versiones instaladas:

```bash
python --version
pip --version
git --version
```

> En algunos sistemas Linux o macOS puede ser necesario utilizar `python3` en lugar de `python`.

---

# Obtener el código fuente

## Clonar el repositorio

Si desea utilizar Escuadra como usuario:

```bash
git clone https://github.com/sis-inf/escuadra.git
cd escuadra
```

Si trabaja mediante el flujo de contribución del proyecto, clone primero su fork personal:

```bash
git clone https://github.com/TU-USUARIO/escuadra.git
cd escuadra
```

Para más detalles sobre el flujo de contribución consulte:

```text
docs/guia-contribuidor-primeros-pasos.md
```

---

# Entorno virtual en Linux/macOS

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

---

# Entorno virtual en Windows

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar en PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activar en CMD:

```cmd
.venv\Scripts\activate
```

Cuando el entorno esté activo, la terminal mostrará un prefijo similar a:

```text
(.venv)
```

---

# Instalación con pip

Desde el directorio raíz del proyecto ejecutar:

```bash
pip install -e .
```

La opción `-e` (*editable*) instala el proyecto enlazándolo al código fuente local. Esto permite que los cambios realizados en el código se reflejen inmediatamente sin necesidad de reinstalar el paquete.

La instalación registra además el comando:

```bash
escuadra
```

definido en el archivo `pyproject.toml`.

---

# Dependencias de desarrollo (opcional)

Si va a contribuir al proyecto o ejecutar pruebas, instale también las dependencias de desarrollo:

```bash
pip install -e ".[dev]"
```

Estas dependencias incluyen herramientas para pruebas, validación de código y empaquetado.

---

# Verificar la instalación

Verificar que Escuadra esté disponible:

```bash
escuadra --help
```

Consultar la versión instalada:

```bash
escuadra --version
```

También es posible ejecutar la aplicación mediante:

```bash
python -m escuadra --help
```

Si la instalación fue exitosa, se mostrará la ayuda de la aplicación o la versión instalada.

---

# Ejecución

Mostrar la ayuda general:

```bash
escuadra --help
```

Ejecutar el paquete directamente:

```bash
python -m escuadra
```

---

# Desactivar el entorno virtual

Cuando finalice su sesión de trabajo:

```bash
deactivate
```

---

# Problemas comunes

## El comando `python` no es reconocido

Verifique que Python esté instalado correctamente y agregado al PATH del sistema.

## El comando `pip` no es reconocido

Reinstale Python asegurándose de habilitar la opción:

```text
Add Python to PATH
```

durante la instalación.

## El comando `escuadra` no funciona

Verifique que:

1. El entorno virtual esté activo.
2. La instalación se haya realizado correctamente.
3. Se haya ejecutado:

```bash
pip install -e .
```

## Error por dependencias faltantes

Reinstale las dependencias del proyecto:

```bash
pip install -e .
```

---

# Documentación relacionada

* README.md
* docs/guia-contribuidor-primeros-pasos.md
* docs/arquitectura.md
* pyproject.toml