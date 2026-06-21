# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7, 16GB RAM)
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento registra los tiempos de ejecución de las herramientas principales para funciones de cálculo numérico, con el objetivo de detectar regresiones de rendimiento.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|-------------------|------------------------------------|----------------------------------|
| NumPy             | 5.2 s                              | 5200                             |
| SciPy             | 8.1 s                              | 8100                             |
| Pandas            | 3.4 s                              | 3400                             |
| CuPy (GPU)        | 1.9 s                              | 1900                             |
| Numba (JIT)       | 2.1 s                              | 2100                             |

*Nota: Los tiempos fueron medidos usando `timeit` con una cantidad suficiente de repeticiones para obtener una media confiable.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.sum(np.random.rand(1000, 1000))"
  print(timeit.timeit(stmt, setup, number=1000))
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (1000 microsegundos) en promedio para 1000 ejecuciones.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento que requiere revisión.

Documentación actualizada el 2025-04-05.