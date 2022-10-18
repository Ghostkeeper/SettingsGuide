Alternar pared adicional
====
Esta configuración añade una pared adicional cada dos capas. De este modo, el relleno queda encajado verticalmente entre las paredes, lo que resulta en impresiones más fuertes.

Por ejemplo, si establece el recuento de líneas de pared a dos paredes y activa la pared extra alterna, se imprimirán dos paredes en las capas pares y tres paredes en las capas impares.

<!--screenshot {
"image_path": "alternate_extra_perimeter.gif",
"models": [
    {
        "script": "gear.scad",
        "transformation": ["scale(0.7)"]
    }
],
"camera_position": [0, 30, 123],
"settings": {
    "zig_zaggify_infill": true,
    "alternate_extra_perimeter": true
},
"layer": [15, 16, 17, 18],
"minimum_layer": [15, 16, 17, 18],
"colours": 32
}-->
![Esta imagen muestra las paredes que se ven afectadas al cambiar esta configuración] (../images/alternate_extra_perimeter.gif)

Activar esta configuración le llevará un tiempo extra, aproximadamente la mitad de lo que le llevaría añadir una pared extra. En algunos aspectos, esta pared extra alternada es casi tan buena como una pared extra completa, y en otros no:
* Aumenta en gran medida la unión entre el relleno y las paredes, ya que las líneas de relleno también pueden pegarse verticalmente a la pared extra por encima y por debajo de ellas. En este aspecto, la pared adicional supera su categoría. Es muy eficaz. 
* Aporta a la rigidez de la impresión tanto como la mitad de una pared adicional. Al adherirse a la pared adyacente, distribuye la tensión sobre más cordones y proporciona un mayor brazo contra las fuerzas en la dirección horizontal. La pared extra alternada no tiene una ventaja particular para hacer esto, ni una desventaja particular.
* Una pared extra real también añadiría resistencia a la unión de las capas. Las paredes se imprimen lentamente, por lo que son una fuente importante de fuerza de unión de las capas. Sin embargo, la pared extra alternada no se adhiere a las capas adyacentes porque sólo se produce cada dos capas.

Como resultado, la pared extra alternada es una forma eficiente de añadir rigidez horizontal, pero no una forma eficiente de añadir resistencia vertical.