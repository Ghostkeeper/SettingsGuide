Inserción de alisado
====
El alisado normalmente no se alisa hasta el borde exterior. Si lo hiciera, la presión continua en la cámara de boquillas haría que el material fluyera por encima del borde, lo que provoca una especie de efecto de ondulación. Este ajuste determina a qué distancia del borde se mantendrá el alisado.

<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true
},
"colours": 64
}-->
<!--screenshot {
"image_path": "ironing_inset.png",
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
    "ironing_inset": 1.2
},
"colours": 64
}-->
![Inserción por defecto de media línea de ancho](../images/ironing_enabled_enabled.png)
![Un mayor recorte de 1,2mm](../images/ironing_inset.png)

Hay dos casos principales de uso para este ajuste:
* Para asegurarse de que el material no se deposita sobre el borde.
* Como una forma de filtrar las tiras finas que normalmente se alisan. Si tiene una pendiente poco profunda, puede que no quiera que se alisen todas las capas de esa pendiente. Aumentar este ajuste puede filtrar las tiras más finas, pero también hará que las partes más grandes no se planchen hasta el borde.