"""Herramientas educativas para cálculo y verificación de bits de paridad."""


def calcular_bit_paridad(datos_binarios: str, tipo: str = "par") -> int:
    """
    Calcula el bit de paridad para una cadena binaria.

    Args:
        datos_binarios: Cadena compuesta por 0 y 1.
        tipo: Tipo de paridad ("par" o "impar").

    Returns:
        Bit de paridad calculado (0 o 1).
    """
    unos = datos_binarios.count("1")

    if tipo == "par":
        return 0 if unos % 2 == 0 else 1

    if tipo == "impar":
        return 1 if unos % 2 == 0 else 0

    raise ValueError("El tipo debe ser 'par' o 'impar'")


def verificar_paridad(datos_con_paridad: str, tipo: str = "par") -> bool:
    """
    Verifica si una cadena binaria cumple con la paridad indicada.

    Args:
        datos_con_paridad: Datos incluyendo el bit de paridad.
        tipo: Tipo de paridad ("par" o "impar").

    Returns:
        True si la paridad es correcta, False en caso contrario.
    """
    cantidad_unos = datos_con_paridad.count("1")

    if tipo == "par":
        return cantidad_unos % 2 == 0

    if tipo == "impar":
        return cantidad_unos % 2 != 0

    raise ValueError("El tipo debe ser 'par' o 'impar'")
