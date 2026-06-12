# Registro de herramientas (subcomandos CLI)

Este documento describe el proceso para agregar nuevos subcomandos al CLI del proyecto.

---

## 🧩 1. Crear el módulo del comando

Cada subcomando debe implementarse en un archivo independiente dentro de la carpeta de comandos.

Ejemplo:


cli/commands/nuevo_comando.py


---

## 🧩 2. Definir el comando y su parser

Dentro del módulo se define la lógica del comando y su configuración:

```python
import argparse

def ejecutar(args):
    print("Ejecutando nuevo comando")


def add_parser(subparsers):
    parser = subparsers.add_parser(
        "nuevo-comando",
        help="Descripción del nuevo comando"
    )

    parser.add_argument(
        "--opcion",
        help="Descripción de la opción"
    )

    parser.set_defaults(func=ejecutar)
```

##  Registro de herramientas

| Nombre de herramienta              | Módulo      | Archivo                               | PR   | Estado       |
| ---------------------------------- | ----------- | ------------------------------------- | ---- | ------------ |
| herramienta_divisor_tension        | electrica   | herramienta_divisor_tension.py        | #269 | implementada |
| herramienta_ley_ohm                | electrica   | herramienta_ley_ohm.py                | #423 | implementada |
| herramienta_calculo_area           | geometria   | herramienta_calculo_area.py           | #205 | implementada |
| herramienta_calculadora_cientifica | matematicas | herramienta_calculadora_cientifica.py | #390 | implementada |
| herramienta_conversion_unidades    | matematicas | herramienta_conversion_unidades.py    | #151 | implementada |
| herramienta_sistemas_lineales      | matematicas | herramienta_sistemas_lineales.py      | #375 | implementada |
| herramienta_complemento_a_2        | sistemas    | herramienta_complemento_a_2.py        | #270 | implementada |
| herramienta_conversion_bases       | sistemas    | herramienta_conversion_bases.py       | #372 | implementada |
| herramienta_tablas_verdad          | sistemas    | herramienta_tablas_verdad.py          | #149 | implementada |
