Borde sólo en el exterior
====
Si su modelo tiene agujeros en la capa inicial de la placa de construcción, este ajuste evitará que se imprima un borde a lo largo del interior del agujero.

<!--screenshot {
"image_path": "brim_outside_only_original.png",
"models": [{"script": "holes_in_panel.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "adhesion_type": "brim",
    "brim_line_count": 10,
    "brim_outside_only": false
},
"layer": 1,
"colours": 32
}-->
<!--screenshot {
"image_path": "brim_outside_only_enabled.png",
"models": [{"script": "holes_in_panel.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "adhesion_type": "brim",
    "brim_line_count": 10,
    "brim_outside_only": true
},
"layer": 1,
"colours": 32
}-->
![Borde impreso en todas partes](../images/brim_outside_only_original.png)
![Borde sólo en el exterior](../images/brim_outside_only_enabled.png)

El borde en el interior suele añadir muy poca fuerza de adhesión adicional entre la impresión y la placa de impresión y no tiene ningún efecto en la prevención de la contracción. Quitar el borde en el interior puede ahorrarle algo de tiempo después de que la impresión se haya completado, porque no necesitará quitar el borde de los agujeros interiores.

**Si hay otro objeto dentro del agujero, el borde no puede ser retirado debido a limitaciones técnicas.**