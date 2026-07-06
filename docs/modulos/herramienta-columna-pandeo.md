# Cálculo de Carga Crítica de Pandeo de Euler

Este documento describe la herramienta de cálculo para determinar la carga crítica de pandeo en columnas utilizando la ecuación de Euler, integrada como complemento de `docs/guia-modulo-civil.md`.

## Fórmula de Euler

La carga crítica ($P_{cr}$) es la fuerza axial máxima que una columna ideal puede soportar antes de sufrir inestabilidad por pandeo elástico. Se calcula mediante la siguiente expresión:

$$P_{cr} = \frac{\pi^2 \cdot E \cdot I}{(K \cdot L)^2}$$

Donde:
*   **$E$:** Módulo de elasticidad del material.
*   **$I$:** Menor momento de inercia de la sección transversal de la columna.
*   **$L$:** Longitud real de la columna.
*   **$K$:** Factor de longitud efectiva, el cual depende de las condiciones de soporte en los extremos.

## Condiciones de Soporte Soportadas

El módulo admite las cuatro configuraciones estándar de sujeción extrema para determinar el factor $K$:

1.  **Articulado - Articulado (Apoyado - Apoyado):** Ambos extremos libres para rotar. 
    *   $K = 1.0$
2.  **Empotrado - Empotrado:** Ambos extremos rígidamente fijos contra rotación y traslación.
    *   $K = 0.5$
3.  **Empotrado - Articulado:** Un extremo fijo y el otro libre para rotar pero fijo en posición.
    *   $K = 0.7$ (valor teórico) / $0.65$ (valor de diseño común).
4.  **Empotrado - Libre (Columna en voladizo):** Un extremo rígidamente fijo y el otro completamente libre.
    *   $K = 2.0$

## Ejemplo de Uso

Para evaluar una columna de acero estructural con los siguientes parámetros:
*   **Módulo de Elasticidad ($E$):** $200 \text{ GPa}$
*   **Momento de Inercia ($I$):** $40 \times 10^{-6} \text{ m}^4$
*   **Longitud ($L$):** $5 \text{ m}$
*   **Condición de soporte:** Empotrado - Articulado ($K = 0.7$)

**Cálculo de la longitud efectiva ($K \cdot L$):**
$$0.7 \times 5 \text{ m} = 3.5 \text{ m}$$

**Aplicación de la fórmula:**
$$P_{cr} = \frac{\pi^2 \cdot (200 \times 10^9 \text{ Pa}) \cdot (40 \times 10^{-6} \text{ m}^4)}{(3.5 \text{ m})^2} \approx 6,445.8 \text{ kN}$$

La herramienta procesará estas propiedades mecánicas y geométricas para entregar el límite de carga axial seguro antes del fallo por inestabilidad.
