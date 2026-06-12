"""
Herramienta de resolución de sistemas de ecuaciones lineales para Escuadra.
Resuelve sistemas A·x = b usando eliminación gaussiana con pivoteo parcial.
"""

from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta

# ── Lógica de resolución (separada de la UI) ────────────────────────────────

def resolver_sistema(A: list[list[float]], b: list[float]) -> list[float] | None:
    """
    Resuelve el sistema A·x = b usando eliminación gaussiana con pivoteo parcial.

    Args:
        A: Matriz de coeficientes n×n.
        b: Vector de términos independientes de tamaño n.

    Returns:
        Lista con la solución x, o None si el sistema es singular.
    """
    n = len(A)

    # Crear copia aumentada [A|b] para no modificar los originales
    M = [A[i][:] + [b[i]] for i in range(n)]

    # ── Eliminación hacia adelante con pivoteo parcial ───────────────────
    for col in range(n):

        # Buscar la fila con el mayor valor absoluto en esta columna (pivote)
        fila_pivote = max(range(col, n), key=lambda f: abs(M[f][col]))

        # Intercambiar la fila actual con la del pivote
        M[col], M[fila_pivote] = M[fila_pivote], M[col]

        pivote = M[col][col]

        # Si el pivote es cercano a cero, el sistema es singular
        if abs(pivote) < 1e-10:
            return None

        # Eliminar los coeficientes debajo del pivote
        for fila in range(col + 1, n):
            factor = M[fila][col] / pivote
            for j in range(col, n + 1):
                M[fila][j] -= factor * M[col][j]

    # ── Sustitución hacia atrás ──────────────────────────────────────────
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for j in range(i + 1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]

    return x


# ── Widget ───────────────────────────────────────────────────────────────────

class HerramientaSistemasLineales(Herramienta):
    nombre      = "Sistemas de ecuaciones lineales"
    carrera     = Carrera.MATEMATICAS
    descripcion = "Resuelve sistemas A·x = b para tamaños entre 2x2 y 5x5."

    def crear_widget(self) -> QWidget:
        self._widget = QWidget()
        root = QVBoxLayout()
        root.setSpacing(10)

        # ── Selector de tamaño ───────────────────────────────────────────
        fila_size = QHBoxLayout()
        fila_size.addWidget(QLabel("Tamaño del sistema:"))
        self._spinbox = QSpinBox()
        self._spinbox.setMinimum(2)
        self._spinbox.setMaximum(5)
        self._spinbox.setValue(2)
        self._spinbox.valueChanged.connect(self._reconstruir_grilla)
        fila_size.addWidget(self._spinbox)
        fila_size.addStretch()
        root.addLayout(fila_size)

        # ── Contenedor de la grilla ──────────────────────────────────────
        self._grilla_container = QVBoxLayout()
        root.addLayout(self._grilla_container)

        # ── Botones ──────────────────────────────────────────────────────
        botones = QHBoxLayout()
        btn_resolver = QPushButton("Resolver")
        btn_resolver.clicked.connect(self._resolver)
        btn_limpiar  = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self._limpiar)
        botones.addWidget(btn_resolver)
        botones.addWidget(btn_limpiar)
        root.addLayout(botones)

        # ── Resultado ────────────────────────────────────────────────────
        self._resultado_label = QLabel("")
        self._resultado_label.setWordWrap(True)
        root.addWidget(self._resultado_label)

        # ── Error ────────────────────────────────────────────────────────
        self._error_label = QLabel("")
        self._error_label.setStyleSheet("color: red;")
        self._error_label.setWordWrap(True)
        root.addWidget(self._error_label)

        root.addStretch()
        self._widget.setLayout(root)

        # Construir grilla inicial
        self._inputs_A: list[list[QLineEdit]] = []
        self._inputs_b: list[QLineEdit] = []
        self._reconstruir_grilla(2)

        return self._widget

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _reconstruir_grilla(self, n: int) -> None:
        """Reconstruye la grilla de inputs conservando valores que aún encajan."""

        # Guardar valores anteriores
        valores_A = [
            [self._inputs_A[i][j].text() for j in range(len(self._inputs_A[i]))]
            for i in range(len(self._inputs_A))
        ]
        valores_b = [self._inputs_b[i].text() for i in range(len(self._inputs_b))]

        # Limpiar grilla anterior
        while self._grilla_container.count():
            item = self._grilla_container.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self._limpiar_layout(item.layout())

        # Crear nueva grilla
        grilla = QGridLayout()
        grilla.setSpacing(6)

        # Encabezados
        for j in range(n):
            grilla.addWidget(QLabel(f"x{j+1}"), 0, j + 1)
        grilla.addWidget(QLabel("b"), 0, n + 2)

        self._inputs_A = []
        self._inputs_b = []

        for i in range(n):
            grilla.addWidget(QLabel(f"Ec {i+1}:"), i + 1, 0)
            fila_inputs = []
            for j in range(n):
                campo = QLineEdit()
                campo.setPlaceholderText("0")
                campo.setFixedWidth(60)
                # Restaurar valor si existía
                if i < len(valores_A) and j < len(valores_A[i]):
                    campo.setText(valores_A[i][j])
                grilla.addWidget(campo, i + 1, j + 1)
                fila_inputs.append(campo)
            self._inputs_A.append(fila_inputs)

            # Separador visual entre A y b
            grilla.addWidget(QLabel("|"), i + 1, n + 1)

            # Campo b
            campo_b = QLineEdit()
            campo_b.setPlaceholderText("0")
            campo_b.setFixedWidth(60)
            if i < len(valores_b):
                campo_b.setText(valores_b[i])
            grilla.addWidget(campo_b, i + 1, n + 2)
            self._inputs_b.append(campo_b)

        contenedor = QWidget()
        contenedor.setLayout(grilla)
        self._grilla_container.addWidget(contenedor)

    def _limpiar_layout(self, layout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def _resolver(self) -> None:
        self._error_label.setText("")
        self._resultado_label.setText("")
        n = self._spinbox.value()

        # Leer matriz A
        A = []
        for i in range(n):
            fila = []
            for j in range(n):
                texto = self._inputs_A[i][j].text().strip()
                try:
                    fila.append(float(texto))
                except ValueError:
                    self._error_label.setText(
                        f"Error: valor inválido en A[{i+1}][{j+1}]: «{texto}»"
                    )
                    return
            A.append(fila)

        # Leer vector b
        b = []
        for i in range(n):
            texto = self._inputs_b[i].text().strip()
            try:
                b.append(float(texto))
            except ValueError:
                self._error_label.setText(
                    f"Error: valor inválido en b[{i+1}]: «{texto}»"
                )
                return

        # Resolver
        solucion = resolver_sistema(A, b)

        if solucion is None:
            self._error_label.setText(
                "El sistema no tiene solución única (matriz singular)."
            )
            return

        lineas = [f"x{i+1} = {round(v, 6)}" for i, v in enumerate(solucion)]
        self._resultado_label.setText("Solución:\n" + "\n".join(lineas))

    def _limpiar(self) -> None:
        self._error_label.setText("")
        self._resultado_label.setText("")
        for fila in self._inputs_A:
            for campo in fila:
                campo.clear()
        for campo in self._inputs_b:
            campo.clear()
