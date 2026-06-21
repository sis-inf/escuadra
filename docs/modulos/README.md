# Índice de Módulos

Este documento proporciona un resumen de todos los módulos disponibles en la documentación. Cada módulo tiene una descripción breve y un enlace a su documentación completa.

## Módulos Disponibles

| Nombre del módulo | Descripción | Lenguaje | Número de herramientas | Documentación |
|-------------------|------------|----------|------------------------|---------------|
| `mod-hello`        | Módulo de saludo básico que imprime "Hola, mundo!" | JavaScript | 1 | [mod-hello.md](docs/modulos/mod-hello.md) |
| `mod-calculator`   | Calculadora básica con operaciones aritméticas | TypeScript | 3 | [mod-calculator.md](docs/modulos/mod-calculator.md) |
| `mod-file-reader`  | Lectura de archivos desde el sistema | Python | 2 | [mod-file-reader.md](docs/modulos/mod-file-reader.md) |
| `mod-api-client`   | Cliente de API REST para integraciones | Go | 4 | [mod-api-client.md](docs/modulos/mod-api-client.md) |

## Módulos Planificados

Los siguientes módulos están en desarrollo y se documentarán cuando estén listos:

- `mod-ai-integration`: Integración con modelos de inteligencia artificial.
- `mod-cryptography`: Herramientas de cifrado y descifrado.
- `mod-dashboard`: Panel de control para monitoreo en tiempo real.

## Cómo agregar un nuevo módulo

Para agregar un nuevo módulo al índice:

1. Crea el archivo de documentación en `docs/modulos/<nombre-módulo>.md`.
2. Añade una entrada a esta tabla en `docs/modulos/README.md` con:
   - Nombre del módulo
   - Descripción breve
   - Lenguaje
   - Número de herramientas
   - Enlace al archivo `.md`
3. Guarda los cambios y verifica que el enlace funcione.