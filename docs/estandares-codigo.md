# 📘 Estandarización de código en Python
## 🎯 Objetivo

Esta guía define convenciones para escribir código Python limpio, consistente y mantenible, siguiendo buenas prácticas.

## 🧾 1. Nombres de variables y funciones

- Usar `snake_case` (minúsculas con `_`).
- Los nombres deben ser descriptivos.
- Evitar abreviaciones innecesarias.
- Constantes en `UPPER_SNAKE_CASE`.

### ✅ Ejemplos:

```py
user_age = 25
total_price = 100.5
is_valid = True

def calculate_total(price, quantity):
    return price * quantity
```

## 📁 2. Nombres de archivos y módulos

- Usar `snake_case`.
- Archivos en minúsculas.
- Evitar nombres genéricos como utils.py.

### ✅ Ejemplos:

```bash
user_service.py
payment_processor.py
data_validator.py
```

## 📐 3. Indentación y formato

- Usar 4 espacios por nivel.
- No usar tabs.
- Máximo recomendado: 79 caracteres por línea.
- Dejar líneas en blanco para separar funciones.

### ✅ Ejemplo:

```py
if is_valid:
    process_data()
```

## 💬 4. Comentarios y docstrings

- Usar `#` para comentarios simples.
- Explicar el por qué, no el qué.
- Usar docstrings (`""" """`) para documentar funciones y módulos.
- Seguir formato claro y consistente.

### ✅ Ejemplo:

```py
# Evita división por cero
if value != 0:
    result = total / value
```

## 🧩 5. Ejemplo de función bien documentada

```py
def calculate_total(price, quantity):
    """
    Calcula el precio total de una compra.

    Args:
        price (float): Precio unitario del producto.
        quantity (int): Cantidad de productos.

    Returns:
        float: Precio total calculado.
    """
    return price * quantity
```

## 🚫 6. Buenas prácticas clave

- Usar `is` para comparar con `None`
- Evitar líneas demasiado largas
- Mantener funciones pequeñas y claras
- Usar nombres significativos
- Evitar código duplicado
- Seguir el principio de legibilidad (`Pythonic`)

## 🔥 Conclusión rápida

- `snake_case` → variables y funciones
- `snake_case` → archivos
- 4 espacios → indentación
- docstrings → documentación
- 79 caracteres → límite por línea
- Consistencia > preferencias personales
- Código → Español

> [!NOTE]
> Los ejemplos presentados son ilustrativos.
> No es necesario que el código sea exactamente igual, pero sí que respete las buenas prácticas descritas.