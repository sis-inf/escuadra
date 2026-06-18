import pytest

from escuadra.modulos.civil.viga import calcular_reacciones


def test_carga_distribuida_simetrica():
    ra, rb = calcular_reacciones(
        longitud=10,
        carga_total=100,
        tipo_carga="distribuida"
    )

    assert ra == 50
    assert rb == 50


def test_carga_puntual_centro():
    ra, rb = calcular_reacciones(
        longitud=10,
        carga_total=200,
        posicion=5,
        tipo_carga="puntual"
    )

    assert ra == 100
    assert rb == 100


def test_carga_puntual_extremo():
    ra, rb = calcular_reacciones(
        longitud=10,
        carga_total=300,
        posicion=0,
        tipo_carga="puntual"
    )

    assert ra == 0
    assert rb == 300


def test_valores_negativos():
    with pytest.raises(ValueError):
        calcular_reacciones(
            longitud=-10,
            carga_total=100,
            tipo_carga="distribuida"
        )


def test_longitud_cero():
    with pytest.raises(ValueError):
        calcular_reacciones(
            longitud=0,
            carga_total=100,
            tipo_carga="distribuida"
        )
