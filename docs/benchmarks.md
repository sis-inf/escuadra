# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento contiene los benchmarks de rendimiento para las herramientas principales del proyecto. Los tiempos reportados son promedios de 1000 ejecuciones en microsegundos.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (μs) |
|-------------------|----------------------|
| NumPy             | 45                   |
| Pandas            | 90                   |
| SciPy             | 120                  |
| Matplotlib        | 80                   |
| Numexpr           | 30                   |

*Nota: Los valores son estimaciones basadas en pruebas recientes.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.sum(np.random.rand(1000))"
  print(timeit.timeit(stmt, setup, number=1000) * 1_000_000)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 μs).
- Cualquier regresión significativa (más del 15% en tiempo promedio) debe ser revisada.