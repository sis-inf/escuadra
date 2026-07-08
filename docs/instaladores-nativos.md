# Instaladores Nativos por Plataforma

## Descripcion general

Escuadra genera instaladores nativos segun el sistema operativo usando PyInstaller.

## Formatos disponibles

| Plataforma | Formato | Extension |
|---|---|---|
| Windows | Microsoft Installer | .msi |
| macOS | Disk Image | .dmg |
| Linux (Debian/Ubuntu) | Debian Package | .deb |

## Windows MSI

Requisitos: Windows 10+, Python 3.10+, PyInstaller.

Generar ejecutable:

    pyinstaller escuadra.spec

El archivo queda en dist/. Incluye asistente de instalacion e integracion con el menu Inicio.

## macOS DMG

Requisitos: macOS 11+, Python 3.10+, PyInstaller.

Generar bundle:

    pyinstaller escuadra.spec

El archivo queda en dist/. Compatible con Apple Silicon e Intel.

## Linux DEB

Requisitos: Ubuntu 20.04+ o Debian 11+, Python 3.10+, dpkg-deb.

Instalar:

    sudo dpkg -i dist/escuadra.deb

Desinstalar:

    sudo dpkg -r escuadra

## Comparacion de formatos

| Caracteristica | MSI | DMG | DEB |
|---|---|---|---|
| Sistema operativo | Windows | macOS | Linux Debian/Ubuntu |
| Requiere admin | Si | No | Si |
| Desinstalacion | Panel de Control | Arrastrar a papelera | dpkg -r |

## Generar todos los instaladores

    python build_app.py

Los archivos quedan en dist/.
