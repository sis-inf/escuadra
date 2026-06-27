import pytest

from escuadra.modulos.sistemas.conversor_bases import convertir


def test_conversiones_basicas_entre_bases():
    assert convertir("10", 10, 2)["resultado"] == "1010"
    assert convertir("1010", 2, 10)["resultado"] == "10"
    assert convertir("F", 16, 10)["resultado"] == "15"
    assert convertir("17", 8, 10)["resultado"] == "15"
    assert convertir("10", 10, 16)["resultado"] == "A"
    assert convertir("12", 8, 2)["resultado"] == "1010"


def test_conversion_base_no_soportada_lanza_error():
    with pytest.raises(ValueError):
        convertir("10", 5, 10)


def test_conversion_digito_invalido_lanza_error():
    with pytest.raises(ValueError):
        convertir("102", 2, 10)
