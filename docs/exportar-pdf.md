s# 📄 Exportación a Reportes PDF

Esta guía explica cómo exportar los resultados de los cálculos de Escuadra a un **reporte en formato PDF**.

---

## 🎯 ¿Qué permite la exportación a PDF?

La exportación a PDF permite:

- **Guardar** los resultados de los cálculos realizados.
- **Compartir** reportes con clientes, colegas o docentes.
- **Archivar** los resultados de forma profesional y legible.
- **Incluir** gráficos, tablas y datos numéricos en un solo documento.

---

## 📋 Requisitos previos

| Requisito | Descripción |
|-----------|-------------|
| **Python 3.8+** | Lenguaje de programación |
| **PySide6** | Librería para la interfaz gráfica |
| **ReportLab** | Librería para generar PDF |

> **Nota:** ReportLab se instala automáticamente con las dependencias del proyecto.

---

## 🚀 Cómo exportar un reporte PDF

### Desde la interfaz gráfica

1. **Realizá los cálculos** necesarios en la herramienta correspondiente.
2. Hacé clic en el botón **"Exportar a PDF"** (o similar) en la ventana de resultados.
3. Seleccioná la ubicación donde guardar el archivo.
4. El PDF se generará automáticamente con los resultados.

### Desde la línea de comandos

```bash
escuadra exportar-pdf --archivo reporte.pdf --formato A4
