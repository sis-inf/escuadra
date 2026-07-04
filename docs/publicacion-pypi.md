# Publicación del paquete en PyPI

## Descripción

Este documento describe el proceso general de publicación del paquete `escuadra` en PyPI mediante un flujo de release basado en versiones y tags.

## Requisitos previos

Antes de realizar una publicación, verificar lo siguiente:

* Contar con permisos para crear tags en el repositorio.
* Tener la rama `dev` actualizada.
* Confirmar que las pruebas del proyecto se ejecutan correctamente.
* Verificar que la versión del paquete esté actualizada.

## Actualización de la versión

La versión del paquete se define en el archivo `pyproject.toml`.

Ejemplo:

```toml
[project]
version = "0.1.0"
```

Antes de generar una nueva publicación, actualizar este valor según la versión que se desea liberar.

## Verificación local

Se recomienda comprobar que el proyecto funciona correctamente antes de crear una nueva versión.

Ejecutar las pruebas:

```bash
pytest
```

Ejecutar las verificaciones de estilo:

```bash
ruff check .
```

## Creación del tag

Una vez que los cambios se encuentren integrados y validados, crear un tag para identificar la nueva versión.

Ejemplo:

```bash
git tag v0.1.1
```

Subir el tag al repositorio remoto:

```bash
git push origin v0.1.1
```

## Proceso de publicación

El flujo de publicación utiliza la versión definida en el proyecto y el tag asociado al release.

Durante este proceso se generan los artefactos necesarios para distribuir el paquete y publicarlo en PyPI.

## Verificación de la publicación

Después de completar la publicación:

1. Revisar el resultado del workflow correspondiente.
2. Confirmar que la nueva versión se encuentre disponible en PyPI.
3. Verificar que el paquete pueda instalarse correctamente.

## Instalación de prueba

Para comprobar la publicación, instalar el paquete desde PyPI:

```bash
pip install escuadra
```

También puede instalarse una versión específica:

```bash
pip install escuadra==0.1.1
```

## Solución de problemas

### La versión ya existe

PyPI no permite publicar dos veces la misma versión. Si una versión ya fue publicada, incrementar el número de versión y generar un nuevo tag.

### Error durante la ejecución del workflow

Revisar los registros de GitHub Actions para identificar la causa del error y corregirla antes de generar una nueva publicación.

### Error de instalación

Verificar que la versión publicada aparezca correctamente en PyPI y que todas las dependencias requeridas estén disponibles.
