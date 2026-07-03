# Salida JSON en el CLI

## Estado actual

El proyecto incluye un módulo `src/escuadra/io/exportador_json.py`
que permite exportar resultados en formato JSON.

Actualmente este módulo no se encuentra integrado con la interfaz de
línea de comandos, por lo que el CLI no ofrece opciones para generar
archivos JSON.

## Componentes disponibles

- `exportar_resultado()`
- `exportar_lista()`

Estas funciones permiten serializar resultados en archivos JSON utilizando
UTF-8 e indentación de dos espacios.

## Integración pendiente

Actualmente el CLI no dispone de opciones como:

- `--json`
- `--output`
- `--format`

Por ello, la exportación de resultados desde la línea de comandos aún no está disponible.

## Trabajo futuro

Para incorporar esta funcionalidad será necesario:

- agregar argumentos de exportación al CLI;
- utilizar el módulo `exportador_json.py`;
- definir un formato uniforme para los resultados;
- actualizar la documentación del CLI.