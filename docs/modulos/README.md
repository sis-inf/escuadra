# Índice de Módulos

Este documento proporciona un resumen de todos los módulos disponibles en el proyecto. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `modular-cli`      | CLI para gestionar módulos y proyectos modulares. | TypeScript/JavaScript | 12 | [modular-cli.md](./modular-cli.md) |
| `modular-config`   | Gestiona configuraciones compartidas entre módulos. | Python | 8 | [modular-config.md](./modular-config.md) |
| `modular-deps`     | Resuelve dependencias entre módulos. | Rust | 15 | [modular-deps.md](./modular-deps.md) |
| `modular-test`     | Framework para pruebas integradas de módulos. | Go | 10 | [modular-test.md](./modular-test.md) |
| `modular-ui`       | Componentes UI reutilizables para aplicaciones modulares. | React/Vue | 20 | [modular-ui.md](./modular-ui.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `modular-auth`: Sistema de autenticación integrado.
- `modular-cache`: Capa de caché para mejorar el rendimiento.
- `modular-monitor`: Monitoreo en tiempo real de módulos.

## Cómo agregar un nuevo módulo

Para incluir un nuevo módulo en este índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo: `<nombre-módulo>`
   - Descripción: Breve explicación del propósito.
   - Lenguaje: Tecnologías utilizadas.
   - Número de herramientas: Cantidad de herramientas o componentes.
   - Documentación: Enlace al archivo creado.
3. Guarda los cambios y haz un commit.

Este índice será actualizado automáticamente cuando se creen nuevos módulos.