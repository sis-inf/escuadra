# Arquitectura del Sistema - Proyecto Escuadra

## 1. Visión General
El proyecto **Escuadra** está diseñado como una plataforma modular de herramientas orientadas a distintas ramas de la ingeniería. La arquitectura sigue un principio de **Separación de Responsabilidades**, permitiendo que cada área de ingeniería implemente sus propias soluciones de forma independiente.

El sistema prioriza la escalabilidad, permitiendo agregar nuevas herramientas sin afectar el funcionamiento general.

---

## 2. Componentes Principales
- **Capa de Aplicación (Core)**: Contiene la lógica de cada herramienta de ingeniería, incluyendo algoritmos, cálculos y procesamiento de datos.
- **Capa de API (Flask)**: Expone las funcionalidades mediante endpoints REST para permitir el acceso a las herramientas desde clientes externos.
- **Capa de Soporte (Utils)**: Incluye utilidades comunes como validación de datos, manejo de errores y formateo de resultados.

---

## 3. Organización por Ramas de Ingeniería
El sistema está estructurado en módulos independientes según cada área:
escuadra/
	├── src/
	│ 	├── mecanica/
	│ 	├── sistemas/
	│ 	├── industrial/
	│ 	├── civil/
	│ 	├── electrica/
	├── docs/	

Cada módulo contiene herramientas específicas de su rama de ingeniería, permitiendo desarrollo paralelo sin conflictos.

---

## 4. Tecnologías Utilizadas

| Componente | Tecnología | Versión | Justificación |
|---|---|---|---|
| **Lenguaje Base** | Python | 3.10+ | Facilidad para implementar lógica y cálculos |
| **Framework API** | Flask | Actual | Permite exponer funcionalidades como servicios REST |
| **Gestión de dependencias** | pip | N/A | Manejo sencillo mediante requirements.txt |
| **Documentación** | Markdown | N/A | Estándar para documentación en repositorios Git |

---

## 5. Decisiones de Diseño

### Decisión 1: Arquitectura Modular por Ingeniería
**Contexto:** El proyecto involucra múltiples áreas de ingeniería con distintas necesidades.  
**Decisión:** Separar cada rama en módulos independientes dentro de `src/`.  
**Consecuencias:** Permite que diferentes equipos trabajen en paralelo sin interferencias.

---

### Decisión 2: Uso de API REST con Flask
**Contexto:** Se requiere que las herramientas puedan ser consumidas externamente.  
**Decisión:** Implementar una capa de API utilizando Flask.  
**Consecuencias:** Facilita la integración con otras aplicaciones y servicios.

---

### Decisión 3: Consistencia Tecnológica
**Contexto:** Es necesario mantener coherencia entre módulos.  
**Decisión:** Usar Python como lenguaje base y pip para dependencias.  
**Consecuencias:** Simplifica la instalación y mantenimiento del proyecto.

---

## 6. Flujo de Datos
1. El usuario o cliente realiza una solicitud a la API.
2. La API (Flask) recibe los parámetros y los valida.
3. La solicitud se envía al módulo correspondiente en el Core.
4. El Core procesa la información y genera un resultado.
5. La API devuelve la respuesta al cliente en formato estructurado (JSON).

## 7. Diagrama de clases del core

classDiagram

    class Registry {
        +register_tool(name)
        +get_tools()
    }

    class Dispatcher {
        +run_convert()
        +run_matrix()
        +dispatch(subcommand)
    }

    class Historial {
        +agregar()
        +listar()
        +limpiar()
    }

    Dispatcher --> Registry : utiliza
    Dispatcher --> Historial : utiliza

Descripción

- Registry administra el registro de herramientas disponibles.
- Dispatcher enruta y ejecuta los subcomandos solicitados por el usuario.
- Historial almacena y consulta el historial de ejecuciones realizadas.

El Dispatcher utiliza Registry para localizar herramientas disponibles y utiliza Historial para registrar las operaciones ejecutadas.