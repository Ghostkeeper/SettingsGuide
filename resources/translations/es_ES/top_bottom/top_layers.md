Capas superiores
====
Este ajuste configura cuántas capas sólidas se imprimen en la parte superior de la impresión. Estas capas sólidas se imprimen en lugar del relleno. Están pensadas para cerrar la parte superior.

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
![14 capas superiores](../images/top_bottom_thickness_0.8.png)
![50 capas superiores](../images/top_thickness.png)

Más capas superiores tendrán varios efectos, beneficiosos para la calidad de la superficie superior pero perjudiciales para la productividad.
* Su pieza será más fuerte. Tener más capas superiores significará que una parte más pequeña de su impresión se llenará con el patrón de relleno escaso. En su lugar, se hace completamente sólido.
* La superficie superior será más suave. Cualquier almohadillado y flacidez en la piel superior se suavizará en las capas puestas encima.
* Es más probable que su modelo sea hermético. Más capas en la parte superior serán capaces de bloquear el agua u otros fluidos de entrar, ya que más capas se llenan completamente.
* Su impresión utilizará más material, ya que más capas se llenan completamente.
* Su impresión tomará más tiempo, ya que más material debe ser colocado hacia abajo y estas capas se imprimen normalmente más lentamente que el relleno.