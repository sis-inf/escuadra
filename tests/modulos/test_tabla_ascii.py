import pytest

from escuadra.modulos.sistemas.tabla_ascii import (
    ascii_a_caracter,
    caracter_a_ascii,
    listar_ascii_rango,
)


def test_caracter_a_ascii_A():
    resultado = caracter_a_ascii("A")
    assert resultado["caracter"] == "A"
    assert resultado["decimal"] == 65


def test_caracter_a_ascii_0():
    resultado = caracter_a_ascii("0")
    assert resultado["decimal"] == 48


def test_caracter_a_ascii_vacio_lanza_error():
    with pytest.raises(ValueError):
        caracter_a_ascii("")


def test_caracter_a_ascii_multi_caracter_lanza_error():
    with pytest.raises(ValueError):
        caracter_a_ascii("AB")


def test_caracter_a_ascii_fuera_de_rango():
    with pytest.raises(ValueError):
        caracter_a_ascii("ñ")


def test_ascii_a_caracter_65():
    resultado = ascii_a_caracter(65)
    assert resultado["caracter"] == "A"


def test_ascii_a_caracter_48():
    resultado = ascii_a_caracter(48)
    assert resultado["caracter"] == "0"


def test_ascii_a_caracter_negativo_lanza_error():
    with pytest.raises(ValueError):
        ascii_a_caracter(-1)


def test_ascii_a_caracter_fuera_de_rango():
    with pytest.raises(ValueError):
        ascii_a_caracter(128)


def test_listar_ascii_rango_65_67():
    resultado = listar_ascii_rango(65, 67)
    assert len(resultado) == 3
    assert resultado[0]["caracter"] == "A"
    assert resultado[1]["caracter"] == "B"
    assert resultado[2]["caracter"] == "C"


def test_listar_ascii_rango_inicio_mayor_que_fin():
    with pytest.raises(ValueError):
        listar_ascii_rango(10, 5)


def test_listar_ascii_rango_fuera_de_rango():
    with pytest.raises(ValueError):
        listar_ascii_rango(-1, 10)
