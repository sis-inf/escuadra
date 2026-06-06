import math


def perimetro_circulo(radio):
    if radio <= 0:
        raise ValueError("El radio debe ser mayor que cero")

    return 2 * math.pi * radio


def perimetro_cuadrado(lado):
    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero")

    return 4 * lado


def perimetro_rectangulo(largo, ancho):
    if largo <= 0 or ancho <= 0:
        raise ValueError("Las dimensiones deben ser mayores que cero")

    return 2 * (largo + ancho)


def perimetro_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Los lados deben ser mayores que cero")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("El triángulo no cumple la desigualdad triangular")

    return a + b + c


def perimetro_hexagono_regular(lado):
    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero")

    return 6 * lado
