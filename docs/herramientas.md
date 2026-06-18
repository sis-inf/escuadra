# Catálogo de herramientas de la suite Escuadra

Este documento describe las herramientas actualmente implementadas en la suite Escuadra. Todas las herramientas listadas corresponden a clases que implementan la interfaz base `Herramienta`.

## Herramientas disponibles

| Herramienta                       | Módulo      | Descripción                                                                                            | Comando CLI sugerido              |
| --------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------ | --------------------------------- |
| Calculadora científica            | Matemáticas | Calculadora con operaciones aritméticas, trigonométricas, logarítmicas y constantes matemáticas.       | `escuadra calculadora-cientifica` |
| Conversión de unidades            | Matemáticas | Convierte valores entre unidades de longitud, masa, tiempo y temperatura.                              | `escuadra conversion-unidades`    |
| Sistemas de ecuaciones lineales   | Matemáticas | Resuelve sistemas lineales de tamaño 2×2 hasta 5×5 mediante eliminación gaussiana con pivoteo parcial. | `escuadra sistemas-lineales`      |
| Ley de Ohm                        | Eléctrica   | Calcula voltaje, corriente o resistencia a partir de las otras dos magnitudes y obtiene la potencia.   | `escuadra ley-ohm`                |
| Divisor de tensión                | Eléctrica   | Calcula voltaje de salida o resistencias necesarias en un divisor de tensión.                          | `escuadra divisor-tension`        |
| Conversión de unidades eléctricas | Eléctrica   | Convierte entre unidades de potencia y energía.                                                        | `escuadra conversion-electrica`   |
| Conversión de bases               | Sistemas    | Convierte números entre decimal, binario, octal y hexadecimal.                                         | `escuadra conversion-bases`       |
| Complemento a 2                   | Sistemas    | Convierte entre enteros con signo y representación binaria en complemento a dos.                       | `escuadra complemento-a-2`        |
| Tablas de verdad                  | Sistemas    | Genera tablas de verdad para expresiones booleanas de hasta cuatro variables.                          | `escuadra tablas-verdad`          |
| Cálculo de áreas                  | Geometría   | Calcula el área de triángulos, círculos, rectángulos y trapecios.                                      | `escuadra calculo-area`           |

## Organización por módulo

## Matemáticas

#### Calculadora científica

Permite evaluar expresiones matemáticas utilizando:

* Operaciones aritméticas básicas.
* Potencias y raíces.
* Funciones trigonométricas.
* Logaritmos y logaritmos naturales.
* Constantes π y e.
* Modo angular en grados o radianes.

**Comando CLI sugerido:**

```bash
escuadra calculadora-cientifica --expresion "sin(45)+sqrt(16)"
```

#### Conversión de unidades

Permite convertir entre diferentes categorías de unidades:

* Longitud.
* Masa.
* Tiempo.
* Temperatura.

Incluye conversiones entre unidades métricas e imperiales.

**Comando CLI sugerido:**

```bash
escuadra conversion-unidades \
  --categoria longitud \
  --de km \
  --a m \
  --valor 3.5
```

#### Sistemas de ecuaciones lineales

Resuelve sistemas lineales cuadrados de tamaño entre 2×2 y 5×5 mediante eliminación gaussiana con pivoteo parcial.

Muestra la solución para cada incógnita del sistema.

**Comando CLI sugerido:**

```bash
escuadra sistemas-lineales \
  --matriz "2,1;5,7" \
  --vector "11,13"
```

## Eléctrica

#### Ley de Ohm

Calcula automáticamente:

* Voltaje (V).
* Corriente (I).
* Resistencia (R).
* Potencia (P).

A partir de dos magnitudes conocidas.

**Comando CLI sugerido:**

```bash
escuadra ley-ohm --corriente 5 --resistencia 10
```

#### Divisor de tensión

Permite:

* Calcular Vout.
* Calcular R1.
* Calcular R2.

Utilizando las ecuaciones de un divisor resistivo.

**Comando CLI sugerido:**

```bash
escuadra divisor-tension \
  --vin 12 \
  --r1 1000 \
  --r2 2200
```

#### Conversión de unidades eléctricas

Realiza conversiones entre:

**Potencia**

* W
* kW
* MW
* HP
* CV

**Energía**

* J
* kJ
* Wh
* kWh
* MJ

**Comando CLI sugerido:**

```bash
escuadra conversion-electrica \
  --categoria potencia \
  --de kW \
  --a HP \
  --valor 5
```

## Sistemas

#### Conversión de bases

Convierte números entre:

* Decimal.
* Binario.
* Octal.
* Hexadecimal.

Soporta números negativos.

**Comando CLI sugerido:**

```bash
escuadra conversion-bases \
  --base 10 \
  --valor 255
```

#### Complemento a 2

Permite convertir:

* Decimal → Complemento a 2.
* Complemento a 2 → Decimal.

Con tamaños de palabra de:

* 4 bits.
* 8 bits.
* 16 bits.
* 32 bits.

**Comando CLI sugerido:**

```bash
escuadra complemento-a-2 \
  --decimal -5 \
  --bits 8
```

#### Tablas de verdad

Genera tablas de verdad para expresiones booleanas utilizando operadores:

* AND
* OR
* NOT
* XOR

Admite hasta cuatro variables lógicas y permite copiar el resultado al portapapeles.

**Comando CLI sugerido:**

```bash
escuadra tablas-verdad \
  --expresion "A AND (B OR C)"
```

## Geometría

#### Cálculo de áreas

Calcula áreas de las siguientes figuras geométricas:

* Triángulo.
* Círculo.
* Rectángulo.
* Trapecio.

Los resultados se expresan en unidades cuadradas.

**Comando CLI sugerido:**

```bash
escuadra calculo-area \
  --figura circulo \
  --radio 5
```

## Leyenda de disponibilidad

Actualmente las herramientas documentadas se encuentran implementadas como componentes de la interfaz gráfica de Escuadra.

## Nota

Los comandos CLI mostrados corresponden a la convención de nomenclatura prevista para las herramientas de Escuadra. La disponibilidad real de cada comando depende de su integración en la interfaz de línea de comandos (CLI), la cual puede encontrarse en desarrollo.

## Contribuciones

Si deseas contribuir con nuevas herramientas o mejorar las existentes, consulta la documentación para contribuidores disponible en el directorio `CONTRIBUTING.md`.
