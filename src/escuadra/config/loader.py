"""
Módulo para cargar configuración desde archivos YAML.
"""

from pathlib import Path

import yaml


def load(path: str) -> dict:
    """
    Carga un archivo YAML y retorna su contenido como diccionario.

    Args:
        path: Ruta al archivo YAML.

    Returns:
        Diccionario con la configuración cargada.
        Retorna dict vacío si el archivo está vacío.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        yaml.YAMLError: Si el archivo tiene formato YAML inválido.

    Examples:
        >>> config = load("config.yaml")
        >>> print(config)
        {'nombre': 'escuadra', 'version': '1.0'}
    """
    archivo = Path(path)

    if not archivo.exists():
        raise FileNotFoundError(f"Archivo de configuración no encontrado: {path}")

    with archivo.open("r", encoding="utf-8") as f:
        try:
            contenido = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error al parsear el archivo YAML: {e}")

    if contenido is None:
        return {}

    return contenido
