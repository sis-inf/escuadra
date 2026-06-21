# Índice de Módulos

Este documento proporciona un resumen de todos los módulos disponibles en el proyecto. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `modular-cli`      | CLI para gestionar módulos y herramientas. | TypeScript/JavaScript | 5 | [modular-cli.md](./modular-cli.md) |
| `modular-core`     | Lógica central para la gestión de módulos. | Rust | 3 | [modular-core.md](./modular-core.md) |
| `modular-ui`       | Interfaz gráfica para gestionar módulos. | HTML/CSS/JavaScript | 4 | [modular-ui.md](./modular-ui.md) |
| `modular-data`     | Gestión de datos y bases de datos. | Python | 6 | [modular-data.md](./modular-data.md) |
| `modular-security` | Funcionalidades de seguridad para módulos. | Go | 2 | [modular-security.md](./modular-security.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `modular-ai`: Integración de inteligencia artificial en los módulos.
- `modular-caching`: Sistema de caché para mejorar el rendimiento.
- `modular-integration`: Herramientas para integrar con otros sistemas.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada a esta tabla en `docs/modulos/README.md` con:
   - Nombre del módulo
   - Descripción breve
   - Lenguaje(s) utilizado(s)
   - Número de herramientas
   - Enlace al archivo `.md`
3. Guarda los cambios y verifica que el índice sea navegable.