Extrusor de superficie superior del forro
====
Para las impresoras que tienen múltiples extrusores, esto selecciona el extrusor que se utilizará para imprimir la superficie superior.

<!--screenshot {
"image_path": "roofing_extruder_nr.png",
"models": [
    {
        "script": "question_stick_clip.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, -90, 60],
"settings": {
    "wall_line_count": 0,
    "skin_outline_count": 0,
    "roofing_layer_count": 1,
    "roofing_extruder_nr": 1
},
"colour_scheme": "material_colour",
"colours": 32
}-->
![Este modelo se imprimirá sólo con las capas de la superficie superior en un color diferente](../images/roofing_extruder_nr.png)

De esta manera puedes darle a la superficie superior un color o material diferente. Tenga en cuenta que el extrusor de las paredes no se ajusta con esta configuración, por lo que todavía habrá un borde alrededor de la superficie superior.

Además de dar a la superficie superior un color diferente, también puedes usar esto para imprimir la superficie superior con un material diferente. Esto puede dar una variedad de efectos:
* Imprime la superficie superior y la pared exterior en PLA mientras imprimes el resto con un material más rígido para obtener un objeto fuerte que también tenga un buen aspecto.
* Imprimir la superficie superior con TPU pero el resto con un material más duro para conseguir una superficie de agarre suave y de alta fricción.
* Imprima la superficie superior con un material más resbaladizo que el material más fuerte que necesita para el interior del modelo, si algo necesita deslizarse sobre la superficie.

**Si el material para la superficie superior no se adhiere bien al material de abajo, tiende a soltarse después de la impresión. Ten especial cuidado con los materiales con altos ratios de contracción.**