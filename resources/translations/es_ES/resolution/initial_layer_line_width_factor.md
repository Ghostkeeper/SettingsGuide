Ancho de línea de la capa inicial
====
Esto hace que las líneas de la capa inicial sean más anchas o más finas en una determinada proporción.

<!--screenshot {
"image_path": "initial_layer_line_width_factor.png",
"models": [{"script": "hex_foot.scad"}],
"camera_position": [0, 92, 122],
"settings": {
    "adhesion_type": "brim",
    "initial_layer_line_width_factor": 200
},
"colours": 32
}-->
![Las líneas de la capa inicial son el doble de anchas que el resto](../images/initial_layer_line_width_factor.png)

El objetivo de este ajuste es mejorar la adhesión a la placa de construcción. Para imprimir líneas más anchas, la boquilla tiene que extrudir más material y ese material tiene que fluir más hacia afuera. Esto hace que la boquilla presione el material con más fuerza sobre la placa de impresión, lo que aumenta la adhesión entre el filamento y la placa de impresión.
* Las líneas no sólo serán más anchas o más finas, sino que también estarán más separadas o más juntas por el mismo factor, por lo que no se produciría una sobreextrusión o una subextrusión.
* Este ajuste afecta a todos los anchos de línea; piel, paredes, adhesión, soporte, la torre principal, etc. Se harán más anchas o más finas en la misma proporción.