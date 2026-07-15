from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

from escuadra.modulos.matematicas.financiera import (
    calcular_valor_futuro,
    calcular_valor_presente,
    calcular_interes_compuesto,
)


class HerramientaFinanciera(Herramienta):
    nombre = "Matemática financiera"

    carrera = Carrera.MATEMATICAS

    descripcion = (
        "Calcula valor futuro, valor presente "
        "e interés compuesto."
    )

    def crear_widget(self) -> QWidget:
        return QWidget()
