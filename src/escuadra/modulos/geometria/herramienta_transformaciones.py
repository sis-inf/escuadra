from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

from escuadra.modulos.geometria.transformaciones import (
    rotar_punto,
    trasladar_punto,
    escalar_punto,
)


class HerramientaTransformaciones(Herramienta):
    nombre = "Transformaciones Geométricas"

    carrera = Carrera.GEOMETRIA

    descripcion = (
        "Permite rotar, trasladar y escalar puntos "
        "en el plano cartesiano."
    )

    def crear_widget(self) -> QWidget:
        return QWidget()
