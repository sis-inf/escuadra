# Referencia del CLI de escuadra

Este documento proporciona una referencia completa de los subcomandos disponibles en la interfaz de línea de comandos (CLI) de escuadra.

## Instalación

Para instalar el CLI de escuadra en tu entorno local:

```bash
pip install -e .
```

Esto instala el paquete en modo editable, permitiendo que los cambios en el código fuente se reflejen inmediatamente en el CLI.

## Uso básico

Para ver la ayuda general del CLI:

```bash
escuadra --help
```

Esto muestra todos los subcomandos disponibles y las opciones globales.

Para ver la versión del programa:

```bash
escuadra --version
# o
escuadra -v
```

## Autocompletado de shell

Escuadra soporta autocompletado de subcomandos mediante `argcomplete`.

Instala las dependencias del proyecto y activa el autocompletado:

### Bash

```bash
eval "$(register-python-argcomplete escuadra)"
```

### Zsh

```bash
autoload -U bashcompinit
bashcompinit
eval "$(register-python-argcomplete escuadra)"
```

Después podrás presionar `Tab` para completar automáticamente los subcomandos disponibles.

## Flags globales

Los siguientes flags están disponibles en todos los subcomandos:

| Flag | Corto | Descripción |
|------|-------|-------------|
| `--version` | `-v` | Muestra la versión del programa y sale |
| `--help` | `-h` | Muestra el mensaje de ayuda y sale |

## Subcomandos disponibles

### viga - Cálculo de reacciones en vigas

Calcula las reacciones en vigas simplemente apoyadas bajo carga puntual.

#### Sintaxis

```bash
escuadra viga --longitud LONGITUD --carga CARGA
```

#### Argumentos

| Argumento | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `--longitud` | float | Sí | Longitud de la viga en metros |
| `--carga` | float | Sí | Carga puntual en kN |

#### Valores por defecto

Ninguno. Todos los argumentos son requeridos.

#### Ejemplo de invocación

```bash
escuadra viga --longitud 5.0 --carga 10.0
```

#### Salida esperada

```
La herramienta 'viga' aún está en construcción y no está disponible.
```

**Nota:** Este subcomando está actualmente en desarrollo y no está completamente implementado en el CLI.

---

### tension - Cálculo de caída de tensión

Calcula la caída de tensión en conductores eléctricos monofásicos.

#### Sintaxis

```bash
escuadra tension --longitud LONGITUD --corriente CORRIENTE --seccion SECCION
```

#### Argumentos

| Argumento | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `--longitud` | float | Sí | Longitud del conductor en metros |
| `--corriente` | float | Sí | Corriente en amperios |
| `--seccion` | float | Sí | Sección del conductor en mm² |

#### Valores por defecto

Ninguno. Todos los argumentos son requeridos.

#### Ejemplo de invocación

```bash
escuadra tension --longitud 100 --corriente 15 --seccion 4
```

#### Salida esperada

```
La herramienta 'tension' aún está en construcción y no está disponible.
```

**Nota:** Este subcomando está actualmente en desarrollo y no está completamente implementado en el CLI.

## Estado de implementación

Los subcomandos del CLI están actualmente en desarrollo. Aunque la sintaxis y los argumentos están definidos, la ejecución de los cálculos aún no está disponible a través de la línea de comandos.

Para acceder a las funcionalidades de cálculo, se recomienda utilizar la interfaz gráfica de usuario (GUI) de escuadra, donde las herramientas están completamente implementadas.

## Ayuda adicional

Para obtener ayuda específica de cada subcomando:

```bash
escuadra viga --help
escuadra tension --help
```

Esto mostrará la sintaxis, argumentos y descripciones detalladas para cada subcomando.
