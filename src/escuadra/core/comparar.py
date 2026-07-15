"""
Módulo para comparar resultados numéricos con tolerancia configurable.
"""


def comparar_resultados(resultado1, resultado2, tolerancia=1e-6):
    """
    Compara dos resultados numéricos verificando si son equivalentes
    dentro de una tolerancia definida.

    Args:
        resultado1 (float): Primer resultado a comparar.
        resultado2 (float): Segundo resultado a comparar.
        tolerancia (float): Diferencia máxima permitida.

    Returns:
        dict: Resultado de la comparación con detalle.
    """

    diferencia = abs(resultado1 - resultado2)

    equivalente = diferencia <= tolerancia

    return {
        "equivalente": equivalente,
        "resultado1": resultado1,
        "resultado2": resultado2,
        "diferencia": diferencia,
        "tolerancia": tolerancia,
    }
