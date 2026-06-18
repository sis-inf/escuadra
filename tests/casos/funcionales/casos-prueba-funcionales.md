# Casos de Prueba Funcionales

## Herramienta: Cálculo de Reacciones en Vigas

### CP-001
- **Descripción:** Viga simplemente apoyada con carga puntual central
- **Entrada:** longitud 6m, carga puntual 10 kN en el centro
- **Resultado esperado:** Reacción en A = 5 kN, Reacción en B = 5 kN

### CP-002
- **Descripción:** Viga simplemente apoyada con carga distribuida
- **Entrada:** longitud 4m, carga distribuida 2 kN/m
- **Resultado esperado:** Reacción en A = 4 kN, Reacción en B = 4 kN

### CP-003
- **Descripción:** Viga en voladizo con carga puntual en el extremo
- **Entrada:** longitud 3m, carga 5 kN en el extremo libre
- **Resultado esperado:** Reacción vertical = 5 kN, Momento = 15 kN·m

## Herramienta: Cálculo de Momento Flector

### CP-004
- **Descripción:** Momento máximo en viga simplemente apoyada con carga central
- **Entrada:** longitud 6m, carga 10 kN en el centro
- **Resultado esperado:** Momento máximo = 15 kN·m en el centro

### CP-005
- **Descripción:** Momento en viga con carga distribuida uniforme
- **Entrada:** longitud 4m, carga distribuida 3 kN/m
- **Resultado esperado:** Momento máximo = 6 kN·m en el centro

## Herramienta: Cálculo de Caída de Tensión

### CP-006
- **Descripción:** Caída de tensión en conductor de cobre
- **Entrada:** longitud 100m, corriente 10A, sección 2.5mm²
- **Resultado esperado:** Caída de tensión = 8.8V

### CP-007
- **Descripción:** Caída de tensión en conductor de aluminio
- **Entrada:** longitud 50m, corriente 15A, sección 4mm²
- **Resultado esperado:** Caída de tensión = 7.8V

## Herramienta: Cálculo de Resistencia de Conductores

### CP-008
- **Descripción:** Resistencia de conductor de cobre a 20°C
- **Entrada:** longitud 200m, sección 6mm²
- **Resultado esperado:** Resistencia = 0.573 Ω

### CP-009
- **Descripción:** Resistencia de conductor con variación de temperatura
- **Entrada:** longitud 100m, sección 4mm², temperatura 60°C
- **Resultado esperado:** Resistencia = 0.517 Ω

## Herramienta: Cálculo de Potencia Eléctrica

### CP-010
- **Descripción:** Potencia en circuito monofásico
- **Entrada:** voltaje 220V, corriente 5A, factor de potencia 0.9
- **Resultado esperado:** Potencia activa = 990W

## Herramienta: Conversor de Temperatura

### CP-011

* **Descripción:** Conversión de Celsius a Fahrenheit
* **Entrada:** 100°C
* **Resultado esperado:** 212°F

### CP-012

* **Descripción:** Conversión de Fahrenheit a Celsius
* **Entrada:** 32°F
* **Resultado esperado:** 0°C

### CP-013

* **Descripción:** Validación de temperatura Kelvin negativa
* **Entrada:** -5 K
* **Resultado esperado:** Mensaje de error indicando que Kelvin no puede tener valores negativos

## Herramienta: Cálculo de Reacciones en Vigas

### CP-014

* **Descripción:** Viga simplemente apoyada con carga puntual de 20 kN
* **Entrada:** longitud 10m, carga puntual 20 kN en el centro
* **Resultado esperado:** Reacción en A = 10 kN, Reacción en B = 10 kN

### CP-015

* **Descripción:** Viga simplemente apoyada con carga puntual de 16 kN
* **Entrada:** longitud 8m, carga puntual 16 kN en el centro
* **Resultado esperado:** Reacción en A = 8 kN, Reacción en B = 8 kN

### CP-016

* **Descripción:** Validación de longitud de viga inválida
* **Entrada:** longitud 0m, carga puntual 20 kN
* **Resultado esperado:** Mensaje de error indicando que la longitud debe ser mayor que cero

## Herramienta: Cálculo de Potencia Eléctrica

### CP-017

* **Descripción:** Potencia eléctrica con voltaje de 220V y corriente de 5A
* **Entrada:** voltaje 220V, corriente 5A
* **Resultado esperado:** Potencia = 1100W

### CP-018

* **Descripción:** Potencia eléctrica con corriente nula
* **Entrada:** voltaje 220V, corriente 0A
* **Resultado esperado:** Potencia = 0W
EOF