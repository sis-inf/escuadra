"""
Pruebas para el módulo cargador_herramienta.py
"""

import pytest
from unittest.mock import MagicMock, patch

from escuadra.ui.cargador_herramienta import CargadorHerramienta


class TestCargadorHerramienta:
    """Pruebas para la clase CargadorHerramienta"""

    def test_cargador_initialization(self):
        """Verifica que el cargador se inicializa correctamente"""
        mock_ventana = MagicMock()
        cargador = CargadorHerramienta(mock_ventana)
        assert cargador is not None
        assert cargador._ventana == mock_ventana

    def test_cargar_herramienta_exitosa(self):
        """Verifica que carga una herramienta correctamente"""
        mock_ventana = MagicMock()
        cargador = CargadorHerramienta(mock_ventana)
        
        # Crear una herramienta mock
        mock_widget = MagicMock()
        mock_herramienta = MagicMock()
        mock_herramienta.crear_widget.return_value = mock_widget
        
        # Crear una clase mock que retorne la herramienta
        mock_clase = MagicMock()
        mock_clase.return_value = mock_herramienta
        mock_clase.__name__ = "HerramientaTest"
        
        cargador.cargar(mock_clase)
        
        mock_clase.assert_called_once()
        mock_herramienta.crear_widget.assert_called_once()
        mock_ventana.mostrar_herramienta.assert_called_once_with(mock_widget)
        mock_ventana.mostrar_mensaje_estado.assert_called_once_with(
            "Herramienta activa: HerramientaTest"
        )
        assert cargador._herramienta_actual == mock_herramienta
        assert cargador._widget_actual == mock_widget

    def test_cargar_herramienta_con_error(self):
        """Verifica que maneja correctamente errores durante la carga"""
        mock_ventana = MagicMock()
        cargador = CargadorHerramienta(mock_ventana)
        
        # Crear una clase mock que lance una excepción
        mock_clase = MagicMock()
        mock_clase.side_effect = ImportError("Error al importar")
        
        with patch('escuadra.ui.cargador_herramienta.mostrar_error') as mock_error:
            with patch('escuadra.ui.cargador_herramienta.logger') as mock_logger:
                cargador.cargar(mock_clase)
                
                mock_clase.assert_called_once()
                mock_error.assert_called_once()
                mock_logger.error.assert_called_once()

    def test_cargar_herramienta_libera_anterior(self):
        """Verifica que al cargar una nueva herramienta, la anterior se libera"""
        mock_ventana = MagicMock()
        cargador = CargadorHerramienta(mock_ventana)
        
        # Primera herramienta
        mock_widget1 = MagicMock()
        mock_herramienta1 = MagicMock()
        mock_herramienta1.crear_widget.return_value = mock_widget1
        mock_clase1 = MagicMock()
        mock_clase1.return_value = mock_herramienta1
        mock_clase1.__name__ = "Herramienta1"
        
        cargador.cargar(mock_clase1)
        
        # Segunda herramienta
        mock_widget2 = MagicMock()
        mock_herramienta2 = MagicMock()
        mock_herramienta2.crear_widget.return_value = mock_widget2
        mock_clase2 = MagicMock()
        mock_clase2.return_value = mock_herramienta2
        mock_clase2.__name__ = "Herramienta2"
        
        cargador.cargar(mock_clase2)
        
        # Verificar que el primer widget fue liberado
        mock_widget1.setParent.assert_called_with(None)
        mock_widget1.deleteLater.assert_called_once()
        
        # Verificar que el segundo widget se mostró
        mock_ventana.mostrar_herramienta.assert_called_with(mock_widget2)

    def test_herramienta_actual(self):
        """Verifica que herramienta_actual devuelve la herramienta cargada"""
        mock_ventana = MagicMock()
        cargador = CargadorHerramienta(mock_ventana)
        
        # Crear una herramienta mock
        mock_widget = MagicMock()
        mock_herramienta = MagicMock()
        mock_herramienta.crear_widget.return_value = mock_widget
        mock_clase = MagicMock()
        mock_clase.return_value = mock_herramienta
        mock_clase.__name__ = "HerramientaTest"
        
        cargador.cargar(mock_clase)
        
        resultado = cargador.herramienta_actual()
        
        assert resultado == mock_herramienta
