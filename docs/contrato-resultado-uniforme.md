# Contrato uniforme ResultadoCalculo

`ResultadoCalculo` es la convencion usada para representar salidas de calculo en
Escuadra mediante diccionarios serializables. Su objetivo es que una herramienta pueda
mostrar, guardar o exportar resultados sin depender de una clase especifica de la
interfaz grafica.

## Forma general

Un resultado debe ser un `dict` de Python con claves de tipo `str` y valores simples:

```python
{
    "resultado": 42.0,
    "unidad": "m",
    "parametro": "valor"
}
```

Los valores deben poder serializarse a JSON. Se recomiendan estos tipos:

- `int` y `float` para magnitudes numericas.
- `str` para unidades, etiquetas y valores textuales.
- `bool` para indicadores de aceptacion o validacion.
- `list` o `dict` anidados solo cuando el resultado requiere una tabla o una estructura
  compuesta.

## Campos recomendados

El contrato no exige que todos los modulos usen exactamente las mismas claves, porque
cada calculo tiene variables propias. Sin embargo, se recomienda mantener estos campos
cuando apliquen:

| Campo | Uso |
| --- | --- |
| `resultado` | Valor principal cuando el calculo devuelve una sola magnitud. |
| `unidad` | Unidad comun del valor principal, por ejemplo `V`, `ohm`, `kN` o `m`. |
| `valor_original` | Entrada original cuando el calculo es una conversion. |
| `unidad_original` | Unidad de entrada en conversiones. |
| `valor_convertido` | Salida numerica de una conversion. |
| `unidad_destino` | Unidad final de una conversion. |
| `admisible` | Indicador booleano para calculos que comparan contra un limite. |

Cuando el calculo produce varias magnitudes equivalentes, las claves pueden nombrar cada
resultado directamente, por ejemplo `voltaje`, `corriente`, `resistencia`, `Ra` o `Rb`.

## Ejemplos actuales

Conversion de bases:

```python
{
    "numero_original": "FF",
    "base_origen": 16,
    "resultado": "255",
    "base_destino": 10
}
```

Ley de Ohm:

```python
{
    "voltaje": 12,
    "unidad_v": "V",
    "corriente": 2,
    "unidad_i": "A",
    "resistencia": 6,
    "unidad_r": "ohm"
}
```

Caida de tension:

```python
{
    "caida_v": 12.9,
    "porcentaje": 5.8636,
    "admisible": False
}
```

## Modulos que ya lo adoptan

Estos modulos devuelven diccionarios compatibles con el contrato:

- `src/escuadra/modulos/civil/viga.py`
- `src/escuadra/modulos/civil/momento_flector.py`
- `src/escuadra/modulos/civil/deflexion_viga.py`
- `src/escuadra/modulos/civil/carga_distribuida.py`
- `src/escuadra/modulos/electrica/caida_tension.py`
- `src/escuadra/modulos/electrica/divisor_tension.py`
- `src/escuadra/modulos/electrica/ley_ohm.py`
- `src/escuadra/modulos/matematicas/conversor_longitud.py`
- `src/escuadra/modulos/sistemas/conversor_bases.py`
- `src/escuadra/modulos/sistemas/herramienta_conversion_bases.py`
- `src/escuadra/modulos/sistemas/tabla_ascii.py`

Tambien consumen o almacenan resultados con esta forma:

- `src/escuadra/core/historial.py`, que guarda `resultado: dict` junto con la
  herramienta, parametros y timestamp.
- `src/escuadra/io/exportador_json.py`, que exporta un `dict` o una lista de
  resultados a JSON.

## Reglas para nuevos calculos

1. Devuelve un `dict`, no una cadena formateada, cuando la funcion de dominio represente
   un calculo reutilizable.
2. Usa nombres de claves descriptivos y estables.
3. Incluye unidades cuando el valor sea una magnitud fisica.
4. Redondea solo cuando el modulo ya tenga una precision definida para presentar o
   comparar resultados.
5. Lanza excepciones para entradas invalidas en lugar de devolver errores como texto
   dentro del resultado.

Las herramientas graficas pueden transformar este contrato a etiquetas, tablas o campos
visuales, pero la logica de calculo debe conservar una salida estructurada para que sea
facil de probar, registrar y exportar.
