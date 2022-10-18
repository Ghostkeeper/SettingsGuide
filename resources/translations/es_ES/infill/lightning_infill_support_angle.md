Ángulo de soporte del relleno del rayo
====
El patrón de relleno Lightning sólo está pensado para soportar la impresión desde el interior. Este ajuste determina el ángulo máximo de voladizo, no sólo de las superficies que soportará sino también interno en el propio relleno. Si se reduce este ajuste, se genera más relleno. Si se aumenta, se reduce la cantidad de relleno.

El patrón soporta la cara superior de la impresión desde el interior, pero sólo la cara superior que sobresale significativamente, más de este ángulo. El patrón también tiene puntos finales que sobresalen en un determinado ángulo para crear una estructura de árbol ramificado, y los lados de esta estructura ramificada tienen un ángulo interno para llegar más lejos en ciertas áreas. Estos tres aspectos del voladizo también pueden controlarse individualmente con los ajustes [Ángulo de voladizo del relleno del rayo](lightning_infill_overhang_angle.md), [Ángulo de poda del relleno del rayo](lightning_infill_prune_angle.md) y [Ángulo de enderezamiento del relleno del rayo](lightning_infill_straightening_angle.md) respectivamente.

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
"image_path": "lightning_infill_support_angle_60.png",
"models": [{"script": "half_sphere.scad"}],
"camera_position": [130, 87, 47],
"settings": {
    "infill_pattern": "lightning",
    "wall_line_count": 0,
    "top_layers": 0,
    "lightning_infill_support_angle": 60
},
"colours": 64
}-->
![Con un ángulo de voladizo bajo, se necesita mucho apoyo](../images/lightning_infill_support_angle_30.png)
![Con un ángulo de voladizo alto, se permiten voladizos pronunciados](../images/lightning_infill_support_angle_60.png)

Aumentar este ajuste reducirá la cantidad de material necesario en gran medida, y reducirá el tiempo de impresión. Sin embargo, también causará hundimiento. Este hundimiento está en el interior del modelo, por lo que no es inmediatamente visible. Sin embargo, si el [Espesor de la parte superior](../top_bottom/top_thickness.md) no es suficiente, puede provocar [pillowing](../troubleshooting/pillowing.md). Dado que también se permite que los ángulos internos del relleno sobresalgan más, es probable que el relleno comience más arriba a lo largo de las paredes.