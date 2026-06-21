# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Ubuntu 22.04 LTS

Este documento registra los tiempos de ejecución de las herramientas principales para funciones de cálculo numérico, con el objetivo de detectar posibles regresiones de rendimiento.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|-------------------|------------------------------------|----------------------------------|
| NumPy             | 12.3 ms                           | 12,300                          |
| SciPy             | 25.7 ms                           | 25,700                          |
| Pandas            | 18.9 ms                           | 18,900                          |
| Matplotlib        | 45.2 ms                           | 45,200                          |
| CuPy (GPU)        | 8.1 ms                            | 8,100                           |

*Nota: Los tiempos fueron medidos usando `timeit` con 1000 repeticiones.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```bash
  python -m timeit -n 1000 "import numpy as np; np.random.rand(1000)"
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v --benchmark-only benchmarks/
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** en promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento que requiere revisión.

Documentación actualizada el 2025-04-05.