# Herramienta de circuitos RC/RL

Esta herramienta documenta los cálculos de constante de tiempo disponibles para
circuitos de primer orden con resistencias, capacitores e inductores. Está orientada a
ejercicios introductorios de corriente continua y transitorios exponenciales.

## Concepto de constante de tiempo

La constante de tiempo, representada como `tau` o `τ`, indica qué tan rápido responde un
circuito después de un cambio brusco, por ejemplo conectar una fuente o descargar un
elemento almacenador de energía.

En un circuito de primer orden:

- Después de `1τ`, la variable alcanza aproximadamente el 63.2 % del cambio final en
  una carga exponencial.
- Después de `5τ`, la respuesta suele considerarse prácticamente estable para fines
  educativos, porque supera el 99 % del valor final.

## Circuitos RC

Un circuito RC combina una resistencia `R` y un capacitor `C`. La constante de tiempo se
calcula con:

```text
τ = R · C
```

Donde:

- `R` se expresa en ohmios (`Ω`).
- `C` se expresa en faradios (`F`).
- `τ` se obtiene en segundos (`s`).

Ejemplo:

```python
from escuadra.modulos.electrica.circuitos_rc_rl import calcular_constante_tiempo_rc

tau = calcular_constante_tiempo_rc(resistencia=1000, capacitancia=0.000001)
print(tau)  # 0.001 segundos
```

En este caso, una resistencia de `1000 Ω` y un capacitor de `1 µF` producen una constante
de tiempo de `0.001 s`, equivalente a `1 ms`.

## Carga exponencial de un capacitor

Cuando un capacitor se carga desde una fuente de voltaje continua, el voltaje en sus
terminales aumenta de forma exponencial:

```text
Vc(t) = Vf · (1 - e^(-t / τ))
```

Donde:

- `Vc(t)` es el voltaje del capacitor en el instante `t`.
- `Vf` es el voltaje de la fuente.
- `t` es el tiempo transcurrido en segundos.
- `τ` es la constante de tiempo RC.

Ejemplo:

```python
from escuadra.modulos.electrica.circuitos_rc_rl import (
    calcular_constante_tiempo_rc,
    calcular_voltaje_carga_capacitor,
)

tau = calcular_constante_tiempo_rc(resistencia=1000, capacitancia=0.000001)
voltaje = calcular_voltaje_carga_capacitor(
    voltaje_fuente=5,
    tiempo=0.001,
    constante_tiempo=tau,
)
print(round(voltaje, 3))  # 3.161
```

El resultado muestra que, tras una constante de tiempo, el capacitor está cerca del 63.2
% de una fuente de `5 V`.

## Descarga exponencial de un capacitor

La descarga de un capacitor sigue la forma:

```text
Vc(t) = V0 · e^(-t / τ)
```

Donde `V0` es el voltaje inicial antes de descargar. La implementación actual documenta
esta relación para interpretar ejercicios, pero la función disponible en el módulo calcula
la carga del capacitor, no la descarga directa. Para estimar una descarga se debe aplicar
la fórmula manualmente hasta que exista una función específica.

## Circuitos RL

Un circuito RL combina una resistencia `R` y un inductor `L`. La constante de tiempo se
calcula con:

```text
τ = L / R
```

Donde:

- `L` se expresa en henrios (`H`).
- `R` se expresa en ohmios (`Ω`).
- `τ` se obtiene en segundos (`s`).

Ejemplo:

```python
from escuadra.modulos.electrica.circuitos_rc_rl import calcular_constante_tiempo_rl

tau = calcular_constante_tiempo_rl(resistencia=50, inductancia=0.2)
print(tau)  # 0.004 segundos
```

Una inductancia de `0.2 H` con una resistencia de `50 Ω` produce una constante de tiempo
de `0.004 s`, equivalente a `4 ms`.

## Carga y descarga en inductores

En un circuito RL conectado a una fuente continua, la corriente del inductor crece de
forma exponencial hacia su valor final:

```text
I(t) = If · (1 - e^(-t / τ))
```

Al desconectar la fuente y descargar la energía almacenada, la corriente disminuye:

```text
I(t) = I0 · e^(-t / τ)
```

La versión actual del módulo calcula la constante de tiempo RL. Las curvas de corriente
de carga y descarga se describen aquí para contextualizar el uso de `τ`, pero no tienen
una función dedicada en el código actual.

## Validaciones

Las funciones implementadas validan que:

- La resistencia sea mayor que cero.
- La capacitancia sea mayor que cero en circuitos RC.
- La inductancia sea mayor que cero en circuitos RL.
- El tiempo no sea negativo al calcular el voltaje de carga de un capacitor.
- La constante de tiempo usada en la carga del capacitor sea mayor que cero.

Si alguna condición no se cumple, se lanza `ValueError` para evitar resultados físicos
inválidos.

## Alcance actual

El módulo `src/escuadra/modulos/electrica/circuitos_rc_rl.py` incluye:

- `calcular_constante_tiempo_rc(resistencia, capacitancia)`
- `calcular_constante_tiempo_rl(resistencia, inductancia)`
- `calcular_voltaje_carga_capacitor(voltaje_fuente, tiempo, constante_tiempo)`

No reemplaza un simulador SPICE ni contempla efectos no ideales como resistencia serie
equivalente, saturación del inductor, tolerancias de componentes o fuentes variables en
el tiempo.
