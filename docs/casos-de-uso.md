## Casos de Uso — Escuadra

### Actores del sistema

**1. Estudiante de ingeniería:** Persona que cursa una carrera de ingeniería y utiliza Escuadra como apoyo académico para resolver ejercicios, verificar cálculos y aplicar conceptos teóricos vistos en clase. Puede tener conocimientos básicos o intermedios según el semestre en curso.

**2. Docente:**Profesional del área de ingeniería que imparte clases y utiliza Escuadra como recurso didáctico para demostrar procedimientos, plantear ejemplos prácticos y apoyar la enseñanza de conceptos técnicos.

### Casos de uso

## CU-01: Calcular propiedades geométricas de una figura

**Actor:** Estudiantes
**Descripcion:** El usuario selecciona una figura geométrica (triángulo, círculo, rectángulo, etc.), ingresa sus dimensiones y obtiene propiedades como área, perímetro o volumen.
**Flujo principal:** 
1. El usuario accede a la herramienta de geometría.  
2. Selecciona el tipo de figura.  
3. Ingresa los valores de las dimensiones requeridas.  
4. El sistema calcula y muestra los resultados (área, perímetro, etc.).  
5. El usuario puede copiar o reingresar nuevos valores.

## CU-02: Resolver un sistema de ecuaciones lineales

**Actor:** Estudiante de ingeniería / Docente
**Descripcion:** El usuario ingresa los coeficientes de un sistema de ecuaciones lineales y el sistema devuelve la solución mediante métodos como Gauss-Jordan o sustitución.
**Flujo principal:**
1. El usuario accede a la herramienta de álgebra lineal.  
2. Selecciona el número de ecuaciones e incógnitas.  
3. Ingresa los coeficientes de cada ecuación.  
4. El sistema aplica el método seleccionado y muestra la solución paso a paso.  
5. El usuario revisa el procedimiento y el resultado final.

## CU-03: Consultar fórmulas técnicas por área de ingeniería

**Actor:** Docente / Estudiante de ingeniería
**Descripcion:** El usuario navega por un repositorio de fórmulas organizadas por rama de ingeniería (civil, mecánica, sistemas, etc.) para consultar, entender y aplicar las expresiones matemáticas relevantes a su área.
**Flujo principal:** 
1. El usuario accede al módulo de referencia técnica.  
2. Selecciona la rama de ingeniería de interés.  
3. Explora las categorías de fórmulas disponibles.  
4. Selecciona una fórmula para ver su descripción, variables y ejemplo de aplicación.  
5. Puede usar la fórmula directamente en una herramienta de cálculo vinculada.

## CU-04: Convertir unidades de medida entre sistemas

**Actor:** Estudiante de ingeniería
**Descripcion:** El usuario ingresa un valor con su unidad de origen y selecciona la unidad destino. El sistema realiza la conversión de forma inmediata (longitud, masa, presión, temperatura, etc.).
**Flujo principal:** 
1. El usuario accede a la herramienta de conversión de unidades.  
2. Selecciona la categoría (longitud, masa, temperatura, etc.).  
3. Ingresa el valor y la unidad de origen.  
4. Selecciona la unidad destino.  
5. El sistema muestra el resultado convertido.

## CU-05: Analizar un circuito eléctrico básico

**Actor:** Estudiante de ingeniería 
**Descripcion:**El usuario ingresa los componentes de un circuito (resistencias, voltaje, corriente) y el sistema calcula magnitudes como resistencia equivalente, corriente total y caída de tensión, aplicando las leyes de Ohm y Kirchhoff.
**Flujo principal:** 
1. El usuario accede a la herramienta de ingeniería electrónica.  
2. Selecciona el tipo de circuito (serie, paralelo o mixto).  
3. Ingresa los valores de los componentes.  
4. El sistema calcula las magnitudes eléctricas correspondientes.  
5. El usuario visualiza los resultados y puede modificar los valores para nuevos análisis.

