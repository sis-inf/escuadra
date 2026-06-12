# Guía Teórica del Módulo Civil

Este documento presenta los fundamentos teóricos utilizados en el módulo civil para el cálculo estructural de vigas y elementos de construcción. Las fórmulas y conceptos presentados se basan en la teoría clásica de resistencia de materiales y constituyen la base para los cálculos implementados en el software.

## Viga Simplemente Apoyada

Una viga simplemente apoyada es un elemento estructural horizontal soportado en sus extremos mediante apoyos simples que permiten rotación pero restringen la traslación vertical. Esta configuración es fundamental en el análisis estructural debido a su simplicidad y amplia aplicación en la construcción.

**Condiciones de apoyo:**
- Apoyo izquierdo: restricción de desplazamiento vertical, libre rotación
- Apoyo derecho: restricción de desplazamiento vertical, libre rotación
- No existe restricción al desplazamiento horizontal (a menos que se considere fricción)

**Diagrama de apoyos:**
```
    ◯─────────────────────────◯
    ↑                         ↑
   R1                        R2
```

Donde los círculos representan apoyos simples y las flechas indican las reacciones verticales. Esta configuración permite que la viga se flexione bajo carga sin generar momentos flectores en los apoyos.

## Carga Puntual Central

Cuando se aplica una carga puntual $P$ en el centro de una viga simplemente apoyada de longitud $L$, se generan esfuerzos internos que pueden calcularse mediante las siguientes expresiones:

**Momento flector máximo:**
$$ M_{max} = \frac{P \cdot L}{4} $$

Este momento se presenta en el punto medio de la viga, donde la carga es aplicada. El momento flector es el responsable principal de las tensiones de flexión en la sección transversal.

**Fuerza cortante:**
$$ V = \frac{P}{2} $$

La fuerza cortante es constante en cada tramo de la viga y cambia de signo en el punto de aplicación de la carga. En los apoyos, la cortante es igual a las reacciones verticales.

**Diagrama de cortante:**
```
    P/2 │           │ P/2
        │           │
        │     ↓     │
   ─────┼───────────┼────
        │           │
   -P/2 │           │ -P/2
```

**Diagrama de momento:**
```
    M_max
      │
      │     ╱╲
      │    ╱  ╲
   ───┼───╱────╲───
      │  ╱      ╲
      │ ╱        ╲
      0
```

**Limitaciones:** Estas fórmulas asumen que la carga se aplica exactamente en el centro de la viga y que el material se comporta de manera lineal elástica. No consideran efectos de segundo orden ni deformaciones grandes.

## Carga Distribuida Uniforme

Para una carga distribuida uniforme $w$ (fuerza por unidad de longitud) que actúa sobre toda la longitud de la viga, las expresiones de cálculo son:

**Reacciones en los apoyos:**
$$ R_1 = R_2 = \frac{w \cdot L}{2} $$

Las reacciones son iguales debido a la simetría de la carga y la configuración de apoyos. Cada apoyo soporta exactamente la mitad de la carga total aplicada.

**Momento flector máximo:**
$$ M_{max} = \frac{w \cdot L^2}{8} $$

El momento máximo se presenta en el centro de la viga, al igual que en el caso de carga puntual central. Esta expresión se obtiene integrando la ecuación diferencial de la elástica.

**Fuerza cortante:** La cortante varía linealmente desde $+\frac{w \cdot L}{2}$ en el apoyo izquierdo hasta $-\frac{w \cdot L}{2}$ en el apoyo derecho, siendo nula en el centro de la viga.

**Diagrama de cortante:**
```
    wL/2│
       │╲
       │ ╲
   ────┼──╲────
       │   ╲
       │    ╲
   -wL/2│
```

**Diagrama de momento:**
```
    M_max
      │
      │   ╱──╲
      │  ╱    ╲
   ───┼─╱──────╲──
      │╱        ╲
      0
```

## Deflexión Elástica

La deflexión elástica de una viga se basa en la hipótesis de Euler-Bernoulli, que establece las siguientes suposiciones fundamentales:

**Hipótesis de Euler-Bernoulli:**
1. Las secciones transversales planas permanecen planas después de la deformación
2. Las secciones transversales permanecen perpendiculares al eje neutro de la viga
3. El material es homogéneo, isotrópico y se comporta de manera lineal elástica
4. Las deformaciones son pequeñas (teoría de primer orden)
5. No se consideran efectos de cortante en la deflexión (vigas esbeltas)

**Deflexión máxima para carga puntual central:**
$$ \delta_{max} = \frac{P \cdot L^3}{48 \cdot E \cdot I} $$

**Deflexión máxima para carga distribuida uniforme:**
$$ \delta_{max} = \frac{5 \cdot w \cdot L^4}{384 \cdot E \cdot I} $$

Donde:
- $E$ es el módulo de elasticidad del material (Pa)
- $I$ es el momento de inercia de la sección transversal (m⁴)
- $\delta_{max}$ es la deflexión máxima en el centro de la viga (m)

**Limitaciones:** Estas fórmulas no son válidas para vigas cortas donde los efectos de cortante son significativos, ni para materiales con comportamiento no lineal. Tampoco consideran la deformación por cortante ni los efectos de segundo orden (P-delta).

## Área de Sección Transversal

El área de la sección transversal $A$ es un parámetro geométrico fundamental en el diseño estructural que influye en múltiples aspectos del comportamiento del elemento:

**Importancia en el diseño:**

1. **Resistencia axial:** El área determina la capacidad del elemento para resistir cargas axiales de compresión o tracción. El esfuerzo axial se calcula como:
$$ \sigma = \frac{N}{A} $$
donde $N$ es la fuerza axial y $\sigma$ es el esfuerzo normal.

2. **Rigidez axial:** La rigidez axial del elemento depende directamente del área y del módulo de elasticidad:
$$ k_{axial} = \frac{E \cdot A}{L} $$

3. **Peso propio:** El área de la sección, junto con la densidad del material $\rho$, determina el peso por unidad de longitud:
$$ w_{propio} = \rho \cdot A \cdot g $$

4. **Interacción con otros parámetros:** Aunque el área no aparece directamente en las fórmulas de momento flector o deflexión, influye indirectamente a través del momento de inercia $I$, que depende de la distribución del área alrededor del eje neutro.

**Consideraciones de diseño:** Al seleccionar el área de la sección, se debe buscar un equilibrio entre resistencia, rigidez y peso. Un área excesiva puede resultar en un elemento sobredimensionado con mayor costo y peso, mientras que un área insuficiente puede comprometer la seguridad estructural.

**Limitaciones:** El área por sí sola no es suficiente para caracterizar completamente el comportamiento a flexión de una sección. Para análisis de flexión, es necesario considerar también el momento de inercia y el módulo de sección, que dependen de la forma y distribución del área, no solo de su magnitud.
