Direcciones de línea de relleno
====
Las líneas de relleno suelen dirigirse en un ángulo de 45 grados en la medida de lo posible. En este ángulo, tanto el motor X como el Y trabajan juntos para obtener la máxima aceleración del cabezal de impresión, cuando se utiliza una impresora con el mecanismo de pórtico cartesiano común.

Con esta configuración, puedes ajustar este ángulo. Puedes especializarlo para crear una mayor fuerza para tu modelo específico, o lograr una mayor aceleración para tu sistema de pórtico específico (como para las impresoras delta).

<!--screenshot {
"image_path": "infill_pattern_lines.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "lines"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "infill_angles_0_30.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "lines",
    "infill_angles": [0, 30]
},
"colours": 32
}-->
Líneas de relleno con ángulos predeterminados de 45 y 135 grados](../images/infill_pattern_lines.png)
Líneas de relleno con ángulos personalizados de 0 y 30 grados](../images/infill_angles_0_30.png)

El valor de este ajuste debe ser una lista de ángulos separada por comas y rodeada de paréntesis. Un ángulo de 0 grados dará como resultado una línea paralela al eje Y. La lista de ángulos se alternará sobre las capas.
* La impresión final será más fuerte en las direcciones de las líneas de relleno. Si necesita que la impresión lleve una fuerza específica en una dirección horizontal, es útil orientar las líneas de relleno alrededor de esa dirección.
* Deje el ajuste en una lista vacía para utilizar el valor por defecto.
* El valor por defecto depende del patrón de relleno:
  * Para los patrones de relleno Cross y Cross 3D, el valor por defecto es [22]. Esto orienta tantas líneas como sea posible cerca de las diagonales.
  * Para los patrones de relleno Líneas y Zigzag, el valor por defecto es [45,135]. Esto hace que la orientación se altere capa a capa entre las dos diagonales.
  * Todos los demás patrones utilizan un valor por defecto de [45]. Esto orienta tantas líneas como sea posible cerca de las diagonales.