# Módulo de Ingeniería Civil

## Descripción

Este módulo está enfocado en el análisis de estructuras y cálculo estático, específicamente diseñado para aplicaciones en ingeniería civil. Proporciona herramientas fundamentales para el análisis y diseño de elementos estructurales como vigas, columnas y losas, permitiendo a ingenieros y estudiantes realizar cálculos de resistencia de materiales, mecánica estructural y análisis de cargas. El módulo cubre desde el cálculo de reacciones en apoyos hasta la determinación de momentos flectores, deflexiones y propiedades geométricas de secciones transversales, siendo esencial para el diseño seguro y eficiente de estructuras en edificaciones, puentes y obras civiles en general.

## Fundamentos Teóricos

Las vigas simplemente apoyadas son elementos estructurales fundamentales en ingeniería civil que se caracterizan por tener dos apoyos simples: uno en cada extremo, que permiten rotación pero restringen el desplazamiento vertical. Estas vigas son ampliamente utilizadas en construcción debido a su simplicidad estructural y eficiencia en la transferencia de cargas. Los apoyos simples pueden ser rodillos o articulaciones, donde los rodillos permiten movimiento horizontal mientras que las articulaciones lo restringen. Las aplicaciones típicas incluyen vigas de entrepiso en edificios, vigas de puente de luz simple, y elementos estructurales en marcos de acero o concreto. El análisis de vigas simplemente apoyadas es el punto de partida para entender comportamientos más complejos en estructuras hiperestáticas.

El momento flector es una magnitud fundamental en el análisis estructural que representa la tendencia de una fuerza a causar rotación en una sección de la viga. Se define como el producto de una fuerza por su distancia perpendicular al eje de rotación, y se calcula integrando las fuerzas a un lado de la sección considerada. El momento flector varía a lo largo de la longitud de la viga y alcanza valores máximos en puntos críticos como el centro de vigas simplemente apoyadas con carga puntual central. Los diagramas de momento flector son representaciones gráficas que muestran cómo varía el momento a lo largo de la viga, siendo herramientas esenciales para identificar secciones críticas donde el momento es máximo y donde se requiere mayor refuerzo o dimensionamiento. El signo del momento flector indica la dirección de la curvatura: positivo cuando causa compresión en la fibra superior y tracción en la inferior.

La deflexión en vigas es el desplazamiento vertical que experimenta una viga cuando está sometida a cargas, y es un parámetro crítico en el diseño estructural ya que afecta tanto la funcionalidad como la estética de la estructura. La deflexión está directamente relacionada con el momento flector a través de la ecuación diferencial de la curva elástica: EI·d²v/dx² = M(x), donde E es el módulo de elasticidad del material, I es el momento de inercia de la sección, y v es la deflexión. Una deflexión excesiva puede causar problemas como agrietamiento en elementos no estructurales, incomodidad para los ocupantes, y mal funcionamiento de equipos sensibles. Los códigos de construcción establecen límites máximos de deflexión típicamente como fracciones de la luz de la viga (L/240, L/360, L/480) dependiendo del uso de la estructura. El cálculo preciso de deflexiones es especialmente importante en vigas de gran luz, materiales con módulo de elasticidad bajo, o cuando se requieren tolerancias estrictas.

## Herramientas disponibles

| Herramienta | Fórmulas usadas | Parámetros de entrada |
|-------------|----------------|----------------------|
| `viga` | Ecuaciones de equilibrio estático, ΣF=0, ΣM=0 | Longitud, apoyos, cargas |
| `momento_flector` | M(x) = R_A·x - P·(x-a) - w·x²/2 | Distancia, reacciones, cargas puntuales/distribuidas |
| `deflexion_viga` | δ = (P·L³)/(48·E·I) (viga simplemente apoyada, carga puntual central) | Carga, longitud, módulo de Young, momento de inercia |
| `area_seccion` | A = b·h (rectangular), A = π·d²/4 (circular) | Base, altura, diámetro |
| `carga_distribuida` | w = F/L, V(x) = R_A - w·x, M(x) = R_A·x - w·x²/2 | Fuerza total, longitud, tipo de distribución |
| `momento_inercia` | I = (b·h³)/12 (rectangular), I = (π·d⁴)/64 (circular) | Base, altura, diámetro |

## Ejemplos completos

### Ejemplo 1: Viga simplemente apoyada con carga puntual central

