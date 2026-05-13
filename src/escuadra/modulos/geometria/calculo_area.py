"""
Funciones de cálculo de áreas para figuras geométricas básicas.

Este módulo contiene la lógica pura de cálculo, sin dependencias de UI,
para facilitar las pruebas unitarias y la reutilización.
"""

import math


def area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dada su base y altura.

    Args:
        base: Longitud de la base del triángulo (debe ser positiva).
        altura: Altura perpendicular del triángulo (debe ser positiva).

    Returns:
        El área del triángulo.

    Raises:
        ValueError: Si base o altura son menores o iguales a cero.

    Examples:
        >>> area_triangulo(6, 4)
        12.0
    """
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos.")
    return (base * altura) / 2


def area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio: Radio del círculo (debe ser positivo).

    Returns:
        El área del círculo usando math.pi.

    Raises:
        ValueError: Si el radio es menor o igual a cero.

    Examples:
        >>> round(area_circulo(1), 5)
        3.14159
    """
    if radio <= 0:
        raise ValueError("El radio debe ser un valor positivo.")
    return math.pi * (radio ** 2)


def area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo dada su base y altura.

    Args:
        base: Longitud de la base del rectángulo (debe ser positiva).
        altura: Altura del rectángulo (debe ser positiva).

    Returns:
        El área del rectángulo.

    Raises:
        ValueError: Si base o altura son menores o iguales a cero.

    Examples:
        >>> area_rectangulo(5, 3)
        15.0
    """
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos.")
    return base * altura


def area_trapecio(base_mayor: float, base_menor: float, altura: float) -> float:
    """
    Calcula el área de un trapecio dadas sus dos bases y su altura.

    Args:
        base_mayor: Longitud de la base mayor (debe ser positiva).
        base_menor: Longitud de la base menor (debe ser positiva).
        altura: Altura perpendicular entre las bases (debe ser positiva).

    Returns:
        El área del trapecio.

    Raises:
        ValueError: Si alguno de los parámetros es menor o igual a cero.

    Examples:
        >>> area_trapecio(8, 4, 5)
        30.0
    """
    if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
        raise ValueError("Las bases y la altura deben ser valores positivos.")
    return ((base_mayor + base_menor) * altura) / 2
