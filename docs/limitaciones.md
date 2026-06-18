# Limitaciones de Escuadra - Versión Inicial (v1)

# 

##### A continuación, se detallan las limitaciones conocidas y esperadas de Escuadra en su versión inicial, así como algunas funcionalidades previstas para futuras versiones.

# 

# 1\. Falta de integración con herramientas de diseño gráfico

# 

##### Descripción: En esta versión no se incluye soporte para importar ni exportar archivos de herramientas como Adobe Illustrator, Figma o Inkscape. No es posible trabajar directamente con estos formatos.

# 

##### ¿Solución temporal? Sí. Los archivos deben exportarse o convertirse a formatos compatibles (PNG, JPG o SVG simple) antes de utilizarlos en Escuadra.

##### 

##### ¿Planeado para futuras versiones? Sí. Se tiene previsto integrar soporte para estos formatos en la versión v1.2.

# 

# 2\. No soporta sistemas operativos móviles

# 

##### Descripción: La herramienta solo funciona en sistemas operativos de escritorio como Windows, Linux y macOS. No es posible utilizarla en Android ni iOS.

##### 

##### ¿Solución temporal? No. Actualmente no existe una forma oficial de ejecutarla en dispositivos móviles.

##### 

##### ¿Planeado para futuras versiones? No. Esta funcionalidad no se encuentra dentro de los planes a corto o mediano plazo, ya que se priorizarán otras características.

# 

# 3\. No gestiona proyectos colaborativos simultáneos

# 

##### Descripción: La herramienta solo permite trabajar con un usuario a la vez en un mismo proyecto. No cuenta con edición en tiempo real ni control de versiones compartido.

##### 

##### ¿Solución temporal? Sí. Los usuarios pueden compartir archivos manualmente y fusionar los cambios mediante herramientas externas.

##### 

##### ¿Planeado para futuras versiones? Sí. Esta funcionalidad está prevista para la versión v2.0.



# 4\. Sin soporte para bases de datos externas



##### Descripción: Actualmente no es posible conectar, leer ni escribir información en bases de datos externas como MySQL, PostgreSQL o MongoDB. La herramienta únicamente trabaja con archivos locales.

##### 

##### ¿Solución temporal? No. Por el momento no existe una forma de conectarse a fuentes de datos externas.

##### 

##### ¿Planeado para futuras versiones? Sí. Se agregará conectividad básica con bases de datos en la versión v1.5.

##### 

# 5\. Limitaciones por módulo

# 

# 5.1 Módulo Civil

##### 

##### Descripción: El módulo Civil implementa un conjunto limitado de funcionalidades para el análisis estructural.

##### 

##### Limitaciones conocidas

##### 

##### \- Solo soporta vigas simplemente apoyadas.

##### \- No soporta vigas continuas.

##### \- No soporta marcos estructurales complejos.

##### \- No realiza análisis sísmico.

##### \- No contempla cargas dinámicas avanzadas.

##### \- Los resultados deben considerarse aproximaciones para escenarios básicos.

##### 

# 5.2 Módulo Eléctrica

##### 

##### Descripción: El módulo Eléctrica está orientado a circuitos básicos de corriente continua.

##### 

##### Limitaciones conocidas

##### 

##### \- Solo trabaja con corriente continua (DC).

##### \- No soporta corriente alterna (AC).

##### \- Solo considera resistencias puras.

##### \- No soporta capacitores ni inductores.

##### \- No realiza análisis fasorial.

##### \- No contempla fenómenos avanzados de potencia eléctrica.



# 5.3 Módulo Matemáticas

##### 

##### Descripción: El módulo Matemáticas utiliza la precisión numérica estándar del lenguaje.

##### 

##### Limitaciones conocidas

##### 

##### \- No utiliza bibliotecas de alta precisión numérica.

##### \- Pueden existir errores de redondeo.

##### \- Pueden existir errores de punto flotante.

##### \- Las operaciones repetidas pueden acumular pequeñas diferencias numéricas.

##### \- Algunos resultados pueden variar ligeramente dependiendo de la plataforma utilizada.

##### 

# 5.4 Módulo Geometría

##### 

##### Descripción: El módulo Geometría se enfoca en operaciones geométricas básicas.

##### 

##### Limitaciones conocidas

##### 

##### \- Solo soporta figuras regulares.

##### \- No soporta figuras irregulares complejas.

##### \- No incluye modelado tridimensional avanzado.

##### \- Algunas fórmulas asumen condiciones ideales.

##### \- No contempla geometría computacional avanzada.



# 5.5 Módulo Sistemas

##### 

##### Descripción: El módulo Sistemas implementa soporte limitado para el manejo de caracteres.

##### 

##### Limitaciones conocidas

##### 

##### \- Solo soporta caracteres ASCII en el rango de 0 a 127.

##### \- No soporta completamente Unicode.

##### \- Los caracteres especiales pueden producir resultados inesperados.

##### \- No existe soporte completo para alfabetos internacionales.

##### \- El procesamiento avanzado de texto no está implementado.

