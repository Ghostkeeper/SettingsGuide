Habilitar el Escudo de Exudado
====
Cuando se imprime con múltiples extrusores, los extrusores inactivos a veces todavía tienen algo de material en ellos. Si las boquillas están todavía calientes, este material tiende a rezumar. Ese es el problema que el escudo de exudado está destinado a evitar. El escudo contra la exudación es un borde alrededor del objeto que atrapa cualquier exudación debajo de la boquilla.

<!--screenshot {
"image_path": "ooze_shield.png",
"models": [
    {
        "script": "rocket_dual.scad",
        "scad_params": ["extruder=0"],
        "object_settings": {
            "extruder_nr": 0
        },
        "transformation": ["scale(0.5)"]
    },
    {
        "script": "rocket_dual.scad",
        "scad_params": ["extruder=1"],
        "object_settings": {
            "extruder_nr": 1
        },
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [-62, 102, 87],
"settings": {
    "ooze_shield_enabled": true,
    "layer_height": 0.2,
    "line_width": 0.6
},
"colour_scheme": "material_colour",
"colours": 64
}-->
![El escudo de exudado se imprime con el primer extrusor de una capa, causando un patrón alternativo si se imprime con dos extrusores](../images/ooze_shield.png)
Pueden ajustarse algunos parámetros para el escudo de exudado](../images/ooze_shield.svg)

El escudo de exudado imprimirá hasta la altura del interruptor más alto del extrusor. Por encima de esa altura, ninguna boquilla se moverá en la impresión después de estar en modo de espera, por lo que la impresión de un escudo ooze es innecesaria. El escudo de exudado se imprimirá con el extrusor que comienza en una capa. Este extrusor alternará cada capa, lo cual es un peligro cuando se trabaja con dos materiales diferentes que no se pegan bien entre sí. Sin embargo imprimirlo después, cuando el otro extrusor se activa, destruye el efecto del escudo de exudado en gran medida.

El escudo de exudado es lo suficientemente delgado como para romperse o cortarse fácilmente, y mantiene su distancia de su modelo para que pueda ser removido sin marcar la superficie.