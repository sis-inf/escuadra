# Integración con Google Sheets

Ejemplo de función personalizada usando Google Apps Script para invocar cálculos de Escuadra desde una hoja de cálculo.

## Uso

1. Ejecutar Escuadra localmente con la API HTTP activada.
2. Abrir Google Sheets.
3. Crear un proyecto de Apps Script.
4. Copiar el contenido de `funcion-personalizada.gs`.

Ejemplo:

=ESCUADRA_CALCULAR("herramienta", A1:B2)

## Limitación

Esta integración requiere que Escuadra esté ejecutándose localmente y que el servidor HTTP esté disponible.

La función realiza una petición al endpoint local y devuelve el resultado recibido.
