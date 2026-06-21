# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento registra los tiempos de ejecución de las herramientas principales para funciones de cálculo numérico, con el objetivo de detectar posibles regresiones de rendimiento.

## Resultados de benchmarks

Las mediciones se realizaron ejecutando cada función 1000 veces y promediando los tiempos en microsegundos (μs).

| Herramienta       | Tiempo promedio (μs) |
|-------------------|----------------------|
| NumPy             | 45                   |
| Pandas            | 68                   |
| SciPy             | 92                   |
| Matplotlib        | 120                  |
| Matplotlib (plot) | 85                   |

*Nota: Los tiempos son aproximados y pueden variar ligeramente según el entorno.*

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
- Si una herramienta supera este umbral, se considera posible regresión de rendimiento que requiere investigación.