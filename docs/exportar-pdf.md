#  Exportación a Reportes PDF

Esta guía explica cómo exportar los resultados de los cálculos de Escuadra a un **reporte en formato PDF**.

---

##  ¿Qué permite la exportación a PDF?

La exportación a PDF permite:

- **Guardar** los resultados de los cálculos realizados.
- **Compartir** reportes con clientes, colegas o docentes.
- **Archivar** los resultados de forma profesional y legible.
- **Incluir** gráficos, tablas y datos numéricos en un solo documento.

---

##  Requisitos previos

| Requisito | Descripción |
|-----------|-------------|
| **Python 3.8+** | Lenguaje de programación |
| **PySide6** | Librería para la interfaz gráfica |
| **ReportLab** | Librería para generar PDF |

> **Nota:** ReportLab se instala automáticamente con las dependencias del proyecto.

---

##  Cómo exportar un reporte PDF

### Desde la interfaz gráfica

1. Realizá los cálculos necesarios en la herramienta correspondiente.
2. Hacé clic en el botón **"Exportar a PDF"** (o similar) en la ventana de resultados.
3. Seleccioná la ubicación donde guardar el archivo.
4. El PDF se generará automáticamente con los resultados.

### Desde la línea de comandos

```bash
escuadra exportar-pdf --archivo reporte.pdf --formato A4
```

Donde:

- `--archivo` indica el nombre del archivo PDF a generar.
- `--formato` permite seleccionar el tamaño de página deseado.

---

##  Ejemplo de reporte generado

A continuación se muestra un ejemplo simplificado del contenido que puede incluir un reporte PDF exportado desde Escuadra.

### Reporte de cálculo

**Herramienta:** Cálculo de área de losa

**Fecha de generación:** 15/07/2026

#### Parámetros de entrada

| Parámetro | Valor |
|-----------|-------|
| Largo | 5 m |
| Ancho | 3 m |

#### Resultado

Área calculada:

```text
15 m²
```

#### Observaciones

El cálculo fue realizado utilizando los parámetros proporcionados por el usuario y el resultado fue incorporado automáticamente al reporte PDF.

---

Este ejemplo ilustra la estructura típica de un reporte exportado, incluyendo información de identificación, parámetros de entrada y resultados obtenidos.

---

##  Información incluida en el reporte

Dependiendo de la herramienta utilizada, el reporte PDF puede contener:

- Nombre de la herramienta o cálculo ejecutado.
- Fecha y hora de generación.
- Parámetros de entrada.
- Resultados obtenidos.
- Tablas de datos.
- Observaciones o notas adicionales.

---

##  Beneficios de utilizar reportes PDF

- Facilita la conservación de resultados para futuras consultas.
- Permite compartir información sin depender de software específico.
- Mantiene el formato del documento independientemente del dispositivo utilizado.
- Ofrece una presentación profesional de los cálculos realizados.