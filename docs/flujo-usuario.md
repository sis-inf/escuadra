# Flujo de usuario

## 1. Perfil del usuario

Escuadra está dirigido a estudiantes, docentes y usuarios que necesitan usar herramientas matemáticas y de ingeniería para resolver problemas de forma rápida, clara y verificable.

El usuario busca:

- Resolver operaciones matemáticas y técnicas.
- Visualizar resultados de forma clara.
- Reducir errores de cálculo manual.
- Entender qué datos debe ingresar antes de ejecutar una herramienta.
- Corregir entradas inválidas sin perder el contexto de la operación.

---

## 2. Flujo general de uso

El flujo de uso se repite en la mayoría de las herramientas de Escuadra. El usuario elige una función, ingresa datos, el sistema valida la información, ejecuta el cálculo correspondiente y muestra una respuesta comprensible.

```text
Inicio
  --> Usuario abre Escuadra
  --> Sistema muestra herramientas disponibles
  --> Usuario selecciona una herramienta
  --> Sistema solicita datos de entrada
  --> Usuario ingresa valores
  --> Sistema valida formato, rangos y campos obligatorios
  --> Datos válidos?
      --> Sí --> Sistema ejecuta cálculo
              --> Sistema muestra resultado y unidad
              --> Usuario revisa resultado
              --> Fin
      --> No --> Sistema muestra mensaje de error
              --> Usuario corrige datos
              --> Sistema vuelve a validar
```

### Qué ocurre en cada paso

1. El usuario abre la aplicación o ejecuta el comando disponible.
2. Escuadra presenta las herramientas registradas por área de ingeniería.
3. El usuario selecciona la herramienta que necesita.
4. El sistema muestra los campos requeridos para esa operación.
5. El usuario ingresa valores numéricos, unidades o parámetros.
6. El sistema valida que los campos estén completos y sean coherentes.
7. Si la entrada es válida, se invoca el módulo de cálculo.
8. Si la entrada es inválida, se informa el problema y se permite corregir.
9. El resultado se muestra con una descripción, valor y unidad cuando aplica.

---

## 3. Flujo 1: usuario calcula área de una figura

Este flujo representa el uso de una herramienta de geometría para calcular áreas como triángulo, rectángulo, círculo o trapecio. El camino feliz ocurre cuando el usuario selecciona la figura, completa todos los datos y estos son positivos. El camino de error ocurre cuando falta un dato o se ingresa un valor no permitido.

```text
Inicio
  --> Usuario selecciona "Cálculo de área"
  --> Sistema muestra lista de figuras
  --> Usuario elige figura
  --> Sistema solicita medidas necesarias
      --> Triángulo: base y altura
      --> Círculo: radio
      --> Rectángulo: base y altura
      --> Trapecio: base mayor, base menor y altura
  --> Usuario ingresa medidas
  --> Sistema valida campos
      --> Campo vacío?
          --> Sí --> Sistema muestra "Completa todos los campos"
                  --> Usuario corrige la entrada
                  --> Sistema valida campos
      --> Valor menor o igual a cero?
          --> Sí --> Sistema muestra "Las medidas deben ser positivas"
                  --> Usuario corrige la medida
                  --> Sistema valida campos
      --> No hay errores
          --> Sistema calcula área según la figura
          --> Sistema muestra resultado con unidad cuadrada
          --> Usuario revisa el área calculada
          --> Fin
```

### Descripción del flujo

1. El usuario entra a la herramienta de cálculo de área.
2. El sistema ofrece las figuras soportadas para que el usuario elija una.
3. Según la figura seleccionada, el sistema cambia los campos de entrada.
4. El usuario escribe las dimensiones requeridas.
5. La validación comprueba que no existan campos vacíos, texto no numérico o medidas menores o iguales a cero.
6. Si hay errores, el sistema muestra un mensaje concreto y conserva la selección de la figura.
7. Si la entrada es válida, Escuadra ejecuta la fórmula correspondiente.
8. El resultado se presenta con el valor calculado y la unidad de superficie.

---

## 4. Flujo 2: usuario convierte temperatura

Este flujo cubre la conversión entre escalas de temperatura. El usuario ingresa un valor, selecciona unidad de origen y unidad destino, y el sistema transforma el dato usando la fórmula adecuada. El camino de error principal ocurre cuando el valor no es numérico o cuando se intenta convertir una temperatura físicamente inválida, como un Kelvin negativo.

