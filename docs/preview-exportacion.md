# Vista Previa antes de Exportar

## Introducción

Antes de confirmar cualquier exportación, Estante muestra una vista previa de los datos que serán exportados. Este paso permite verificar que el contenido, el formato y la cantidad de registros sean los esperados antes de generar el archivo.

---

## ¿Cuándo aparece la vista previa?

La vista previa se activa automáticamente al seleccionar la opción de exportación luego de ejecutar una consulta de lectura. Se presenta independientemente del formato elegido (CSV, JSON o Excel).

---

## Flujo general

1. Ejecutar una consulta de lectura.
2. Seleccionar la opción de exportación.
3. Elegir el formato de exportación (CSV, JSON o Excel).
4. Revisar la vista previa que muestra los datos a exportar.
5. Confirmar o cancelar la exportación.

---

## Vista previa por formato

### CSV

La vista previa muestra las primeras filas del resultado en formato tabular, con los encabezados de columna en la primera fila.

Ejemplo de vista previa:

id | nombre | edad

1 | Ana    | 21

2 | Carlos | 25

3 | María  | 22

Información visible antes de confirmar:

- Nombres de las columnas detectadas.
- Cantidad total de filas a exportar.
- Separador que se utilizará (coma `,`).

---

### JSON

La vista previa muestra una representación estructurada de los datos, donde cada fila del resultado aparece como un objeto dentro de un arreglo.

Ejemplo de vista previa:

```json
[
  {
    "id": 1,
    "nombre": "Ana",
    "activo": true
  },
  {
    "id": 2,
    "nombre": "Carlos",
    "activo": false
  }
]
```

Información visible antes de confirmar:

- Estructura de claves y valores del primer registro.
- Tipos de datos inferidos (número, booleano, texto, nulo).
- Cantidad total de objetos a incluir en el arreglo.

---

## Confirmación y cancelación

Una vez revisada la vista previa, el usuario puede:

- **Confirmar**: genera el archivo y permite elegir la ubicación donde se guardará.
- **Cancelar**: descarta la exportación y regresa a la pantalla de resultados sin modificar nada.

---

## Recomendaciones

- Revisar la cantidad de filas antes de confirmar, especialmente en conjuntos de datos grandes.
- Verificar que los encabezados de columna sean los esperados.
- Si los datos no coinciden con lo esperado, cancelar y ajustar la consulta antes de volver a exportar.