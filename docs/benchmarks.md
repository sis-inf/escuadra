# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7)
- **RAM**: 16 GB
- **Sistema operativo**: Ubuntu 22.04 LTS

Este documento registra los tiempos de ejecución de las herramientas principales para funciones de cálculo numérico, con el objetivo de detectar posibles regresiones de rendimiento.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|-------------------|------------------------------------|----------------------------------|
| NumPy             | 12.3 ms                           | 12,300                          |
| Pandas            | 18.7 ms                           | 18,700                          |
| SciPy             | 25.1 ms                           | 25,100                          |
| Matplotlib        | 8.9 ms                            | 8,900                           |
| Matplotlib (plot) | 15.4 ms                           | 15,400                          |

*Nota: Los tiempos fueron medidos usando `timeit` con una cantidad suficiente de repeticiones para obtener una media confiable.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000).sum()"
  print(timeit.timeit(stmt, setup, number=1000))
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

Asegúrate de que el entorno de ejecución coincida con el "Entorno de referencia" para comparaciones válidas.

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** en promedio.
- Para herramientas más complejas (por ejemplo, algoritmos avanzados), se permite un margen razonable, siempre que se documenten claramente.
- Cualquier aumento significativo en el tiempo de ejecución respecto a los benchmarks actuales debe ser analizado como posible regresión de rendimiento.

Este documento será actualizado periódicamente con nuevos resultados.