# Tema Oscuro/Claro Configurable

## Descripción

La aplicación soporta dos temas visuales configurables por el usuario:

- **Tema claro:** interfaz con fondo blanco y texto oscuro.
- **Tema oscuro:** interfaz con fondo oscuro y texto claro, ideal para ambientes con poca luz.

El tema se puede cambiar desde la configuración de la aplicación y se guarda automáticamente para sesiones futuras.

---

## Aspecto visual

### Tema Claro
┌─────────────────────────────────────────┐
│  Escuadra                  [Config] │
├─────────────────────────────────────────┤
│  Fondo:      Blanco  (#FFFFFF)          │
│  Texto:      Gris oscuro (#333333)      │
│  Primario:   Azul (#1E6BE6)             │
│  Borde:      Gris claro (#DDDDDD)       │
│  Superficie: Blanco humo (#F5F5F5)      │
└─────────────────────────────────────────┘

### Tema Oscuro
┌─────────────────────────────────────────┐
│  Escuadra                 [Config] │
├─────────────────────────────────────────┤
│  Fondo:      Negro suave (#1E1E1E)      │
│  Texto:      Blanco (#F0F0F0)           │
│  Primario:   Azul claro (#4DA6FF)       │
│  Borde:      Gris oscuro (#444444)      │
│  Superficie: Gris muy oscuro (#2C2C2C)  │
└─────────────────────────────────────────┘

---

## Cómo cambiar el tema

1. Abrir la aplicación.
2. Ir a **Configuración** (ícono de engranaje).
3. Seleccionar la sección **Apariencia**.
4. Elegir entre **Claro** u **Oscuro**.
5. El cambio se aplica de inmediato y se guarda automáticamente.

---

## Uso en el sistema

```python
from ui import tema

# Obtener tema actual
actual = tema.obtener()
print(actual)  # → "claro" o "oscuro"

# Cambiar tema
tema.establecer("oscuro")

# Alternar entre temas
tema.alternar()
```

---

## Notas

- El tema predeterminado es **claro**.
- El tema seleccionado persiste entre sesiones.
- Todos los componentes de la interfaz respetan el tema configurado.