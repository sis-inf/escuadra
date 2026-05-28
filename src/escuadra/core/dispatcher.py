"""
Despachador de comandos que mapea subcomandos a funciones ejecutables.
"""

import sys


def run_convert() -> int:
    """Ejecuta el subcomando convert."""
    print("Ejecutando conversión...")
    return 0


def run_matrix() -> int:
    """Ejecuta el subcomando matrix."""
    print("Ejecutando operaciones de matriz...")
    return 0


COMMANDS: dict[str, callable] = {
    "convert": run_convert,
    "matrix": run_matrix,
}


def dispatch(subcommand: str) -> int:
    """
    Despacha un subcomando a su función ejecutable correspondiente.

    Args:
        subcommand: Nombre del subcomando a ejecutar.

    Returns:
        Código de salida entero (0 para éxito).

    Raises:
        KeyError: Si el subcomando no existe (manejado internamente).

    Examples:
        >>> dispatch("convert")
        Ejecutando conversión...
        0
        >>> dispatch("desconocido")
        Error: subcomando desconocido 'desconocido'
        1
    """
    try:
        handler = COMMANDS[subcommand]
    except KeyError:
        print(
            f"Error: subcomando desconocido '{subcommand}'",
            file=sys.stderr,
        )
        return 1

    try:
        return handler()
    except (ImportError, ModuleNotFoundError):
        print(
            "Error: El módulo solicitado no está disponible o no existe.",
            file=sys.stderr,
        )
        return 1