```text
Inicio
  --> Usuario selecciona "Conversor de temperatura"
  --> Sistema muestra campo de valor y unidades disponibles
  --> Usuario ingresa temperatura
  --> Usuario selecciona unidad origen
  --> Usuario selecciona unidad destino
  --> Sistema valida entrada
      --> Valor no numérico?
          --> Sí --> Sistema muestra "Ingresa un número válido"
                  --> Usuario corrige el valor
                  --> Sistema valida entrada
      --> Temperatura menor que cero Kelvin?
          --> Sí --> Sistema muestra "Kelvin no puede ser negativo"
                  --> Usuario corrige valor o unidad
                  --> Sistema valida entrada
      --> Unidad origen igual a unidad destino?
          --> Sí --> Sistema mantiene el valor y avisa que no hay cambio de escala
                  --> Sistema muestra resultado
                  --> Fin
      --> No hay errores
          --> Sistema aplica fórmula de conversión
          --> Sistema redondea o formatea el resultado
          --> Sistema muestra valor convertido
          --> Usuario revisa equivalencia
          --> Fin
```

### Descripción del flujo

1. El usuario abre la herramienta de conversión de temperatura.
2. El sistema muestra las escalas disponibles, por ejemplo Celsius, Fahrenheit y Kelvin.
3. El usuario ingresa el valor que quiere convertir.
4. El usuario define desde qué escala parte y a qué escala quiere llegar.
5. El sistema valida que el valor sea numérico y que no viole restricciones físicas.
6. Si hay un error, se muestra una explicación breve para corregirlo.
7. Si la unidad origen y destino son iguales, el sistema evita un cálculo innecesario y devuelve el mismo valor.
8. Si todo es válido, se ejecuta la fórmula de conversión.
9. El resultado se muestra con su unidad destino.

---

## 5. Flujo 3: usuario analiza viga

Este flujo describe el cálculo de reacciones en una viga simplemente apoyada. El usuario proporciona longitud, carga y, cuando corresponde, posición de la carga. El sistema valida que la longitud sea positiva, que la carga sea coherente y que la posición esté dentro de la viga antes de calcular las reacciones.

```text
Inicio
  --> Usuario selecciona "Análisis de viga"
  --> Sistema solicita longitud de viga
  --> Sistema solicita carga puntual
  --> Sistema solicita posición de la carga
  --> Usuario ingresa datos
  --> Sistema valida datos estructurales
      --> Longitud menor o igual a cero?
          --> Sí --> Sistema muestra "La longitud debe ser mayor que cero"
                  --> Usuario corrige longitud
                  --> Sistema valida datos estructurales
      --> Carga negativa o vacía?
          --> Sí --> Sistema muestra "La carga debe ser un valor válido"
                  --> Usuario corrige carga
                  --> Sistema valida datos estructurales
      --> Posición fuera del tramo?
          --> Sí --> Sistema muestra "La posición debe estar entre 0 y la longitud"
                  --> Usuario corrige posición
                  --> Sistema valida datos estructurales
      --> No hay errores
          --> Sistema calcula reacciones Ra y Rb
          --> Sistema muestra resultados en kN
          --> Usuario revisa equilibrio de la viga
          --> Fin
```

### Descripción del flujo

1. El usuario abre la herramienta civil para análisis de vigas.
2. El sistema solicita los datos mínimos del problema: longitud, carga y posición.
3. El usuario ingresa los valores en las unidades esperadas por la herramienta.
4. La validación evita cálculos imposibles, como una viga sin longitud o una carga ubicada fuera del tramo.
5. Si se detecta un error, el sistema informa qué dato debe corregirse.
6. Si los datos son válidos, se llama al módulo de cálculo de reacciones.
7. El sistema calcula las reacciones en los apoyos de la viga.
8. El resultado se muestra con nombres de variables, valores y unidad.
9. El usuario usa el resultado para revisar el equilibrio o continuar su análisis.

---

## 6. Resultado esperado

El usuario obtiene un resultado rápido y entendible, pero también recibe orientación cuando la entrada no puede procesarse. Cada flujo debe ayudar a que el usuario sepa qué información necesita, cómo será validada y qué salida puede esperar al finalizar el cálculo.

En todos los casos, Escuadra debe mantener una interacción clara:

- Entrada del usuario: datos, unidad, figura o tipo de cálculo.
- Validación: revisión de campos obligatorios, formato numérico y restricciones del problema.
- Cálculo: ejecución del módulo correspondiente.
- Salida: resultado con valor, unidad y mensaje comprensible.
- Error recuperable: mensaje claro y posibilidad de corregir sin reiniciar todo el proceso.
