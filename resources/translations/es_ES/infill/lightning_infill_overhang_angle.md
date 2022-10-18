Ángulo del voladizo del rayo
====
El relleno de rayos sólo apoyará la parte superior del modelo desde el interior donde sobresale. Este ajuste determina el ángulo de voladizo que soporta el rayo desde el interior del modelo.

<!--screenshot {
"image_path": "lightning_infill_support_angle_30.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "lightning_infill_overhang_angle_70.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 30,
    "lightning_infill_overhang_angle": 70
},
"colours": 64
}-->
![Hasta 30° de voladizo se deja sin soportes](../images/lightning_infill_support_angle_30.png)
![Hasta 70° sin soportes, dejando sólo la parte superior de la esfera con soporte](../images/lightning_infill_overhang_70.png)

Aumentando este ángulo se reduce la cantidad de relleno generado. Se apoyará menos superficie superior, si no es un voladizo muy pronunciado. Esto ahorra tiempo y material, pero también puede hacer que la superficie superior se hunda en algunas partes. El resultado podría ser [pillowing](../troubleshooting/pillowing.md) o, en general, una superficie más rugosa.

Al contrario que el ajuste principal [Ángulo de soporte del relleno del rayo](lightning_infill_support_angle.md), este ajuste no influye en el voladizo del propio patrón de relleno.