**Enunciado:** Una viga de acero simplemente apoyada de 6 metros de longitud está sometida a una carga puntual de 10 kN aplicada en el centro de la viga. Determine las reacciones en los apoyos, el momento flector máximo y la deflexión máxima. Considere que el acero tiene un módulo de elasticidad de 200 GPa y la sección transversal de la viga tiene un momento de inercia de 8.33×10⁶ mm⁴.

**Datos:**
- Longitud de la viga (L): 6 m
- Carga puntual (P): 10 kN = 10,000 N
- Módulo de elasticidad del acero (E): 200 GPa = 200×10⁹ Pa = 200×10³ N/mm²
- Momento de inercia (I): 8.33×10⁶ mm⁴
- Posición de la carga: centro de la viga (x = L/2 = 3 m)

**Desarrollo:**

1. **Cálculo de reacciones en los apoyos:**
   Por simetría, la carga puntual central se distribuye equitativamente entre los dos apoyos.
   - ΣF_y = 0: R_A + R_B - P = 0
   - Por simetría: R_A = R_B = P/2 = 10 kN / 2 = 5 kN
   - Reacción en apoyo A: R_A = 5 kN
   - Reacción en apoyo B: R_B = 5 kN

2. **Cálculo del momento flector máximo:**
   El momento flector máximo ocurre en el centro de la viga donde se aplica la carga.
   - M_max = R_A · (L/2) = 5 kN · 3 m = 15 kN·m
   - M_max = 15,000 N·m = 15×10⁶ N·mm

3. **Cálculo de la deflexión máxima:**
   Para una viga simplemente apoyada con carga puntual central:
   - δ_max = (P · L³) / (48 · E · I)
   - Primero convertimos todas las unidades a consistentes (N y mm):
   - P = 10,000 N
   - L = 6 m = 6,000 mm
   - E = 200×10³ N/mm²
   - I = 8.33×10⁶ mm⁴
   - δ_max = (10,000 · 6,000³) / (48 · 200×10³ · 8.33×10⁶)
   - δ_max = (10,000 · 216×10⁹) / (48 · 200×10³ · 8.33×10⁶)
   - δ_max = (2.16×10¹⁵) / (79.97×10¹²)
   - δ_max = 27.01 mm

**Resultado esperado:**
- Reacciones: R_A = 5 kN, R_B = 5 kN
- Momento flector máximo: M_max = 15 kN·m
- Deflexión máxima: δ_max = 27.01 mm

**Código Python:**
```python
# Ejemplo 1: Viga simplemente apoyada con carga puntual central
import numpy as np

# Datos de entrada
L = 6.0  # Longitud de la viga en metros
P = 10.0  # Carga puntual en kN
E = 200e9  # Módulo de elasticidad en Pa
I = 8.33e-6  # Momento de inercia en m^4 (8.33e6 mm^4 convertido a m^4)

# Cálculo de reacciones
R_A = P / 2  # kN
R_B = P / 2  # kN

# Cálculo del momento flector máximo
M_max = R_A * (L / 2)  # kN·m

# Cálculo de la deflexión máxima
# Convertimos unidades a SI para el cálculo
P_si = P * 1000  # Convertir kN a N
L_si = L  # Longitud en metros
E_si = E  # Pa
I_si = I  # m^4

delta_max = (P_si * L_si**3) / (48 * E_si * I_si)  # Deflexión en metros
delta_max_mm = delta_max * 1000  # Convertir a mm

# Resultados
print(f"=== Resultados del Ejemplo 1 ===")
print(f"Reacción en apoyo A: {R_A:.2f} kN")
print(f"Reacción en apoyo B: {R_B:.2f} kN")
print(f"Momento flector máximo: {M_max:.2f} kN·m")
print(f"Deflexión máxima: {delta_max_mm:.2f} mm")
print(f"\nVerificación de límites de deflexión:")
print(f"Deflexión/L = {delta_max_mm/(L*1000):.4f} (típico L/240 = {1/240:.4f})")
```

### Ejemplo 2: Viga simplemente apoyada con carga distribuida uniforme

**Enunciado:** Una viga de concreto simplemente apoyada de 4 metros de longitud soporta una carga distribuida uniforme de 5 kN/m a lo largo de toda su luz. Calcule las reacciones en los apoyos, el momento flector máximo y la deflexión máxima. El concreto tiene un módulo de elasticidad de 200 GPa y la sección transversal tiene un momento de inercia de 5.21×10⁶ mm⁴.

