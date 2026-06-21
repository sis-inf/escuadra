# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7, 16GB RAM)
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento registra los tiempos de ejecución de las herramientas principales para funciones de cálculo numérico, con el objetivo de detectar posibles regresiones de rendimiento.

## Resultados de benchmarks

Las mediciones se realizaron ejecutando cada función 1000 veces y promediando los tiempos en microsegundos (μs).

| Herramienta       | Tiempo promedio (μs) |
|-------------------|----------------------|
| NumPy             | 12.5                 |
| Pandas            | 8.3                  |
| SciPy             | 18.7                 |
| Matplotlib        | 25.1                 |
| Matplotlib (plot) | 42.3                 |

*Nota: Los tiempos son referencias y pueden variar según el entorno.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.sum(np.random.rand(1000))"
  print(timeit.timeit(stmt, setup, number=1000) * 1000000)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 μs) en operaciones básicas.
- Cualquier aumento superior al 15% en tiempo promedio respecto a los benchmarks actuales se considera potencialmente problemático y requiere revisión.