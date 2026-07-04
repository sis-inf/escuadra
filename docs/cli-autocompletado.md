
  GNU nano 8.7               docs/cli-autocompletado.md
#  ~D Autocompletado de Shell para el CLI

Esta guía explica cómo activar el **autocompletado de shell** para el CLI de Es>

---

##  M-/ ¿Qué es el autocompletado de shell?

El autocompletado de shell permite:

- **Completar** comandos y subcomandos automáticamente.
- **Sugerir** opciones y argumentos disponibles.
- **Ahorrar tiempo** al escribir comandos largos.
- **Evitar errores** tipográficos.

---

##  ~@ Cómo activar el autocompletado

### Para Bash

1. **Generar el script de autocompletado:**

```bash
escuadra autocompletado --shell bash > ~/.escuadra-completion.bash
echo "source ~/.escuadra-completion.bash" >> ~/.bashrc
source ~/.bashrc
escuadra autocompletado --shell zsh > ~/.escuadra-completion.zsh
echo "source ~/.escuadra-completion.zsh" >> ~/.zshrc
source ~/.zshrc
escuadra autocompletado --shell fish > ~/.config/fish/completions/escuadra.fish
source ~/.config/fish/config.fish$
$ escuadra viga --longitud 5.0 --carga 10.0

