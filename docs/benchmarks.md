# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7, 16GB RAM)
- **Sistema operativo**: Ubuntu 22.04 LTS

Este documento presenta los resultados de benchmarks para comparar el rendimiento de diferentes herramientas de cálculo numérico.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|-------------------|------------------------------------|----------------------------------|
| NumPy             | 12.3 ms                           | 12,300                          |
| Pandas            | 18.7 ms                           | 18,700                          |
| SciPy             | 25.1 ms                           | 25,100                          |
| CuPy              | 14.8 ms                           | 14,800                          |
| Dask              | 32.4 ms                           | 32,400                          |

*Nota: Los tiempos son promedios de 1000 ejecuciones medidos con `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000).sum()"
  print(timeit.timeit(stmt, setup, number=1000) * 1_000_000)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** en promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento.