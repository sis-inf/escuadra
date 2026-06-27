# Herramienta de sistemas lineales NxN

Esta herramienta resuelve sistemas de ecuaciones lineales cuadrados de la forma:

```text
A · x = b
```

Donde:

- `A` es la matriz de coeficientes.
- `x` es el vector de incógnitas.
- `b` es el vector de términos independientes.

La implementación actual está pensada para uso educativo desde la interfaz gráfica de
Escuadra y permite sistemas entre `2x2` y `5x5`.

## Método usado

El módulo `src/escuadra/math/sistemas_lineales_nxn.py` utiliza eliminación gaussiana con
pivoteo parcial.

El proceso general es:

1. Construir una matriz aumentada `[A|b]`.
2. Recorrer cada columna de la matriz de coeficientes.
3. Elegir como pivote la fila con mayor valor absoluto en la columna actual.
4. Intercambiar filas para colocar ese pivote en la posición activa.
5. Eliminar los coeficientes debajo del pivote.
6. Aplicar sustitución hacia atrás para obtener `x1`, `x2`, ..., `xN`.

El pivoteo parcial mejora la estabilidad numérica frente a una eliminación gaussiana sin
intercambio de filas, especialmente cuando el pivote natural es muy pequeño.

## Sistemas singulares

Durante la eliminación, si el pivote queda demasiado cerca de cero, el sistema se trata
como singular y la función devuelve `None`.

En la interfaz gráfica esto se muestra como:

```text
El sistema no tiene solución única (matriz singular).
```

Esto cubre sistemas sin solución única, por ejemplo sistemas dependientes o incompatibles.

## Cómo elegir el tamaño N en la UI

La herramienta gráfica `HerramientaSistemasLineales` muestra un control llamado
`Tamaño del sistema`.

Para usarlo:

1. Abre la herramienta `Sistemas de ecuaciones lineales`.
2. En `Tamaño del sistema`, elige un valor entre `2` y `5`.
3. La grilla se reconstruye automáticamente con `N` filas y `N` columnas para la matriz
   `A`, más una columna `b` para los términos independientes.
4. Completa todos los campos con valores numéricos.
5. Presiona `Resolver`.

Si cambias el tamaño del sistema, la herramienta conserva los valores anteriores que
siguen encajando dentro de la nueva grilla.

## Ejemplo 2x2

Sistema:

```text
2x1 +  x2 = 5
 x1 + 3x2 = 6
```

Matriz y vector:

```python
A = [
    [2, 1],
    [1, 3],
]
b = [5, 6]
```

Uso desde código:

```python
from escuadra.math.sistemas_lineales_nxn import resolver_sistema

solucion = resolver_sistema(A, b)
print(solucion)
```

Resultado aproximado:

```text
[1.8, 1.4]
```

En la UI se presenta como:

```text
Solución:
x1 = 1.8
x2 = 1.4
```

## Ejemplo 3x3

Sistema:

```text
 x1 +  x2 +  x3 = 6
2x1 + 5x2 + 5x3 = -4
2x1 + 3x2 + 8x3 = 5
```

Uso desde código:

```python
from escuadra.math.sistemas_lineales_nxn import resolver_sistema

A = [
    [1, 1, 1],
    [2, 5, 5],
    [2, 3, 8],
]
b = [6, -4, 5]

print(resolver_sistema(A, b))
```

El resultado es una lista con los valores de `x1`, `x2` y `x3`.

## Validaciones de entrada

La interfaz convierte cada campo a `float`. Si un campo no contiene un número válido, la
herramienta detiene el cálculo y muestra qué posición debe corregirse:

```text
Error: valor inválido en A[1][2]: «texto»
```

o:

```text
Error: valor inválido en b[3]: «texto»
```

## Alcance y límites

- La UI permite tamaños de `2x2` a `5x5`.
- La función de dominio recibe una matriz cuadrada `A` y un vector `b` del mismo tamaño.
- El resultado se redondea a seis decimales al mostrarse en la interfaz.
- No calcula familias paramétricas de soluciones.
- No muestra el paso a paso de la eliminación; solo devuelve la solución final o informa
  que no existe solución única.
