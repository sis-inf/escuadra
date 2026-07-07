import pytest

from escuadra.modulos.geometria.calculo_area import area_circulo, area_rectangulo, area_triangulo


def test_area_triangulo():
    assert area_triangulo(10, 5) == 25


def test_area_triangulo_cero():
    assert area_triangulo(0, 5) == 0


def test_area_circulo():
    assert area_circulo(1) == pytest.approx(3.1416)


def test_area_circulo_radio_cero():
    assert area_circulo(0) == 0


def test_area_rectangulo():
    assert area_rectangulo(4, 5) == 20


def test_area_rectangulo_cero():
    assert area_rectangulo(0, 5) == 0
