# Dependencias del Proyecto

Este documento describe las dependencias utilizadas por el proyecto, su propósito y los criterios para incorporar nuevas librerías.

Estas dependencias son gestionadas en el archivo `requirements.txt`.

| Dependencia | Versión | Propósito | ¿Crítica? | ¿Puede eliminarse? | Documentación |
| :--- | :--- | :--- | :---: | :---: | :--- |
| PySide6 | >=6.6 | Framework basado en Qt para el desarrollo de la interfaz gráfica de usuario del proyecto. | Sí | No | https://doc.qt.io/qtforpython/ |
| pyyaml | No especificada | Permite leer y escribir archivos YAML utilizados para la configuración del proyecto. | Sí | No | https://pyyaml.org/wiki/PyYAMLDocumentation |

---


Estas dependencias son gestionadas en el archivo `requirements-dev.txt`.

| Dependencia | Versión | Propósito | ¿Crítica? | ¿Puede eliminarse? | Documentación |
| :--- | :--- | :--- | :---: | :---: | :--- |
| pytest | >=8.0 | Framework para la creación y ejecución de pruebas automatizadas. | Sí | No | https://docs.pytest.org/ |
| ruff | >=0.4 | Herramienta para análisis estático y formateo de código. | No | Sí, pero afectaría la calidad y consistencia del código. | https://docs.astral.sh/ruff/ |
| pre-commit | >=3.7 | Ejecuta verificaciones automáticas antes de cada commit. | No | Sí, pero reduciría los controles de calidad del desarrollo. | https://pre-commit.com/ |
| build | >=1.2 | Permite generar paquetes distribuibles del proyecto. | No | Sí, si el proyecto no necesita generar distribuciones. | https://build.pypa.io/ |

---

## Política de Dependencias

Antes de agregar una nueva dependencia al proyecto, se deben cumplir los siguientes criterios:

1. Verificar que la funcionalidad no pueda resolverse con la biblioteca estándar de Python.
2. Evaluar el mantenimiento, soporte y comunidad de la dependencia.
3. Revisar riesgos de seguridad y compatibilidad de licencias.
4. Justificar claramente su necesidad y valor para el proyecto.
5. Documentar su propósito, versión y uso.
6. Mantener las dependencias actualizadas.
7. Eliminar dependencias que ya no se utilicen.