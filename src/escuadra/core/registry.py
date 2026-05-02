from collections.abc import Callable
from typing import Any

ToolFunction = Callable[..., Any]

_TOOLS: dict[str, ToolFunction] = {}


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


def get_tools() -> dict[str, ToolFunction]:
    """Devuelve una copia de las herramientas registradas."""

    return _TOOLS.copy()