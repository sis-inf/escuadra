# Guía de Depuración

## Introducción

La depuración permite identificar y corregir errores en módulos de cálculo, interfaces gráficas y problemas relacionados con la configuración del proyecto.

Esta guía recopila técnicas útiles para diagnosticar errores frecuentes encontrados durante el desarrollo de Escuadra.

---

## Verificar la codificación de un archivo Python

Algunos errores pueden ser causados por archivos guardados con una codificación incorrecta.

### Síntoma

```text
SyntaxError: source code string cannot contain null bytes
```

### Inspeccionar el contenido del archivo

```bash
cat archivo.py
```

Si aparecen caracteres extraños o símbolos inesperados, es posible que el archivo no esté guardado en UTF-8.

### Verificar la codificación

```bash
file archivo.py
```

Salida esperada:

```text
archivo.py: UTF-8 Unicode text
```

### Inspeccionar bytes del archivo

```bash
xxd archivo.py
```

La presencia de secuencias repetidas como `00` puede indicar que el archivo fue guardado en UTF-16 u otra codificación incompatible.

### Solución

Guardar nuevamente el archivo utilizando codificación UTF-8 desde el editor utilizado.

---

## Depuración de módulos de cálculo

Los módulos de cálculo pueden depurarse utilizando las herramientas integradas de Python.

### Uso de breakpoint()

Insertar un punto de interrupción en el código:

```python
def calcular_area(base, altura):
    breakpoint()

    return (base * altura) / 2
```

Ejecutar normalmente el programa:

```bash
python archivo.py
```

La ejecución se detendrá en la línea indicada.

### Comandos útiles

| Comando    | Descripción                      |
| ---------- | -------------------------------- |
| n          | Ejecuta la siguiente línea       |
| s          | Ingresa a una función            |
| p variable | Muestra el valor de una variable |
| c          | Continúa la ejecución            |
| q          | Sale del depurador               |

---

## Uso de pdb

También es posible iniciar el depurador directamente desde la línea de comandos.

```bash
python -m pdb archivo.py
```

Esto permite recorrer paso a paso la ejecución del programa.

---

## Depuración de interfaces PySide6

Los errores relacionados con la interfaz gráfica pueden comportarse de forma distinta en integración continua (CI).

Para reproducir localmente un entorno similar al utilizado por GitHub Actions se recomienda ejecutar Qt en modo offscreen.

### Linux

```bash
QT_QPA_PLATFORM=offscreen pytest
```

### Windows (CMD)

```cmd
set QT_QPA_PLATFORM=offscreen
pytest
```

### Windows (PowerShell)

```powershell
$env:QT_QPA_PLATFORM="offscreen"
pytest
```

Este modo permite ejecutar widgets sin necesidad de una pantalla física o servidor gráfico.

---

## Recomendaciones generales

* Leer cuidadosamente el mensaje completo de error.
* Revisar primero los errores de importación y configuración.
* Verificar que los archivos estén codificados en UTF-8.
* Utilizar `breakpoint()` para aislar problemas en cálculos complejos.
* Ejecutar pruebas antes de abrir un Pull Request.
* Intentar reproducir localmente las condiciones del entorno de CI.

---

## Conclusión

La combinación de revisión de codificación, uso de herramientas de depuración y ejecución de pruebas en entornos similares a CI facilita la identificación temprana de errores y mejora la calidad del proyecto.
