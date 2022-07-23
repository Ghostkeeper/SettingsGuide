Soporte de relleno
====
Cuando se activa, se trata el relleno como soporte. El relleno sólo se generará donde sea necesario para soportar la superficie superior. Se comporta como si el modelo fuera hueco y genera soporte en su interior, pero este soporte se genera utilizando los ajustes de relleno.

<!--screenshot {
"image_path": "infill_support_enabled_disabled.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_support_enabled": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_support_angle_low.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_support_enabled": true,
    "infill_support_angle": 40
},
"colours": 64
}-->
![Relleno normal](../images/infill_support_enabled_disabled.png)
![Relleno habilitado](../images/infill_support_angle_low.png)

* Esto ahorra mucho material de relleno con muy poco coste visual.
* Las superficies superiores pueden combarse un poco más con esta opción.
* Sin embargo, la resistencia horizontal del relleno puede verse comprometida. En muchos casos, no habrá relleno detrás de los muros, si éstos forman parte de una pendiente pronunciada.