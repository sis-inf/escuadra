# Herramienta: Figuras Compuestas

## Descripción

Las **figuras compuestas** son formas geométricas que se forman combinando dos o más figuras simples mediante operaciones de **suma** (unión) o **resta** (sustracción). Esta herramienta permite calcular el **área** y el **volumen** de dichas figuras.

---

## Conceptos Clave

| Operación | Descripción |
|-----------|-------------|
| **Suma** | Se añade una figura simple a otra. El área/volumen total es la suma de las partes. |
| **Resta** | Se extrae una figura simple de otra. El área/volumen total es la diferencia entre las partes. |

---

## Cálculo de Área

### Fórmula General
Área_compuesta = Área_figura1 ± Área_figura2 ± ... ± Área_figuraN

- Usa `+` cuando la figura se **agrega**.
- Usa `-` cuando la figura se **sustrae** (es un hueco o recorte).

---

## Ejemplo: Figura Compuesta (Suma y Resta)

### Descripción de la figura

1. Se parte de un **rectángulo grande** (figura base).
2. Se **resta** un rectángulo pequeño en una esquina (para formar la L).
3. Se **resta** un cuadrado interior (el agujero).

### Datos del ejemplo

| Figura | Tipo | Dimensiones | Operación |
|--------|------|-------------|-----------|
| Rectángulo base | Rectángulo | 10 m × 8 m | + (suma) |
| Recorte esquina | Rectángulo | 4 m × 3 m | − (resta) |
| Agujero interior | Cuadrado | 2 m × 2 m | − (resta) |

### Cálculo paso a paso
Área_base      = 10 × 8 = 80 m²

Área_recorte   = 4 × 3  = 12 m²

Área_agujero   = 2 × 2  =  4 m²

Área_compuesta = 80 - 12 - 4 = 64 m²

**Resultado: 64 m²**

---

## Cálculo de Volumen

### Fórmula General
Volumen_compuesto = Volumen_sólido1 ± Volumen_sólido2 ± ... ± Volumen_sólidoN

### Ejemplo: Bloque con cavidad cilíndrica

| Sólido | Tipo | Dimensiones | Operación |
|--------|------|-------------|-----------|
| Prisma rectangular | Cuboid | 6 m × 4 m × 3 m | + (suma) |
| Cavidad cilíndrica | Cilindro | radio = 1 m, altura = 3 m | − (resta) |
Volumen_prisma    = 6 × 4 × 3 = 72 m³

Volumen_cilindro  = π × 1² × 3 ≈ 9.42 m³
Volumen_compuesto = 72 - 9.42 ≈ 62.58 m³

**Resultado: ≈ 62.58 m³**

---

## Uso en el sistema

```python
from figuras import Rectangulo, Cuadrado, FiguraCompuesta

base     = Rectangulo(ancho=10, alto=8)
recorte  = Rectangulo(ancho=4, alto=3)
agujero  = Cuadrado(lado=2)

figura = FiguraCompuesta()
figura.agregar(base)
figura.restar(recorte)
figura.restar(agujero)

print(figura.area())  # → 64.0
```