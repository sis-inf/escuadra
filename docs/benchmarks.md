# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento presenta los tiempos de ejecución de referencia para varias herramientas de cálculo numérico. Los resultados se obtuvieron bajo el entorno de referencia anterior.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (1000 ejecuciones) [μs] |
|---------------------|----------------------------------------|
| NumPy               | 2.1                                    |
| Pandas              | 4.3                                    |
| SciPy               | 8.7                                    |
| Matplotlib          | 15.2                                   |
| Matplotlib (plot)   | 32.5                                   |

*Nota: Los tiempos son promedios de 1000 ejecuciones medias con `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000).sum()"
  print(timeit.timeit(stmt, setup, number=1000) * 1000000)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** en promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento.