# Integracion con Google Sheets

## Descripcion general

Escuadra permite exportar resultados directamente a Google Sheets mediante una funcion personalizada en Google Apps Script.

## Requisitos previos

- Escuadra ejecutandose localmente con la API HTTP activada
- Una cuenta de Google con acceso a Google Sheets
- Acceso al editor de Apps Script

## Configurar OAuth en Google Cloud Console

1. Ir a https://console.cloud.google.com
2. Crear un proyecto nuevo o seleccionar uno existente
3. Ir a APIs y servicios > Credenciales
4. Clic en Crear credenciales > ID de cliente OAuth
5. Seleccionar tipo de aplicacion: Aplicacion web
6. Agregar en Origenes autorizados: http://localhost:8000
7. Copiar el Client ID y Client Secret generados

## Activar la API HTTP de Escuadra

En el archivo de configuracion de Escuadra activar el servidor HTTP:

    escuadra --api

El servidor queda disponible en http://localhost:8000

## Crear la funcion personalizada en Google Sheets

1. Abrir Google Sheets
2. Ir a Extensiones > Apps Script
3. Copiar el siguiente codigo:

    function ESCUADRA_CALCULAR(herramienta, parametros) {
      var url = "http://localhost:8000/calcular/" + herramienta;
      var opciones = {
        method: "post",
        contentType: "application/json",
        payload: JSON.stringify({ parametros: parametros })
      };
      var respuesta = UrlFetchApp.fetch(url, opciones);
      var datos = JSON.parse(respuesta.getContentText());
      return datos.resultado;
    }

4. Guardar el proyecto con Ctrl+S
5. Ejecutar la funcion una vez para autorizar los permisos

## Usar la funcion en la hoja de calculo

En cualquier celda de Google Sheets:

    =ESCUADRA_CALCULAR("herramienta", A1:B2)

Donde:
- herramienta: nombre del modulo de Escuadra a invocar
- A1:B2: rango de celdas con los parametros de entrada

## Limitaciones

- Requiere que Escuadra este ejecutandose localmente
- El servidor HTTP debe estar disponible en el momento del calculo
- No es compatible con Google Sheets en modo offline
