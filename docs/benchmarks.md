# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H, 2.4 GHz)
- **RAM**: 16 GB
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este entorno se utilizará como referencia para comparar el rendimiento de las herramientas.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|---------------------|------------------------------------|----------------------------------|
| NumPy               | 1200                              | 1200                            |
| Pandas              | 1500                              | 1500                            |
| SciPy               | 2100                              | 2100                            |
| Matplotlib          | 800                               | 800                             |
| Scikit-learn        | 1800                              | 1800                            |
| NumPy + Pandas      | 2200                              | 2200                            |

*Nota: Los tiempos son promedios de 1000 ejecuciones medidos con `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados:

1. Usar `timeit`:
   ```python
   import timeit
   setup = "import numpy as np"
   stmt = "np.array([1, 2, 3]) + np.array([4, 5, 6])"
   print(timeit.timeit(stmt, setup, number=1000))
   ```

2. Usar `pytest-benchmark`:
   - Instalar: `pip install pytest-benchmark`
   - Ejemplo de archivo `conftest.py`:
     ```python
     import pytest
     from pytest_benchmark import benchmark

     @benchmark
     def test_numpy_add():
         import numpy as np
         return np.array([1, 2, 3]) + np.array([4, 5, 6])
     ```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10000 microsegundos) en promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento.