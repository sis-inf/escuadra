from typing import Dict, Any

def calcular_momento_max(longitud: float, carga: float, tipo_carga: str = 'puntual_central') -> Dict[str, Any]:
    """
    Calcula el momento de flexión en un elemento civil.

    Args:
        longitud (float): La longitud del elemento.
        carga (float): La carga aplicada al elemento.
        tipo_carga (str): El tipo de carga ('puntual_central' o 'distribuida').

    Returns:
        Dict[str, Any]: Un diccionario con los siguientes campos:
            - momento_max: El momento de flexión máximo.
            - posicion: La posicion del punto de aplicación de la carga (en metros).
            - unidad: La unidad del momento de flexión ('kN·m').

    Raises:
        ValueError: Si el tipo_carga no es 'puntual_central' ni 'distribuida',
                   o si longitud <= 0 o carga <= 0.
    """
    if tipo_carga not in ['puntual_central', 'distribuida']:
        raise ValueError(
            f"Tipo de carga '{tipo_carga}' no soportado. "
            "Los tipos aceptados son: 'puntual_central' y 'distribuida'."
        )
    
    if longitud <= 0:
        raise ValueError(
            f"El parámetro 'longitud' debe ser mayor que cero. "
            f"Se recibió: {longitud}."
        )
    
    if carga <= 0:
        raise ValueError(
            f"El parámetro 'carga' debe ser mayor que cero. "
            f"Se recibió: {carga}."
        )
    
    if tipo_carga == 'puntual_central':
        momento = carga * longitud / 4
    elif tipo_carga == 'distribuida':
        momento = carga * (longitud ** 2) / 8
    
    return {
        'momento_max': float(momento),
        'posicion': float(longitud / 2),
        'unidad': 'kN·m'
    }