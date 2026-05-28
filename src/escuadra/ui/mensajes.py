from PyQt6.QtWidgets import QMessageBox


def mostrar_error(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de error crítico."""
    QMessageBox.critical(parent, titulo, mensaje)

def mostrar_advertencia(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de advertencia."""
    QMessageBox.warning(parent, titulo, mensaje)

def mostrar_informacion(parent, titulo, mensaje):
    """Muestra un cuadro de diálogo con ícono de información."""
    QMessageBox.information(parent, titulo, mensaje)

def confirmar(parent, titulo, mensaje):
    """
    Muestra un diálogo de confirmación con botones Sí/No en español.
    Devuelve True si el usuario confirma, False en caso contrario.
    """
    caja = QMessageBox(parent)
    caja.setWindowTitle(titulo)
    caja.setText(mensaje)
    caja.setIcon(QMessageBox.Icon.Question)

    # Agregar botones personalizados en español
    boton_si = caja.addButton("Sí", QMessageBox.ButtonRole.YesRole)
    boton_no = caja.addButton("No", QMessageBox.ButtonRole.NoRole)

    caja.exec()

    return caja.clickedButton() == boton_si
