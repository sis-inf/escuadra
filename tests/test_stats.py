import math

import pytest

from escuadra.math.stats import (
    calcular_desviacion_estandar,
    calcular_media,
    calcular_mediana,
)


def test_calcular_media_con_valor_referencia():
    assert calcular_media([2, 4, 6, 8]) == 5.0


def test_calcular_mediana_lista_impar():
    assert calcular_mediana([9, 1, 5]) == 5.0


def test_calcular_mediana_lista_par():
    assert calcular_mediana([10, 2, 8, 4]) == 6.0


def test_calcular_desviacion_estandar_muestral():
    resultado = calcular_desviacion_estandar([2, 4, 4, 4, 5, 5, 7, 9])

    assert math.isclose(resultado, 2.138089935, rel_tol=1e-9)


@pytest.mark.parametrize(
    "funcion",
    [calcular_media, calcular_mediana, calcular_desviacion_estandar],
)
def test_lista_vacia_lanza_error(funcion):
    with pytest.raises(ValueError, match="La lista está vacía"):
        funcion([])
