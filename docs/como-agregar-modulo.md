# Cómo agregar un nuevo módulo a Escuadra

Esta guía explica cómo crear e integrar una nueva herramienta dentro del proyecto Escuadra.  
El objetivo es mantener una estructura clara, consistente y fácil de mantener para todos los contribuidores.

---

# Estructura de módulos

Los módulos deben organizarse según la rama de ingeniería correspondiente.

Ejemplo de estructura:

```text
modulos/
├── civil/
├── electrica/
├── electronica/
├── industrial/
├── mecanica/
├── sistemas/
└── informatica/
```

Cada carpeta contiene herramientas relacionadas con su área.

Ejemplos:

```text
modulos/civil/calculo_vigas.py
modulos/electrica/ley_ohm.py
modulos/mecanica/calculo_velocidad.py
```

---

# Pasos para crear un nuevo módulo

## 1. Elegir la rama de ingeniería

Seleccionar la carpeta adecuada dentro de `modulos/`.

Ejemplo:

```text
modulos/civil/
```

---

## 2. Crear el archivo del módulo

El archivo debe tener un nombre descriptivo y usar `snake_case`.

Ejemplos válidos:

```text
calculo_vigas.py
analisis_circuito.py
conversion_temperatura.py
```

Evitar nombres genéricos como:

```text
archivo1.py
modulo.py
prueba123.py
```

---

## 3. Definir funciones claras

Las funciones deben:

- Usar `snake_case`
- Seguir la estructura verbo + sustantivo
- Tener una única responsabilidad

Ejemplos correctos:

```python
calcular_area()
obtener_voltaje()
analizar_carga()
```

Ejemplos incorrectos:

```python
calc()
funcion1()
datos()
```

---

# Convención de retorno

Todas las funciones deben devolver un `dict` con claves descriptivas.

Esto permite:

- Mantener consistencia entre módulos
- Facilitar integraciones futuras
- Hacer más legible la salida

Ejemplo:

```python
return {
    "resultado": area,
    "unidad": "m2"
}
```

Evitar retornos ambiguos como:

```python
return 25
```

---

# Agregar pruebas

Cada módulo nuevo debe incluir pruebas básicas.

Ejemplo de estructura:

```text
tests/
├── test_calculo_vigas.py
```

Las pruebas deben validar:

- Casos correctos
- Valores límite
- Manejo de errores simples

---

# Ejemplo completo

```python
# Archivo:
# modulos/civil/calculo_triangulo.py

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    """

    if base <= 0 or altura <= 0:
        return {
            "error": "La base y la altura deben ser mayores a cero"
        }

    area = (base * altura) / 2

    return {
        "base": base,
        "altura": altura,
        "area": area,
        "unidad": "m2"
    }


def mostrar_resultado(resultado):
    """
    Muestra el resultado en pantalla.
    """

    if "error" in resultado:
        print("Error:", resultado["error"])
        return

    print("Base:", resultado["base"])
    print("Altura:", resultado["altura"])
    print("Área:", resultado["area"], resultado["unidad"])


resultado = calcular_area_triangulo(10, 5)

mostrar_resultado(resultado)
```

Salida esperada:

```python
Base: 10
Altura: 5
Área: 25.0 m2
```

---

# Buenas prácticas

- Mantener funciones pequeñas y reutilizables
- Documentar funciones con docstrings
- Evitar duplicar lógica
- Usar nombres descriptivos
- Mantener consistencia en el formato de retorno
- Agregar pruebas antes de abrir un Pull Request

---

# Antes de abrir el Pull Request

Verificar que:

- El módulo funciona correctamente
- El archivo sigue las convenciones del proyecto
- Existen pruebas básicas
- La rama fue creada desde `dev`
- El PR apunta hacia `dev`
- No se modificaron archivos fuera del alcance del issue

## Ruta del módulo

Las herramientas deben crearse dentro de la estructura actual del proyecto:

src/escuadra/modulos/NOMBRE_DOMINIO/nombre_herramienta.py

Ejemplos:

src/escuadra/modulos/civil/momento_flector.py
src/escuadra/modulos/electrica/herramienta_divisor_tension.py
src/escuadra/modulos/sistemas/complemento_dos.py

## Crear un nuevo dominio

Si el dominio no existe, debe crearse una carpeta nueva dentro de "src/escuadra/modulos/".

Ejemplo:

src/escuadra/modulos/geotecnica/

Además, es obligatorio agregar el archivo:

src/escuadra/modulos/geotecnica/__init__.py

Esto permite que Python reconozca el directorio como un paquete del proyecto.

## Template básico de una herramienta

El siguiente ejemplo muestra una estructura válida para una herramienta de Escuadra:

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


class HerramientaEjemplo(Herramienta):
    nombre = "Herramienta de ejemplo"
    carrera = Carrera.CIVIL
    descripcion = "Descripción breve de la herramienta."

    def crear_widget(self):
        raise NotImplementedError

El nombre de la clase debe ser descriptivo y heredar de "Herramienta".

## Registro de herramientas

Después de crear una nueva herramienta, debe registrarse en el sistema correspondiente para que pueda ser detectada y utilizada por la aplicación.

Verificar que la herramienta quede incorporada al registro utilizado por el proyecto y que aparezca correctamente dentro de la categoría o dominio correspondiente.

## Verificación final

Antes de abrir el Pull Request verificar que:

- La herramienta se encuentra en "src/escuadra/modulos/NOMBRE_DOMINIO/"
- El código Python es válido
- Existe un archivo "__init__.py" si se creó un dominio nuevo
- La herramienta fue agregada al registro correspondiente
- El PR apunta a la rama "dev"