
def __init__(self, parent=None):
    super().__init__(parent)
    self._setup_ui()
    self._setup_comparacion()

def _setup_comparacion(self):
    # Botón para comparar
    self.btn_comparar = QPushButton("Comparar", self)
    self.btn_comparar.clicked.connect(self._comparar_seleccion)
    self.btn_comparar.setEnabled(False)
    
    # Conectar selección de la lista
    self.lista_historial.itemSelectionChanged.connect(self._on_seleccion_cambiada)

def _on_seleccion_cambiada(self):
    seleccionados = self.lista_historial.selectedItems()
    self.btn_comparar.setEnabled(len(seleccionados) == 2)

def _comparar_seleccion(self):
    from src.escuadra.ui.dialogo_comparar_historial import DialogoCompararHistorial
    seleccionados = self.lista_historial.selectedItems()
    if len(seleccionados) == 2:
        entrada1 = self._obtener_datos(seleccionados[0])
        entrada2 = self._obtener_datos(seleccionados[1])
        dialogo = DialogoCompararHistorial(entrada1, entrada2, self)
        dialogo.exec()

def _obtener_datos(self, item):
    return {"texto": item.text()}
