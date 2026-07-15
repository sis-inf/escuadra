"""Módulo de interfaz para el panel de historial y su exportación en PySide6."""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QMessageBox
)
from escuadra.io.exportador_json import exportar_lista


class PanelHistorial(QWidget):
    """Panel visual que gestiona y permite exportar el historial de operaciones."""

    def __init__(self, parent=None):
        super().__init__(parent)
        # Lista que almacenará las entradas del historial cumpliendo con:
        # parámetros, resultado y timestamp.
        self.historial_datos = []
        
        self._configurar_interfaz()

    def _configurar_interfaz(self):
        """Construye y dispone los elementos visuales del panel."""
        self.layout_principal = QVBoxLayout(self)

        # TODO: Aquí puedes agregar listas, tablas u otros widgets que muestren 
        # visualmente el historial en tu aplicación.

        # Botón requerido estrictamente por el issue: 'Exportar historial'
        self.btn_exportar = QPushButton("Exportar historial", self)
        self.btn_exportar.clicked.connect(self.exportar_historial)
        
        # Agregar el botón al layout del panel
        self.layout_principal.addWidget(self.btn_exportar)

    def agregar_entrada(self, parametros: dict, resultado: any, timestamp: str):
        """
        Registra una nueva entrada en el historial.
        Asegura que contenga parámetros, resultado y timestamp según criterios de aceptación.
        """
        entrada = {
            "timestamp": timestamp,
            "parametros": parametros,
            "resultado": resultado
        }
        self.historial_datos.append(entrada)

    def exportar_historial(self):
        """
        Acción del botón 'Exportar historial'.
        Abre un diálogo de selección de archivo y guarda la lista de historial en formato JSON.
        """
        if not self.historial_datos:
            QMessageBox.warning(
                self, 
                "Historial vacío", 
                "No hay entradas en el historial para exportar."
            )
            return

        # Abrir diálogo nativo para que el usuario elija la ruta y nombre del archivo
        ruta_archivo, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar historial completo",
            "",  # Directorio inicial por defecto
            "Archivos JSON (*.json);;Todos los archivos (*.*)"
        )

        # Si el usuario seleccionó una ruta y no canceló el diálogo
        if ruta_archivo:
            # Asegurarse de que termine con la extensión .json
            if not ruta_archivo.endswith(".json"):
                ruta_archivo += ".json"

            try:
                # Se llama a exportar_lista pasando sobreescribir=True, ya que el propio
                # QFileDialog se encarga de pedir confirmación al usuario si el archivo ya existe.
                exportar_lista(self.historial_datos, ruta_archivo, sobreescribir=True)
                
                QMessageBox.information(
                    self, 
                    "Exportación exitosa", 
                    f"El historial se ha exportado correctamente a:\n{ruta_archivo}"
                )
            except Exception as error:
                QMessageBox.critical(
                    self, 
                    "Error al exportar", 
                    f"Ocurrió un error al guardar el archivo:\n{str(error)}"
                )