# Documentación de Pruebas (Tests)

Este directorio contiene toda la suite de pruebas del proyecto. Para mantener el código organizado y asegurar la calidad del software, es fundamental respetar la estructura de carpetas y las convenciones de nombres detalladas a continuación.

---

## Estructura de carpetas

A continuación se describe el propósito de cada directorio dentro de `tests/`. Por favor, asegúrate de ubicar tus nuevos archivos de prueba en el lugar correcto.

| Directorio | Tipo de Test / Contenido | Descripción |
| :--- | :--- | :--- |
| `automatizados/unit/` | Pruebas Unitarias | Pruebas aisladas de funciones, métodos o clases individuales. No tienen dependencias externas (bases de datos, APIs). |
| `automatizados/integration/` | Pruebas de Integración | Pruebas que verifican la interacción entre dos o más módulos, componentes o con la base de datos. |
| `manuales/` | Pruebas Manuales | Documentos, guías y scripts para pruebas que requieren intervención humana y no están automatizadas. |
| `casos/` | Casos de Prueba | Documentación detallada de los escenarios de prueba diseñados (QA), tanto de éxito como de fallo. |
| `plan/` | Plan de Pruebas | El plan maestro de pruebas que define el alcance, estrategia, recursos y cronograma del testing. |

---

## Ejecución de Pruebas

Para ejecutar las pruebas automatizadas, asegúrate de tener el entorno virtual activo y todas las dependencias instaladas.

Para correr absolutamente todas las pruebas automatizadas del proyecto, ejecuta el siguiente comando en la raíz:
```bash
pytest

``` 

