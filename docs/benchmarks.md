# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento contiene los benchmarks de rendimiento para las herramientas principales de cálculo numérico. Los tiempos reportados son promedios de 1000 ejecuciones en microsegundos.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (μs) |
|---------------------|----------------------|
| NumPy               | 45                   |
| Pandas (DataFrame)  | 89                   |
| SciPy               | 121                  |
| Matplotlib (plot)   | 320                  |
| Matplotlib (animation) | 1,500             |

*Nota: Los tiempos pueden variar según el tamaño de los datos y la implementación específica.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000).mean()"
  print(timeit.timeit(stmt, setup, number=1000) * 1e6)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 μs).
- Para operaciones más complejas (como procesamiento de grandes datos), se aceptan tiempos hasta 100 ms, siempre que se documenten las condiciones.