# Arquitectura del Sistema - Escuadra

## 1. Visión General

Escuadra es una suite modular de herramientas orientadas a distintas ramas de la ingeniería.  
La arquitectura está diseñada bajo el principio de **separación de responsabilidades**, permitiendo que cada componente cumpla una función específica y sea fácilmente mantenible y escalable.

---

## 2. Componentes Principales

- **Core (src/):**
  Contiene la lógica principal del sistema y los algoritmos de cálculo.

- **Módulos de herramientas:**
  Cada herramienta de ingeniería se implementa como un módulo independiente dentro del core.

- **Capa de presentación:**
  Encargada de la interacción con el usuario (CLI o futura interfaz gráfica).

- **Utilidades (utils):**
  Manejo de errores, validaciones y funciones auxiliares.

---

## 3. Estructura del Proyecto


escuadra/
│
├── src/
│ ├── core/
│ ├── tools/
│ └── utils/
│
├── documentos/
│ └── arquitectura.md
│
├── pruebas/
└── datos/


---

## 4. Diagrama de Arquitectura


Usuario
│
▼
Interfaz (CLI / UI)
│
▼
Core (Lógica de negocio)
│
▼
Módulos de herramientas
│
▼
Resultados


---

## 5. Tecnologías Utilizadas

| Componente | Tecnología | Justificación |
|-----------|-----------|--------------|
| Lenguaje  | Python    | Simplicidad para cálculos y prototipos |
| Testing   | pytest    | Pruebas automatizadas |
| Gestión   | Git       | Control de versiones |
| Docs      | Markdown  | Documentación clara |

---

## 6. Decisiones de Diseño

### Decisión 1: Arquitectura modular

**Contexto:** Se requieren múltiples herramientas independientes.  
**Decisión:** Separar cada herramienta en módulos.  
**Consecuencia:** Facilita mantenimiento y escalabilidad.

---

### Decisión 2: Separación de lógica y presentación

**Contexto:** Evitar mezclar UI con lógica.  
**Decisión:** Mantener la lógica en `src/core`.  
**Consecuencia:** Código más limpio y reutilizable.

---

## 7. Flujo de Datos

1. El usuario ingresa datos
2. La interfaz envía datos al core
3. El core procesa mediante un módulo
4. Se genera resultado
5. Se devuelve al usuario