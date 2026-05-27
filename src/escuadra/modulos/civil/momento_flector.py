from typing import Dict


def calculator_momento_mx(
    longitud: float,
    carga: float,
    tipo_carga: str = 'puntual_central',
) -> Dict[str, float]:
    """
    Calcula el momento de flexión en un elemento civil.

    Args:
        longitud (float): La longitud del elemento.
        carga (float): La carga aplicada al elemento.
        tipo_carga (str): El tipo de carga ('puntual_central' o 'distribuida').

    Returns:
        Dict[str, float]: Un diccionario con los siguientes campos:
            - momento_mx: El momento de flexión en N.mm
            - posición: La posición del punto de aplicación de la carga (en metros)
            - unidad: La unidad del momento de flexión

    Raises:
        ValueError: Si el tipo_carga no es 'puntual_central' ni 'distribuida',
                   o si longitud <= 0 o carga <= 0.
    """
    if longitud <= 0:
        raise ValueError(f"La longitud no puede ser negativa o cero. Valor recibido: {longitud}")

    if carga <= 0:
        raise ValueError(f"La carga no puede ser negativa o cero. Valor recibido: {carga}")

    if tipo_carga not in ['puntual_central', 'distribuida']:
        raise ValueError(
            f"Tipo de carga no soportado: '{tipo_carga}'. "
            f"Tipos aceptados: puntual_central, distribuida"
        )

    if tipo_carga == 'puntual_central':
        momento = carga * longitud / 4
    elif tipo_carga == 'distribuida':
        momento = carga * (longitud ** 2) / 8

    return {
        'momento_mx': float(momento),
        'posición': longitud / 2,
        'unidad': 'N.mm'
    }
