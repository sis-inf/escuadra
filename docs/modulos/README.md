# Índice de Módulos

Este archivo lista todos los módulos disponibles en el proyecto, con una breve descripción y enlaces a su documentación completa. Los módulos están organizados alfabéticamente por nombre.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `modular-cli`      | CLI para gestionar módulos y proyectos modulares. | TypeScript/JavaScript | 12 | [modular-cli.md](./modular-cli.md) |
| `modular-core`     | Lógica central para la gestión de dependencias y ejecución. | TypeScript | 8 | [modular-core.md](./modular-core.md) |
| `modular-docs`     | Generador automático de documentación para módulos. | Python/Markdown | 5 | [modular-docs.md](./modular-docs.md) |
| `modular-test`     | Framework de pruebas integrado para módulos. | TypeScript/JavaScript | 7 | [modular-test.md](./modular-test.md) |
| `modular-ui`       | Componentes UI reutilizables para aplicaciones modulares. | TypeScript/HTML/CSS | 9 | [modular-ui.md](./modular-ui.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y su documentación será agregada cuando estén listos:

- `modular-auth`: Sistema de autenticación integrado.
- `modular-cache`: Capa de caché para mejorar el rendimiento.
- `modular-monitor`: Herramienta para monitorear el estado de los módulos.

## Cómo agregar un nuevo módulo

Para incluir un nuevo módulo en este índice:

1. Crea el archivo del módulo en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada a la tabla en este archivo:
   - Nombre del módulo (mismo que el archivo).
   - Breve descripción en una línea.
   - Lenguaje(s) utilizado(s).
   - Número de herramientas (o "0" si no aplica).
   - Enlace al archivo `.md` del módulo.
3. Guarda los cambios y verifica que el enlace funcione.

Este índice es la primera página que ven los usuarios nuevos, por lo que debe ser claro y actualizado siempre.