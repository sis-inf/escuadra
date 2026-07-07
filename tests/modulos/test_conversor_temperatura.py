import pytest

from escuadra.modulos.matematicas.conversor_temperatura import (
    celsius_a_fahrenheit,
    celsius_a_kelvin,
    fahrenheit_a_celsius,
    kelvin_a_celsius,
)


def test_celsius_a_fahrenheit_0():
    assert celsius_a_fahrenheit(0) == 32


def test_celsius_a_fahrenheit_100():
    assert celsius_a_fahrenheit(100) == 212


def test_celsius_a_fahrenheit_negativo():
    assert celsius_a_fahrenheit(-40) == -40


def test_celsius_a_fahrenheit_bajo_cero_absoluto():
    with pytest.raises(ValueError):
        celsius_a_fahrenheit(-300)


def test_fahrenheit_a_celsius_32():
    assert fahrenheit_a_celsius(32) == 0


def test_fahrenheit_a_celsius_212():
    assert fahrenheit_a_celsius(212) == 100


def test_fahrenheit_a_celsius_negativo():
    assert fahrenheit_a_celsius(-40) == -40


def test_fahrenheit_a_celsius_bajo_cero_absoluto():
    with pytest.raises(ValueError):
        fahrenheit_a_celsius(-500)


def test_celsius_a_kelvin_0():
    assert celsius_a_kelvin(0) == pytest.approx(273.15)


def test_celsius_a_kelvin_100():
    assert celsius_a_kelvin(100) == pytest.approx(373.15)


def test_celsius_a_kelvin_bajo_cero_absoluto():
    with pytest.raises(ValueError):
        celsius_a_kelvin(-300)


def test_kelvin_a_celsius_273():
    assert kelvin_a_celsius(273.15) == pytest.approx(0)


def test_kelvin_a_celsius_373():
    assert kelvin_a_celsius(373.15) == pytest.approx(100)


def test_kelvin_a_celsius_negativo_lanza_error():
    with pytest.raises(ValueError):
        kelvin_a_celsius(-1)
