# Flujo de Usuario

## Introducción

Este documento describe los principales flujos de interacción entre el usuario y la aplicación mediante la interfaz de línea de comandos (CLI). Los diagramas muestran el recorrido completo desde la entrada de datos hasta la obtención de resultados, incluyendo validaciones y escenarios de error.

---

# Flujo 1: Cálculo de Área de una Figura

## Descripción

Este flujo permite al usuario calcular el área de una figura geométrica. El sistema solicita el tipo de figura y los parámetros necesarios para realizar el cálculo.

### Diagrama de flujo

```text
Inicio
  -->
Usuario selecciona "Calcular área"
  -->
Ingresa tipo de figura
  -->
Validar figura
  --> (válida)
Solicitar dimensiones
  -->
Validar dimensiones
  --> (válidas)
Realizar cálculo
  -->
Mostrar resultado
  -->
Fin

Validar figura
  --> (error)
Mostrar mensaje de figura no soportada
  -->
Solicitar nuevamente

Validar dimensiones
  --> (error)
Mostrar mensaje de dimensiones inválidas
  -->
Solicitar nuevamente
```

## Explicación de pasos

1. El usuario selecciona la opción de cálculo de área.
2. El sistema solicita el tipo de figura.
3. Se verifica que la figura exista dentro de las opciones soportadas.
4. Se solicitan las dimensiones requeridas.
5. Se valida que los valores sean numéricos y positivos.
6. Se ejecuta la fórmula correspondiente.
7. Se presenta el resultado al usuario.

---

# Flujo 2: Conversión de Temperatura

## Descripción

Este flujo permite convertir temperaturas entre diferentes escalas como Celsius, Fahrenheit y Kelvin.

### Diagrama de flujo

```text
Inicio
  -->
Usuario selecciona "Convertir temperatura"
  -->
Ingresa temperatura
  -->
Validar valor numérico
  --> (válido)
Seleccionar escala origen
  -->
Seleccionar escala destino
  -->
Validar conversión
  --> (válida)
Realizar conversión
  -->
Mostrar resultado
  -->
Fin

Validar valor numérico
  --> (error)
Mostrar mensaje de dato inválido
  -->
Solicitar nuevamente

Validar conversión
  --> (error)
Mostrar escalas no compatibles
  -->
Solicitar nuevamente
```

## Explicación de pasos

1. El usuario selecciona la funcionalidad de conversión.
2. Introduce una temperatura.
3. El sistema valida que el dato sea numérico.
4. El usuario selecciona la escala de origen.
5. El usuario selecciona la escala de destino.
6. El sistema verifica que la conversión sea posible.
7. Se aplica la fórmula correspondiente.
8. Se muestra el resultado final.

---

# Flujo 3: Análisis de Viga

## Descripción

Este flujo permite analizar una viga a partir de sus características estructurales y las cargas aplicadas.

### Diagrama de flujo

```text
Inicio
  -->
Usuario selecciona "Analizar viga"
  -->
Ingresa longitud
  -->
Validar longitud
  --> (válida)
Ingresa cargas
  -->
Validar cargas
  --> (válidas)
Ejecutar análisis estructural
  -->
Generar resultados
  -->
Mostrar resultados
  -->
Fin

Validar longitud
  --> (error)
Mostrar longitud inválida
  -->
Solicitar nuevamente

Validar cargas
  --> (error)
Mostrar carga inválida
  -->
Solicitar nuevamente
```

## Explicación de pasos

1. El usuario accede al módulo de análisis estructural.
2. Introduce la longitud de la viga.
3. El sistema valida que la longitud sea positiva.
4. Se registran las cargas aplicadas.
5. Se verifica que las cargas tengan formato correcto.
6. Se ejecutan los cálculos estructurales.
7. Se generan reacciones, esfuerzos o resultados asociados.
8. El sistema presenta la información al usuario.

---

# Consideraciones Generales

Todos los flujos siguen una estructura común:

```text
Entrada del usuario
  -->
Validación
  -->
Cálculo o procesamiento
  -->
Salida de resultados
```

Las validaciones son obligatorias para garantizar que los cálculos se realicen con datos consistentes. Ante cualquier error, el sistema informa claramente el problema y permite al usuario corregir la entrada sin reiniciar completamente el proceso.

La utilización de este enfoque mejora la experiencia de uso del CLI y reduce errores durante la ejecución de operaciones matemáticas, conversiones y análisis estructurales.