"""
Funciones de matemática financiera básica.
"""


def calcular_valor_futuro(valor_presente: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor futuro usando interés compuesto.

    VF = VP * (1 + i) ** n
    """
    return valor_presente * (1 + tasa) ** periodos


def calcular_valor_presente(valor_futuro: float, tasa: float, periodos: int) -> float:
    """
    Calcula el valor presente.

    VP = VF / (1 + i) ** n
    """
    return valor_futuro / (1 + tasa) ** periodos


def calcular_interes_compuesto(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula únicamente el interés ganado.

    I = VF - Capital
    """
    valor_futuro = calcular_valor_futuro(capital, tasa, periodos)
    return valor_futuro - capital
