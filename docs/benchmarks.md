# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7)
- **RAM**: 16 GB
- **Sistema operativo**: Ubuntu 22.04 LTS

Este documento contiene los benchmarks de rendimiento para las herramientas principales de cálculo numérico. Los tiempos reportados son promedios de 1000 ejecuciones en microsegundos.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (μs) |
|---------------------|----------------------|
| NumPy               | 12.5                 |
| Pandas (DataFrame)  | 45.3                 |
| SciPy               | 38.7                 |
| Matplotlib (plot)   | 92.1                 |
| Matplotlib (animation) | 210.5              |

*Nota: Los tiempos pueden variar según el tamaño de los datos y la complejidad de la operación.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000).sum()"
  print(timeit.timeit(stmt, setup, number=1000) * 1e6)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 μs).
- Para operaciones más complejas (como gráficos animados), se permite un margen mayor, siempre que se mantenga consistencia con respecto a versiones anteriores.