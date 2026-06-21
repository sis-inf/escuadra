# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7)
- **RAM**: 16 GB
- **Sistema operativo**: Ubuntu 22.04 LTS

Este documento registra los tiempos de ejecución promedio de varias herramientas de cálculo numérico, para ayudar a detectar regresiones de rendimiento.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (microsegundos) |
|---------------------|----------------------------------|
| NumPy               | 450                              |
| Pandas (DataFrame)  | 890                              |
| SciPy               | 1200                             |
| Matplotlib (plot)   | 3200                             |
| CuPy (GPU)          | 210                              |

*Nota: Los tiempos son promedios de 1000 ejecuciones usando `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados:

1. Usar `timeit`:
   ```python
   import timeit
   setup = "import numpy as np"
   stmt = "np.random.rand(1000).sum()"
   print(timeit.timeit(stmt, setup, number=1000) * 1e6)  # microsegundos
   ```

2. Usar `pytest-benchmark`:
   ```bash
   pip install pytest-benchmark
   pytest -v -m "benchmark"
   ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 microsegundos).
- Si una herramienta supera este límite, se considera posible regresión de rendimiento que requiere revisión.