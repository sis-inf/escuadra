def convertir_presion(valor, unidad_origen, unidad_destino):
    if valor < 0:
        raise ValueError("El valor debe ser mayor o igual a 0")

    factores = {
        "Pa": 1.0,
        "kPa": 1000.0,
        "MPa": 1000000.0,
        "bar": 100000.0,
        "atm": 101325.0,
        "psi": 6894.76,
        "mmHg": 133.322,
    }

    if unidad_origen not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_origen}. "
            f"Unidades válidas: {list(factores.keys())}"
        )

    if unidad_destino not in factores:
        raise ValueError(
            f"Unidad desconocida: {unidad_destino}. "
            f"Unidades válidas: {list(factores.keys())}"
        )

    valor_pa = valor * factores[unidad_origen]

    return valor_pa / factores[unidad_destino]
