import pytest

from escuadra.modulos.matematicas.conversor_masa import convertir_masa


def test_kg_a_g():
    assert convertir_masa(1, "kg", "g") == 1000


def test_g_a_kg():
    assert convertir_masa(1000, "g", "kg") == 1


def test_kg_a_lb():
    assert convertir_masa(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-3)


def test_oz_a_g():
    assert convertir_masa(1, "oz", "g") == pytest.approx(28.3495, rel=1e-3)


def test_t_a_kg():
    assert convertir_masa(1, "t", "kg") == 1000


def test_mg_a_kg():
    assert convertir_masa(1000000, "mg", "kg") == 1


def test_valor_negativo_lanza_error():
    with pytest.raises(ValueError):
        convertir_masa(-1, "kg", "g")


def test_unidad_origen_desconocida_lanza_error():
    with pytest.raises(ValueError):
        convertir_masa(1, "desconocido", "kg")


def test_unidad_destino_desconocida_lanza_error():
    with pytest.raises(ValueError):
        convertir_masa(1, "kg", "desconocido")
