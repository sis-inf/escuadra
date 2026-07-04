# Herramienta: Transformaciones Geométricas 2D

## Descripción

Las transformaciones geométricas permiten modificar la posición, orientación o tamaño de una figura en un plano cartesiano mediante operaciones matemáticas sobre sus coordenadas.

Las transformaciones fundamentales documentadas son:

- Traslación
- Rotación
- Escala

Estas operaciones son ampliamente utilizadas en geometría analítica, gráficos por computadora, CAD, ingeniería y modelado matemático.

---

# Transformación por Traslación

## Descripción

La traslación desplaza todos los puntos de una figura la misma distancia y en la misma dirección.

La forma y el tamaño de la figura permanecen sin cambios.

## Fórmulas

```
x' = x + dx

y' = y + dy
```

Donde:

- `(x,y)` es el punto original.
- `(dx,dy)` representa el desplazamiento.
- `(x',y')` es el nuevo punto.

## Ejemplo

Punto inicial

```
(3,2)
```

Desplazamiento

```
dx = 4
dy = -1
```

Resultado

```
(7,1)
```

---

# Transformación por Rotación

## Descripción

La rotación consiste en girar una figura alrededor de un punto fijo, normalmente el origen del sistema de coordenadas.

Durante la rotación:

- Las distancias entre los puntos permanecen constantes.
- La figura conserva su tamaño y forma.
- Solo cambia su orientación.

## Fórmulas

Para una rotación de un ángulo θ alrededor del origen:

```
x' = x cos(θ) − y sin(θ)

y' = x sin(θ) + y cos(θ)
```

## Ejemplo

Punto inicial

```
(2,1)
```

Rotación

```
90°
```

Resultado

```
(-1,2)
```

---

# Transformación por Escala

## Descripción

La escala modifica el tamaño de una figura multiplicando las coordenadas por uno o más factores de escala.

Puede:

- ampliar una figura;
- reducir una figura;
- deformarla si los factores son diferentes.

## Fórmulas

```
x' = sx · x

y' = sy · y
```

Donde:

- `sx` es el factor de escala horizontal.
- `sy` es el factor de escala vertical.

## Ejemplo

Punto inicial

```
(3,2)
```

Factores

```
sx = 2

sy = 3
```

Resultado

```
(6,6)
```

---

# Comparación de las transformaciones

| Transformación | Cambia posición | Cambia orientación | Cambia tamaño |
|----------------|-----------------|--------------------|----------------|
| Traslación | Sí | No | No |
| Rotación | Sí | Sí | No |
| Escala | Sí | No | Sí |

---

# Aplicaciones

Las transformaciones geométricas son utilizadas en:

- diseño asistido por computadora (CAD);
- gráficos por computadora;
- modelado geométrico;
- ingeniería civil;
- arquitectura;
- procesamiento de imágenes.

---

# Observaciones

Las transformaciones pueden combinarse para producir movimientos más complejos.

El orden en que se aplican las transformaciones modifica el resultado final.

Esta documentación describe los fundamentos matemáticos de las transformaciones geométricas 2D mediante ejemplos ilustrativos.