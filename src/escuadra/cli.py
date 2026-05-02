"""
Módulo CLI de Escuadra.
Punto de entrada principal con subcomandos para las herramientas.
"""

import argparse

__version__ = "0.1.0"


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


if __name__ == "__main__":
    main()