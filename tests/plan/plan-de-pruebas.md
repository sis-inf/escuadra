# Plan de Pruebas - Proyecto Escuadra

## 1. Objetivo
Asegurar la calidad y confiabilidad de los módulos de cálculo de la suite de ingeniería Escuadra, garantizando que los resultados matemáticos sean exactos y que el sistema sea estable bajo diferentes escenarios de uso.

## 2. Alcance
### En alcance
- Verificación de fórmulas matemáticas de ingeniería aplicadas en los módulos.
- Validación de la precisión numérica y manejo correcto de decimales en cálculos complejos.
- Pruebas de la interfaz de usuario para la entrada de datos técnicos.
### Fuera de alcance
- Compatibilidad con navegadores web obsoletos (Internet Explorer).
- Pruebas de integración con hardware externo o sensores de medición.

## 3. Tipos de prueba
- [x] Unitarias
- [x] Integración
- [x] Funcionales manuales
- [ ] Rendimiento
- [ ] Seguridad
- [x] Regresión

## 4. Entornos

| Entorno | SO | Versión |
|---|---|---|
| Local | Windows 10/11 | Git Bash / VS Code |
| CI | Ubuntu latest | GitHub Actions |

## 5. Responsables

| Rol | Responsable |
|---|---|
| Diseño de casos | Rodrigo Baltazar Borras |
| Ejecución manual | Rodrigo Baltazar Borras |
| Automatización | DevOps / Equipo de QA |
| Reporte | Rodrigo Baltazar Borras |

## 6. Criterios de salida
- [x] Cobertura mínima de pruebas del 85% en módulos de cálculo.
- [x] Cero bugs de severidad "Crítica" o "Alta" abiertos.
- [x] Todos los casos de prueba manuales ejecutados y aprobados.
- [x] **Precisión Numérica:** Margen de error máximo aceptable de $10^{-6}$.

## 7. Riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Errores en fórmulas de cálculo | Media | Muy Alto | Revisión técnica de fórmulas y doble validación manual. |
| Inestabilidad en la rama principal | Baja | Alto | Uso obligatorio de Pull Requests con revisión de código. |
| Datos de entrada fuera de rango | Alta | Medio | Implementación de validaciones de tipo y límites en los campos. |