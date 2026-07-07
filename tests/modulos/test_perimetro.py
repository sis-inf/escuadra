import math

import pytest

from escuadra.modulos.geometria.perimetro import (
    perimetro_circulo,
    perimetro_cuadrado,
    perimetro_hexagono_regular,
    perimetro_rectangulo,
    perimetro_triangulo,
)


def test_perimetro_circulo():
    assert perimetro_circulo(1) == pytest.approx(2 * math.pi)


def test_perimetro_circulo_radio_cero_lanza_error():
    with pytest.raises(ValueError):
        perimetro_circulo(0)


def test_perimetro_cuadrado():
    assert perimetro_cuadrado(4) == 16


def test_perimetro_cuadrado_lado_cero_lanza_error():
    with pytest.raises(ValueError):
        perimetro_cuadrado(0)


def test_perimetro_rectangulo():
    assert perimetro_rectangulo(4, 5) == 18


def test_perimetro_rectangulo_dimension_cero_lanza_error():
    with pytest.raises(ValueError):
        perimetro_rectangulo(0, 5)


def test_perimetro_triangulo():
    assert perimetro_triangulo(3, 4, 5) == 12


def test_perimetro_triangulo_lado_negativo_lanza_error():
    with pytest.raises(ValueError):
        perimetro_triangulo(-1, 4, 5)


def test_perimetro_triangulo_desigualdad_triangular():
    with pytest.raises(ValueError):
        perimetro_triangulo(1, 1, 3)


def test_perimetro_hexagono_regular():
    assert perimetro_hexagono_regular(3) == 18


def test_perimetro_hexagono_regular_lado_cero_lanza_error():
    with pytest.raises(ValueError):
        perimetro_hexagono_regular(0)
