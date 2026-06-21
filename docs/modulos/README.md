# Índice de Módulos

Este documento proporciona un resumen de todos los módulos disponibles en el proyecto. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `modular-cli`      | CLI para gestionar módulos y proyectos modulares. | TypeScript/JavaScript | 12 | [modular-cli.md](./modular-cli.md) |
| `modular-config`   | Gestiona configuraciones compartidas entre módulos. | Python | 8 | [modular-config.md](./modular-config.md) |
| `modular-deps`     | Resuelve dependencias entre módulos. | Go | 15 | [modular-deps.md](./modular-deps.md) |
| `modular-test`     | Framework para pruebas integradas de módulos. | Rust | 7 | [modular-test.md](./modular-test.md) |
| `modular-ui`       | Componentes UI reutilizables para aplicaciones modulares. | React/Vue | 10 | [modular-ui.md](./modular-ui.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `modular-auth`: Sistema de autenticación integrado.
- `modular-cache`: Capa de caché para mejorar el rendimiento.
- `modular-monitor`: Monitoreo en tiempo real de módulos.

## Cómo agregar un nuevo módulo

Para incluir un nuevo módulo en este índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo
   - Breve descripción
   - Lenguaje
   - Número de herramientas (o "0" si no aplica)
   - Enlace al archivo `.md`
3. Actualiza la fecha de última actualización al final del documento.

Última actualización: 2024-07-15