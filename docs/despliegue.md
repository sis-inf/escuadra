# Guía de Despliegue

## Prerrequisitos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

* Python 3.10 o superior
* pip (gestor de paquetes de Python)
* Git (opcional, para clonar el repositorio)

---

## Instalación con pip y Entorno Virtual

Siga estos pasos para instalar el proyecto utilizando `pip` y configurar un entorno virtual.

### 1. Clonar el repositorio

```bash
git clone https://github.com/sis-inf/escuadra.git
cd escuadra
```

### 2. Crear y activar el entorno virtual

**En Linux/macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

**En Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar el proyecto

Ejecute el siguiente comando desde el directorio del fork clonado para instalar el paquete en modo editable:

```bash
pip install -e .
```

### 4. Verificar la instalación

Compruebe que la instalación fue exitosa ejecutando:

```bash
escuadra --version
# o
escuadra --help
```

### 5. Desactivar el entorno virtual

Cuando haya terminado de trabajar, desactive el entorno virtual con:

```bash
deactivate
```

---

## Entornos

### Local

```bash
# Clonar el repositorio
git clone https://github.com/sis-inf/escuadra.git
cd escuadra

# (Opcional) Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
# o alternativamente:
flask run
```

La aplicación se ejecutará por defecto en:

```
http://localhost:5000
```

---

### Producción

```bash
# Clonar repositorio
git clone https://github.com/sis-inf/escuadra.git
cd escuadra

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
export FLASK_APP=app.py
export FLASK_ENV=production

# Ejecutar servidor
flask run --host=0.0.0.0 --port=5000
```

Nota: Para entornos productivos reales se recomienda usar servidores como gunicorn o uWSGI junto a un proxy como Nginx.

---

## Variables de entorno

| Variable  | Descripción                                 | Ejemplo     |
| --------- | ------------------------------------------- | ----------- |
| FLASK_APP | Archivo principal de la aplicación Flask    | app.py      |
| FLASK_ENV | Modo de ejecución (desarrollo o producción) | development |
| PORT      | Puerto en el que se ejecuta la aplicación   | 5000        |

---

## Solución de problemas comunes

**Error: comando `pip` no reconocido**

* Verificar que Python esté correctamente instalado y agregado al PATH.

**Error: módulos no encontrados**

* Ejecutar nuevamente:

```bash
pip install -r requirements.txt
```

**El servidor no inicia**

* Verificar que el archivo principal (`app.py`) exista.
* Revisar errores en consola.

**Puerto en uso**

* Cambiar el puerto:

```bash
flask run --port=5001
```

**Problemas con entorno virtual**

* Asegurarse de que esté activado antes de instalar dependencias.