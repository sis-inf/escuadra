import yaml
from pathlib import Path

def load(path: str) -> dict:
    """
    Carga un archivo YAML y lo retorna como un diccionario.
    """
    try:
        # Usamos Path para un manejo de rutas más moderno
        file_path = Path(path)
        if not file_path.exists():
            return {}

        with open(file_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            return config if isinstance(config, dict) else {}

    except yaml.YAMLError:
        # Eliminamos la variable 'e' si no se va a usar (Fix F841)
        return {}
