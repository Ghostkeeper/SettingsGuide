Tamaño del paso de variación de las capas adaptativas
====
Si el grosor deseado de una capa es muy diferente al de la capa adyacente, habrá una gran diferencia en el caudal que sale de la boquilla, lo que puede causar una sobreextrusión o una subextrusión. Este ajuste asegura que la diferencia en el grosor de la capa es un cambio gradual, para evitar eso. Con este ajuste se puede especificar el cambio máximo en el grosor de la capa entre dos capas adyacentes.

<!--screenshot {
"image_path": "adaptive_layer_height_variation_step_0_05.png",
"models": [{"script": "barn.scad"}],
"camera_position": [-108, -229, 118],
"settings": {
    "adaptive_layer_height_enabled": true,
    "adaptive_layer_height_variation_step": 0.05,
    "layer_height": 0.2
},
"colour_scheme": "layer_thickness",
"colours": 128
}-->
<!--screenshot {
"image_path": "adaptive_layer_height_enabled.png",
"models": [{"script": "barn.scad"}],
"camera_position": [-108, -229, 118],
"settings": {
    "adaptive_layer_height_enabled": true,
    "layer_height": 0.2
},
"colour_scheme": "layer_thickness",
"colours": 128
}-->
![Un tamaño de paso grande permite cambios muy bruscos en el grosor de la capa](../images/adaptive_layer_height_variation_step_0_05.png)
![Un tamaño de paso pequeño requiere que los cambios en el grosor de las capas sean más suaves](../images/adaptive_layer_height_enabled.png)

Si se reduce este ajuste, la transición del grosor de la capa será más gradual. Esto tiene una serie de efectos en la impresión:
* Habrá menos sobreextrusión al pasar a un grosor de capa menor, porque el flujo que sale de la boquilla tiene algo de tiempo para ajustarse a una tasa de flujo menor. Esto evita la formación de manchas en la superficie.
* Del mismo modo, habrá menos subextrusión al pasar a un espesor de capa mayor, porque el flujo que sale de la boquilla puede ajustarse gradualmente a un caudal mayor.
* Las bandas serán menos visibles. Aunque las zonas con diferentes espesores de capa seguirán teniendo una textura y un color diferentes, estas zonas están ahora más separadas, lo que hace más difícil verlas.
* Donde hay un ángulo agudo en el modelo que debería causar una transición repentina a capas más finas, el efecto de topografía volverá a aparecer. Esto se debe a que el grosor de las capas no podrá ajustarse tan rápidamente, por lo que deberán utilizarse capas más gruesas para las superficies poco profundas.
* Del mismo modo, donde hay un ángulo agudo en el modelo que debería causar una transición repentina a capas más gruesas, la impresora creará capas innecesariamente finas, perdiendo tiempo de impresión donde no es necesario.

Debido a la implementación del algoritmo de Capas Adaptativas, la transición gradual a un grosor de capa diferente siempre se producirá *por encima* del ángulo en el modelo que provoca la transición.