from collections.abc import Callable
from pathlib import Path
from typing import Any
import logging

ToolFunction = Callable[..., Any]

_TOOLS: dict[str, ToolFunction] = {}

MODULOS_DIR = Path(__file__).parent.parent / "modulos"

logger = logging.getLogger(__name__)


def register_tool(name: str) -> Callable[[ToolFunction], ToolFunction]:
    """Registra una herramienta usando un nombre."""

    if not name or not name.strip():
        raise ValueError("El nombre de la herramienta no puede estar vacío")

    tool_name = name.strip()

    def decorator(func: ToolFunction) -> ToolFunction:
        if tool_name in _TOOLS:
            raise ValueError(f"La herramienta '{tool_name}' ya está registrada")

        _TOOLS[tool_name] = func
        return func

    return decorator


def get_tools():
    """Devuelve las herramientas registradas."""

    if not MODULOS_DIR.exists() or not any(MODULOS_DIR.iterdir()):
        logger.warning("No se encontraron herramientas en el directorio modulos.")
        return []

    return _TOOLS.copy()