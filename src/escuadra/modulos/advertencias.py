"""
Módulo para capturar advertencias de Python de forma estructurada.

Proporciona un context manager para capturar warnings.emitidos
por los módulos de cálculo y mostrarlos en la UI.
"""

import warnings
from contextlib import contextmanager


@contextmanager
def capturar_advertencias():
    """
    Context manager que captura warnings.emitidos durante la ejecución.

    Ejemplo:
        with capturar_advertencias() as advertencias:
            resultado = calcular_algo()
        if advertencias:
            mostrar_en_ui(advertencias)
    """
    advertencias = []
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        yield advertencias
        for warning in w:
            advertencias.append(str(warning.message))
