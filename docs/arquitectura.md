# Arquitectura del Sistema

## Visión general
El proyecto Escuadra está diseñado como una **Aplicación Web** de arquitectura distribuida para garantizar que todos los miembros del equipo puedan colaborar y acceder a la información en tiempo real sin necesidad de instalaciones locales complejas.

## Componentes principales
El sistema se estructura bajo un modelo de **N-Capas**:

* **Capa de Presentación (Frontend):** Interfaz de usuario que se ejecuta en el navegador.
* **Capa de Lógica de Negocio (Backend):** Servidor encargado de procesar las reglas del sistema.
* **Capa de Datos:** Repositorio centralizado para la persistencia de la información.
## Diagrama de arquitectura

graph TD
    A[Navegador del Usuario] -->|Peticiones HTTP/REST| B[Servidor Backend]
    B -->|Consultas SQL| C[(Base de Datos)]

## Tecnologías utilizadas

| Componente | Tecnología | Versión | Justificación |
|---|---|---|---|
| Frontend|HTML5 / JavaScript |ES6+ |Estándar universal para aplicaciones web que facilita la colaboración del equipo. |
|Backend |Java / Node.js |LTS |Permite el despliegue continuo (CI/CD) y una lógica distribuida robusta. |
|Base de Datos |SQL (PostgreSQL/MySQL) |v8.0+ |Garantiza la integridad de los datos y la persistencia del sistema Escuadra. |

## Decisiones de diseño

### Decisión 1
**Contexto:** El equipo analizó las opciones de desarrollo (Web, Desktop y Móvil) para asegurar la accesibilidad y facilidad de mantenimiento.
**Decisión:** Se seleccionó una Arquitectura Web.
**Consecuencias:** Se facilita la distribución del sistema y se eliminan los problemas de instalación manual en los equipos de los usuarios finales.

## Flujo de datos
El usuario interactúa con la interfaz web y envía una solicitud.

El Backend recibe la petición, valida la lógica de negocio y solicita datos si es necesario.

La Base de Datos procesa la consulta y devuelve los resultados al servidor.

El sistema responde al navegador con la información procesada para que el usuario la visualice.