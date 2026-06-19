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

### ✓ Correcto (snake_case en nombres de funciones):

```py
def calculate_total(price, quantity):
    return price * quantity

def get_user_data(user_id):
    return {"name": "Juan", "age": 30}
```

### ❌ Incorrecto (camelCase o nombres no descriptivos):

```py
def calculateTotal(price, quantity):
    return price * quantity

def get_data(uid):
    return {"name": "Juan", "age": 30}
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

### ✓ Correcto (Docstrings en formato NumPy):

```py
def calculate_total(price, quantity):
    """
    Calcula el precio total de una compra.

    Parameters
    ----------
    price : float
        Precio unitario del producto.
    quantity : int
        Cantidad de productos.

    Returns
    -------
    float
        Precio total calculado.
    """
    return price * quantity
```

### ✓ Correcto (Docstrings en formato Google):

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

### ❌ Incorrecto (Sin docstring o formato incorrecto):

```py
def calculate_total(price, quantity):
    return price * quantity

def calculate_total(price, quantity):
    # Calcula el total
    return price * quantity
```

## 🚫 6. Type hints

- Usar type hints para mejorar la legibilidad y facilitar el mantenimiento.
- Especificar tipos de parámetros y valores de retorno.
- Importar tipos desde `typing` cuando sea necesario.

### ✓ Correcto (Con type hints):

```py
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def get_user_data(user_id: int) -> dict[str, str | int]:
    return {"name": "Juan", "age": 30}

from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    return None
```

### ❌ Incorrecto (Sin type hints):

```py
def calculate_total(price, quantity):
    return price * quantity

def get_user_data(user_id):
    return {"name": "Juan", "age": 30}
```

## 🚫 7. Manejo de errores

- Usar `ValueError` con mensajes descriptivos para validaciones.
- Incluir contexto claro en el mensaje de error.
- Evitar mensajes genéricos como "Error" o "Invalid input".

### ✓ Correcto (ValueError con mensajes descriptivos):

```py
def calculate_total(price: float, quantity: int) -> float:
    if price < 0:
        raise ValueError(f"El precio no puede ser negativo: {price}")
    if quantity < 0:
        raise ValueError(f"La cantidad no puede ser negativa: {quantity}")
    return price * quantity

def set_age(age: int) -> None:
    if age < 0 or age > 150:
        raise ValueError(f"Edad inválida: {age}. Debe estar entre 0 y 150.")
```

### ❌ Incorrecto (Sin mensajes descriptivos):

```py
def calculate_total(price: float, quantity: int) -> float:
    if price < 0:
        raise ValueError("Error")
    if quantity < 0:
        raise ValueError("Invalid input")
    return price * quantity
```

## 🚫 8. Estructura de herramientas (tools)

- Organizar funciones relacionadas en módulos coherentes.
- Separar lógica de negocio de la interfaz.
- Usar clases cuando sea apropiado para encapsular estado.

### ✓ Correcto (Estructura organizada):

```py
# user_service.py
from typing import Optional

class UserService:
    """Servicio para gestionar usuarios."""

    def __init__(self, db_connection):
        self.db = db_connection

    def get_user(self, user_id: int) -> Optional[dict]:
        """
        Obtiene un usuario por su ID.

        Args:
            user_id: ID del usuario a buscar.

        Returns:
            Diccionario con datos del usuario o None si no existe.
        """
        return self.db.query("SELECT * FROM users WHERE id = ?", user_id)

    def create_user(self, name: str, email: str) -> int:
        """
        Crea un nuevo usuario.

        Args:
            name: Nombre del usuario.
            email: Email del usuario.

        Returns:
            ID del usuario creado.

        Raises:
            ValueError: Si el email es inválido.
        """
        if "@" not in email:
            raise ValueError(f"Email inválido: {email}")
        return self.db.insert("INSERT INTO users (name, email) VALUES (?, ?)", name, email)
```

### ❌ Incorrecto (Estructura desorganizada):

```py
# utils.py
def get_user(db, user_id):
    return db.query("SELECT * FROM users WHERE id = ?", user_id)

def create_user(db, name, email):
    if "@" not in email:
        raise ValueError("Error")
    return db.insert("INSERT INTO users (name, email) VALUES (?, ?)", name, email)

def calculate_total(price, quantity):
    return price * quantity
```

## 🚫 9. Buenas prácticas clave

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