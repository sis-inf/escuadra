# Índice de Módulos

Este archivo lista todos los módulos disponibles en la documentación. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `modular`         | Framework modular para estructurar aplicaciones. | TypeScript | 3 | [modular.md](./modular.md) |
| `cli`             | Interfaz de línea de comandos para gestionar proyectos. | JavaScript | 5 | [cli.md](./cli.md) |
| `state`           | Gestión de estado en aplicaciones reactivas. | Python | 2 | [state.md](./state.md) |
| `router`          | Ruteo dinámico para aplicaciones web. | HTML/CSS/JS | 4 | [router.md](./router.md) |
| `auth`            | Sistemas de autenticación y autorización. | Go | 6 | [auth.md](./auth.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `cache`: Sistema de caché para mejorar el rendimiento.
- `database`: Capa de acceso a bases de datos.
- `notifications`: Notificaciones push y email.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo: `<nombre>`
   - Descripción: Breve explicación del módulo.
   - Lenguaje: Tecnologías utilizadas.
   - Número de herramientas: Cantidad de herramientas o componentes.
   - Documentación: Enlace al archivo `.md` recién creado.
3. Guarda los cambios y verifica que el enlace funcione.