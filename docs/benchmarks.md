\# Benchmarks de Herramientas

\## Entorno de referencia

Las mediciones fueron realizadas en el siguiente entorno:

- Python 3.14.6
- Sistema operativo: Windows
- CPU: Intel Core i5-1235U (12th Gen)
- RAM: 8 GB (8247566336 bytes)

Los resultados fueron obtenidos mediante un script basado en `timeit`, ejecutando cada herramienta 1000 veces y calculando el tiempo promedio por ejecución.

\## Resultados de benchmarks

Promedio de 1000 ejecuciones por herramienta.

| Herramienta | Tiempo promedio (µs) |

|------------|----------------------:|

| calcular\_ohm | 0.33 |

| calcular\_tension\_salida | 0.18 |

| area\_rectangulo | 0.05 |

| seno | 0.11 |

| convertir | 0.37 |

\## Cómo ejecutar los benchmarks

Ejemplo utilizando `timeit`:

```python

from timeit import timeit

tiempo = timeit(

&#x20;   lambda: calcular\_ohm(voltaje=12, corriente=2),

&#x20;   number=1000

)

print(tiempo)

```

También pueden utilizarse herramientas como:

```bash

pytest-benchmark

```

para obtener métricas más detalladas.

\## Criterios de rendimiento aceptable


\- Ninguna herramienta simple debe tardar más de 10 ms por ejecución.

\- Los cambios que introduzcan regresiones significativas de rendimiento deben revisarse antes de ser integrados.

\- Los benchmarks deben ejecutarse nuevamente después de optimizaciones o refactorizaciones relevantes.

