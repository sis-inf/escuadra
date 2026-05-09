import pytest
import math

from escuadra.modulos.matematicas.herramienta_calculadora_cientifica import (
    HerramientaCalculadoraCientifica,
)


def test_calculadora_existe():
    calculadora = HerramientaCalculadoraCientifica()
    assert calculadora.nombre == "Calculadora científica"
    assert calculadora.carrera.name == "MATEMATICAS"


def test_suma():
    calculadora = HerramientaCalculadoraCientifica()
    widget = calculadora.crear_widget()
    assert calculadora is not None


def test_expresion_simple():
    resultado_esperado = 14
    expresion = "2 + 3 * 4"

    calculadora = HerramientaCalculadoraCientifica()
    resultado = calculadora.evaluar_expresion(expresion)
    assert resultado == resultado_esperado


def test_sqrt():
    resultado_esperado = 4
    expresion = "sqrt(16)"

    calculadora = HerramientaCalculadoraCientifica()
    resultado = calculadora.evaluar_expresion(expresion)
    assert resultado == resultado_esperado


def test_potencia():
    resultado_esperado = 1024
    expresion = "2 ** 10"

    calculadora = HerramientaCalculadoraCientifica()
    resultado = calculadora.evaluar_expresion(expresion)
    assert resultado == resultado_esperado


def test_logaritmo():
    resultado_esperado = 2
    expresion = "log(100)"

    calculadora = HerramientaCalculadoraCientifica()
    resultado = calculadora.evaluar_expresion(expresion)
    assert resultado == resultado_esperado


def test_pi():
    calculadora = HerramientaCalculadoraCientifica()
    expresion = "π"
    resultado = calculadora.evaluar_expresion(expresion)
    assert abs(resultado - math.pi) < 0.001


def test_sin_radianes():
    resultado_esperado = 0
    expresion = "sin(0)"

    calculadora = HerramientaCalculadoraCientifica()
    resultado = calculadora.evaluar_expresion(expresion)
    assert abs(resultado - resultado_esperado) < 0.0001


def test_error_expresion_invalida():
    calculadora = HerramientaCalculadoraCientifica()

    with pytest.raises(ValueError):
        calculadora.evaluar_expresion("2 + + 3")


def test_error_division_por_cero():
    calculadora = HerramientaCalculadoraCientifica()

    with pytest.raises(ValueError, match="División por cero"):
        calculadora.evaluar_expresion("1 / 0")
