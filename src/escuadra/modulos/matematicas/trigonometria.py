import math


def seno(angulo_grados):
    """Calcula el seno de un ángulo en grados."""
    return math.sin(math.radians(angulo_grados))


def coseno(angulo_grados):
    """Calcula el coseno de un ángulo en grados."""
    return math.cos(math.radians(angulo_grados))


def tangente(angulo_grados):
    """Calcula la tangente de un ángulo en grados."""
    angulo_normalizado = angulo_grados % 180

    if math.isclose(angulo_normalizado, 90.0, abs_tol=1e-9):
        raise ValueError("Tangente indefinida para este ángulo")

    return math.tan(math.radians(angulo_grados))


def arcoseno(valor):
    """Calcula el arcoseno y devuelve el resultado en grados."""
    if valor < -1 or valor > 1:
        raise ValueError("El valor debe estar en el rango [-1, 1]")

    return math.degrees(math.asin(valor))


def arcocoseno(valor):
    """Calcula el arcocoseno y devuelve el resultado en grados."""
    if valor < -1 or valor > 1:
        raise ValueError("El valor debe estar en el rango [-1, 1]")

    return math.degrees(math.acos(valor))


def arcotangente(valor):
    """Calcula el arcotangente y devuelve el resultado en grados."""
    return math.degrees(math.atan(valor))
