  # Herramientas

  ## calculo_area
  Descripción: Calcula el área de distintas figuras geométricas.

  ### Fórmulas
  - **Cuadrado**: $A = l^2$ (unidad: m²)
  - **Rectángulo**: $A = l \times w$ (unidad: m²)
  - **Triángulo**: $A = \frac{b \times h}{2}$ (unidad: m²)
  - **Círculo**: $A = \pi r^2$ (unidad: m²)

  ### Ejemplo de invocación
  ```bash
  python -m escuadra.tools.calculo_area --figura cuadrado --lado 5
  # Salida: Área = 25.00 m²
  ```

  ## volumen
  Descripción: Calcula el volumen de distintos sólidos.

  ### Fórmulas
  - **Cubo**: $V = l^3$ (unidad: m³)
  - **Cilindro**: $V = \pi r^2 h$ (unidad: m³)
  - **Esfera**: $V = \frac{4}{3}\pi r^3$ (unidad: m³)
  - **Prisma rectangular**: $V = l \times w \times h$ (unidad: m³)

  ### Ejemplo de invocación
  ```bash
  python -m escuadra.tools.volumen --solido cilindro --radio 2 --altura 5
  # Salida: Volumen = 62.83 m³
  ```

  ## perimetro
  Descripción: Calcula el perímetro de distintas figuras.

  ### Fórmulas
  - **Cuadrado**: $P = 4l$ (unidad: m)
  - **Rectángulo**: $P = 2(l + w)$ (unidad: m)
  - **Triángulo**: $P = a + b + c$ (unidad: m)
  - **Círculo** (circunferencia): $P = 2\pi r$ (unidad: m)

  ### Ejemplo de invocación
  ```bash
  python -m escuadra.tools.perimetro --figura triangulo --lado1 3 --lado2 4 --lado3 5
  # Salida: Perímetro = 12.00 m
  ```