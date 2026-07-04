# 🔄 Autocompletado de Shell para el CLI

Esta guía explica cómo activar el **autocompletado de shell** para el CLI de Escuadra, una funcionalidad que permite completar automáticamente comandos, opciones y argumentos al presionar la tecla `Tab`.

---

## 🎯 ¿Qué es el autocompletado de shell?

El autocompletado de shell permite:

- **Completar** comandos y subcomandos automáticamente.
- **Sugerir** opciones y argumentos disponibles.
- **Ahorrar tiempo** al escribir comandos largos.
- **Evitar errores** tipográficos.

---

## 🚀 Cómo activar el autocompletado

### Para Bash

1. **Generar el script de autocompletado:**

```bash
escuadra autocompletado --shell bash > ~/.escuadra-completion.bash

