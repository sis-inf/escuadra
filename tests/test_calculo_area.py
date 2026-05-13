"""
Pruebas unitarias para el módulo de cálculo de áreas geométricas.

Ejecutar con:
    pytest tests/test_calculo_area.py -v
"""

import math
import pytest

from src.escuadra.modulos.geometria.calculo_area import (
    area_triangulo,
    area_circulo,
    area_rectangulo,
    area_trapecio,
)


# ── Triángulo ────────────────────────────────────────────────────────────────

class TestAreaTriangulo:
    def test_caso_basico(self):
        """Triángulo con base 6 y altura 4 → área 12."""
        assert area_triangulo(6, 4) == 12.0

    def test_valores_decimales(self):
        """Acepta valores de punto flotante."""
        resultado = area_triangulo(3.5, 2.0)
        assert abs(resultado - 3.5) < 1e-10

    def test_base_cero_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_triangulo(0, 5)

    def test_altura_negativa_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_triangulo(5, -3)

    def test_ambos_negativos_lanzan_excepcion(self):
        with pytest.raises(ValueError):
            area_triangulo(-1, -1)


# ── Círculo ──────────────────────────────────────────────────────────────────

class TestAreaCirculo:
    def test_radio_uno(self):
        """Círculo de radio 1 → área ≈ π."""
        assert abs(area_circulo(1) - math.pi) < 1e-10

    def test_radio_cinco(self):
        resultado = area_circulo(5)
        esperado = math.pi * 25
        assert abs(resultado - esperado) < 1e-10

    def test_radio_cero_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_circulo(0)

    def test_radio_negativo_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_circulo(-2.5)

    def test_usa_math_pi(self):
        """Verifica que el cálculo usa math.pi (no la aproximación 3.1416)."""
        resultado = area_circulo(1)
        assert resultado != 3.1416
        assert abs(resultado - math.pi) < 1e-12


# ── Rectángulo ───────────────────────────────────────────────────────────────

class TestAreaRectangulo:
    def test_caso_basico(self):
        assert area_rectangulo(5, 3) == 15.0

    def test_cuadrado(self):
        """Un cuadrado es un rectángulo con base == altura."""
        assert area_rectangulo(4, 4) == 16.0

    def test_base_cero_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_rectangulo(0, 10)

    def test_altura_cero_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_rectangulo(10, 0)

    def test_valores_decimales(self):
        resultado = area_rectangulo(2.5, 4.0)
        assert abs(resultado - 10.0) < 1e-10


# ── Trapecio ─────────────────────────────────────────────────────────────────

class TestAreaTrapecio:
    def test_caso_basico(self):
        """Trapecio con bases 8 y 4, altura 5 → área 30."""
        assert area_trapecio(8, 4, 5) == 30.0

    def test_bases_iguales_equivale_a_rectangulo(self):
        """Cuando las dos bases son iguales el resultado es base × altura."""
        resultado = area_trapecio(6, 6, 3)
        assert abs(resultado - 18.0) < 1e-10

    def test_base_mayor_cero_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_trapecio(0, 4, 5)

    def test_base_menor_negativa_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_trapecio(8, -1, 5)

    def test_altura_cero_lanza_excepcion(self):
        with pytest.raises(ValueError):
            area_trapecio(8, 4, 0)
