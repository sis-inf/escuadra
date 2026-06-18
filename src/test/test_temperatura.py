import pytest

from escuadra.modulos.matematicas.conversor_temperatura import c_to_k, f_to_k, k_to_c, k_to_f


def test_celsius_to_kelvin():
    assert c_to_k(0) == 273.15


def test_kelvin_to_celsius():
    assert k_to_c(273.15) == 0


def test_fahrenheit_to_kelvin():
    assert f_to_k(32) == 273.15


def test_kelvin_to_fahrenheit():
    assert k_to_f(273.15) == 32


def test_negative_kelvin():
    with pytest.raises(ValueError):
        k_to_c(-1)


def test_absolute_zero():
    assert c_to_k(-273.15) == 0
