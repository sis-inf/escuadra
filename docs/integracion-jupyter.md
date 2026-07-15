# 📓 Integración con Jupyter Notebooks

Esta guía explica cómo usar **Escuadra** como librería en **Jupyter Notebooks**, permitiendo realizar cálculos de ingeniería desde un entorno interactivo.

---

## 🎯 ¿Para qué usar Escuadra en Jupyter?

| Ventaja | Descripción |
|---------|-------------|
| **Interactividad** | Probá cálculos en tiempo real sin necesidad de compilar |
| **Visualización** | Generá gráficos y tablas dinámicas |
| **Educación** | Ideal para enseñar conceptos de ingeniería |
| **Investigación** | Hacé experimentos rápidos y documentá resultados |

---

## 📋 Requisitos previos

| Requisito | Descripción |
|-----------|-------------|
| **Python 3.8+** | Lenguaje de programación |
| **Jupyter** | `pip install jupyter` o usar Anaconda |
| **Escuadra** | Instalado en modo desarrollo: `pip install -e .` |

---

## 🚀 Cómo importar módulos de Escuadra

### Importación directa (sin UI)

```python
# Importar módulos de cálculo puro
from escuadra.modulos.civil import vigas
from escuadra.modulos.electrica import caida_tension
from escuadra.modulos.geometria import figuras

# Ejemplo: Calcular una viga
resultado = vigas.calcular_momento(longitud=5.0, carga=10.0)
print(resultado)
  ## 📝 Ejemplo completo en Jupyter

### 1. Configuración inicial

```python
# Importar escuadra
import escuadra as es

# Ver versión
print(f"Escuadra v{es.__version__}")
from escuadra.modulos.civil import vigas

# Definir parámetros
longitud = 5.0  # metros
carga = 10.0    # kN

# Calcular momento flector
momento = vigas.calcular_momento(longitud, carga)

# Calcular cortante
cortante = vigas.calcular_cortante(longitud, carga)

from escuadra.modulos.electrica import caida_tension

# Parámetros
longitud = 100.0   # metros
corriente = 20.0   # amperios
seccion = 10.0     # mm²

# Calcular caída de tensión
caida = caida_tension.calcular(longitud, corriente, seccion)

print(f"⚡ Caída de tensión: {caida:.3f} V")
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
longitudes = np.linspace(1, 10, 10)
momentos = [vigas.calcular_momento(l, 10.0) for l in longitudes]

# Graficar
plt.plot(longitudes, momentos, 'b-', linewidth=2)
plt.xlabel('Longitud (m)')
plt.ylabel('Momento flector (kN·m)')
plt.title('Momento flector vs Longitud')
plt.grid(True)
plt.show()
