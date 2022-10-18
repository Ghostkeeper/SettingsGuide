Grosor superior/inferior
====
Con el Grosor superior/inferior puede ajustar el grosor de la piel sólida que se crea en la parte superior e inferior de su impresión.

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
"image_path": "top_bottom_thickness_3.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 203, 30],
"settings": {
    "wall_line_count": 0,
    "top_bottom_thickness": 3
},
"colours": 64
}-->
![Espesor superior e inferior normal](../images/top_bottom_thickness_0.8.png)
![Espesor superior e inferior mucho mayor](../images/top_bottom_thickness_3.png)

Esto afecta tanto a la parte superior como a la inferior de la impresión. La parte superior e inferior también pueden configurarse individualmente con los ajustes [Grosor superior](top_thickness.md) y [Grosor inferior](bottom_thickness.md).

Si este ajuste no es un múltiplo de la altura de la capa, se redondeará al múltiplo más cercano. Este ajuste sólo determina cuántas capas superiores e inferiores se generarán.

Un mayor espesor superior e inferior tendrá varios efectos, beneficiosos para la calidad total pero perjudiciales para la productividad.
* Su pieza será más fuerte. Un mayor grosor superior e inferior significará que una menor parte de su impresión se llenará con el patrón de relleno escaso. En su lugar, se hace completamente sólida.
* La superficie superior será más suave. Cualquier almohadillado y flacidez en la piel superior se suavizará en las capas puestas encima.
* Es más probable que el modelo sea impermeable. Tanto en la parte superior como en la inferior habrá más capas para bloquear la entrada de agua u otros fluidos, y para recuperarse de los voladizos.
* Su impresión utilizará más material, ya que se llenan más capas por completo.
* Su impresión tardará más tiempo, ya que hay que colocar más material hacia abajo y estas capas se imprimen normalmente más despacio que el relleno.
