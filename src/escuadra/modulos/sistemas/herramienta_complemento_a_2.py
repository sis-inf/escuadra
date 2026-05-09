from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta
from PyQt6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)


class HerramientaComplementoA2(Herramienta):
    nombre = "Complemento a 2"
    carrera = Carrera.SISTEMAS
    descripcion = "Convierte entre decimal con signo y representación en complemento a 2."

    def crear_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # Selector de bits
        bits_layout = QHBoxLayout()
        bits_label = QLabel("Ancho de bits:")
        self.bits_combo = QComboBox()
        self.bits_combo.addItems(["4", "8", "16", "32"])
        self.bits_combo.setCurrentText("8")
        self.bits_combo.currentTextChanged.connect(self.actualizar_rango)
        self.bits_combo.currentTextChanged.connect(self.calcular_a_binario)
        self.bits_combo.currentTextChanged.connect(self.calcular_a_decimal)

        bits_layout.addWidget(bits_label)
        bits_layout.addWidget(self.bits_combo)
        bits_layout.addStretch()
        layout.addLayout(bits_layout)

        # Etiqueta de rango
        self.rango_label = QLabel("")
        layout.addWidget(self.rango_label)

        # Grupo: Decimal a Complemento a 2
        grupo_dec_bin = QGroupBox("Decimal a Complemento a 2")
        layout_dec_bin = QFormLayout()

        self.input_decimal = QLineEdit()
        self.input_decimal.setPlaceholderText("Ej. -5")
        self.input_decimal.textChanged.connect(self.calcular_a_binario)

        self.output_binario = QLineEdit()
        self.output_binario.setReadOnly(True)

        self.error_dec_bin = QLabel("")
        self.error_dec_bin.setStyleSheet("color: red;")

        layout_dec_bin.addRow("Decimal con signo:", self.input_decimal)
        layout_dec_bin.addRow("Complemento a 2:", self.output_binario)
        layout_dec_bin.addRow("", self.error_dec_bin)
        grupo_dec_bin.setLayout(layout_dec_bin)
        layout.addWidget(grupo_dec_bin)

        # Grupo: Complemento a 2 a Decimal
        grupo_bin_dec = QGroupBox("Complemento a 2 a Decimal")
        layout_bin_dec = QFormLayout()

        self.input_binario = QLineEdit()
        self.input_binario.setPlaceholderText("Ej. 11111011")
        self.input_binario.textChanged.connect(self.calcular_a_decimal)

        self.output_decimal = QLineEdit()
        self.output_decimal.setReadOnly(True)

        self.error_bin_dec = QLabel("")
        self.error_bin_dec.setStyleSheet("color: red;")

        layout_bin_dec.addRow("Complemento a 2:", self.input_binario)
        layout_bin_dec.addRow("Decimal con signo:", self.output_decimal)
        layout_bin_dec.addRow("", self.error_bin_dec)
        grupo_bin_dec.setLayout(layout_bin_dec)
        layout.addWidget(grupo_bin_dec)

        layout.addStretch()
        widget.setLayout(layout)

        self.actualizar_rango()
        return widget

    def actualizar_rango(self):
        bits = int(self.bits_combo.currentText())
        min_val = -(2 ** (bits - 1))
        max_val = (2 ** (bits - 1)) - 1
        self.rango_label.setText(f"Rango con {bits} bits: {min_val} a {max_val}")

    def decimal_a_complemento(self, numero: int, bits: int) -> str:
        min_val = -(2 ** (bits - 1))
        max_val = (2 ** (bits - 1)) - 1

        if not (min_val <= numero <= max_val):
            raise ValueError(f"Error de rango: el número debe estar entre {min_val} y {max_val}.")

        if numero >= 0:
            return f"{numero:0{bits}b}"
        else:
            return f"{(2 ** bits + numero):0{bits}b}"

    def complemento_a_decimal(self, binario: str, bits: int) -> int:
        if len(binario) != bits:
            raise ValueError(f"Error de longitud: debe tener exactamente {bits} bits.")
        if not all(c in '01' for c in binario):
            raise ValueError("Error de formato: debe contener solo '0' y '1'.")

        if binario[0] == '0':
            return int(binario, 2)
        else:
            valor = int(binario, 2)
            return valor - (2 ** bits)

    def calcular_a_binario(self):
        texto = self.input_decimal.text().strip()
        self.output_binario.clear()
        self.error_dec_bin.clear()

        if not texto:
            return

        try:
            numero = int(texto)
            bits = int(self.bits_combo.currentText())
            resultado = self.decimal_a_complemento(numero, bits)
            self.output_binario.setText(resultado)
        except ValueError as e:
            if "Error de rango" in str(e):
                self.error_dec_bin.setText(str(e))
            else:
                self.error_dec_bin.setText("Error: Ingrese un número entero válido.")

    def calcular_a_decimal(self):
        texto = self.input_binario.text().strip()
        self.output_decimal.clear()
        self.error_bin_dec.clear()

        if not texto:
            return

        try:
            bits = int(self.bits_combo.currentText())
            resultado = self.complemento_a_decimal(texto, bits)
            self.output_decimal.setText(str(resultado))
        except ValueError as e:
            self.error_bin_dec.setText(str(e))
