  # Plan de pruebas

  ## Módulo civil
  ### Funciones a probar
  - `calcular_resistencia_material`
  - `diseño_viga`
  - `verificacion_carga_acentrada`

  ### Casos de prueba recomendados
  - **Normales**: entradas dentro de rangos típicos.
  - **Borde**: valores límite (p. ej., carga máxima permitida).
  - **Error**: datos fuera de dominio (p. ej., valores negativos).

  ### Cobertura objetivo
  - 85 % de líneas cubiertas.

  ## Módulo electrica
  ### Funciones a probar
  - `calcular_caida_tension`
  - `dimensionar_conductor`
  - `seleccionar_fusible`

  ### Casos de prueba recomendados
  - **Normales**: parámetros dentro de especificaciones.
  - **Borde**: valores extremos de longitud y corriente.
  - **Error**: secciones no válidas o corrientes fuera de rango.

  ### Cobertura objetivo
  - 80 % de líneas cubiertas.

  ## Módulo geometria
  ### Funciones a probar
  - `area_poligono`
  - `distancia_punto_linea`
  - `interseccion_circulo_rectangulo`

  ### Casos de prueba recomendados
  - **Normales**: coordenadas dentro del rango esperado.
  - **Borde**: puntos sobre los límites del polígono o círculo.
  - **Error**: entradas no numéricas o geometrías imposibles.

  ### Cobertura objetivo
  - 90 % de líneas cubiertas.