# Plan de Pruebas - Proyecto Escuadra

## 1. Objetivo
Garantizar la fiabilidad, precisión numérica y estabilidad de la suite de cálculo de ingeniería **Escuadra**, asegurando que los algoritmos matemáticos entreguen resultados exactos dentro de las tolerancias permitidas y que el sistema responda correctamente ante datos de entrada anómalos.

## 2. Alcance
### En alcance
- Validación de algoritmos de cálculo estructural y estadístico.
- Verificación de la precisión decimal (tolerancia de error 1e-7).
- Pruebas de manejo de excepciones (divisiones por cero, raíces negativas).
- Compatibilidad del entorno de ejecución local y CI.

### Fuera de alcance
- Seguridad de red o ataques externos (Pentesting).
- Pruebas de interfaz gráfica de usuario (UI/UX) avanzadas (el foco es el motor de cálculo).
- Compatibilidad con sistemas operativos móviles.

## 3. Tipos de prueba
- [x] **Unitarias:** Validación de funciones matemáticas individuales.
- [x] **Integración:** Verificación del flujo de datos entre módulos de cálculo.
- [x] **Funcionales manuales:** Validación de casos de uso específicos de ingeniería.
- [x] **Rendimiento:** Evaluación de tiempos de respuesta con grandes matrices de datos.
- [ ] Seguridad
- [x] **Regresión:** Asegurar que nuevos cálculos no afecten fórmulas ya validadas.

## 4. Entornos

| Entorno | SO | Versión |
|---|---|---|
| Local | Windows 10/11 / Linux | JDK 17 / Maven 3.8 |
| CI | Ubuntu latest | GitHub Actions |

## 5. Responsables

| Rol | Responsable |
|---|---|
| Diseño de casos | BALTAZAR BORRAS |
| Ejecución manual | BALTAZAR BORRAS |
| Automatización | BALTAZAR BORRAS / GitHub Actions |
| Reporte | BALTAZAR BORRAS |

## 6. Criterios de salida
- [x] Cobertura mínima de **80%** de las funciones críticas de cálculo.
- [x] Cero bugs críticos abiertos (especialmente errores de precisión).
- [x] Todos los casos de prueba matemáticos ejecutados y validados.

## 7. Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Errores de precisión decimal | Alta | Crítico | Uso de `double` y validación con tablas estándar. |
| Desbordamiento de memoria (grandes datos) | Media | Alto | Implementación de pruebas de estrés y límites de entrada. |
| Inconsistencia en CI (Ubuntu) vs Local | Baja | Medio | Uso de contenedores o entornos estandarizados en GitHub Actions. |
| Fórmulas matemáticas mal implementadas | Media | Crítico | Revisión por pares y contraste con software de ingeniería (Matlab/Excel). |