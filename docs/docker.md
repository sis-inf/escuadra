# Docker con soporte X11 Forwarding

## Descripción

Este documento explica cómo utilizar la imagen Docker del proyecto Escuadra con soporte para X11 Forwarding, permitiendo ejecutar la interfaz gráfica desde un contenedor.

## ¿Qué es X11 Forwarding?

X11 Forwarding es un mecanismo que permite mostrar aplicaciones gráficas que se ejecutan dentro de un contenedor Docker en la pantalla del equipo anfitrión.

Esta funcionalidad es necesaria para utilizar las herramientas con interfaz gráfica incluidas en Escuadra.

## Requisitos

Antes de ejecutar la imagen Docker se debe contar con:

- Docker instalado.
- Un servidor X11 disponible en el sistema operativo.
- Soporte para X11 Forwarding habilitado.

## Uso

Una vez configurado X11 Forwarding, se puede ejecutar la imagen Docker siguiendo las instrucciones del proyecto.

Si la configuración es correcta, las aplicaciones gráficas podrán mostrarse en el equipo anfitrión.

## Limitaciones

El uso de la interfaz gráfica depende de que X11 Forwarding esté correctamente configurado.

Si el entorno no dispone de soporte para X11, las aplicaciones gráficas no podrán visualizarse correctamente.

## Recomendaciones

- Verificar que el servidor X11 esté funcionando antes de iniciar el contenedor.
- Comprobar que Docker tenga acceso a la pantalla del sistema.
- Revisar la configuración del sistema operativo si la interfaz gráfica no aparece.