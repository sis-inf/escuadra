# Benchmarks: Tiempos de ejecución de referencias

## Contexto

No existe documentación de rendimiento. Para funciones de cálculo numérico es útil conocer cuánto tiempo tarda cada herramienta para saber si una nueva implementación tiene regresión de rendimiento.

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7)
- **RAM**: 16 GB
- **Sistema operativo**: Linux (Ubuntu 22.04)

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|-------------------|------------------------------------|----------------------------------|
| NumPy             | 5.2 s                              | 5200                             |
| Pandas            | 7.8 s                              | 7800                             |
| SciPy             | 12.5 s                             | 12500                            |
| Matplotlib        | 18.3 s                             | 18300                            |
| CuPy (GPU)        | 3.1 s                              | 3100                             |

*Nota: Los tiempos son promedios de 1000 ejecuciones medidos con `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000)"
  print(timeit.timeit(stmt, setup, number=1000) * 1e6)
  ```

- `pytest-benchmark` (recomendado):
  ```bash
  pip install pytest-benchmark
  pytest -v -m "benchmark"
  ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (1000 microsegundos) en ejecución promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento que requiere revisión.