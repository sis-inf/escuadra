# API HTTP Local (Opcional)

Este documento describe la API HTTP local diseñada para invocar herramientas desde otros programas externos.

## Estado por Defecto y Seguridad

* **Desactivada por defecto:** Por razones de seguridad, la API no se encuentra activa al iniciar la aplicación. El usuario debe habilitarla de forma consciente.
* **Restricción de red:** La API está configurada para escuchar única y exclusivamente en `localhost` (127.0.0.1). No aceptará conexiones externas provenientes de otros dispositivos de la red.

## Pasos para Activación Consciente

Para habilitar y utilizar esta API local, siga los siguientes pasos:

1. Diríjase al archivo de configuración global del proyecto.
2. Localice la variable de entorno o propiedad `ENABLE_LOCAL_HTTP_API`.
3. Cambie su valor a `true`.
4. Reinicie la aplicación para aplicar los cambios.
5. Verifique que el servicio esté respondiendo correctamente realizando una petición de prueba a `http://localhost:[PUERTO]`.
