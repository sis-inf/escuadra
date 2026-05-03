# Guía de Despliegue

## Prerrequisitos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

* Python 3.10 o superior
* pip (gestor de paquetes de Python)
* Git (opcional, para clonar el repositorio)

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
python main.py
```

La aplicación abrirá una interfaz gráfica (UI) donde el usuario podrá interactuar con las herramientas de cálculo.

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

# Ejecutar aplicación
python main.py
```

Nota: Al tratarse de una aplicación de escritorio, no requiere servidor web. La ejecución se realiza directamente en el entorno del usuario.

---

## Variables de entorno

| Variable   | Descripción                  | Ejemplo     |
| ---------- | ---------------------------- | ----------- |
| PYTHONPATH | Ruta de módulos del proyecto | ./src       |
| APP_ENV    | Entorno de ejecución         | development |

---

## Solución de problemas comunes

**Error: comando `pip` no reconocido**

* Verificar que Python esté instalado correctamente y agregado al PATH.

**Error: módulos no encontrados**

* Ejecutar nuevamente:

```bash
pip install -r requirements.txt
```

**La aplicación no inicia**

* Verificar que el archivo principal (`main.py`) exista.
* Revisar errores en consola.

**Problemas con entorno virtual**

* Asegurarse de que el entorno esté activado antes de instalar dependencias.

**Interfaz gráfica no se abre**

* Verificar que las librerías de UI (Tkinter o PySide) estén correctamente instaladas.
