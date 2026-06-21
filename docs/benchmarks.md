# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)

Este documento presenta los tiempos de ejecución de referencia para varias herramientas de cálculo numérico. Los resultados se obtuvieron bajo el entorno de referencia anterior.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (1000 ejecuciones) [μs] |
|---------------------|----------------------------------------|
| NumPy               | 12.5                                   |
| Pandas              | 8.7                                    |
| SciPy               | 18.3                                   |
| Matplotlib          | 25.1                                   |
| CuPy (GPU)          | 9.2                                    |

*Nota: Los tiempos son promedios de 1000 ejecuciones medias con `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar benchmarks personalizados, puedes usar:

- `timeit`:
  - Ejemplo: `python -m timeit -n 1000 "import numpy as np; np.random.rand(1000)"`

- `pytest-benchmark` (recomendado):
  - Instalar: `pip install pytest-benchmark`
  - Ejemplo: 
    ```python
    # tests/test_performance.py
    import pytest
    import numpy as np

    @pytest.mark.benchmark
    def test_numpy_random():
        return np.random.rand(1000)
    ```
  - Ejecutar: `pytest tests/ -v`

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** en promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento.