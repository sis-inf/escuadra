"""
Módulo CLI de Escuadra.
Punto de entrada principal con subcomandos para las herramientas.
"""

import argparse
import platform
import sys


def verificar_entorno():
    """Verifica la versión de Python y la disponibilidad de PySide6."""

    if sys.version_info < (3, 10):
        print(
            f"Error: Escuadra requiere Python 3.10 o superior.\n"
            f"Versión detectada: {sys.version.split()[0]}\n"
            "Actualice Python e inténtelo nuevamente."
        )
        sys.exit(1)

    try:
        # noqa: F401
        import PySide6
    except ImportError:
        print(
            "Error: PySide6 no está instalado.\n"
            "Instálelo ejecutando:\n"
            "    pip install PySide6"
        )
        sys.exit(1)


__version__ = "0.1.0"


MODULOS_DISPONIBLES = set()


def herramienta_no_disponible(nombre_herramienta):
    """Muestra mensaje para herramientas no implementadas."""
    print(f"La herramienta '{nombre_herramienta}' aún está en construcción.")


def ejecutar_herramienta(args):
    """Ejecuta el subcomando correspondiente si el módulo existe."""
    herramienta = args.herramienta

    if herramienta not in MODULOS_DISPONIBLES:
        herramienta_no_disponible(herramienta)
        return

    try:
        modulo = __import__(
            f"escuadra.modulos.{herramienta}", fromlist=["ejecutar"]
        )
    except (ModuleNotFoundError, ImportError):
        herramienta_no_disponible(herramienta)
        return

    kwargs = vars(args).copy()
    kwargs.pop("herramienta")
    modulo.ejecutar(**kwargs)


def mostrar_version_detallada():
    """Imprime la versión del proyecto junto con datos de diagnóstico."""
    print(f"Escuadra versión: {__version__}")
    print(f"Python versión: {platform.python_version()}")

    try:
        import PySide6

        pyside_version = PySide6.__version__
    except ImportError:
        pyside_version = "No instalado / No detectado"

    print(f"PySide6 versión: {pyside_version}")
    print(
        f"Sistema Operativo: {platform.system()} "
        f"{platform.release()} ({platform.machine()})"
    )


def main():
    """Punto de entrada principal del CLI de Escuadra."""
    try:
        parser = argparse.ArgumentParser(
            prog="escuadra",
            description="Herramientas de cálculo de ingeniería."
        )

        parser.add_argument(
            "--version", "-v", action="version",
            version=f"%(prog)s {__version__}"
        )

        subparsers = parser.add_subparsers(
            title="herramientas", dest="herramienta", help="Herramienta"
        )

        subparsers.add_parser(
            "version",
            help="Muestra la versión e información de diagnóstico"
        )

        subparsers.add_parser(
            "interactivo",
            help="Modo interactivo paso a paso (REPL)"
        )

        viga_parser = subparsers.add_parser(
            "viga", help="Cálculo de reacciones en vigas"
        )
        viga_parser.add_argument(
            "--longitud", type=float, required=True, help="Longitud (m)"
        )
        viga_parser.add_argument(
            "--carga", type=float, required=True, help="Carga (kN)"
        )

        tension_parser = subparsers.add_parser(
            "tension", help="Cálculo de caída de tensión"
        )
        tension_parser.add_argument(
            "--longitud", type=float, required=True, help="Longitud (m)"
        )
        tension_parser.add_argument(
            "--corriente", type=float, required=True, help="Corriente (A)"
        )
        tension_parser.add_argument(
            "--seccion", type=float, required=True, help="Sección (mm²)"
        )

        args = parser.parse_args()

        if args.herramienta is None:
            parser.print_help()
            sys.exit(0)

        if args.herramienta == "version":
            mostrar_version_detallada()
            sys.exit(0)

        verificar_entorno()
        ejecutar_herramienta(args)

    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        sys.exit(130)


if __name__ == "__main__":
    main()