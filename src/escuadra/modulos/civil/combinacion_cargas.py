"""
Modulo para combinacion de cargas vivas y muertas en ingenieria civil.

Este calculo es educativo y simplificado.
No reemplaza la normativa estructural local vigente.
"""


def combinar_cargas_lrfd(
    carga_muerta: float,
    carga_viva: float,
    factor_muerta: float = 1.2,
    factor_viva: float = 1.6,
) -> float:
    """
    Calcula la carga ultima de diseno mediante factores LRFD.

    Formula:
        U = factor_muerta * carga_muerta + factor_viva * carga_viva

    Args:
        carga_muerta: carga permanente o muerta.
        carga_viva: carga variable o viva.
        factor_muerta: factor aplicado a carga muerta.
        factor_viva: factor aplicado a carga viva.

    Returns:
        Carga ultima combinada.
    """
    return factor_muerta * carga_muerta + factor_viva * carga_viva
