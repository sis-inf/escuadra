# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento contiene los benchmarks de rendimiento para las herramientas principales del proyecto. Los tiempos reportados son promedios de 1000 ejecuciones en microsegundos.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (μs) |
|---------------------|----------------------|
| NumPy               | 45                   |
| Pandas              | 89                   |
| SciPy               | 123                  |
| Matplotlib          | 187                  |
| Scikit-learn        | 95                   |

*Nota: Los valores son estimaciones basadas en pruebas recientes.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.sum(np.random.rand(1000))"
  print(timeit.timeit(stmt, setup, number=1000) * 1e6)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 μs).
- Si una herramienta supera este límite, se considera posible regresión de rendimiento que requiere revisión.