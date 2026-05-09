import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton,
    QGridLayout, QComboBox
)
from PyQt6.QtCore import Qt

from escuadra.core.herramienta import Herramienta
from escuadra.core.carrera import Carrera


class HerramientaCalculadoraCientifica(Herramienta):
    nombre = "Calculadora científica"
    carrera = Carrera.MATEMATICAS
    descripcion = "Calculadora con operaciones aritméticas, trigonométricas, logarítmicas y constantes."

    def crear_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()

        modo_layout = QHBoxLayout()
        modo_layout.addWidget(QLabel("Modo:"))
        self.modo_combo = QComboBox()
        self.modo_combo.addItems(["Radianes", "Grados"])
        modo_layout.addWidget(self.modo_combo)
        layout.addLayout(modo_layout)

        self.display = QLineEdit()
        self.display.setReadOnly(False)
        self.display.setStyleSheet("font-size: 16px; padding: 10px;")
        layout.addWidget(self.display)

        self.resultado_label = QLabel("Resultado: ")
        self.resultado_label.setStyleSheet("font-size: 14px; color: blue;")
        layout.addWidget(self.resultado_label)

        grid = QGridLayout()

        botones = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "←"],
            ["1", "2", "3", "-", "="],
            ["0", ".", "(", ")", "+"],
            ["sin", "cos", "tan", "√", "π"],
            ["log", "ln", "^", "e", "Del"]
        ]

        for fila_idx, fila in enumerate(botones):
            for col_idx, texto in enumerate(fila):
                boton = QPushButton(texto)
                boton.setStyleSheet("padding: 10px; font-size: 12px;")

                if texto == "=":
                    boton.clicked.connect(self.calcular)
                    boton.setStyleSheet("padding: 10px; font-size: 12px; background-color: green; color: white;")
                elif texto == "C":
                    boton.clicked.connect(self.limpiar)
                    boton.setStyleSheet("padding: 10px; font-size: 12px; background-color: red; color: white;")
                elif texto == "←":
                    boton.clicked.connect(self.borrar_ultimo)
                elif texto == "Del":
                    boton.clicked.connect(self.limpiar)
                else:
                    boton.clicked.connect(lambda checked, t=texto: self.agregar_texto(t))

                grid.addWidget(boton, fila_idx, col_idx)

        layout.addLayout(grid)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        widget.setLayout(layout)
        return widget

    def agregar_texto(self, texto):
        self.error_label.setText("")

        if texto == "π":
            self.display.setText(self.display.text() + "π")
        elif texto == "√":
            self.display.setText(self.display.text() + "sqrt(")
        elif texto == "sin":
            self.display.setText(self.display.text() + "sin(")
        elif texto == "cos":
            self.display.setText(self.display.text() + "cos(")
        elif texto == "tan":
            self.display.setText(self.display.text() + "tan(")
        elif texto == "log":
            self.display.setText(self.display.text() + "log(")
        elif texto == "ln":
            self.display.setText(self.display.text() + "ln(")
        elif texto == "^":
            self.display.setText(self.display.text() + "^")
        elif texto == "e":
            self.display.setText(self.display.text() + "e")
        else:
            self.display.setText(self.display.text() + texto)

    def borrar_ultimo(self):
        self.error_label.setText("")
        self.display.setText(self.display.text()[:-1])

    def limpiar(self):
        self.display.setText("")
        self.resultado_label.setText("Resultado: ")
        self.error_label.setText("")

    def calcular(self):
        self.error_label.setText("")
        expresion = self.display.text().strip()

        if not expresion:
            self.error_label.setText("Ingrese una expresión.")
            return

        try:
            resultado = self.evaluar_expresion(expresion)
            self.resultado_label.setText(f"Resultado: {resultado}")
            self.display.setText(str(resultado))
        except Exception as e:
            self.error_label.setText(f"Error: {str(e)}")

    def evaluar_expresion(self, expresion):
        expresion = expresion.replace("^", "**")
        expresion = expresion.replace("π", str(math.pi))
        expresion = expresion.replace("e", str(math.e))

        modo = self.modo_combo.currentText()

        namespace = {
            "sin": lambda x: math.sin(math.radians(x) if modo == "Grados" else x),
            "cos": lambda x: math.cos(math.radians(x) if modo == "Grados" else x),
            "tan": lambda x: math.tan(math.radians(x) if modo == "Grados" else x),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "__builtins__": {}
        }

        caracteres_permitidos = set("0123456789+-*/(). ^πesincogtanlognqrt")
        if not all(c in caracteres_permitidos for c in expresion.lower()):
            raise ValueError("Expresión contiene caracteres no permitidos.")

        try:
            resultado = eval(expresion, namespace)
            return round(resultado, 10)
        except ZeroDivisionError:
            raise ValueError("División por cero.")
        except ValueError as ve:
            raise ValueError(f"Error en dominio o sintaxis: {str(ve)}")
        except Exception as e:
            raise ValueError(f"Error en evaluación: {str(e)}")
