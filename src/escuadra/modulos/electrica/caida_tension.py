"""
Modulo para el calculo de caida de tension en conductores electricos.

Formula aplicada:
    DV = 2 * p * L * I / S

Donde:
    p = resistividad del material (Ohm*mm2/m)
    L = longitud del conductor (m)
    I = corriente (A)
    S = seccion transversal del conductor (mm2)
"""

from __future__ import annotations

# Resistividades en Ohm*mm2/m a 20 C
RESISTIVIDADES: dict[str, float] = {
    "cobre": 0.0172,
    "aluminio": 0.0282,
}

TENSION_REFERENCIA_V: float = 220.0
PORCENTAJE_ADMISIBLE: float = 3.0


def calcular_caida(
    longitud: float,
    corriente: float,
    seccion: float,
    material: str = "cobre",
) -> dict[str, float | bool]:
    """Calcula la caida de tension en un conductor electrico.

    Aplica la formula DV = 2 * p * L * I / S para circuitos
    monofasicos de ida y vuelta.

    Args:
        longitud:  Longitud del conductor en metros (m). Debe ser > 0.
        corriente: Corriente que circula en amperios (A). Debe ser > 0.
        seccion:   Seccion transversal del conductor en mm2. Debe ser > 0.
        material:  Material del conductor. Valores aceptados: ``'cobre'``
                   (por defecto) y ``'aluminio'``.

    Returns:
        Diccionario con los siguientes campos:

        * ``caida_v``    - Caida de tension en voltios (float).
        * ``porcentaje`` - Caida expresada como porcentaje respecto a
                           220 V (float).
        * ``admisible``  - ``True`` si el porcentaje es <= 3 % (bool).

    Raises:
        ValueError: Si ``material`` no esta entre los reconocidos.
        ValueError: Si alguno de los parametros numericos no es positivo.

    Examples:
        >>> calcular_caida(longitud=100, corriente=15, seccion=4)
        {'caida_v': 12.9, 'porcentaje': 5.8636, 'admisible': False}
    """
    # Validar material
    material_lower = material.lower()
    if material_lower not in RESISTIVIDADES:
        materiales_validos = ", ".join(f"'{m}'" for m in RESISTIVIDADES)
        raise ValueError(
            f"Material '{material}' no reconocido. "
            f"Valores aceptados: {materiales_validos}."
        )

    # Validar parametros positivos
    parametros = {"longitud": longitud, "corriente": corriente, "seccion": seccion}
    for nombre, valor in parametros.items():
        if valor <= 0:
            raise ValueError(
                f"El parametro '{nombre}' debe ser positivo. "
                f"Se recibio: {valor}."
            )

    resistividad = RESISTIVIDADES[material_lower]
    caida_v = 2 * resistividad * longitud * corriente / seccion
    porcentaje = (caida_v / TENSION_REFERENCIA_V) * 100
    admisible = porcentaje <= PORCENTAJE_ADMISIBLE

    return {
        "caida_v": round(caida_v, 4),
        "porcentaje": round(porcentaje, 4),
        "admisible": admisible,
    }
