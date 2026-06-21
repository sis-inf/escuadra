# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-1165G7, 16GB RAM)
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento contiene los benchmarks de rendimiento para las herramientas principales del proyecto. Los tiempos reportados son promedios de 1000 ejecuciones en microsegundos.

## Resultados de benchmarks

| Herramienta       | Tiempo promedio (μs) |
|-------------------|----------------------|
| NumPy             | 45                   |
| Pandas            | 89                   |
| SciPy             | 123                  |
| Matplotlib        | 187                  |
| Matplotlib (plot) | 321                  |

*Nota: Los tiempos pueden variar según el entorno y el tamaño de los datos.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar `timeit` o `pytest-benchmark`:

### Usando timeit

Ejemplo básico:
```python
import timeit

setup = "import numpy as np"
stmt = "np.random.rand(1000).sum()"
time = timeit.timeit(stmt, setup, number=1000)
print(f"Tiempo promedio: {time * 1_000_000:.0f} μs")
```

### Usando pytest-benchmark

Instala el paquete:
```bash
pip install pytest-benchmark
```

Ejemplo de archivo de prueba:
```python
# tests/test_performance.py
import pytest
from mymodule import my_function

@pytest.mark.benchmark
def test_my_function(benchmark):
    benchmark(my_function)
```

Ejecuta:
```bash
pytest tests/ -v
```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10,000 μs).
- Si una herramienta supera este límite, se considera posible regresión de rendimiento.
- Los resultados deben ser revisados periódicamente al introducir nuevas implementaciones.