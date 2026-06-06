# Guía de Estilo para Mensajes de Commit

## Introducción

Este proyecto utiliza la convención Conventional Commits para mantener un historial de cambios claro, consistente y fácil de entender. El objetivo es que cualquier colaborador pueda identificar rápidamente el propósito de un cambio únicamente leyendo el mensaje de commit.

La estructura recomendada es:

(tipo(ámbito): descripción)

Ejemplo:

feat(civil): agregar cálculo de carga distribuida

El tipo indica la naturaleza del cambio, el ámbito señala el módulo afectado y la descripción resume brevemente la modificación realizada.

---

## Tipos de commit permitidos

| Tipo | Descripción |
|--------|-------------|
| feat | Nueva funcionalidad |
| fix | Corrección de errores |
| docs | Cambios en documentación |
| test | Agregar o modificar pruebas |
| chore | Tareas de mantenimiento |
| refactor | Reestructuración sin cambiar funcionalidad |
| style | Cambios de formato o estilo |
| ci | Configuración de integración continua |

---

## Ámbitos recomendados

Los ámbitos ayudan a identificar la parte del proyecto afectada.

- civil
- electrica
- matematicas
- sistemas
- geometria
- core
- io
- cli
- config

Ejemplos:

- feat(civil): agregar cálculo de vigas
- fix(matematicas): corregir error de redondeo
- docs(core): actualizar documentación principal

---

## Ejemplos correctos

### 1

```text
feat(civil): agregar cálculo de cargas
```

### 2

```text
fix(matematicas): corregir error en interpolación
```

### 3

```text
docs(core): actualizar guía de instalación
```

### 4

```text
test(geometria): agregar pruebas para triangulación
```

### 5

```text
chore(config): actualizar dependencias
```

### 6

```text
refactor(io): simplificar lectura de archivos
```

### 7

```text
style(cli): mejorar formato del código
```

### 8

```text
ci(config): configurar GitHub Actions
```

---

## Ejemplos incorrectos y corrección

### Incorrecto 1

```text
arreglos varios
```

Correcto:

```text
fix(core): corregir errores menores
```

### Incorrecto 2

```text
nuevo metodo
```

Correcto:

```text
feat(matematicas): agregar nuevo método numérico
```

### Incorrecto 3

```text
actualizacion
```

Correcto:

```text
docs(core): actualizar documentación principal
```

### Incorrecto 4

```text
test
```

Correcto:

```text
test(civil): agregar pruebas para estructuras
```

### Incorrecto 5

```text
correcciones
```

Correcto:

```text
fix(geometria): corregir validación de polígonos
```

---

## Buenas prácticas

- Utilizar verbos en infinitivo.
- Mantener descripciones cortas y claras.
- Especificar el ámbito cuando sea posible.
- Evitar mensajes genéricos.
- Mantener consistencia entre todos los colaboradores.

## Conclusión

Seguir estas convenciones mejora la trazabilidad del proyecto, facilita las revisiones de código y permite comprender rápidamente el historial de cambios. Un mensaje de commit bien escrito contribuye a una colaboración más eficiente y profesional.
