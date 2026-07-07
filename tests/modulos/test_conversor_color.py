import pytest

from escuadra.modulos.sistemas.conversor_color import (
    hex_a_rgb,
    rgb_a_hex,
    rgb_a_hsl,
)


def test_rgb_a_hex_rojo():
    assert rgb_a_hex(255, 0, 0) == "#FF0000"


def test_rgb_a_hex_verde():
    assert rgb_a_hex(0, 255, 0) == "#00FF00"


def test_rgb_a_hex_azul():
    assert rgb_a_hex(0, 0, 255) == "#0000FF"


def test_rgb_a_hex_blanco():
    assert rgb_a_hex(255, 255, 255) == "#FFFFFF"


def test_rgb_a_hex_negro():
    assert rgb_a_hex(0, 0, 0) == "#000000"


def test_rgb_a_hex_valor_fuera_de_rango_bajo():
    with pytest.raises(ValueError):
        rgb_a_hex(-1, 0, 0)


def test_rgb_a_hex_valor_fuera_de_rango_alto():
    with pytest.raises(ValueError):
        rgb_a_hex(256, 0, 0)


def test_hex_a_rgb_con_prefijo():
    assert hex_a_rgb("#FF0000") == (255, 0, 0)


def test_hex_a_rgb_sin_prefijo():
    assert hex_a_rgb("00FF00") == (0, 255, 0)


def test_hex_a_rgb_longitud_invalida():
    with pytest.raises(ValueError):
        hex_a_rgb("#FFF")


def test_hex_a_rgb_caracteres_invalidos():
    with pytest.raises(ValueError):
        hex_a_rgb("#GGGGGG")


def test_rgb_a_hsl_rojo():
    h, s, l = rgb_a_hsl(255, 0, 0)
    assert h == 0
    assert s == 100
    assert l == 50


def test_rgb_a_hsl_verde():
    h, s, l = rgb_a_hsl(0, 255, 0)
    assert h == 120
    assert s == 100
    assert l == 50


def test_rgb_a_hsl_azul():
    h, s, l = rgb_a_hsl(0, 0, 255)
    assert h == 240
    assert s == 100
    assert l == 50


def test_rgb_a_hsl_blanco():
    h, s, l = rgb_a_hsl(255, 255, 255)
    assert l == 100


def test_rgb_a_hsl_negro():
    h, s, l = rgb_a_hsl(0, 0, 0)
    assert l == 0


def test_rgb_a_hsl_valor_fuera_de_rango():
    with pytest.raises(ValueError):
        rgb_a_hsl(300, 0, 0)
