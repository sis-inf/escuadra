import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from conversor_bases import convertir_base
except ImportError:
    from src.conversor_bases import convertir_base

def test_conversiones_basicas():
    """Aquí probamos que los números se conviertan bien entre bases"""
    
    assert convertir_base("10", 10, 2) == "1010"
    assert convertir_base("1010", 2, 10) == "10"
    assert convertir_base("F", 16, 10) == "15"
    assert convertir_base("17", 8, 10) == "15"
    assert convertir_base("10", 10, 16) == "A"
    assert convertir_base("12", 8, 2) == "1010"

def test_validar_errores():
    """Aquí probamos que el programa avise cuando algo está mal"""
    
    with pytest.raises(ValueError):
        convertir_base("10", 5, 10)
        
    with pytest.raises(ValueError):
        convertir_base("102", 2, 10)
