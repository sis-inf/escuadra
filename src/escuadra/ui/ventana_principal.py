"""
ventana_principal.py
====================
Ventana principal de la aplicación Escuadra.

Es el contenedor raíz de la UI: provee la barra de menú, el área central
donde se monta la herramienta activa y la barra de estado.  La ventana es
intencionalmente pasiva: no descubre herramientas ni construye widgets de
herramientas; solo expone los puntos de extensión necesarios para que otros
componentes (constructor de menú dinámico, integración de herramientas, etc.)
la configuren.
"""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QMenuBar,
    QStackedWidget,
    QStatusBar,
    QWidget,
)


class VentanaPrincipal(QMainWindow):
    """Ventana principal de Escuadra.

    Hereda de ``QMainWindow`` para aprovechar el soporte nativo de barra de
    menú, widget central y barra de estado.

    Estructura visual
    -----------------
    - **Título**: "Escuadra".
    - **Tamaño inicial**: 1 000 × 700 px; libremente redimensionable.
    - **Menú superior**: Archivo · Carrera · Herramientas · Ayuda.
    - **Área central**: ``QStackedWidget`` que aloja la herramienta activa.
    - **Barra de estado**: mensaje inicial "Lista para usar".

    Puntos de extensión
    -------------------
    - :py:meth:`menu_carrera` y :py:meth:`menu_herramientas` para que el
      constructor de menú dinámico (issue #9) añada entradas.
    - :py:meth:`mostrar_herramienta` para que la integración de herramientas
      reemplace el widget central.
    - :py:attr:`accion_acerca_de` para que la integración (issue #27) conecte
      el handler correspondiente.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._configurar_ventana()
        self._construir_menus()
        self._construir_area_central()
        self._construir_barra_estado()

    # ------------------------------------------------------------------
    # Configuración base
    # ------------------------------------------------------------------

    def _configurar_ventana(self) -> None:
        """Aplica título y tamaño inicial."""
        self.setWindowTitle("Escuadra")
        self.resize(1000, 700)
        # Permitir redimensionado libre (comportamiento por defecto en Qt,
        # pero se hace explícito para mayor claridad).
        self.setSizePolicy(
            self.sizePolicy().horizontalPolicy(),
            self.sizePolicy().verticalPolicy(),
        )

    # ------------------------------------------------------------------
    # Menú superior
    # ------------------------------------------------------------------

    def _construir_menus(self) -> None:
        """Crea la barra de menú con los cuatro menús iniciales."""
        barra: QMenuBar = self.menuBar()

        # ── Archivo ────────────────────────────────────────────────────
        menu_archivo: QMenu = barra.addMenu("Archivo")
        self._accion_salir = menu_archivo.addAction("Salir")
        self._accion_salir.triggered.connect(QApplication.quit)

        # ── Carrera ────────────────────────────────────────────────────
        # Vacío al construirse; lo llena el constructor de menú dinámico.
        self._menu_carrera: QMenu = barra.addMenu("Carrera")

        # ── Herramientas ───────────────────────────────────────────────
        # Vacío al construirse; lo llena el constructor de menú dinámico.
        self._menu_herramientas: QMenu = barra.addMenu("Herramientas")

        # ── Ayuda ──────────────────────────────────────────────────────
        menu_ayuda: QMenu = barra.addMenu("Ayuda")
        self.accion_acerca_de = menu_ayuda.addAction("Acerca de")
        # El handler se conecta desde la integración (issue #27).

    # ------------------------------------------------------------------
    # Área central
    # ------------------------------------------------------------------

    def _construir_area_central(self) -> None:
        """Crea el ``QStackedWidget`` que aloja la herramienta activa."""
        self._stack = QStackedWidget(self)
        # Placeholder vacío inicial para que el stack nunca esté vacío.
        self._stack.addWidget(QWidget(self._stack))
        self.setCentralWidget(self._stack)

    # ------------------------------------------------------------------
    # Barra de estado
    # ------------------------------------------------------------------

    def _construir_barra_estado(self) -> None:
        """Configura la barra de estado con el mensaje inicial."""
        barra: QStatusBar = self.statusBar()
        barra.showMessage("Lista para usar")

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------

    @property
    def menu_carrera(self) -> QMenu:
        """Devuelve el menú "Carrera" para que el constructor dinámico lo llene."""
        return self._menu_carrera

    @property
    def menu_herramientas(self) -> QMenu:
        """Devuelve el menú "Herramientas" para que el constructor dinámico lo llene."""
        return self._menu_herramientas

    def mostrar_herramienta(self, widget: QWidget) -> None:
        """Reemplaza el área central por *widget*.

        El widget anterior se retira del stack y se le llama
        ``deleteLater()`` para que Qt libere sus recursos de forma segura
        en el siguiente ciclo del event loop, evitando así leaks de memoria.

        Parameters
        ----------
        widget:
            El nuevo widget de herramienta a mostrar.  Debe ser una instancia
            de ``QWidget``; la ventana se hace cargo de su ciclo de vida a
            partir de este momento.
        """
        # Retirar y destruir el widget anterior (si no es el placeholder).
        anterior: QWidget = self._stack.currentWidget()
        if anterior is not None:
            self._stack.removeWidget(anterior)
            anterior.deleteLater()

        self._stack.addWidget(widget)
        self._stack.setCurrentWidget(widget)

    def mostrar_mensaje_estado(self, texto: str, timeout_ms: int = 0) -> None:
        """Muestra *texto* en la barra de estado.

        Parameters
        ----------
        texto:
            Mensaje a mostrar.
        timeout_ms:
            Si es mayor que cero, el mensaje se borra automáticamente
            transcurridos ese número de milisegundos.  Si es 0 (valor por
            defecto), el mensaje permanece hasta que se llame de nuevo a
            este método.
        """
        self.statusBar().showMessage(texto, timeout_ms)
