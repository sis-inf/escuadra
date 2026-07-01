# Módulo de Código de Paridad

## Descripción

La **paridad** es un método de detección de errores que consiste en agregar un bit adicional a un conjunto de bits para que el total de bits en `1` sea par (paridad par) o impar (paridad impar). Permite detectar errores de **un solo bit**.

---

## Conceptos Clave

- **Bit de paridad:** bit extra que se agrega al dato original.
- **Paridad par:** el total de bits en `1` debe ser par.
- **Paridad impar:** el total de bits en `1` debe ser impar.
- **Detección de error:** si al recibir los datos la paridad no coincide, hubo un error.

---

## Ejemplos de uso

### Ejemplo 1: Calcular bit de paridad par

**Enunciado:** Dado el dato `1011001`, calcular el bit de paridad par y el mensaje a transmitir.

**Datos:**
- Dato original: `1011001`
- Tipo de paridad: par

**Desarrollo:**

1. **Contar los bits en 1 del dato original:**
   - `1011001` → bits en 1: posiciones 1, 3, 4, 7 → total = 4 bits en 1

2. **Determinar el bit de paridad:**
   - Total de bits en 1 = 4 (ya es par)
   - Bit de paridad = `0` (no se necesita agregar un 1)

3. **Mensaje transmitido:**
   - Dato + bit de paridad = `1011001 0`

**Resultado:** bit de paridad = `0`, mensaje = `10110010`

---

### Ejemplo 2: Calcular bit de paridad impar

**Enunciado:** Dado el dato `1101`, calcular el bit de paridad impar.

**Datos:**
- Dato original: `1101`
- Tipo de paridad: impar

**Desarrollo:**

1. **Contar los bits en 1:**
   - `1101` → bits en 1: posiciones 1, 2, 4 → total = 3 bits en 1

2. **Determinar el bit de paridad:**
   - Total de bits en 1 = 3 (ya es impar)
   - Bit de paridad = `0` (no se necesita agregar un 1)

3. **Mensaje transmitido:**
   - Dato + bit de paridad = `1101 0`

**Resultado:** bit de paridad = `0`, mensaje = `11010`

---

### Ejemplo 3: Verificación de paridad y detección de error

**Enunciado:** Se recibe el mensaje `10110011` con paridad par. ¿Hubo error de transmisión?

**Datos:**
- Mensaje recibido: `10110011`
- Tipo de paridad: par

**Desarrollo:**

1. **Contar los bits en 1 del mensaje recibido:**
   - `10110011` → bits en 1: posiciones 1, 3, 4, 7, 8 → total = 5 bits en 1

2. **Verificar paridad:**
   - Se espera paridad par → total de 1s debe ser par
   - Total recibido = 5 (impar) → **no coincide**

3. **Conclusión:**
   - La paridad no coincide → se detectó un error de transmisión

**Resultado:** Error detectado en la transmisión.

---

## Uso en el sistema

```python
from herramientas import codigo_paridad

# Calcular bit de paridad par
bit = codigo_paridad.calcular_paridad("1011001", tipo="par")
print(bit)  # → 0

# Verificar paridad de un mensaje recibido
error = codigo_paridad.verificar_paridad("10110011", tipo="par")
print(error)  # → True (se detectó error)
```