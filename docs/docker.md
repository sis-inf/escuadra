# Docker

Este documento explica cómo construir y ejecutar la aplicación utilizando Docker con soporte para X11 forwarding.

## Requisitos

- Docker instalado.
- Un servidor X11 en el host.
- En macOS se recomienda utilizar XQuartz.

## Construir la imagen

```bash
docker build -t escuadra .
```

## Ejecutar en Linux

Permitir conexiones al servidor X:

```bash
xhost +local:docker
```

Ejecutar el contenedor:

```bash
docker run \
    --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    escuadra
```

## Ejecutar en macOS

1. Instalar XQuartz.
2. Abrir XQuartz.
3. Permitir conexiones de clientes de red.
4. Configurar la variable DISPLAY.
5. Ejecutar el contenedor:

```bash
docker run \
    --rm \
    -e DISPLAY=host.docker.internal:0 \
    escuadra
```