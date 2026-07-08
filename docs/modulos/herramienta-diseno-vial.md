# Herramienta: Diseño Vial Básico

## Descripción

La herramienta **Diseño Vial Básico** permite realizar cálculos simplificados de **pendientes longitudinales** y **peraltes** empleados en el diseño preliminar de carreteras y caminos.

Su propósito es apoyar el aprendizaje de conceptos básicos de ingeniería vial mediante ejemplos sencillos y resultados fáciles de interpretar.

---

# Cálculo de pendientes

La pendiente longitudinal expresa la variación de altura respecto a la distancia recorrida.

Se calcula mediante la expresión:

```text
Pendiente (%) = (Desnivel / Distancia horizontal) × 100
```

## Parámetros de entrada

| Parámetro            | Descripción                           | Unidad |
| -------------------- | ------------------------------------- | ------ |
| Desnivel             | Diferencia de altura entre dos puntos | m      |
| Distancia horizontal | Longitud horizontal del tramo         | m      |

---

## Ejemplo de cálculo de pendiente

### Datos

| Parámetro            | Valor |
| -------------------- | ----- |
| Desnivel             | 6 m   |
| Distancia horizontal | 120 m |

### Cálculo

```text
Pendiente = (6 / 120) × 100
Pendiente = 5 %
```

### Resultado

La pendiente del tramo es:

**5 %**

---

# Cálculo de peralte

El peralte es la inclinación transversal de la calzada utilizada para mejorar la estabilidad de los vehículos al recorrer una curva.

En una aproximación simplificada puede calcularse mediante:

```text
e = V² / (127 × R)
```

donde:

* **e** = peralte.
* **V** = velocidad de diseño (km/h).
* **R** = radio de la curva (m).

---

## Parámetros de entrada

| Parámetro           | Descripción                          | Unidad |
| ------------------- | ------------------------------------ | ------ |
| Velocidad de diseño | Velocidad considerada para el diseño | km/h   |
| Radio de la curva   | Radio de la curva horizontal         | m      |

---

## Ejemplo de cálculo de peralte

### Datos

| Parámetro | Valor   |
| --------- | ------- |
| Velocidad | 60 km/h |
| Radio     | 250 m   |

### Cálculo

```text
e = 60² / (127 × 250)

e = 3600 / 31750

e = 0.113
```

Expresado como porcentaje:

```text
Peralte = 11.3 %
```

### Resultado

El peralte calculado es aproximadamente:

**11.3 %**

---

# Interpretación de resultados

* Una **pendiente** elevada puede dificultar la circulación y aumentar el consumo de combustible de los vehículos.
* Un **peralte** adecuado mejora la estabilidad durante el recorrido de curvas y contribuye a la seguridad vial.

Los resultados obtenidos permiten comprender la influencia de estos parámetros en un diseño vial básico.

---

# Consideraciones

* La herramienta utiliza un modelo simplificado con fines educativos.
* No contempla todas las variables consideradas en proyectos reales de ingeniería vial.
* Para el diseño definitivo deben utilizarse las normas y reglamentos técnicos vigentes de la jurisdicción correspondiente.
