import math
import warnings


def calcular_carga_critica_euler(
    modulo_elasticidad: float,
    momento_inercia: float,
    longitud: float,
    condicion_apoyo: str = "biarticulada",
    area_seccion: float = None,
    radio_giro: float = None,
) -> float:
    """
    Calcula la carga crítica de pandeo de Euler para columnas a compresión.

    Fórmula:
        P_cr = π² · E · I / (K · L)²

    Unidades:
        - E: módulo de elasticidad en Pascales (Pa) o MPa
        - I: momento de inercia en m⁴
        - L: longitud de la columna en metros (m)
        - P_cr: carga crítica en Newtons (N)

    Factores de longitud efectiva (K):
        - biarticulada: K = 1.0
        - empotrada-libre: K = 2.0
        - empotrada-empotrada: K = 0.5
        - empotrada-articulada: K = 0.7

    Args:
        modulo_elasticidad: Módulo de elasticidad del material (Pa)
        momento_inercia: Momento de inercia de la sección (m⁴)
        longitud: Longitud de la columna (m)
        condicion_apoyo: Tipo de condición de apoyo (default: 'biarticulada')
        area_seccion: Área de la sección transversal (m²) - opcional
        radio_giro: Radio de giro de la sección (m) - opcional

    Returns:
        Carga crítica de pandeo en Newtons (N)

    Raises:
        ValueError: Si los parámetros no son válidos o la condición de apoyo no existe

    Warnings:
        Si se proveen area_seccion y radio_giro, se genera una advertencia
        cuando la relación de esbeltez λ < 100, indicando que la fórmula
        de Euler podría no ser válida para columnas cortas.
    """
    if modulo_elasticidad <= 0:
        raise ValueError("modulo_elasticidad debe ser mayor que 0")

    if momento_inercia <= 0:
        raise ValueError("momento_inercia debe ser mayor que 0")

    if longitud <= 0:
        raise ValueError("longitud debe ser mayor que 0")

    # Definir factores K según condición de apoyo
    factores_k = {
        "biarticulada": 1.0,
        "empotrada-libre": 2.0,
        "empotrada-empotrada": 0.5,
        "empotrada-articulada": 0.7,
    }

    if condicion_apoyo not in factores_k:
        raise ValueError(
            f"condicion_apoyo debe ser una de: {list(factores_k.keys())}. "
            f"Valor recibido: {condicion_apoyo}"
        )

    K = factores_k[condicion_apoyo]

    # Calcular carga crítica de Euler
    # P_cr = π² · E · I / (K · L)²
    pi_cuadrado = math.pi ** 2
    longitud_efectiva = K * longitud
    carga_critica = (pi_cuadrado * modulo_elasticidad * momento_inercia) / (longitud_efectiva ** 2)

    # Verificar esbeltez si se proveen parámetros adicionales
    if area_seccion is not None and radio_giro is not None:
        if radio_giro <= 0:
            raise ValueError("radio_giro debe ser mayor que 0")

        esbeltez = longitud_efectiva / radio_giro

        if esbeltez < 100:
            warnings.warn(
                f"La relación de esbeltez λ = {esbeltez:.1f} es menor que 100. "
                f"La fórmula de Euler podría no ser válida para columnas cortas "
                f"donde domina el aplastamiento, no el pandeo. "
                f"Considere usar fórmulas para columnas intermediarias o cortas.",
                UserWarning,
                stacklevel=2,
            )

    return float(carga_critica)
