# Catálogo de herramientas de la suite Escuadra

Este documento describe las herramientas que componen la suite Escuadra, diseñada para resolver problemas de ingeniería y análisis numérico.

## Herramientas disponibles

| Herramienta | Descripción | Propósito | Estado |
|-------------|-------------|-----------|--------|
| **Solucionador de ecuaciones lineales 2x2** | Resuelve sistemas de dos ecuaciones lineales con dos incógnitas | Encontrar valores de x e y que satisfagan ambas ecuaciones | Listo |
| **Método de bisección** | Encuentra raíces de funciones continuas mediante intervalos | Resolver ecuaciones no lineales | Listo |
| **Método de Newton-Raphson** | Aproxima raíces usando derivadas | Resolver ecuaciones no lineales con convergencia rápida | En progreso |
| **Derivación numérica** | Calcula derivadas aproximadas usando diferencias finitas | Análisis de tasas de cambio sin función analítica | Listo |
| **Integración numérica** | Aproxima integrales definidas mediante métodos como Simpson o trapecio | Calcular áreas bajo curvas | Pendiente |
| **Interpolación polinomial** | Encuentra polinomios que pasan por puntos dados | Estimar valores entre datos conocidos | Pendiente |
| **Regresión lineal** | Ajusta una recta a un conjunto de datos | Modelar relaciones lineales entre variables | En progreso |

## Problemas de ingeniería que resuelve cada herramienta

### Solucionador de ecuaciones lineales 2x2
Resuelve problemas de equilibrio en sistemas físicos, circuitos eléctricos (leyes de Kirchhoff) y análisis estructural.

### Método de bisección
Útil para encontrar raíces en problemas de ingeniería civil (análisis de vigas), mecánica (puntos de equilibrio) y termodinámica.

### Método de Newton-Raphson
Aplicable en problemas de flujo de carga en sistemas eléctricos, análisis de redes y optimización de procesos.

### Derivación numérica
Permite calcular velocidades y aceleraciones en sistemas mecánicos a partir de datos de posición.

### Integración numérica
Útil para calcular momentos de inercia, trabajo mecánico, flujo de calor y áreas en diseños de ingeniería.

### Interpolación polinomial
Ayuda a estimar valores intermedios en experimentos, como resistencia de materiales a temperaturas no medidas.

### Regresión lineal
Permite predecir comportamientos y tendencias en datos experimentales, como correlación entre esfuerzo y deformación.
## Herramientas de geometría

### calculo_area

Calcula el área de figuras geométricas.

**Fórmulas:**

- Cuadrado: A = lado²
- Rectángulo: A = largo × ancho
- Triángulo: A = (base × altura) / 2
- Círculo: A = π × radio²

**Unidades de entrada:** unidades de longitud (m, cm, km, etc.)

**Unidades de salida:** unidades cuadradas (m², cm², km², etc.)

**Ejemplo de invocación:**

```python
area_rectangulo(10, 5)
# Resultado: 50
```

### volumen

Calcula el volumen de sólidos geométricos.

**Fórmulas:**

- Cubo: V = lado³
- Esfera: V = (4/3) × π × radio³
- Cilindro: V = π × radio² × altura
- Cono: V = (1/3) × π × radio² × altura
- Paralelepípedo: V = largo × ancho × alto

**Unidades de entrada:** unidades de longitud (m, cm, km, etc.)

**Unidades de salida:** unidades cúbicas (m³, cm³, km³, etc.)

**Ejemplo de invocación:**

```python
volumen_cubo(4)
# Resultado: 64
```

### perimetro

Calcula el perímetro de figuras geométricas.

**Fórmulas:**

- Círculo: P = 2πr
- Cuadrado: P = 4 × lado
- Rectángulo: P = 2 × (largo + ancho)
- Triángulo: P = a + b + c
- Hexágono regular: P = 6 × lado

**Unidades de entrada:** unidades de longitud (m, cm, km, etc.)

**Unidades de salida:** unidades de longitud (m, cm, km, etc.)

**Ejemplo de invocación:**

```python
perimetro_cuadrado(5)
# Resultado: 20
```
## Leyenda de estados

- **Listo** - Herramienta implementada y probada
- **En progreso** - En desarrollo activo
- **Pendiente** - Planificada para futuras versiones

## Contribuciones

Si deseas contribuir con nuevas herramientas o mejorar las existentes, consulta la guía de contribución en `docs/flujo-git.md`.
