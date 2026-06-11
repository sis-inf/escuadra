"""Cálculo de resistencia equivalente en serie y paralelo."""


def resistencia_serie(*resistencias):
    """
    Calcula la resistencia equivalente en serie.

    Fórmula:
        R_eq = R1 + R2 + ... + Rn
    """
    if len(resistencias) < 2:
        raise ValueError("Se requieren al menos 2 resistencias")

    if any(r <= 0 for r in resistencias):
        raise ValueError("Todas las resistencias deben ser mayores que 0")

    return float(sum(resistencias))


def resistencia_paralelo(*resistencias):
    """
    Calcula la resistencia equivalente en paralelo.

    Fórmula:
        1 / R_eq = 1/R1 + 1/R2 + ... + 1/Rn
    """
    if len(resistencias) < 2:
        raise ValueError("Se requieren al menos 2 resistencias")

    if any(r <= 0 for r in resistencias):
        raise ValueError("Todas las resistencias deben ser mayores que 0")

    suma_inversas = sum(1 / r for r in resistencias)

    return float(1 / suma_inversas)
