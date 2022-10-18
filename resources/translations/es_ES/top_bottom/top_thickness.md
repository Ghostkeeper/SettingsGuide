Grosor superior
====
Este ajuste configura el grosor de la parte superior sólida de la impresión. Esta capa sólida se imprime en lugar del relleno disperso. Su objetivo es cerrar la parte superior.

<!--screenshot {
"image_path": "top_bottom_thickness_0.8.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 203, 30],
"settings": {
    "wall_line_count": 0,
    "top_bottom_thickness": 0.8
},
"colours": 64
}-->
<!--screenshot {
"image_path": "top_thickness.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 203, 30],
"settings": {
    "wall_line_count": 0,
    "top_thickness": 3
},
"colours": 64
}-->
![Grosor superior ordinario](../images/top_bottom_thickness_0.8.png)
![Grosor muy elevado](../images/top_thickness.png)

Una cara superior más gruesa tendrá varios efectos, beneficiosos para la calidad de la superficie superior pero perjudiciales para la productividad.
* Su pieza será más fuerte. Tener una cara superior más gruesa significará que una parte más pequeña de su impresión se llenará con el patrón de relleno escaso. En su lugar, se hace completamente sólido.
* La superficie superior será más suave. Cualquier almohadillado y flacidez en el forro superior se suavizará en las capas adicionales.
* Es más probable que su modelo sea impermeable. Una cara superior más gruesa proporcionará más capas para bloquear la entrada de agua u otros fluidos, ya que más capas se llenan completamente.
* Su impresión utilizará más material, ya que más capas se llenan completamente.
* Su impresión tomará más tiempo, ya que se debe colocar más material hacia abajo y estas capas normalmente se imprimen más lentamente que el relleno.