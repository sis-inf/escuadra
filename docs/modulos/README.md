# Índice de Módulos

Este documento lista todos los módulos disponibles en la documentación. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `basic`           | Módulo básico para comenzar | JavaScript | 3 | [basic.md](./basic.md) |
| `data-fetching`   | Manejo de datos desde APIs | TypeScript | 5 | [data-fetching.md](./data-fetching.md) |
| `ui-components`   | Componentes reutilizables para interfaces | React | 8 | [ui-components.md](./ui-components.md) |
| `auth`            | Sistemas de autenticación y autorización | Python | 4 | [auth.md](./auth.md) |
| `logging`         | Gestión de registros y logs | Go | 2 | [logging.md](./logging.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `caching`: Sistema de caché eficiente para mejorar el rendimiento.
- `notifications`: Notificaciones push y email integradas.
- `payments`: Integración con servicios de pago.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo: `<nombre>`
   - Descripción: Breve explicación del módulo.
   - Lenguaje: Tecnología principal.
   - Número de herramientas: Cantidad de herramientas o funciones.
   - Documentación: Enlace al archivo creado.
3. Guarda los cambios y haz un commit.

Si necesitas ayuda para estructurar un nuevo módulo, consulta el ejemplo del módulo `basic`.