**Datos:**
- Longitud de la viga (L): 4 m
- Carga distribuida uniforme (w): 5 kN/m = 5,000 N/m
- Módulo de elasticidad del concreto (E): 200 GPa = 200×10⁹ Pa = 200×10³ N/mm²
- Momento de inercia (I): 5.21×10⁶ mm⁴

**Desarrollo:**

1. **Cálculo de reacciones en los apoyos:**
   Para una carga distribuida uniforme, la carga total es W = w · L
   - Carga total: W = 5 kN/m · 4 m = 20 kN
   - Por simetría: R_A = R_B = W/2 = 20 kN / 2 = 10 kN
   - Reacción en apoyo A: R_A = 10 kN
   - Reacción en apoyo B: R_B = 10 kN

2. **Cálculo del momento flector máximo:**
   El momento flector máximo para carga distribuida uniforme ocurre en el centro de la viga.
   - M_max = (w · L²) / 8
   - M_max = (5 kN/m · 4² m²) / 8
   - M_max = (5 · 16) / 8 = 80 / 8 = 10 kN·m
   - M_max = 10,000 N·m = 10×10⁶ N·mm

   Alternativamente, usando las reacciones:
   - M_max = R_A · (L/2) - w · (L/2) · (L/4)
   - M_max = 10 kN · 2 m - 5 kN/m · 2 m · 1 m
   - M_max = 20 kN·m - 10 kN·m = 10 kN·m

3. **Cálculo de la deflexión máxima:**
   Para una viga simplemente apoyada con carga distribuida uniforme:
   - δ_max = (5 · w · L⁴) / (384 · E · I)
   - Convertimos unidades a consistentes (N y mm):
   - w = 5 kN/m = 5,000 N/m = 5 N/mm
   - L = 4 m = 4,000 mm
   - E = 200×10³ N/mm²
   - I = 5.21×10⁶ mm⁴
   - δ_max = (5 · 5 · 4,000⁴) / (384 · 200×10³ · 5.21×10⁶)
   - δ_max = (25 · 256×10¹²) / (384 · 200×10³ · 5.21×10⁶)
   - δ_max = (6.4×10¹⁵) / (400.13×10¹²)
   - δ_max = 15.99 mm

**Resultado esperado:**
- Reacciones: R_A = 10 kN, R_B = 10 kN
- Momento flector máximo: M_max = 10 kN·m
- Deflexión máxima: δ_max = 15.99 mm

**Código Python:**
```python
# Ejemplo 2: Viga simplemente apoyada con carga distribuida uniforme
import numpy as np

# Datos de entrada
L = 4.0  # Longitud de la viga en metros
w = 5.0  # Carga distribuida uniforme en kN/m
E = 200e9  # Módulo de elasticidad en Pa
I = 5.21e-6  # Momento de inercia en m^4 (5.21e6 mm^4 convertido a m^4)

# Cálculo de la carga total
W = w * L  # Carga total en kN

# Cálculo de reacciones
R_A = W / 2  # kN
R_B = W / 2  # kN

# Cálculo del momento flector máximo
M_max = (w * L**2) / 8  # kN·m

# Cálculo de la deflexión máxima
# Convertimos unidades a SI para el cálculo
w_si = w * 1000  # Convertir kN/m a N/m
L_si = L  # Longitud en metros
E_si = E  # Pa
I_si = I  # m^4

delta_max = (5 * w_si * L_si**4) / (384 * E_si * I_si)  # Deflexión en metros
delta_max_mm = delta_max * 1000  # Convertir a mm

# Resultados
print(f"=== Resultados del Ejemplo 2 ===")
print(f"Carga total: {W:.2f} kN")
print(f"Reacción en apoyo A: {R_A:.2f} kN")
print(f"Reacción en apoyo B: {R_B:.2f} kN")
print(f"Momento flector máximo: {M_max:.2f} kN·m")
print(f"Deflexión máxima: {delta_max_mm:.2f} mm")
print(f"\nVerificación de límites de deflexión:")
print(f"Deflexión/L = {delta_max_mm/(L*1000):.4f} (típico L/360 = {1/360:.4f})")

# Cálculo adicional: diagrama de momento flector a lo largo de la viga
print(f"\n=== Diagrama de momento flector ===")
x_points = np.linspace(0, L, 11)  # Puntos a lo largo de la viga
for x in x_points:
    if x <= L/2:
        M = R_A * x - w * x * x / 2
    else:
        M = R_B * (L - x) - w * (L - x) * (L - x) / 2
    print(f"x = {x:.2f} m: M = {M:.2f} kN·m")
```
