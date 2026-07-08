"""
Funciones de transformaciones geométricas 2D.
"""

import math


def rotar_punto(
    punto: tuple[float, float],
    angulo: float,
    centro: tuple[float, float] = (0.0, 0.0),
) -> tuple[float, float]:
    """
    Rota un punto alrededor de un centro.
    El ángulo está en grados.
    """
    x, y = punto
    cx, cy = centro

    x -= cx
    y -= cy

    rad = math.radians(angulo)

    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)

    return (xr + cx, yr + cy)


def trasladar_punto(
    punto: tuple[float, float],
    dx: float,
    dy: float,
) -> tuple[float, float]:
    """
    Traslada un punto.
    """
    return (punto[0] + dx, punto[1] + dy)


def escalar_punto(
    punto: tuple[float, float],
    factor: float,
    centro: tuple[float, float] = (0.0, 0.0),
) -> tuple[float, float]:
    """
    Escala un punto respecto a un centro.
    """
    cx, cy = centro

    return (
        cx + (punto[0] - cx) * factor,
        cy + (punto[1] - cy) * factor,
    )
