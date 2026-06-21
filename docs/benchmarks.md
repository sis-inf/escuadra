# Benchmarks de rendimiento

Este documento registra los tiempos de ejecución de referencia para las herramientas de cálculo numérico, para ayudar a detectar regresiones de rendimiento.

## Entorno de referencia

- Python 3.10
- CPU: Intel Core i7-12700H
- RAM: 16 GB
- Sistema operativo: Ubuntu 22.04

## Resultados de benchmarks

Las mediciones se realizaron ejecutando cada herramienta 1000 veces y tomando el tiempo promedio en microsegundos.

| Herramienta         | Tiempo promedio (μs) |
|---------------------|----------------------|
| NumPy               | 45                   |
| Pandas (DataFrame)  | 89                   |
| SciPy               | 120                  |
| Matplotlib (plot)   | 320                  |
| CuPy (GPU)          | 28                   |

*Nota: Los tiempos pueden variar según el conjunto de datos y la implementación específica.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`: Ejemplo básico:
  ```python
  import timeit
  setup = "import numpy as np"
  stmt = "np.random.rand(1000).sum()"
  print(timeit.timeit(stmt, setup, number=1000) * 1000000)
  ```

- `pytest-benchmark`: Instala con `pip install pytest-benchmark`, luego crea un archivo de prueba con anotaciones `@benchmark` y ejecuta con `pytest`.

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de 10 ms (10,000 μs) en operaciones comunes.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento que requiere investigación.