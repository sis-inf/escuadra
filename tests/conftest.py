import pytest


@pytest.fixture
def mock_config():
    """Fixture que simula la carga de configuración YAML sin archivo real"""
    return {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "test_db"
        },
        "api": {
            "timeout": 30,
            "retries": 3
        },
        "logging": {
            "level": "DEBUG",
            "file": "test.log"
        }
    }
