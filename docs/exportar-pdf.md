# 📄 Exportación a Reportes PDF

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
📄 Ejemplo de reporte generado
A continuación se muestra un ejemplo del contenido que genera Escuadra al exportar un reporte en PDF.

Ejemplo: Reporte de Cálculo de Viga
text
┌─────────────────────────────────────────────────────────────┐
│  📐 ESCUADRA - Reporte de Cálculo                           │
│  Fecha: 2026-07-08                                          │
│  Hora: 14:30                                                │
│  Herramienta: Cálculo de Vigas                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📥 Parámetros de entrada:                                  │
│  • Longitud de la viga: 5.0 m                              │
│  • Carga aplicada: 10.0 kN                                 │
│  • Material: Acero estructural                             │
│                                                             │
│  📊 Resultados obtenidos:                                   │
│  • Momento flector máximo: 12.50 kN·m                      │
│  • Cortante máximo: 5.00 kN                                │
│  • Flecha máxima: 2.30 mm                                  │
│                                                             │
│  ✅ Cálculo completado exitosamente                         │
│                                                             │
│  ⚙️ Información adicional:                                  │
│  • Versión de Escuadra: 0.1.0                              │
│  • Tiempo de cálculo: 0.02 s                               │
├─────────────────────────────────────────────────────────────┤
│  Escuadra v0.1.0 | Página 1 de 1                           │
└─────────────────────────────────────────────────────────────┘
Nota: El formato del reporte puede variar según la herramienta utilizada.

⚙️ Personalización del reporte
Opción	Descripción
--formato	Tamaño de página: A4, Letter, Legal
--orientacion	Orientación: vertical (portrait) u horizontal (landscape)
--incluir-graficos	Incluye gráficos en el reporte
--titulo	Título personalizado del reporte
🔧 Solución de problemas
Problema	Solución
No se genera el PDF	Verificar que ReportLab esté instalado: pip install reportlab
Error de permisos	Asegurarse de tener permisos de escritura en la carpeta de destino
Fuentes no encontradas	Instalar fuentes adicionales o usar las fuentes estándar de ReportLab
