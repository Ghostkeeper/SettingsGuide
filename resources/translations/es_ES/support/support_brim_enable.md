Habilitar borde de soporte
====
Cuando se activa el borde de soporte, se dibujará un borde adicional dentro del área de soporte en la primera capa.

<!--screenshot {
"image_path": "support_brim_4mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
    "support_enable": true,
    "support_use_towers": false,
    "support_brim_enable": true,
    "support_brim_width": 4
},
"colours": 64
}-->
![El borde de soporte](../images/support_brim_4mm.png)

El borde de soporte se dibuja hacia el *interior*, a diferencia del borde ordinario. Si el [Tipo de adhesión de la placa de impresión](../platform_adhesion/adhesion_type.md) se establece en Brim, también se dibujará otro borde *alrededor* del soporte.

El propósito de este borde es dar al soporte más superficie donde pueda adherirse a la placa de impresión. Esto también se puede conseguir ajustando la [Distancia de la línea de soporte de la capa inicial] (support_initial_layer_line_distance.md), pero con esta función la adhesión se concentrará alrededor del borde del área de soporte, donde es más eficaz para evitar el alabeo.

Un borde de soporte también aumentará ligeramente la duración de la impresión y el coste del material, pero como sólo está en la primera capa es muy mínimo. Lo que sí hace es que el soporte sea más resistente, por lo que en el caso del patrón de soporte en zigzag puede ser más difícil que se rompa.