UNIDADES_A_JOULE = {
    "J": 1.0,
    "kJ": 1_000.0,
    "MJ": 1_000_000.0,
    "Wh": 3_600.0,
    "kWh": 3_600_000.0,
    "cal": 4.184,
    "kcal": 4_184.0,
    "BTU": 1_055.05585,
    "eV": 1.602176634e-19,
}


def convertir_energia(valor: float, de_unidad: str, a_unidad: str) -> dict:
    """
    Convierte unidades de energía usando Joule como unidad base.

    Unidades soportadas: 'J', 'kJ', 'MJ', 'Wh', 'kWh', 'cal', 'kcal', 'BTU', 'eV'.

    Args:
        valor (float): Valor a convertir.
        de_unidad (str): Unidad origen.
        a_unidad (str): Unidad destino.

    Returns:
        dict: Resultado de la conversión con claves:
            - valor_original
            - unidad_original
            - valor_convertido
            - unidad_destino

    Raises:
        ValueError: Si el valor es negativo o la unidad no es reconocida.
    """
    if valor < 0:
        raise ValueError("El valor no puede ser negativo")

    de_unidad = de_unidad.strip().lower()
    a_unidad = a_unidad.strip().lower()

    if de_unidad not in UNIDADES_A_JOULE:
        raise ValueError(f"Unidad origen no reconocida: {de_unidad}")

    if a_unidad not in UNIDADES_A_JOULE:
        raise ValueError(f"Unidad destino no reconocida: {a_unidad}")

    # Convertir a Joule
    valor_en_joules = valor * UNIDADES_A_JOULE[de_unidad]

    # Convertir desde Joule a unidad destino
    valor_convertido = valor_en_joules / UNIDADES_A_JOULE[a_unidad]

    return {
        "valor_original": valor,
        "unidad_original": de_unidad,
        "valor_convertido": valor_convertido,
        "unidad_destino": a_unidad,
    }
