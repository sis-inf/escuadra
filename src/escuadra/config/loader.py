"""
Módulo para cargar configuración desde archivos YAML.
"""

import zipfile
from pathlib import Path

import yaml

FONT_SCALE_OPTIONS = [1.0, 1.25, 1.5]

DEFAULT_FONT_SCALE = 1.0


def _get_config_dir() -> Path:
    """Retorna el directorio de configuración del usuario."""
    config_dir = Path.home() / ".config" / "escuadra"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def _get_config_path() -> Path:
    """Retorna la ruta al archivo de configuración del usuario."""
    return _get_config_dir() / "config.yaml"


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


def load_font_scale() -> float:
    """
    Carga la escala de fuente guardada en la configuración del usuario.

    Returns:
        La escala de fuente (1.0, 1.25 o 1.5). Default 1.0 si no existe configuración.
    """
    config_path = _get_config_path()
    if not config_path.exists():
        return DEFAULT_FONT_SCALE

    try:
        config = load(str(config_path))
        scale = config.get("font_scale", DEFAULT_FONT_SCALE)
        if scale in FONT_SCALE_OPTIONS:
            return float(scale)
        return DEFAULT_FONT_SCALE
    except (FileNotFoundError, yaml.YAMLError):
        return DEFAULT_FONT_SCALE


def save_font_scale(scale: float) -> None:
    """
    Guarda la escala de fuente en la configuración del usuario.

    Args:
        scale: Escala de fuente a guardar (1.0, 1.25 o 1.5).

    Raises:
        ValueError: Si la escala no es una de las opciones válidas.
    """
    if scale not in FONT_SCALE_OPTIONS:
        raise ValueError(
            f"Escala inválida: {scale}. Opciones válidas: {FONT_SCALE_OPTIONS}"
        )

    config_path = _get_config_path()
    config = {}
    if config_path.exists():
        try:
            config = load(str(config_path))
        except (FileNotFoundError, yaml.YAMLError):
            config = {}

    config["font_scale"] = scale

    with config_path.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


def export_user_data(export_path: str) -> None:
    """
    Exporta toda la configuración y datos del usuario a un archivo ZIP.

    Args:
        export_path: Ruta donde guardar el archivo ZIP de respaldo.

    Raises:
        FileNotFoundError: Si no existe el directorio de configuración.
        zipfile.BadZipFile: Si hay un error al crear el ZIP.
    """
    config_dir = _get_config_dir()

    if not config_dir.exists():
        raise FileNotFoundError(
            f"Directorio de configuración no encontrado: {config_dir}"
        )

    with zipfile.ZipFile(export_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for archivo in config_dir.rglob("*"):
            if archivo.is_file():
                arcname = archivo.relative_to(config_dir)
                zf.write(archivo, arcname)


def import_user_data(import_path: str, overwrite: bool = True) -> None:
    """
    Restaura la configuración y datos del usuario desde un archivo ZIP.

    Args:
        import_path: Ruta al archivo ZIP de respaldo.
        overwrite: Si True, sobrescribe archivos existentes. Default True.

    Raises:
        FileNotFoundError: Si el archivo ZIP no existe.
        zipfile.BadZipFile: Si el archivo no es un ZIP válido.
    """
    if not Path(import_path).exists():
        raise FileNotFoundError(f"Archivo de respaldo no encontrado: {import_path}")

    config_dir = _get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(import_path, "r") as zf:
        for member in zf.namelist():
            destino = config_dir / member

            if destino.exists() and not overwrite:
                continue

            destino.parent.mkdir(parents=True, exist_ok=True)
            zf.extract(member, config_dir)
