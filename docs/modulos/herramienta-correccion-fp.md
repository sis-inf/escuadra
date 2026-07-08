# Herramienta: Corrección del Factor de Potencia con Banco de Capacitores

## Descripción

La herramienta **Corrección del Factor de Potencia** permite calcular la potencia reactiva que debe suministrar un banco de capacitores para mejorar el factor de potencia de una instalación eléctrica.

Su objetivo es facilitar el análisis de la compensación de potencia reactiva y comprender cómo influye en el rendimiento de una instalación.

---

## Parámetros de entrada

La herramienta requiere los siguientes datos:

| Parámetro                  | Descripción                               | Unidad |
| -------------------------- | ----------------------------------------- | ------ |
| Potencia activa (P)        | Potencia consumida por la carga           | kW     |
| Factor de potencia inicial | Factor de potencia antes de la corrección | -      |
| Factor de potencia deseado | Factor de potencia objetivo               | -      |

---

## Método de cálculo

La herramienta calcula la potencia reactiva que debe aportar el banco de capacitores mediante:

1. Calcular el ángulo inicial:

[
\varphi_1=\cos^{-1}(FP_1)
]

2. Calcular el ángulo deseado:

[
\varphi_2=\cos^{-1}(FP_2)
]

3. Calcular la potencia reactiva de compensación:

[
Q_c=P(\tan\varphi_1-\tan\varphi_2)
]

donde:

* **P** = Potencia activa.
* **FP₁** = Factor de potencia inicial.
* **FP₂** = Factor de potencia deseado.
* **Qc** = Potencia reactiva del banco de capacitores.

---

# Ejemplo completo

## Datos

| Parámetro                  | Valor  |
| -------------------------- | ------ |
| Potencia activa            | 100 kW |
| Factor de potencia inicial | 0.80   |
| Factor de potencia deseado | 0.95   |

---

## Paso 1. Ángulo inicial

[
\varphi_1=\cos^{-1}(0.80)=36.87^\circ
]

[
\tan\varphi_1=0.75
]

---

## Paso 2. Ángulo final

[
\varphi_2=\cos^{-1}(0.95)=18.19^\circ
]

[
\tan\varphi_2=0.328
]

---

## Paso 3. Potencia reactiva requerida

[
Q_c=100(0.75-0.328)
]

[
Q_c=42.2\ kVAr
]

---

## Resultado

Para mejorar el factor de potencia de **0.80** a **0.95**, se requiere un banco de capacitores con una potencia reactiva aproximada de:

**42.2 kVAr**

---

## Interpretación

Al instalar un banco de capacitores de aproximadamente **42 kVAr**, la instalación reduce la demanda de potencia reactiva desde la red eléctrica, mejorando el factor de potencia y disminuyendo las pérdidas asociadas.

---

## Consideraciones

* El cálculo corresponde a un caso simplificado.
* Se supone una carga estable durante el análisis.
* En instalaciones reales deben considerarse variaciones de carga, armónicos y las normas técnicas aplicables para la selección del banco de capacitores.
