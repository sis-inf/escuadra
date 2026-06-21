# Índice de Módulos

Este archivo lista todos los módulos disponibles en la documentación. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|-------------|----------|------------------------|---------------|
| `modular`         | Framework modular para estructurar aplicaciones. | TypeScript | 3 | [modular.md](./modular.md) |
| `cli-tools`       | Conjunto de herramientas de línea de comandos. | JavaScript | 5 | [cli-tools.md](./cli-tools.md) |
| `data-access`     | Capa de acceso a datos para múltiples bases. | Python | 2 | [data-access.md](./data-access.md) |
| `auth-service`    | Servicio de autenticación y autorización. | Go | 4 | [auth-service.md](./auth-service.md) |
| `api-gateway`     | Gateway para rutas API y balanceo de carga. | Node.js | 3 | [api-gateway.md](./api-gateway.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `cache-manager`: Gestor de caché integrable.
- `notification-service`: Servicio de notificaciones push y email.
- `analytics`: Integración de análisis de uso.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada en esta tabla:
   - Nombre del módulo: `<nombre-módulo>`
   - Descripción: Breve explicación del módulo.
   - Lenguaje: Ej. `TypeScript`, `Python`, etc.
   - Número de herramientas: Cantidad de herramientas asociadas.
   - Documentación: Enlace al archivo creado.
3. Guarda los cambios y verifica que el enlace funcione.