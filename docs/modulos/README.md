# Índice de Módulos

Este documento proporciona un resumen de todos los módulos disponibles en la documentación. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|------------|----------|------------------------|---------------|
| `modular` | Framework modular para estructurar aplicaciones | TypeScript | 3 | [modular.md](./modular.md) |
| `cli` | Interfaz de línea de comandos para gestionar módulos | JavaScript | 5 | [cli.md](./cli.md) |
| `config` | Gestión de configuraciones en tiempo de ejecución | Python | 2 | [config.md](./config.md) |
| `router` | Enrutamiento dinámico para aplicaciones web | TypeScript | 4 | [router.md](./router.md) |
| `auth` | Sistemas de autenticación integrados | Go | 3 | [auth.md](./auth.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `cache`: Gestión de caché eficiente para mejoras de rendimiento.
- `database`: Conexión y gestión avanzada de bases de datos.
- `notifications`: Sistema de notificaciones push y email.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo: `<nombre>`
   - Descripción: Breve explicación del módulo.
   - Lenguaje: Ej. TypeScript, Python, etc.
   - Número de herramientas: Cantidad de herramientas asociadas.
   - Documentación: Enlace al archivo creado.
3. Guarda los cambios y verifica que el enlace funcione.