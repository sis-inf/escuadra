"""
Herramienta de la Ley de Ohm para Escuadra.
Calcula voltaje, corriente o resistencia a partir de las otras dos magnitudes.
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

# Funciones puras de calculo

def calcular_voltaje(corriente: float, resistencia: float) -> float:
    return corriente * resistencia


def calcular_corriente(voltaje: float, resistencia: float) -> float:
    if resistencia == 0:
        raise ValueError("La resistencia no puede ser cero.")
    return voltaje / resistencia


def calcular_resistencia(voltaje: float, corriente: float) -> float:
    if corriente == 0:
        raise ValueError("La corriente no puede ser cero.")
    return voltaje / corriente


def calcular_potencia(voltaje: float, corriente: float) -> float:
    return voltaje * corriente


# Widget

class HerramientaLeyOhm(Herramienta):
    nombre      = "Ley de Ohm"
    carrera     = Carrera.ELECTRICA
    descripcion = "Calcula voltaje, corriente o resistencia a partir de las otras dos magnitudes."

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # Mensaje de ayuda
        ayuda = QLabel("Ingresa dos valores y deja vacío el tercero para calcularlo.")
        ayuda.setWordWrap(True)
        root.addWidget(ayuda)

        # Campos de entrada
        self._campos: dict[str, QLineEdit] = {}

        for etiqueta, clave in [
            ("Voltaje (V)", "V"),
            ("Corriente (A)", "I"),
            ("Resistencia (Ω)", "R"),
        ]:
            fila = QHBoxLayout()
            label = QLabel(etiqueta)
            label.setFixedWidth(120)
            campo = QLineEdit()
            campo.setPlaceholderText("Dejar vacío para calcular")
            fila.addWidget(label)
            fila.addWidget(campo)
            root.addLayout(fila)
            self._campos[clave] = campo

        # Botones
        botones = QHBoxLayout()
        btn_calcular = QPushButton("Calcular")
        btn_calcular.clicked.connect(self._calcular)
        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)
        botones.addWidget(btn_calcular)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # Resultados
        fila_p = QHBoxLayout()
        fila_p.addWidget(QLabel("Potencia (W):"))
        self._potencia_output = QLineEdit()
        self._potencia_output.setReadOnly(True)
        self._potencia_output.setPlaceholderText("—")
        fila_p.addWidget(self._potencia_output)
        root.addLayout(fila_p)

        # Error
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        root.addStretch()
        widget.setLayout(root)
        return widget

    def _leer_campo(self, clave: str) -> float | None:
        texto = self._campos[clave].text().strip()
        if texto == "":
            return None
        return float(texto)

    def _calcular(self) -> None:
        self._error_label.setText("")
        self._potencia_output.clear()

        # Leer valores
        valores: dict[str, float | None] = {}
        for clave in ("V", "I", "R"):
            texto = self._campos[clave].text().strip()
            if texto == "":
                valores[clave] = None
            else:
                try:
                    v = float(texto)
                    if v < 0:
                        self._error_label.setText(
                            f"Error: el valor de {clave} debe ser positivo."
                        )
                        return
                    valores[clave] = v
                except ValueError:
                    self._error_label.setText(
                        f"Error: «{texto}» no es un número válido."
                    )
                    return

        vacios = [k for k, v in valores.items() if v is None]

        if len(vacios) == 0:
            self._error_label.setText(
                "Deja vacío el campo que deseas calcular."
            )
            return

        if len(vacios) >= 2:
            self._error_label.setText(
                "Ingresa al menos dos valores para poder calcular."
            )
            return

        # Calcular el campo faltante
        try:
            if vacios[0] == "V":
                resultado = calcular_voltaje(valores["I"], valores["R"])
                self._campos["V"].setText(str(round(resultado, 4)))
                voltaje, corriente = resultado, valores["I"]
            elif vacios[0] == "I":
                resultado = calcular_corriente(valores["V"], valores["R"])
                self._campos["I"].setText(str(round(resultado, 4)))
                voltaje, corriente = valores["V"], resultado
            else:
                resultado = calcular_resistencia(valores["V"], valores["I"])
                self._campos["R"].setText(str(round(resultado, 4)))
                voltaje, corriente = valores["V"], valores["I"]
        except ValueError as e:
            self._error_label.setText(str(e))
            return

        # Calcular potencia
        P = calcular_potencia(voltaje, corriente)
        self._potencia_output.setText(str(round(P, 4)))

    def _limpiar(self) -> None:
        self._error_label.setText("")
        self._potencia_output.clear()
        for campo in self._campos.values():
            campo.clear()
