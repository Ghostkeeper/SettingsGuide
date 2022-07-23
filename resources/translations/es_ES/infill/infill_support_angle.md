Ángulo del voladizo de relleno
====
Cuando se utiliza el soporte de relleno, este ajuste determina el ángulo mínimo de voladizo de la superficie que necesita ser soportada. Es similar al ajuste [Ángulo de voladizo](../soporte/ángulo_de_soporte.md) para el soporte ordinario.

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
<!--screenshot {
"image_path": "infill_support_angle_high.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
    "wall_line_count": 0,
    "infill_support_enabled": true,
    "infill_support_angle": 60
},
"colours": 64
}-->
![Un ángulo bajo produce más apoyo](../images/infill_support_angle_low.png)
![Un ángulo alto produce menos apoyo](../images/infill_support_angle_high.png)

Aumentar este ángulo hará que el relleno apoye menos la superficie superior. Esto ahorra tiempo de impresión y material, pero hará que la piel superior se hunda un poco más.
* Un valor de 0° actuará como un relleno normal. Soporta todo.
* Un valor de 90° eliminará todo el material de relleno.