# Arquitectura del Sistema - Proyecto Escuadra

## 1. Visión General
El proyecto **Escuadra** está diseñado como una suite modular de herramientas de cálculo para ingeniería civil y mecánica. La arquitectura sigue el principio de **Separación de Responsabilidades**, dividiendo claramente la lógica matemática de la interfaz de usuario para garantizar precisión, mantenibilidad y escalabilidad.

## 2. Componentes Principales
- **Capa de Aplicación (Core)**: Contiene los algoritmos de cálculo, fórmulas físicas y la lógica de negocio. Es independiente de la interfaz.
- **Capa de Presentación (UI)**: Gestiona la interacción con el usuario, captura de datos y visualización de resultados gráficos.
- **Capa de Soporte (Utils)**: Incluye conversores de unidades técnicas, formateadores de precisión numérica y manejo de errores.

## 3. Diagrama de Arquitectura
El sistema utiliza una arquitectura de capas simple:
`[ Usuario ] <--> [ Capa de Interfaz (UI) ] <--> [ Capa de Lógica (Core) ]`

## 4. Tecnologías Utilizadas

| Componente | Tecnología | Versión | Justificación |
|---|---|---|---|
| **Lenguaje Base** | Python | 3.10+ | Facilidad para el desarrollo de algoritmos de ingeniería. |
| **Interfaz Gráfica** | Tkinter / PySide | Actual | Estándar robusto para aplicaciones de escritorio. |
| **Cálculo Numérico** | NumPy | Actual | Alta precisión en operaciones vectoriales y matriciales. |
| **Documentación** | Markdown | N/A | Estándar de la industria para documentación técnica en Git. |

## 5. Decisiones de Diseño

### Decisión 1: Estructura Basada en Módulos
**Contexto:** El sistema crecerá con múltiples herramientas (vigas, conversor, estadística).
**Decisión:** Cada herramienta vivirá en su propio submódulo dentro de `src/core`.
**Consecuencias:** Permite que varios desarrolladores trabajen en herramientas distintas sin causar conflictos de código.

### Decisión 2: Precisión de Punto Flotante
**Contexto:** Un error de decimales en ingeniería puede ser crítico.
**Decisión:** Se implementa un estándar de precisión de $10^{-6}$ en todos los resultados.
**Consecuencias:** Seguridad técnica en los reportes generados por la suite.

## 6. Flujo de Datos
1. El usuario ingresa parámetros técnicos en la **UI**.
2. La UI envía los datos a la función correspondiente en el **Core**.
3. El Core procesa el cálculo y aplica las constantes de ingeniería.
4. El resultado se devuelve a la UI para ser mostrado con el formato técnico adecuado.