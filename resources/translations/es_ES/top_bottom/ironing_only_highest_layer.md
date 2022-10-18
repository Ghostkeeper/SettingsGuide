Planchar sólo la capa superior
====
Si esta opción está activada, el alisado sólo se aplicará a la capa más alta del objeto. Si su modelo tiene todo tipo de superficies superiores pero sólo la más alta es visible o sólo la más alta necesita ser alisada, entonces este ajuste le permite ahorrar mucho tiempo de impresión.

<!--screenshot {
"image_path": "ironing_only_highest_layer.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true,
    "ironing_only_highest_layer": true
},
"colours": 64
}-->
![El semicírculo de la capa inferior no queda alisado](../images/planchado_solo_capa_más_alta.png)

**Si hay varios objetos en una impresión, la capa más alta de cada objeto será alisada. Esto incluye todas las partes de una impresión multiextrusión.