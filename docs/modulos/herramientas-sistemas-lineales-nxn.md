# Módulo de Sistemas Lineales NxN

## Descripción

Este módulo permite resolver sistemas de ecuaciones lineales de tamaño arbitrario **NxN** mediante el método de **eliminación gaussiana**. El usuario puede especificar el valor de N desde la interfaz y ingresar los coeficientes del sistema.

---

## Método: Eliminación Gaussiana

La eliminación gaussiana transforma el sistema en una matriz escalonada superior y luego aplica **sustitución regresiva** para obtener las soluciones.

### Pasos del método

1. **Construir la matriz aumentada** [A|b] del sistema.
2. **Eliminación hacia adelante:** convertir la matriz en forma escalonada superior usando operaciones de fila.
3. **Sustitución regresiva:** resolver desde la última ecuación hacia la primera.

---

## Cómo especificar el tamaño N desde la UI

1. Abrir el módulo **Sistemas Lineales NxN**.
2. Ingresar el valor de **N** (número de ecuaciones e incógnitas).
3. La interfaz generará automáticamente una grilla de **N × (N+1)** celdas para ingresar los coeficientes.
4. Completar los coeficientes de cada ecuación.
5. Presionar **Resolver**.

---

## Ejemplos de uso

### Ejemplo 1: Sistema 2x2

**Enunciado:** Resolver el sistema:
2x + y  = 5
x  + 3y = 10

**Matriz aumentada:**
| 2  1  | 5  |
| 1  3  | 10 |

**Desarrollo:**

1. **Eliminación:** restar (1/2) · fila1 de fila2:
   - Fila2 = Fila2 - (1/2)·Fila1
   - `| 0  2.5 | 7.5 |`

2. **Matriz escalonada:**
| 2  1   | 5   |
| 0  2.5 | 7.5 |

3. **Sustitución regresiva:**
   - `y = 7.5 / 2.5 = 3`
   - `x = (5 - 1·3) / 2 = 1`

**Resultado:** `x = 1`, `y = 3`

---

### Ejemplo 2: Sistema 3x3

**Enunciado:** Resolver el sistema:
x  + y  + z  = 6
2x + y  - z  = 1
x  - y  + 2z = 5

**Matriz aumentada:**
| 1   1   1  | 6 |
| 2   1  -1  | 1 |
| 1  -1   2  | 5 |

**Desarrollo:**

1. **Eliminar columna 1:**
   - Fila2 = Fila2 - 2·Fila1 → `| 0  -1  -3 | -11 |`
   - Fila3 = Fila3 - 1·Fila1 → `| 0  -2   1 | -1  |`

2. **Eliminar columna 2:**
   - Fila3 = Fila3 - 2·Fila2 → `| 0   0   7 | 21  |`

3. **Matriz escalonada:**
| 1   1   1  |  6  |
| 0  -1  -3  | -11 |
| 0   0   7  |  21 |

4. **Sustitución regresiva:**
   - `z = 21 / 7 = 3`
   - `y = (-11 + 3·3) / -1 = 2`
   - `x = 6 - y - z = 6 - 2 - 3 = 1`

**Resultado:** `x = 1`, `y = 2`, `z = 3`

---

## Uso en el sistema

```python
from herramientas import sistemas_lineales

# Sistema 3x3
A = [
    [1,  1,  1],
    [2,  1, -1],
    [1, -1,  2]
]
b = [6, 1, 5]

resultado = sistemas_lineales.resolver(A, b)
print(resultado)  # → [1, 2, 3]
```