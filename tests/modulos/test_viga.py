import pytest

from escuadra.modulos.civil.viga import calcular_reacciones


def test_carga_distribuida_simetrica():
    resultado = calcular_reacciones(longitud=10, carga=100)

    assert resultado["Ra"] == 50
    assert resultado["Rb"] == 50
    assert resultado["unidad"] == "kN"


def test_carga_puntual_centro():
    resultado = calcular_reacciones(longitud=10, carga=200, posicion=5)

    assert resultado["Ra"] == 100
    assert resultado["Rb"] == 100


def test_carga_puntual_apoyo_izquierdo():
    resultado = calcular_reacciones(longitud=10, carga=300, posicion=0)

    assert resultado["Ra"] == 300
    assert resultado["Rb"] == 0


def test_carga_puntual_apoyo_derecho():
    resultado = calcular_reacciones(longitud=10, carga=300, posicion=10)

    assert resultado["Ra"] == 0
    assert resultado["Rb"] == 300


def test_longitud_negativa_lanza_error():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=-10, carga=100)


def test_longitud_cero_lanza_error():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=0, carga=100)


def test_posicion_fuera_de_la_viga_lanza_error():
    with pytest.raises(ValueError):
        calcular_reacciones(longitud=10, carga=100, posicion=11)
