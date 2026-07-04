# Módulo de Resolución de Triángulos

## Descripción

La **resolución de triángulos** consiste en encontrar los lados y ángulos desconocidos de un triángulo a partir de datos conocidos. Este módulo implementa dos leyes fundamentales:

- **Ley de cosenos:** para cuando se conocen 3 lados (SSS) o 2 lados y el ángulo entre ellos (SAS).
- **Ley de senos:** para cuando se conoce 1 lado y 2 ángulos (AAS o ASA).

---

## Fórmulas

### Ley de Cosenos
a² = b² + c² - 2·b·c·cos(A)
b² = a² + c² - 2·a·c·cos(B)
c² = a² + b² - 2·a·b·cos(C)

### Ley de Senos
a / sen(A) = b / sen(B) = c / sen(C)

---

## Ejemplos de uso

### Ejemplo 1: 3 lados conocidos (SSS) — Ley de Cosenos

**Enunciado:** Dado un triángulo con lados `a = 7`, `b = 5`, `c = 8`, encontrar todos los ángulos.

**Datos:**
- a = 7, b = 5, c = 8

**Desarrollo:**

1. **Calcular ángulo A:**
   - `cos(A) = (b² + c² - a²) / (2·b·c)`
   - `cos(A) = (25 + 64 - 49) / (2·5·8) = 40 / 80 = 0.5`
   - `A = arccos(0.5) = 60°`

2. **Calcular ángulo B:**
   - `cos(B) = (a² + c² - b²) / (2·a·c)`
   - `cos(B) = (49 + 64 - 25) / (2·7·8) = 88 / 112 ≈ 0.7857`
   - `B = arccos(0.7857) ≈ 38.21°`

3. **Calcular ángulo C:**
   - `C = 180° - A - B = 180° - 60° - 38.21° = 81.79°`

**Resultados:** `A = 60°`, `B ≈ 38.21°`, `C ≈ 81.79°`

---

### Ejemplo 2: 1 lado y 2 ángulos conocidos (AAS) — Ley de Senos

**Enunciado:** Dado un triángulo con `a = 10`, `A = 45°`, `B = 60°`, encontrar los lados y ángulo restantes.

**Datos:**
- a = 10, A = 45°, B = 60°

**Desarrollo:**

1. **Calcular ángulo C:**
   - `C = 180° - A - B = 180° - 45° - 60° = 75°`

2. **Calcular lado b:**
   - `b / sen(B) = a / sen(A)`
   - `b = a · sen(B) / sen(A)`
   - `b = 10 · sen(60°) / sen(45°)`
   - `b = 10 · 0.8660 / 0.7071 ≈ 12.25`

3. **Calcular lado c:**
   - `c = a · sen(C) / sen(A)`
   - `c = 10 · sen(75°) / sen(45°)`
   - `c = 10 · 0.9659 / 0.7071 ≈ 13.66`

**Resultados:** `C = 75°`, `b ≈ 12.25`, `c ≈ 13.66`

---

## Uso en el sistema

```python
from herramientas import resolucion_triangulos

# SSS: 3 lados conocidos
resultado = resolucion_triangulos.sss(a=7, b=5, c=8)
print(resultado)  # → {A: 60°, B: 38.21°, C: 81.79°}

# AAS: 1 lado y 2 ángulos conocidos
resultado = resolucion_triangulos.aas(a=10, A=45, B=60)
print(resultado)  # → {C: 75°, b: 12.25, c: 13.66}
```