# ⚡ Potencia Trifásica

Esta herramienta permite calcular la **potencia en sistemas trifásicos**, considerando diferentes configuraciones de conexión (**estrella** y **delta**) y diferenciándola de la potencia monofásica.

---

## 🎯 ¿Qué es la potencia trifásica?

La potencia trifásica es la potencia eléctrica suministrada por un sistema de **tres corrientes alternas** desfasadas entre sí 120°. Es el sistema más utilizado en aplicaciones industriales y comerciales debido a su mayor eficiencia y capacidad de transmisión.

### Diferencia entre monofásica y trifásica

| Característica | Monofásica | Trifásica |
|----------------|------------|-----------|
| **Número de fases** | 1 | 3 |
| **Aplicación** | Residencial | Industrial/Comercial |
| **Potencia** | Menor | Mayor |
| **Eficiencia** | Menor | Mayor |

---

## 📋 Fórmulas utilizadas

### Potencia activa (P)

#### Conexión estrella (Y)
P = √3 × V_L × I_L × cos(φ)

text

#### Conexión delta (Δ)
P = √3 × V_L × I_L × cos(φ)

text

Donde:
- **V_L**: Voltaje de línea (V)
- **I_L**: Corriente de línea (A)
- **cos(φ)**: Factor de potencia

### Potencia reactiva (Q)
Q = √3 × V_L × I_L × sen(φ)

text

### Potencia aparente (S)
S = √3 × V_L × I_L

text

---

## 📝 Ejemplos de uso

### Ejemplo 1: Conexión estrella

**Datos de entrada:**

| Parámetro | Valor |
|-----------|-------|
| Voltaje de línea (V_L) | 400 V |
| Corriente de línea (I_L) | 10 A |
| Factor de potencia (cos φ) | 0.85 |

**Cálculo:**
P = √3 × 400 × 10 × 0.85
P = 1.732 × 400 × 10 × 0.85
P = 5889 W ≈ 5.89 kW

text

**Resultado:** La potencia activa es de aproximadamente **5.89 kW**.

---

### Ejemplo 2: Conexión delta

**Datos de entrada:**

| Parámetro | Valor |
|-----------|-------|
| Voltaje de línea (V_L) | 220 V |
| Corriente de línea (I_L) | 15 A |
| Factor de potencia (cos φ) | 0.90 |

**Cálculo:**
P = √3 × 220 × 15 × 0.90
P = 1.732 × 220 × 15 × 0.90
P = 5145 W ≈ 5.15 kW

text

**Resultado:** La potencia activa es de aproximadamente **5.15 kW**.

---

## 📋 Comparación: Estrella vs Delta

| Característica | Estrella (Y) | Delta (Δ) |
|----------------|--------------|-----------|
| **Voltaje de fase** | V_f = V_L / √3 | V_f = V_L |
| **Corriente de fase** | I_f = I_L | I_f = I_L / √3 |
| **Potencia** | P = √3 × V_L × I_L × cos(φ) | P = √3 × V_L × I_L × cos(φ) |
| **Ventaja** | Menor voltaje por fase | Mayor corriente por fase |

---

## 🛠️ Solución de problemas

| Problema | Solución |
|----------|----------|
| **El resultado no coincide** | Verificar que el factor de potencia esté entre 0 y 1 |
| **Error en el cálculo** | Asegurarse de que los valores de voltaje y corriente sean correctos |

---

## 📚 Referencias

- [Sistemas trifásicos - Wikipedia](https://es.wikipedia.org/wiki/Sistema_trif%C3%A1sico)
- [Conexiones estrella y delta](https://es.wikipedia.org/wiki/Diagrama_estrella-tri%C3%A1ngulo)
