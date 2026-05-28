from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class WidgetHerramienta(QWidget):
    """
    Widget base reutilizable para herramientas.
    """

    def __init__(self, nombre, descripcion, parent=None):
        """
        Inicializa el widget base.
        """
        super().__init__(parent)

        layout_principal = QVBoxLayout(self)

        encabezado = QFrame()
        encabezado.setStyleSheet("""
            background-color: #EAEAEA;
            padding: 10px;
            border-radius: 5px;
        """)

        layout_encabezado = QVBoxLayout(encabezado)

        label_nombre = QLabel(nombre)

        fuente_titulo = QFont()
        fuente_titulo.setPointSize(14)
        fuente_titulo.setBold(True)

        label_nombre.setFont(fuente_titulo)

        label_descripcion = QLabel(descripcion)

        fuente_descripcion = QFont()
        fuente_descripcion.setItalic(True)

        label_descripcion.setFont(fuente_descripcion)

        layout_encabezado.addWidget(label_nombre)
        layout_encabezado.addWidget(label_descripcion)

        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setFrameShadow(QFrame.Sunken)

        self._contenido = QWidget()

        layout_principal.addWidget(encabezado)
        layout_principal.addWidget(separador)
        layout_principal.addWidget(self._contenido)

    def area_contenido(self):
        """
        Devuelve el área de contenido.
        """
        return self._contenido
