import pytest

from escuadra.modulos.sistemas.conversor_bases import convertir


def test_binario_a_decimal():
    # 1010 binario = 10 decimal
    resultado = convertir("1010", 2, 10)
    assert resultado["resultado"] == "10"


def test_decimal_a_hexadecimal():
    # 255 decimal = FF hexadecimal
    resultado = convertir("255", 10, 16)
    assert resultado["resultado"] == "FF"


def test_hexadecimal_a_octal():
    # FF hexadecimal = 377 octal
    resultado = convertir("FF", 16, 8)
    assert resultado["resultado"] == "377"


def test_octal_a_binario():
    # 77 octal = 111111 binario
    resultado = convertir("77", 8, 2)
    assert resultado["resultado"] == "111111"


def test_numero_vacio_lanza_error():
    with pytest.raises(ValueError):
        convertir("", 10, 2)


def test_base_origen_no_soportada_lanza_error():
    with pytest.raises(ValueError):
        convertir("10", 3, 10)


def test_base_destino_no_soportada_lanza_error():
    with pytest.raises(ValueError):
        convertir("10", 10, 3)


def test_numero_base_invalido_lanza_error():
    with pytest.raises(ValueError):
        convertir("GG", 16, 10)


def test_binario_a_hexadecimal():
    resultado = convertir("11111111", 2, 16)
    assert resultado["resultado"] == "FF"


def test_decimal_a_binario():
    resultado = convertir("42", 10, 2)
    assert resultado["resultado"] == "101010"


def test_metadatos_en_resultado():
    resultado = convertir("FF", 16, 10)
    assert resultado["numero_original"] == "FF"
    assert resultado["base_origen"] == 16
    assert resultado["base_destino"] == 10
