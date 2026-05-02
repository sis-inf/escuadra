from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFrame
)
from PyQt5.QtGui import QFont


class WidgetHerramienta(QWidget):
    """
    Widget base para herramientas.

    Contiene:
    - Encabezado con nombre y descripción
    - Separador horizontal
    - Área de contenido donde se agregan los controles específicos
    """

    def __init__(self, nombre, descripcion, parent=None):
        super().__init__(parent)

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # =========================
        # ENCABEZADO
        # =========================
        header = QFrame()
        header_layout = QVBoxLayout(header)

        # Estilo del encabezado
        header.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                padding: 10px;
            }
        """)

        # Titulo
        self.label_nombre = QLabel(nombre)
        font_titulo = QFont()
        font_titulo.setPointSize(14)
        font_titulo.setBold(True)
        self.label_nombre.setFont(font_titulo)

        # Descripcion
        self.label_descripcion = QLabel(descripcion)
        font_desc = QFont()
        font_desc.setItalic(True)
        self.label_descripcion.setFont(font_desc)

        # Agregar al header
        header_layout.addWidget(self.label_nombre)
        header_layout.addWidget(self.label_descripcion)

        # =========================
        # SEPARADOR
        # =========================
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setFrameShadow(QFrame.Sunken)

        # =========================
        # AREA DE CONTENIDO
        # =========================
        self._area_contenido = QWidget()

        # =========================
        # AGREGAR TODO
        # =========================
        layout_principal.addWidget(header)
        layout_principal.addWidget(separador)
        layout_principal.addWidget(self._area_contenido)

    def area_contenido(self):
        """
        Devuelve el QWidget donde la herramienta puede agregar su UI.
        """
        return self._area_contenido