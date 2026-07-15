# Autocompletado de Shell para el CLI

Escuadra soporta autocompletado de comandos en bash y zsh mediante la libreria argcomplete.

## Requisitos

- Python 3.10 o superior
- Escuadra instalado
- argcomplete instalado (incluido como dependencia de Escuadra)

Verificar que argcomplete este instalado:

    pip show argcomplete

## Activar autocompletado en bash

### Metodo 1: Activacion global (recomendado)

Ejecutar una sola vez:

    activate-global-python-argcomplete

Esto activa el autocompletado para todos los scripts que usen argcomplete. Luego recargar el shell:

    source ~/.bashrc

### Metodo 2: Activacion solo para escuadra

Agregar al archivo ~/.bashrc:

    eval "$(register-python-argcomplete escuadra)"

Recargar:

    source ~/.bashrc

## Activar autocompletado en zsh

Agregar al archivo ~/.zshrc:

    autoload -U bashcompinit
    bashcompinit
    eval "$(register-python-argcomplete escuadra)"

Recargar:

    source ~/.zshrc

## Verificar que funciona

Abrir una terminal nueva y escribir:

    escuadra <TAB>

Deberia mostrar la lista de herramientas disponibles. Tambien funciona con argumentos parciales:

    escuadra --<TAB>

## Uso del autocompletado

Una vez activado, presionar Tab en cualquier momento para ver las opciones disponibles:

    escuadra [TAB]          # muestra todas las herramientas
    escuadra --[TAB]        # muestra todas las opciones globales
    escuadra civil [TAB]    # muestra herramientas del modulo civil

## Solucionar problemas

Si el autocompletado no funciona despues de activarlo:

1. Verificar que argcomplete este instalado:

    pip show argcomplete

2. Verificar que el archivo de configuracion del shell fue modificado:

    cat ~/.bashrc | grep argcomplete

3. Abrir una terminal completamente nueva (no solo recargar)

4. Verificar que escuadra sea accesible desde el PATH:

    which escuadra
