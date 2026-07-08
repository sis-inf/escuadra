# Herramienta: Combinación de Cargas (LRFD Simplificado)

## Descripción

La herramienta **Combinación de Cargas (LRFD Simplificado)** permite estimar una carga de diseño a partir de la combinación de cargas muertas y cargas vivas utilizando una versión simplificada del método **LRFD (Load and Resistance Factor Design)**.

Está orientada a fines educativos y de aprendizaje, facilitando la comprensión de los conceptos básicos utilizados en el diseño estructural.

---

## Parámetros de entrada

La herramienta requiere los siguientes datos:

| Parámetro        | Descripción                                        | Unidad |
| ---------------- | -------------------------------------------------- | ------ |
| Carga muerta (D) | Peso permanente de la estructura y elementos fijos | kN     |
| Carga viva (L)   | Cargas variables asociadas al uso de la estructura | kN     |

---

## Método utilizado

La carga de diseño se calcula mediante la combinación:

```text
U = 1.2D + 1.6L
```

donde:

* **U** = carga factorizada de diseño.
* **D** = carga muerta.
* **L** = carga viva.

---

## Ejemplo

### Datos de entrada

| Parámetro        | Valor  |
| ---------------- | ------ |
| Carga muerta (D) | 100 kN |
| Carga viva (L)   | 50 kN  |

### Cálculo

```text
U = 1.2(100) + 1.6(50)
U = 120 + 80
U = 200 kN
```

### Resultado

| Magnitud            | Valor  |
| ------------------- | ------ |
| Carga de diseño (U) | 200 kN |

---

## Interpretación del resultado

La carga obtenida representa una estimación simplificada de la carga factorizada utilizada para fines de análisis y aprendizaje de conceptos básicos de diseño estructural.

---

## Importante

> **Esta herramienta tiene fines exclusivamente educativos.**
>
> El cálculo implementado corresponde a una versión simplificada del método LRFD y **no reemplaza la normativa estructural vigente**, los reglamentos locales, ni el criterio profesional de un ingeniero civil o estructural.
>
> Para proyectos reales deben utilizarse las normas y reglamentos aplicables en la jurisdicción correspondiente, considerando todas las combinaciones de carga y factores exigidos por la normativa vigente.

---

## Limitaciones

* Considera únicamente cargas muertas y cargas vivas.
* No incluye cargas sísmicas.
* No incluye cargas de viento.
* No contempla combinaciones avanzadas de diseño.
* No sustituye procedimientos de diseño estructural profesional.
