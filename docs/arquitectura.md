# Arquitectura del Sistema - Proyecto Escuadra

## 1. Visión General

El proyecto **Escuadra** está diseñado como una plataforma modular de herramientas orientadas a distintas ramas de la ingeniería. La arquitectura sigue un principio de **Separación de Responsabilidades**, permitiendo que cada área de ingeniería implemente sus propias soluciones de forma independiente.

El sistema prioriza la escalabilidad, permitiendo agregar nuevas herramientas sin afectar el funcionamiento general.

---

## 2. Stack Tecnológico

| Componente           | Tecnología | Versión | Justificación                                                                     |
| -------------------- | ---------- | ------- | --------------------------------------------------------------------------------- |
| **Lenguaje Base**    | Python     | 3.10+   | Amplio soporte para cálculo numérico y facilidad de uso                           |
| **Interfaz gráfica** | PySide6    | 6.6+    | Framework Qt oficial para Python; permite crear UIs de escritorio multiplataforma |
| **Testing**          | pytest     | 8+      | Framework estándar para pruebas en Python                                         |
| **Linter**           | ruff       | 0.4+    | Análisis estático y formateo de código rápido                                     |
| **Gestión de deps**  | pip        | ---     | Manejo de dependencias mediante requirements.txt y pyproject.toml                 |
| **Documentación**    | Markdown   | ---     | Estándar para documentación en repositorios Git                                   |

---

## 3. Por qué Python y no Node.js

El repositorio fue inicialmente documentado con instrucciones de Node.js (npm install, node index.js), lo que generaba ambigüedad. La decisión de usar Python se basa en:

- Todo el código fuente del proyecto (src/escuadra/) está escrito en Python.
- Los módulos de cálculo de ingeniería (civil, eléctrica, matemáticas, sistemas) utilizan Python puro.
- El sistema de empaquetado usa pyproject.toml y setuptools, herramientas del ecosistema Python.
- PySide6 es una librería Python para interfaces gráficas, sin dependencia de Node.js.
- Los tests están escritos con pytest, no con ningún framework de JavaScript.

---

## 4. Componentes Principales

- Core (src/escuadra/core/): Lógica central del sistema, dispatcher y registro de herramientas.
- Módulos de ingeniería (src/escuadra/modulos/): Cada rama de ingeniería tiene su propio subdirectorio con herramientas independientes.
- Interfaz de usuario (src/escuadra/ui/): Componentes visuales basados en PySide6.
- Utilidades (src/escuadra/utils/): Funciones auxiliares, validaciones y helpers compartidos.
- Configuración (src/escuadra/config/): Carga y gestión de configuración del proyecto.
- IO (src/escuadra/io/): Parsers para leer archivos de entrada como CSV.
- Matemáticas (src/escuadra/math/): Operaciones matemáticas reutilizables como matrices, estadísticas y sistemas lineales.
- CLI (src/escuadra/cli.py): Interfaz de línea de comandos para acceder a las herramientas.

---

## 5. Organización por Ramas de Ingeniería

**El sistema está estructurado en módulos independientes según cada área:**

```text
escuadra/
├── src/
│   └── escuadra/
│       ├── core/           # Dispatcher y registro de herramientas
│       ├── io/             # Parsers de archivos de entrada (CSV, etc.)
│       ├── math/           # Operaciones matemáticas reutilizables
│       ├── modulos/
│       │   ├── civil/      # Herramientas de ingeniería civil
│       │   ├── electrica/  # Herramientas de ingeniería eléctrica
│       │   ├── geometria/  # Herramientas de geometría
│       │   ├── matematicas/# Herramientas matemáticas
│       │   └── sistemas/   # Herramientas de ingeniería de sistemas
│       ├── ui/             # Componentes de interfaz (PySide6)
│       ├── utils/          # Utilidades compartidas
│       └── config/         # Configuración
├── docs/                   # Documentación del proyecto
├── tests/                  # Pruebas automatizadas
├── requirements.txt        # Dependencias de producción
├── requirements-dev.txt    # Dependencias de desarrollo
└── pyproject.toml          # Metadatos y configuración del paquete
```

---

## 6. Decisiones de Diseño

### Decisión 1: Arquitectura Modular por rama de Ingeniería

**Contexto:** El proyecto cubre múltiples áreas de ingeniería con necesidades distintas.  
**Decisión:** Separar cada rama en módulos independientes dentro de src/escuadra/modulos/  
**Consecuencias:** Permite desarrollo paralelo sin conflictos y facilita agregar nuevas herramientas.

---

### Decisión 2: Interfaz gráfica con PySide6

**Contexto:** Se requiere una aplicación de escritorio accesible para estudiantes y profesionales.  
**Decisión:** Usar PySide6 como framework de UI, con componentes reutilizables en src/escuadra/ui/.  
**Consecuencias:** Interfaz multiplataforma (Windows, Linux, macOS) con el binding oficial de Qt para Python.

---

### Decisión 3: Módulos de cálculo independientes de la UI

**Contexto:** Las funciones de cálculo deben poder usarse desde la UI, la CLI o directamente como librería.  
**Decisión:** Separar la lógica de cálculo (módulos) de la capa de presentación (ui, cli).  
**Consecuencias:** Código reutilizable y más fácil de testear de forma aislada.

---

## 7. Flujo de Datos

1. El usuario interactúa con la UI (PySide6) o la CLI.
2. La interfaz recibe los parámetros de entrada y los valida.
3. Se invoca la función del módulo correspondiente (ej. calcular_reacciones).
4. El módulo procesa los datos usando matemática pura de Python.
5. El resultado se devuelve a la interfaz y se muestra al usuario.

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
