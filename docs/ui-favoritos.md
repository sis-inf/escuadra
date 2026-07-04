# Favoritos de Herramientas

## Descripción

La función de **favoritos** permite al usuario marcar herramientas de uso frecuente para acceder a ellas rápidamente desde la pantalla principal, sin necesidad de buscarlas cada vez.

---

## Cómo marcar una herramienta como favorito

1. Abrir la herramienta deseada.
2. Hacer clic en el ícono de estrella ★ ubicado en la esquina superior derecha.
3. La estrella se resalta indicando que la herramienta fue marcada como favorito.
4. La herramienta aparecerá en la sección **Favoritos** de la pantalla principal.

---

## Cómo desmarcar un favorito

1. Abrir la herramienta marcada como favorito.
2. Hacer clic nuevamente en el ícono de estrella ★.
3. La estrella vuelve a su estado normal indicando que fue eliminada de favoritos.
4. La herramienta desaparece de la sección **Favoritos**.

---

## Aspecto visual

### Herramienta sin favorito
┌─────────────────────────────────┐
│  Calculadora de Áreas      ☆   │
│  ...                            │
└─────────────────────────────────┘

### Herramienta marcada como favorito
┌─────────────────────────────────┐
│  Calculadora de Áreas      ★   │
│  ...                            │
└─────────────────────────────────┘

### Sección de favoritos en pantalla principal
┌─────────────────────────────────┐
│  ★ Favoritos                    │
│  ─────────────────────────────  │
│  • Calculadora de Áreas         │
│  • Resolución de Triángulos     │
│  • Números Complejos            │
└─────────────────────────────────┘

---

## Uso en el sistema

```python
from ui import favoritos

# Marcar herramienta como favorito
favoritos.agregar("calculadora-areas")

# Desmarcar herramienta
favoritos.eliminar("calculadora-areas")

# Verificar si es favorito
es_fav = favoritos.es_favorito("calculadora-areas")
print(es_fav)  # → True o False

# Obtener lista de favoritos
lista = favoritos.obtener_todos()
print(lista)  # → ["calculadora-areas", "resolucion-triangulos", ...]
```

---

## Notas

- Los favoritos se guardan por usuario y persisten entre sesiones.
- No hay límite de herramientas que se pueden marcar como favorito.
- El orden de los favoritos refleja el orden en que fueron agregados.