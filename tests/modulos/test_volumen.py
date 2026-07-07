import math

import pytest

from escuadra.modulos.geometria.volumen import (
    volumen_cilindro,
    volumen_cono,
    volumen_cubo,
    volumen_esfera,
    volumen_paralelepipedo,
)


def test_volumen_cubo():
    assert volumen_cubo(3) == 27


def test_volumen_cubo_lado_cero_lanza_error():
    with pytest.raises(ValueError):
        volumen_cubo(0)


def test_volumen_esfera():
    esperado = (4 / 3) * math.pi * 1 ** 3
    assert volumen_esfera(1) == pytest.approx(esperado)


def test_volumen_esfera_radio_cero_lanza_error():
    with pytest.raises(ValueError):
        volumen_esfera(0)


def test_volumen_cilindro():
    esperado = math.pi * 2 ** 2 * 5
    assert volumen_cilindro(2, 5) == pytest.approx(esperado)


def test_volumen_cilindro_radio_cero_lanza_error():
    with pytest.raises(ValueError):
        volumen_cilindro(0, 5)


def test_volumen_cono():
    esperado = (1 / 3) * math.pi * 2 ** 2 * 6
    assert volumen_cono(2, 6) == pytest.approx(esperado)


def test_volumen_cono_altura_cero_lanza_error():
    with pytest.raises(ValueError):
        volumen_cono(1, 0)


def test_volumen_paralelepipedo():
    assert volumen_paralelepipedo(2, 3, 4) == 24


def test_volumen_paralelepipedo_dimension_cero_lanza_error():
    with pytest.raises(ValueError):
        volumen_paralelepipedo(0, 3, 4)
