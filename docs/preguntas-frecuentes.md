# Preguntas Frecuentes — Suite Escuadra

## Que es Escuadra?

Escuadra es un proyecto que integra diferentes herramientas diseñadas para apoyar el trabajo en diversas áreas de la ingeniería. Permite a los usuarios aplicar conceptos teóricos en situaciones reales mediante soluciones digitales, centralizando herramientas que normalmente estan dispersas.

## Para quien esta dirigido Escuadra?

Escuadra esta dirigido a estudiantes de ingenieria, docentes y profesionales que necesiten herramientas de cálculo o análisis en su trabajo diario.

## Que herramientas incluye la suite?

La suite incluye las siguientes herramientas:

- **Calculadora de Vigas:** cálculo de momentos flectores y fuerzas cortantes en estructuras simples.
- **Conversor de Unidades:** transformación de medidas técnicas (presión, fuerza, longitud) al Sistema Internacional (SI).
- **Análisis Estadístico:** procesamiento de datos experimentales y cálculo de desviaciones estándar.
- **Diseño de Mezclas:** cálculo de proporciones para materiales de construcción según normativas.

## Como se instala Escuadra?

Sigue estos pasos para instalar el proyecto:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/sis-inf/escuadra.git
   cd escuadra
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Ejecuta el proyecto:
   ```bash
   npm start
   ```

## Que plataformas soporta Escuadra?

Escuadra funciona en cualquier plataforma que soporte Node.js, incluyendo Windows, macOS y Linux.

## Como puedo contribuir al proyecto?

Para contribuir a Escuadra se sigue el metodo Forking Workflow:

1. Haz un fork del repositorio.
2. Crea una rama con el nombre sugerido en el issue correspondiente.
3. Realiza tus cambios siguiendo los estandares de codigo del proyecto.
4. Abre un Pull Request con el titulo del issue y completa la descripcion del PR.

Para mas detalles, consulta el archivo `CONTRIBUTING.md` del repositorio.

## Como sincronizo mi fork con los últimos cambios del upstream?

Para mantener tu fork actualizado con el repositorio principal (upstream), sigue estos pasos:

1. Agrega el repositorio upstream si aún no lo has hecho:
   ```bash
   git remote add upstream https://github.com/sis-inf/escuadra.git
   ```
2. Obtén los cambios del upstream:
   ```bash
   git fetch upstream
   ```
3. Cambia a tu rama principal (generalmente `dev` o `main`):
   ```bash
   git checkout dev
   ```
4. Fusiona los cambios del upstream en tu rama:
   ```bash
   git merge upstream/dev
   ```
5. Sube los cambios a tu fork en GitHub:
   ```bash
   git push origin dev
   ```

## Puedo trabajar en más de una issue simultáneamente?

Sí, puedes trabajar en múltiples issues, pero se recomienda crear una rama separada para cada una para evitar conflictos y mantener el historial limpio. Por ejemplo:

```bash
git checkout dev
git checkout -b feature/issue-123
# Trabaja en la issue 123
git checkout dev
git checkout -b feature/issue-456
# Trabaja en la issue 456
```

## Qué pasa si mi PR tiene conflictos de merge?

Si tu Pull Request tiene conflictos, GitHub te lo indicará. Debes resolverlos localmente:

1. Actualiza tu rama con los últimos cambios de `dev`:
   ```bash
   git fetch upstream
   git checkout dev
   git merge upstream/dev
   ```
2. Cambia a tu rama de feature y fusiona `dev`:
   ```bash
   git checkout feature/tu-rama
   git merge dev
   ```
3. Resuelve los conflictos manualmente en los archivos marcados.
4. Marca los conflictos como resueltos y haz commit:
   ```bash
   git add .
   git commit -m "Resuelve conflictos de merge"
   ```
5. Sube los cambios a tu fork:
   ```bash
   git push origin feature/tu-rama
   ```

## Por qué fue cerrado mi PR sin merge?

Un PR puede cerrarse sin merge por varias razones:
- No sigue los estándares de código del proyecto.
- Tiene conflictos de merge no resueltos.
- No pasa las pruebas de CI (Continuous Integration).
- No está relacionado con una issue abierta o no cumple con los criterios de aceptación.
- La rama de destino no es la correcta (debe ser `dev`, no `main`).

Revisa los comentarios del revisor y el log de CI para identificar el problema.

## Cómo sé si mi código pasa el CI antes de hacer el PR?

Puedes ejecutar las pruebas localmente antes de hacer el PR. Asegúrate de tener las dependencias instaladas y corre los scripts de prueba definidos en `package.json`:

```bash
npm install
npm test
```

Si el proyecto usa otras herramientas de linting o análisis estático, ejecútalas también:

```bash
npm run lint
```

Si todos los pasos pasan sin errores, es probable que el CI en GitHub Actions también pase.

## Cómo creo una rama para una nueva issue?

Primero, asegúrate de estar en la rama base (`dev`) y actualizada:

```bash
git checkout dev
git pull upstream dev
```

Luego, crea una nueva rama con un nombre descriptivo que incluya el número de la issue:

```bash
git checkout -b feature/issue-123-descripcion-corta
```

Trabaja en esa rama y haz commit de tus cambios antes de abrir el PR.

## Qué debo hacer si olvido hacer el fork del repositorio?

Si ya clonaste el repositorio original en lugar de hacer un fork, debes:

1. Cambiar el origen remoto a tu fork:
   ```bash
   git remote set-url origin https://github.com/TU_USUARIO/escuadra.git
   ```
2. Agrega el upstream si no lo tienes:
   ```bash
   git remote add upstream https://github.com/sis-inf/escuadra.git
   ```
3. Verifica los remotos:
   ```bash
   git remote -v
   ```
Asegúrate de que `origin` apunte a tu fork y `upstream` al repositorio original.

## Qué áreas de ingeniería cubre Escuadra?

El proyecto contempla herramientas para distintas ramas de ingeniería: Sistemas, Informática, Industrial, Civil, Electrónica y Mecánica.