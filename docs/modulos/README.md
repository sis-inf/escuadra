# Índice de Módulos

Este documento lista todos los módulos disponibles en la documentación. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `basic` | Módulo básico para comenzar | TypeScript | 3 | [basic.md](./basic.md) |
| `advanced` | Módulo avanzado para tareas complejas | JavaScript | 7 | [advanced.md](./advanced.md) |
| `utils` | Herramientas útiles para tareas comunes | Python | 5 | [utils.md](./utils.md) |
| `api` | Interfaz con APIs externas | TypeScript/JavaScript | 4 | [api.md](./api.md) |
| `auth` | Gestión de autenticación | TypeScript | 6 | [auth.md](./auth.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `analytics`: Análisis de datos y métricas.
- `notifications`: Sistema de notificaciones push y email.
- `payments`: Integración con servicios de pago.
- `cache`: Gestión de caché para mejorar el rendimiento.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre>.md`.
2. Añade una entrada al índice en esta página:
   - En la tabla, agrega una fila con:
     - Nombre del módulo
     - Descripción en una línea
     - Lenguaje
     - Número de herramientas
     - Enlace al archivo `.md`
3. Si el módulo está en desarrollo, agrégalo a la sección "Módulos Planificados".

Este índice es la primera página que ven los usuarios nuevos, por lo que debe ser claro y completo.