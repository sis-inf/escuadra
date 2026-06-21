# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H, 2.4 GHz)
- **RAM**: 16 GB
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento contiene los benchmarks de rendimiento para las herramientas principales del proyecto. Los resultados sirven como referencia para detectar regresiones de rendimiento.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (1000 ejecuciones) | Unidad       |
|-------------------|------------------------------------|--------------|
| NumPy             | 45.2                               | microsegundos |
| Pandas            | 98.7                               | microsegundos |
| SciPy             | 123.4                              | microsegundos |
| Matplotlib        | 189.1                              | microsegundos |
| Matplotlib (plot) | 215.3                              | microsegundos |

*Nota: Los tiempos fueron medidos usando `timeit` con una configuración estándar.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000)"
  print(timeit.timeit(stmt, setup, number=1000))
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

Asegúrate de ejecutar los benchmarks en el mismo entorno de referencia para comparaciones válidas.

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 microsegundos) en promedio.
- Si una herramienta supera este límite, se considera una posible regresión de rendimiento que requiere atención.