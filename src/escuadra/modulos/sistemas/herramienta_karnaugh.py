from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

from escuadra.modulos.sistemas.karnaugh import (
    generar_mapa_karnaugh,
    simplificar_expresion,
)


class HerramientaKarnaugh(Herramienta):
    nombre = "Mapas de Karnaugh"

    carrera = Carrera.SISTEMAS

    descripcion = (
        "Genera mapas de Karnaugh y realiza simplificaciones "
        "básicas de expresiones booleanas."
    )

    def crear_widget(self) -> QWidget:
        return QWidget()
