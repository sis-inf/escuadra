import ast
import importlib.util
import sys
from pathlib import Path


def tiene_docstring_modulo(tree):
    return ast.get_docstring(tree) is not None


def funciones_publicas(tree):
    return [
        nodo
        for nodo in ast.walk(tree)
        if isinstance(nodo, ast.FunctionDef)
        and not nodo.name.startswith("_")
    ]


def tiene_docstring_funcion(funcion):
    return ast.get_docstring(funcion) is not None


def tiene_type_hints(funcion):
    parametros_ok = all(arg.annotation is not None for arg in funcion.args.args)
    retorno_ok = funcion.returns is not None
    return parametros_ok and retorno_ok


def es_importable(ruta):
    try:
        spec = importlib.util.spec_from_file_location("modulo_verificado", ruta)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return True
    except Exception:
        return False


def main():
    if len(sys.argv) != 2:
        print("Uso: python scripts/verificar_modulo.py <archivo.py>")
        sys.exit(1)

    ruta = Path(sys.argv[1])

    if not ruta.exists():
        print(f"❌ Archivo no encontrado: {ruta}")
        sys.exit(1)

    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    tree = ast.parse(contenido)

    errores = False

    modulo_doc = tiene_docstring_modulo(tree)
    print(f"{'✅' if modulo_doc else '❌'} Docstring de módulo")
    errores |= not modulo_doc

    funcs = funciones_publicas(tree)

    todas_doc = all(tiene_docstring_funcion(f) for f in funcs)
    print(f"{'✅' if todas_doc else '❌'} Docstrings en funciones públicas")
    errores |= not todas_doc

    todos_types = all(tiene_type_hints(f) for f in funcs)
    print(f"{'✅' if todos_types else '❌'} Type hints en funciones públicas")
    errores |= not todos_types

    importable = es_importable(ruta)
    print(f"{'✅' if importable else '❌'} Módulo importable")
    errores |= not importable

    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()