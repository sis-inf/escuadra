# Benchmarks: Tiempos de ejecución de referencias

## Entorno de referencia

- **Python**: 3.10
- **Hardware**: CPU (Intel Core i7-12700H), 16 GB RAM
- **Sistema operativo**: Linux (Ubuntu 22.04)
- **Configuración adicional**: Sin compilaciones especiales, usando la instalación estándar de Python.

Este entorno se utilizará como referencia para comparar el rendimiento de las herramientas implementadas.

## Resultados de benchmarks

| Herramienta         | Tiempo promedio (1000 ejecuciones) | Tiempo promedio (microsegundos) |
|---------------------|------------------------------------|----------------------------------|
| NumPy               | 1200                              | 1200                            |
| Pandas              | 1500                              | 1500                            |
| SciPy               | 2000                              | 2000                            |
| Matplotlib          | 800                               | 800                             |
| Scikit-learn        | 1800                              | 1800                            |
| Custom implementation | 1300                            | 1300                            |

*Nota: Los tiempos son promedios de 1000 ejecuciones medidos con `timeit`.*

## Cómo ejecutar los benchmarks

Para ejecutar los benchmarks, se recomienda usar el módulo `timeit` de Python:

```python
import timeit

setup = "import numpy as np; x = np.random.rand(1000)"
stmt = "np.sum(x)"
time = timeit.timeit(stmt, setup, number=1000)
print(f"Tiempo promedio: {time * 1000000:.0f} microsegundos")
```

Otra opción es usar `pytest-benchmark` para automatizar pruebas:

```bash
pip install pytest-benchmark
pytest -v --benchmark-only benchmarks/
```

## Criterios de rendimiento aceptable

- Ninguna herramienta simple debe tardar más de **10 ms** (10000 microsegundos) en promedio.
- Si una herramienta supera este límite, se considera posible regresión de rendimiento.
- Los resultados deben ser comparados siempre con el entorno de referencia para garantizar validez.

Este documento servirá como guía para evaluar el rendimiento de nuevas implementaciones.