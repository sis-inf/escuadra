# Guía de pruebas de Escuadra

Este documento describe cómo están organizadas las pruebas del proyecto y cómo ejecutarlas localmente para que cualquier integrante del equipo pueda validar cambios sin ambigüedad.

## Estructura de carpetas de pruebas

La carpeta `tests/` se organiza para cubrir pruebas unitarias, de integración y documentación manual:

| Carpeta | Tipo | Propósito |
| --- | --- | --- |
| `tests/core/` | Unitarias | Pruebas de comportamiento de componentes base reutilizables: funciones núcleo, utilidades comunes y validaciones aisladas. |
| `tests/modulos/` | Unitarias | Pruebas por módulo de dominio (álgebra, conversión de unidades y lógica eléctrica) con foco en casos determinísticos. |
| `tests/automatizados/` | Integración | Casos que consumen varios módulos en conjunto y validan la interacción entre capas del código de prueba. |
| `tests/casos/` | Integración/aceptación | Casos de validación funcional orientados a escenarios típicos del dominio. |
| `tests/casos/funcionales/` | Aceptación | Flujos manuales de validación funcional con entradas y resultados esperados escritos en archivos markdown. |
| `tests/manuales/` | QA manual | Procedimientos para ejecución manual con evidencia para pruebas no totalmente automatizables.
| `tests/plan/` | Planificación de QA | Documentación de estrategia, criterios de salida y plan de pruebas del proyecto.
| `tests/reportes/` | Evidencia | Plantillas y reportes de resultados para auditoría de cambios.
| `tests/datos/` | Soporte | Data de prueba y fixtures estáticos utilizados por diferentes suites.
| `tests/` (raíz) | Mezcla | Pruebas rápidas que no dependen de un submódulo específico.

## Ejecutar todos los tests

Para correr la suite completa de pruebas automatizadas:

```bash
pip install -e ".[dev]"
pytest
```

Comando equivalente (si tienes entornos aislados):

```bash
python -m pytest
```

## Ejecutar tests por categoría

### Unitarias

```bash
pytest tests/core tests/modulos
```

### Integración

```bash
pytest tests/automatizados tests/casos
```

### E2E / funcionales manuales

```bash
pytest tests/casos/funcionales
# o revisar manualmente los casos y reportes en markdown bajo tests/manuales y tests/reportes
```

## Ejecutar con cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

Resultados en consola y en `htmlcov/` para inspección local.

## Agregar un nuevo test

1. Define si tu caso es unitario, integración o funcional.
2. Usa el directorio más cercano al alcance del cambio (`core`, `modulos`, `automatizados`, etc.).
3. Crea archivo con prefijo `test_` dentro del directorio correspondiente (por ejemplo `test_calculo_tension.py`).
4. Escribe casos de prueba deterministas, con nombres descriptivos y una sola aserción principal por caso cuando sea posible.
5. Ejecuta el subconjunto afectado antes de hacer commit:

```bash
pytest tests/core tests/modulos  # ajustar al área modificada
```

6. Si agregas nuevos data files, registra cualquier cambio en la carpeta `tests/datos/` y enlaza su propósito en este README cuando aplique.

## Convenciones de nombres

- `test_<modulo>_<escenario>.py` para archivos de test.
- `test_<funcion>_<comportamiento>_caso_<n>` para funciones dentro del archivo.
- Evita nombres genéricos como `test_final.py` sin contexto.
- Mantén el idioma de los nombres de tests alineado con el idioma del archivo original.
- Añade comentarios breves solo cuando aporten claridad sobre precondiciones del dominio.
