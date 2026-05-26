# Escuadra

> Plataforma de herramientas orientadas a distintas ramas de la ingeniería para resolver problemas técnicos de forma práctica.

## ¿Qué es?

Escuadra es un proyecto que integra diferentes herramientas diseñadas para apoyar el trabajo en diversas áreas de la ingeniería. Permite a los usuarios aplicar conceptos teóricos en situaciones reales mediante soluciones digitales.

## ¿Para quién es?

**Este proyecto está dirigido a:**
	- Estudiantes de ingeniería
	- Docentes
	- Profesionales que necesiten herramientas de cálculo o análisis

## ¿Qué problema resuelve?

**Escuadra busca centralizar herramientas que normalmente están dispersas, facilitando:**
	- Resolución de problemas técnicos
	- Aplicación práctica de conceptos teóricos
	- Ahorro de tiempo en cálculos y análisis

## Ramas de ingeniería cubiertas

**El proyecto contempla herramientas para distintas áreas, entre ellas:**
	- Ingeniería de Sistemas
	- Ingeniería Informática
	- Ingeniería Industrial
	- Ingeniería Civil
	- Ingeniería Electrónica
	- Ingeniería Mecánica

## Stack tecnológico

El proyecto está desarrollado en Python 3.10+ con interfaz gráfica basada en PySide6.

| Componente | Tecnologia | Versión |
|---|---|---|
| Lenguaje | Python | 3.10+ |
| Interfaz gráfica | PySide6 | 6.6+ |
| Testing | pytest | 8+ |
| Linter | ruff | 0.4+ |


## Instalación

**Clonar el repositorio:**
	git clone https://github.com/sis-inf/escuadra.git
	cd escuadra
**Instalar dependencias:**
	pip install -r requirements.txt
**Para desarrollo:**
pip install -r requirements-dev.txt

## Uso rápido

**Ejecutar el proyecto:**
	python -m escuadra
**O directamente desde el paquete instalado:**
	escuadra

## Ejemplo de uso

**Ejemplo simple de una herramienta del proyecto:**
from escuadra.modulos.civil.viga import calcular_reacciones

resultado = calcular_reacciones(longitud=10, carga=20)
print(resultado)
# {'Ra': 10.0, 'Rb': 10.0, 'unidad': 'kN'}

## Documentación
Ver la carpeta [docs/](docs/)

## Contribuir
Ver [CONTRIBUTING.md](CONTRIBUTING.md)

## Licencia
MIT — ver [LICENSE](LICENSE)