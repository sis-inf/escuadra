"""
Tests unitarios para las funciones de cálculo de la Ley de Ohm.
"""

import pytest

from escuadra.modulos.electrica.herramienta_ley_ohm import (
    calcular_corriente,
    calcular_potencia,
    calcular_resistencia,
    calcular_voltaje,
)


def test_calcular_voltaje():
    # V = I * R → 2 * 5 = 10
    assert calcular_voltaje(2, 5) == 10


def test_calcular_corriente():
    # I = V / R → 12 / 3 = 4
    assert calcular_corriente(12, 3) == 4


def test_calcular_resistencia():
    # R = V / I → 10 / 2 = 5
    assert calcular_resistencia(10, 2) == 5


def test_calcular_potencia():
    # P = V * I → 10 * 2 = 20
    assert calcular_potencia(10, 2) == 20


def test_calcular_corriente_division_por_cero():
    # R = 0 debe lanzar error
    with pytest.raises(ValueError):
        calcular_corriente(10, 0)


def test_calcular_resistencia_division_por_cero():
    # I = 0 debe lanzar error
    with pytest.raises(ValueError):
        calcular_resistencia(10, 0)


def test_funciones_aceptan_floats():
    # Las funciones deben aceptar tanto enteros como floats
    assert calcular_voltaje(2.5, 4.0) == pytest.approx(10.0)
    assert calcular_corriente(7.5, 2.5) == pytest.approx(3.0)
    assert calcular_resistencia(9.0, 3.0) == pytest.approx(3.0)
    assert calcular_potencia(5.0, 2.0) == pytest.approx(10.0)
