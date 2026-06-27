import pytest

from escuadra.modulos.matematicas.conversor_temperatura import (
    celsius_a_kelvin,
    fahrenheit_a_celsius,
    kelvin_a_celsius,
)


def test_celsius_a_kelvin():
    assert celsius_a_kelvin(0) == 273.15


def test_kelvin_a_celsius():
    assert kelvin_a_celsius(273.15) == 0


def test_fahrenheit_a_kelvin_via_celsius():
    celsius = fahrenheit_a_celsius(32)
    assert celsius_a_kelvin(celsius) == 273.15


def test_kelvin_a_fahrenheit_via_celsius():
    celsius = kelvin_a_celsius(273.15)
    fahrenheit = celsius * 9 / 5 + 32
    assert fahrenheit == 32


def test_kelvin_negativo_lanza_error():
    with pytest.raises(ValueError):
        kelvin_a_celsius(-1)


def test_cero_absoluto_celsius_a_kelvin():
    assert celsius_a_kelvin(-273.15) == 0
