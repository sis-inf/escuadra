# Índice de Módulos

Este documento lista todos los módulos disponibles en el proyecto, con una breve descripción y enlaces a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|------------|----------|------------------------|---------------|
| `modular-cli`      | CLI para gestionar módulos y proyectos modulares. | TypeScript/JavaScript | 5 | [modular-cli.md](./modular-cli.md) |
| `modular-config`   | Gestiona configuraciones compartidas entre módulos. | Python | 3 | [modular-config.md](./modular-config.md) |
| `modular-deps`     | Resuelve dependencias entre módulos. | Rust | 4 | [modular-deps.md](./modular-deps.md) |
| `modular-test`     | Framework para pruebas en módulos modulares. | Go | 2 | [modular-test.md](./modular-test.md) |
| `modular-ui`       | Componentes UI reutilizables para aplicaciones modulares. | React/Vue | 6 | [modular-ui.md](./modular-ui.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y su documentación será agregada cuando estén listos:

- `modular-auth`: Sistema de autenticación integrado.
- `modular-cache`: Capa de caché para mejorar el rendimiento.
- `modular-monitor`: Monitoreo en tiempo real de módulos.

## Cómo agregar un nuevo módulo

Para incluir un nuevo módulo en este índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo (mismo nombre del archivo).
   - Breve descripción en una línea.
   - Lenguaje usado.
   - Número de herramientas (o "0" si no aplica).
   - Enlace al archivo `.md` creado.
3. Guarda los cambios y haz un commit.

Si necesitas ayuda para estructurar un nuevo módulo, consulta el ejemplo de [modular-cli.md](./modular-cli.md).