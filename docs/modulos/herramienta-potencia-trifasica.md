# Herramienta de Potencia Trifásica

## Descripción

La herramienta de potencia trifásica permite calcular la potencia activa, reactiva y aparente en sistemas eléctricos trifásicos utilizando valores de línea.

## Potencia monofásica y trifásica

### Sistema monofásico

Un sistema monofásico utiliza una única fase y es habitual en instalaciones residenciales y cargas de baja potencia.

La potencia activa se calcula mediante:

$$
P = V \cdot I \cdot \cos(\varphi)
$$

### Sistema trifásico

Un sistema trifásico utiliza tres fases desfasadas 120° entre sí, permitiendo una transmisión de energía más eficiente y una mejor distribución de cargas.

La potencia activa se calcula mediante:

$$
P = \sqrt{3} \cdot V_L \cdot I_L \cdot \cos(\varphi)
$$

Entre sus principales ventajas se encuentran:

- Mayor capacidad de transmisión de potencia.
- Menores pérdidas para una misma potencia transportada.
- Funcionamiento más eficiente de motores eléctricos.
- Distribución más uniforme de la carga.

## Tipos de conexión soportados

### Conexión estrella (Y)

En la conexión estrella, un extremo de cada fase se conecta a un punto común denominado neutro.

Características:

- Permite disponer de tensión de fase y tensión de línea.
- Es ampliamente utilizada en sistemas de distribución eléctrica.
- Facilita la alimentación de cargas monofásicas y trifásicas.

### Conexión triángulo (Δ)

En la conexión triángulo, las tres fases se conectan formando un circuito cerrado.

Características:

- No requiere conductor neutro.
- Es frecuente en motores y aplicaciones industriales.
- Proporciona una alta capacidad de entrega de potencia.

La implementación de Escuadra acepta ambos tipos de conexión mediante el parámetro `conexion`, con los valores `estrella` o `triangulo`.

## Fórmulas utilizadas

La herramienta calcula las tres magnitudes fundamentales de potencia en sistemas trifásicos equilibrados.

### Potencia aparente

La potencia aparente representa la potencia total suministrada por el sistema:

$$
S = \sqrt{3} \cdot V_L \cdot I_L
$$

donde:

- \(S\): potencia aparente (VA)
- \(V_L\): voltaje de línea (V)
- \(I_L\): corriente de línea (A)

### Potencia activa

La potencia activa corresponde a la energía que realiza trabajo útil:

$$
P = \sqrt{3} \cdot V_L \cdot I_L \cdot \cos(\varphi)
$$

donde:

- \(P\): potencia activa (W)
- \(\varphi\): ángulo de desfase entre tensión y corriente
- \(\cos(\varphi)\): factor de potencia

### Potencia reactiva

La potencia reactiva está asociada a los elementos inductivos y capacitivos del sistema:

$$
Q = \sqrt{3} \cdot V_L \cdot I_L \cdot \sin(\varphi)
$$

donde:

- \(Q\): potencia reactiva (VAR)

Estas expresiones son válidas tanto para conexiones estrella (Y) como triángulo (Δ) cuando se utilizan magnitudes de línea.

## Parámetros

| Parámetro | Descripción |
|------------|------------|
| voltaje_linea | Voltaje de línea en V |
| corriente_linea | Corriente de línea en A |
| factor_potencia | Valor entre 0 y 1 |
| conexion | estrella o triangulo |

## Resultado

La herramienta devuelve:

- potencia_activa (W)
- potencia_reactiva (VAR)
- potencia_aparente (VA)

## Validaciones

La herramienta genera errores cuando:

- voltaje_linea ≤ 0
- corriente_linea ≤ 0
- factor_potencia fuera del rango (0,1]
- conexión distinta de estrella o triangulo