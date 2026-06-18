# Guía de Integración Continua (CI/CD)

Este documento detalla el funcionamiento de la infraestructura de Integración y Despliegue Continuo (CI/CD) de nuestro proyecto, explicando cómo interactúan las herramientas de automatización con el flujo de trabajo del equipo de desarrollo.

## Workflows disponibles

El repositorio cuenta con tres flujos de trabajo (workflows) automatizados configurados dentro del directorio `.github/workflows/`:

| Nombre | Cuándo se activa (Trigger) | Qué hace |
|---|---|---|
| `Python CI` (`ci.yml`) | Ante cualquier evento de `push` o `pull_request` en cualquier rama del repositorio (`"**"`). | Levanta un entorno de ejecución con una matriz de versiones de Python (3.10, 3.11 y 3.12). Instala las dependencias y ejecuta el linter `ruff` y la suite de pruebas con `pytest`. |
| `Security scan` (`security.yml`) | Al realizar un `push` en la rama `dev` o al abrir un `pull_request` que apunte hacia la rama `main`. | Utiliza GitHub CodeQL para ejecutar un análisis estático de seguridad (SAST) buscando vulnerabilidades específicas en el código escrito en JavaScript/TypeScript. |
| `Deploy` (`deploy.yml`) | Únicamente al realizar un `push` directo o fusión de rama (merge) en la rama `main`. | Funciona como un esqueleto o *placeholder* preparatorio para el despliegue automático. Actualmente solo ejecuta una instrucción de impresión en consola. |

## Flujo de un PR

El ciclo de vida del código para cualquier contribución sigue un flujo estructurado desde que se inicia el trabajo en un entorno local hasta que se consolida en el repositorio central:

```text
1.  Fork del repositorio principal desde la interfaz de GitHub.
2.  Clonar tu fork de forma local en tu estación de trabajo.
3.  Crear una rama de trabajo local partiendo siempre desde 'dev'.
4.  Realizar modificaciones en el código y asegurar los estados mediante commits.
5. ⬆ Push de la rama de trabajo hacia tu repositorio remoto (tu fork).
6.  Abrir un Pull Request (PR) apuntando exclusivamente a la rama 'dev' del repositorio original.
7.  GitHub Actions intercepta el PR y ejecuta de forma automatizada los flujos del CI.
8.  Revisión de código (Code Review) obligatoria y retroalimentación por parte del equipo.
9. Fusión (Merge) del Pull Request aprobado dentro de la rama 'dev'.
Cómo corregir un CI fallido
Cuando un pipeline automatizado falla, GitHub Actions detendrá las tareas siguientes y marcará el Pull Request con una cruz roja (❌). Para solucionar el problema, debes ingresar a la pestaña "Checks" de tu PR, examinar los registros (logs) de la consola para identificar el error y proceder en tu máquina local según el tipo de fallo:

Errores de Tests (Pruebas unitarias)
Ocurren cuando la lógica modificada altera el comportamiento esperado del sistema, provocando que las aserciones de las pruebas fallen.

Diagnóstico: Revisa el log de la tarea de pruebas en GitHub Actions para localizar el archivo y el nombre exacto de la función de prueba que falló (ej. test_calculo_error).

Procedimiento local:

Activa el entorno virtual de tu proyecto en la terminal.

Instala las dependencias de desarrollo obligatorias:

Bash
pip install -r requirements-dev.txt
Ejecuta la suite de pruebas localmente para reproducir el fallo:

Bash
pytest
Corrige el código fuente en tu editor hasta que el comando pytest se ejecute al 100% sin errores.

Errores de Lint/Formato
El linter valida que el código cumpla estrictamente con las reglas de estilo de Python y no contenga malas prácticas (como variables declaradas que nunca se usan o importaciones duplicadas).

Diagnóstico: El log de la tarea Lint (ruff) especificará el archivo, el número de línea y el identificador de la regla de estilo infringida.

Procedimiento local:

Ejecuta el linter en tu terminal para visualizar los problemas de formato en tu entorno local:

Bash
ruff check .
Para solucionar de forma automatizada la mayoría de los problemas de espaciado y estilo, ejecuta:

Bash
ruff check --fix .
Modifica manualmente las líneas de código que el formateador automático no pueda resolver por sí mismo.

Errores de Seguridad
El pipeline de seguridad inspecciona el código buscando fallas de diseño, vulnerabilidades de inyección o malas prácticas de manejo de datos.

Diagnóstico: Dirígete a la alerta generada por el check Security scan. CodeQL mostrará el camino del flujo de datos inseguro directamente en la interfaz de código de GitHub.

Procedimiento local:

Identifica el archivo JavaScript o TypeScript que disparó la alerta.

Modifica el código aplicando técnicas de sanitización de entradas, consultas parametrizadas o la refactorización recomendada por la documentación que GitHub anexa a la alerta.

Asegúrate de guardar los cambios antes de confirmar.

Ejecutar el CI localmente
Para optimizar el tiempo de desarrollo y asegurar que tus cambios pasen el CI antes de subirlos a la nube, puedes validar tu entorno localmente mediante dos alternativas:

Ejecución de comandos individuales: Antes de realizar un git commit, acostumbra ejecutar de manera nativa los validadores en tu terminal local:

Bash
ruff check .
pytest
Simulación completa con act: Si dispones de la herramienta nektos/act instalada en tu sistema y cuentas con el servicio de Docker activo, puedes emular exactamente el comportamiento de los servidores de GitHub ejecutando en la raíz de tu proyecto:

Bash
act pull_request
Notificaciones
GitHub Actions se encarga de alertar de manera directa y automatizada al autor del Pull Request mediante notificaciones web (el icono de la campana en GitHub) y alertas al correo electrónico asociado a la cuenta en los siguientes escenarios:

Fallo en los flujos de trabajo: En el momento exacto en que cualquiera de las tareas (Python CI o Security scan) falle en sus validaciones.

Actualización e interacciones: Cuando un miembro del equipo de desarrollo aprueba, comenta o solicita cambios específicos (changes requested) dentro del Pull Request.

Cierre o integración: Cuando los mantenedores del proyecto completan la fusión (merge) de la rama de manera exitosa o proceden a cerrar el PR.