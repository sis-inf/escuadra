import yaml
import os

def load(path: str) -> dict:
    """
    Carga un archivo YAML y lo retorna como un diccionario.
    Si ocurre un error, retorna un diccionario vacío.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo no existe en: {path}")

        with open(path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            
            # Validar que el contenido sea un diccionario y no esté vacío
            return config if isinstance(config, dict) else {}

    except (FileNotFoundError, yaml.YAMLError) as e:
        # Aquí podrías imprimir el error para debug si lo deseas
        # print(f"Error cargando configuración: {e}")
        return {}
