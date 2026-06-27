# Uso de Escuadra con Docker y X11 forwarding

Esta guia describe como ejecutar Escuadra desde una imagen Docker cuando se necesita
abrir la interfaz grafica basada en PySide6.

## Requisitos previos

Antes de iniciar el contenedor, verifica que el equipo anfitrion tenga:

- Docker instalado y con permisos para ejecutar contenedores.
- Un servidor X11 activo.
- La variable de entorno `DISPLAY` configurada.
- El repositorio de Escuadra disponible en el directorio de trabajo.

En Linux de escritorio normalmente `DISPLAY` ya esta definida. Puedes comprobarlo con:

```bash
echo "$DISPLAY"
```

Si el comando no muestra ningun valor, la aplicacion no podra abrir ventanas desde el
contenedor hasta que configures un servidor grafico compatible.

## Obtener la imagen

Si el equipo docente o el repositorio del curso publica una imagen de Escuadra,
descargala con el nombre indicado por esa distribucion:

```bash
docker pull <imagen-de-escuadra>
```

En los ejemplos siguientes se usa `escuadra:local` como nombre de referencia. Si tu
imagen tiene otro nombre, reemplazalo en los comandos.

Cuando exista un `Dockerfile` en la raiz del proyecto, tambien puedes construir una
imagen local con:

```bash
docker build -t escuadra:local .
```

La imagen debe instalar las dependencias del proyecto, incluido PySide6, y dejar
disponible `python -m escuadra` o el comando `escuadra`.

## Permitir conexiones X11 locales

Para que el contenedor pueda mostrar la ventana de Escuadra en el escritorio del
anfitrion, permite temporalmente conexiones locales al servidor X11:

```bash
xhost +local:docker
```

Este permiso debe usarse solo en equipos de confianza. Al terminar, puedes retirarlo
con:

```bash
xhost -local:docker
```

## Ejecutar la aplicacion grafica

Ejecuta el contenedor compartiendo el socket de X11 y la variable `DISPLAY`:

```bash
docker run --rm -it \
  -e DISPLAY="$DISPLAY" \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  escuadra:local
```

Si la imagen no define un comando por defecto, indica explicitamente el modulo de
arranque:

```bash
docker run --rm -it \
  -e DISPLAY="$DISPLAY" \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  escuadra:local \
  python -m escuadra
```

## Ejecutar comandos sin interfaz grafica

Para tareas que no abren ventanas, como consultar ayuda o correr pruebas, no es
necesario montar X11:

```bash
docker run --rm escuadra:local escuadra --help
docker run --rm escuadra:local python -m pytest
```

## Limitaciones

- La interfaz grafica requiere X11 forwarding. Sin un servidor X11 accesible, el
  contenedor puede iniciar, pero PySide6 no podra crear la ventana principal.
- En Wayland puede ser necesario habilitar compatibilidad con XWayland o usar una
  sesion X11.
- En macOS y Windows se requiere un servidor X externo o una configuracion equivalente
  en WSL2; Docker por si solo no proporciona salida grafica.
- El permiso otorgado con `xhost +local:docker` abre acceso local al servidor X11 para
  contenedores locales. Retiralo cuando termines de usar la aplicacion.

## Solucion de problemas

Si aparece un error similar a `could not connect to display`, revisa que `DISPLAY`
tenga valor y que `/tmp/.X11-unix` se haya montado en el contenedor.

Si aparece un error de permisos del servidor X, vuelve a ejecutar:

```bash
xhost +local:docker
```

Si el contenedor inicia pero la ventana no se muestra, confirma que estas usando una
sesion grafica compatible con X11 o XWayland.
