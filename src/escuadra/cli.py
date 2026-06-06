"""
Módulo CLI de Escuadra.
Punto de entrada principal con subcomandos para las herramientas.
"""

import argparse

__version__ = "0.1.0"

# Agregar aqui los modulos cuando esten implementados
MODULOS_DISPONIBLES = set()

def herramienta_no_disponible(nombre_herramienta):
    """Muestra mensaje para herramientas no implementadas."""
    print(f"La herramienta '{nombre_herramienta}' aún está en construcción y no está disponible.")

def ejecutar_herramienta(args):
    """
    Ejecuta el subcomando correspondiente si el módulo existe. En caso contrario, muestra un mensaje
    """
    herramienta = args.herramienta

    if herramienta not in MODULOS_DISPONIBLES:
        herramienta_no_disponible(herramienta)
        return

    try:
        modulo = __import__(
            f"escuadra.modulos.{herramienta}",
            fromlist=["ejecutar"]
        )

    except (ModuleNotFoundError, ImportError):
        herramienta_no_disponible(herramienta)
        return

    kwargs = vars(args).copy()
    kwargs.pop("herramienta")

    modulo.ejecutar(**kwargs)


def main():
    """Punto de entrada principal del CLI de Escuadra."""
    parser = argparse.ArgumentParser(
        prog="escuadra",
        description="Herramientas de cálculo de ingeniería civil y eléctrica."
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(
        title="herramientas",
        dest="herramienta",
        help="Herramienta a ejecutar"
    )

    # Subcomando: viga
    viga_parser = subparsers.add_parser("viga", help="Cálculo de reacciones en vigas")
    viga_parser.add_argument("--longitud", type=float, required=True, help="Longitud de la viga en metros")
    viga_parser.add_argument("--carga", type=float, required=True, help="Carga puntual en kN")

    # Subcomando: tension
    tension_parser = subparsers.add_parser("tension", help="Cálculo de caída de tensión")
    tension_parser.add_argument("--longitud", type=float, required=True, help="Longitud del conductor en metros")
    tension_parser.add_argument("--corriente", type=float, required=True, help="Corriente en amperios")
    tension_parser.add_argument("--seccion", type=float, required=True, help="Sección del conductor en mm²")

    args = parser.parse_args()

    if args.herramienta is None:
        parser.print_help()
        return

    ejecutar_herramienta(args)


if __name__ == "__main__":
    main()