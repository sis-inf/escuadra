"""
Carga dinámica de herramientas en la ventana principal.
"""

from escuadra.ui.mensajes import mostrar_error
from escuadra.utils.logging_config import obtener_logger

logger = obtener_logger("cargador_herramienta")


class CargadorHerramienta:
    """
    Router interno que conecta la selección del menú
    con la carga de widgets en la ventana principal.
    """

    def __init__(self, ventana):
        self._ventana = ventana
        self._herramienta_actual = None
        self._widget_actual = None

    def cargar(self, clase_herramienta):
        """
        Instancia una herramienta, crea su widget
        y la muestra en la ventana principal.
        """

        try:
            # Liberar widget anterior si existe
            if self._widget_actual is not None:
                self._widget_actual.setParent(None)
                self._widget_actual.deleteLater()

                self._widget_actual = None
                self._herramienta_actual = None

            herramienta = clase_herramienta()

            widget = herramienta.crear_widget()

            self._ventana.mostrar_herramienta(widget)

            nombre = clase_herramienta.__name__

            self._ventana.mostrar_mensaje_estado(f"Herramienta activa: {nombre}")

            self._herramienta_actual = herramienta
            self._widget_actual = widget

        except Exception as error:
            logger.error(f"Error al cargar herramienta: {error}", exc_info=True)

            mostrar_error(
                self._ventana,
                "Error al cargar herramienta",
                str(error),
            )

    def herramienta_actual(self):
        """
        Devuelve la herramienta actualmente cargada.
        """
        return self._herramienta_actual
