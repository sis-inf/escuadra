# Herramienta: Cálculo de carga crítica de pandeo de Euler

## Introducción

En el ámbito de ingeniería y mecánica de sólidos, la herramienta de cálculo de carga crítica de pandeo permite determinar la carga máxima que puede soportar una columna antes de perder estabilidad por pandeo.

Esta carga es el límite máximo que una pieza puede soportar antes de sufrir deformaciones laterales severas e inestabilidad elástica.

Este cálculo se basa en la teoría de Euler, utilizada para columnas largas sometidas a compresión axial.

---

# Fórmula de Euler

La carga crítica se calcula mediante:

\[
P_{cr}=\frac{\pi^2EI}{(KL)^2}
\]

Donde:

- **Pcr:** carga crítica.
- **E:** módulo de elasticidad del material.
- **I:** momento de inercia de la sección.
- **L:** longitud de la columna.
- **K:** factor de longitud efectiva según el tipo de apoyo.

---

# Condiciones de apoyo soportadas

## 1. Articulada - Articulada

- Factor K = 1.0
- Es la condición clásica utilizada por Euler.

---

## 2. Empotrada - Libre

- Factor K = 2.0
- Representa una columna en voladizo.

---

## 3. Empotrada - Articulada

- Factor K ≈ 0.7
- La columna posee un extremo fijo y otro articulado.

---

## 4. Empotrada - Empotrada

- Factor K = 0.5
- Presenta la mayor resistencia al pandeo.

---

# Ejemplo de uso

Supóngase una columna con:

- Longitud: 3 m
- Módulo de elasticidad: 200 GPa
- Momento de inercia: 8 × 10⁻⁶ m⁴
- Apoyos articulados

La herramienta aplica la fórmula de Euler para obtener la carga crítica correspondiente.

---

# Resultado esperado

La herramienta muestra:

- Carga crítica de pandeo.
- Tipo de apoyo seleccionado.
- Factor K utilizado.
- Datos ingresados por el usuario.

---

# Aplicaciones

Este cálculo puede utilizarse en:

- Diseño estructural.
- Ingeniería civil.
- Diseño de columnas metálicas.
- Diseño de columnas de hormigón.
- Análisis de estabilidad estructural.

---

# Observaciones

La fórmula de Euler es válida principalmente para columnas largas y esbeltas sometidas a carga axial de compresión. 
