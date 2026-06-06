# Estructura del Código Fuente - Escuadra

Esta carpeta contiene el núcleo del sistema de cálculo de ingeniería en Python. El módulo `escuadra` está diseñado para ser modular, mantenible y fácil de extender, siguiendo las mejores prácticas de desarrollo de software.

## Estructura de Directorios

A continuación se presenta el árbol de directorios completo de `src/escuadra/`:

```text
escuadra/
├── __main__.py
├── cli.py
├── core/
│   ├── __init__.py
│   └── engine.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── io/
│   ├── __init__.py
│   ├── reader.py
│   └── writer.py
├── math/
│   ├── __init__.py
│   ├── geometry.py
│   └── calculus.py
├── modulos/
│   ├── __init__.py
│   └── calculo_estructural.py
├── ui/
│   ├── __init__.py
│   └── dashboard.py
└── utils/
    ├── __init__.py
    └── helpers.py
```

## Descripción de Subdirectorios

- **core/**: Contiene la lógica central del motor de cálculo. Aquí se implementan las clases principales que orquestan los procesos de ingeniería y gestionan el flujo de datos entre los diferentes módulos.
- **config/**: Alberga la configuración del sistema, incluyendo parámetros por defecto, rutas de archivos y ajustes de entorno. Permite personalizar el comportamiento de la aplicación sin modificar el código fuente.
- **io/**: Gestiona todas las operaciones de entrada y salida. Incluye funciones para leer archivos de entrada (como datos de carga o geometrías) y escribir resultados en formatos estándar (CSV, JSON, reportes).
- **math/**: Implementa las funciones matemáticas y algoritmos específicos de ingeniería, como cálculos geométricos, integración numérica y resolución de sistemas de ecuaciones.
- **modulos/**: Contiene módulos especializados para diferentes tipos de análisis estructural o mecánico. Cada módulo puede activarse o desactivarse según las necesidades del proyecto.
- **ui/**: Proporciona la interfaz de usuario, ya sea basada en consola o gráfica. Gestiona la interacción con el usuario, la visualización de resultados y la navegación por las opciones disponibles.
- **utils/**: Ofrece herramientas auxiliares y funciones de utilidad reutilizables, como validadores de datos, formateadores de salida y manejadores de errores genéricos.

## Archivos Raíz

- **__main__.py**: Punto de entrada principal para ejecutar el módulo como un script. Permite invocar el motor de cálculo directamente mediante el comando `python -m escuadra`.
- **cli.py**: Define la interfaz de línea de comandos (CLI) utilizando librerías como `argparse` o `click`. Permite a los usuarios ejecutar cálculos específicos, pasar argumentos y gestionar opciones desde la terminal.

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto desde el directorio `src`, asegúrate de tener Python 3.8 o superior instalado y las dependencias necesarias. Sigue estos pasos:

1. Navega al directorio `src`:
   ```bash
   cd src
   ```

2. Ejecuta el módulo `escuadra` utilizando el siguiente comando:
   ```bash
   python -m escuadra
   ```

Este comando invocará el archivo `__main__.py`, iniciando el motor de cálculo o mostrando el menú de la interfaz de línea de comandos definido en `cli.py`. Puedes pasar argumentos adicionales según las opciones disponibles en la CLI para personalizar la ejecución.

Esta estructura garantiza que el código sea modular, fácil de entender y extensible para futuros contribuidores.