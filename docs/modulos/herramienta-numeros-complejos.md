# Módulo de Números Complejos

## Descripción

Un **número complejo** es un número de la forma `a + bi`, donde `a` es la parte real, `b` es la parte imaginaria e `i` es la unidad imaginaria (`i² = -1`). Este módulo soporta operaciones aritméticas y conversión entre forma rectangular y polar.

---

## Operaciones soportadas

| Operación | Descripción |
|-----------|-------------|
| Suma | `(a+bi) + (c+di) = (a+c) + (b+d)i` |
| Resta | `(a+bi) - (c+di) = (a-c) + (b-d)i` |
| Multiplicación | `(a+bi)(c+di) = (ac-bd) + (ad+bc)i` |
| División | `(a+bi)/(c+di) = ((ac+bd)/(c²+d²)) + ((bc-ad)/(c²+d²))i` |
| Módulo | `|z| = √(a² + b²)` |
| Conjugado | `z* = a - bi` |

---

## Conversión Rectangular ↔ Polar

### Rectangular a Polar
|z| = √(a² + b²)

θ   = arctan(b / a)

### Polar a Rectangular
a = |z| · cos(θ)

b = |z| · sen(θ)

---

## Ejemplos de uso

### Ejemplo 1: Suma y resta de números complejos

**Enunciado:** Dados `z1 = 3 + 4i` y `z2 = 1 - 2i`, calcular `z1 + z2` y `z1 - z2`.

**Desarrollo:**

1. **Suma:**
   - Parte real: 3 + 1 = 4
   - Parte imaginaria: 4 + (-2) = 2
   - Resultado: `4 + 2i`

2. **Resta:**
   - Parte real: 3 - 1 = 2
   - Parte imaginaria: 4 - (-2) = 6
   - Resultado: `2 + 6i`

**Resultados:** `z1 + z2 = 4 + 2i`, `z1 - z2 = 2 + 6i`

---

### Ejemplo 2: Conversión de rectangular a polar

**Enunciado:** Convertir `z = 3 + 4i` a forma polar.

**Datos:**
- Parte real: a = 3
- Parte imaginaria: b = 4

**Desarrollo:**

1. **Calcular el módulo:**
   - `|z| = √(3² + 4²) = √(9 + 16) = √25 = 5`

2. **Calcular el ángulo:**
   - `θ = arctan(4 / 3) ≈ 53.13°`

3. **Forma polar:**
   - `z = 5 ∠ 53.13°`

**Resultado:** `z = 5 ∠ 53.13°`

---

### Ejemplo 3: Conversión de polar a rectangular

**Enunciado:** Convertir `z = 10 ∠ 30°` a forma rectangular.

**Datos:**
- Módulo: |z| = 10
- Ángulo: θ = 30°

**Desarrollo:**

1. **Parte real:**
   - `a = 10 · cos(30°) = 10 · 0.866 = 8.66`

2. **Parte imaginaria:**
   - `b = 10 · sen(30°) = 10 · 0.5 = 5`

3. **Forma rectangular:**
   - `z = 8.66 + 5i`

**Resultado:** `z = 8.66 + 5i`

---

## Uso en el sistema

```python
from herramientas import numeros_complejos

z1 = numeros_complejos.crear(3, 4)
z2 = numeros_complejos.crear(1, -2)

print(numeros_complejos.sumar(z1, z2))       # → 4 + 2i
print(numeros_complejos.restar(z1, z2))      # → 2 + 6i
print(numeros_complejos.a_polar(z1))         # → (5, 53.13°)
print(numeros_complejos.a_rectangular(5, 53.13))  # → 3 + 4i
```