N'étirer que la couche supérieure
====
Si ce paramètre est activé, le repassage ne sera appliqué que sur la couche la plus haute de l'objet. Si votre modèle présente toutes sortes de surfaces supérieures mais que seule la plus haute est visible ou que seule la plus haute doit être lisse, ce réglage vous permet de gagner beaucoup de temps d'impression.

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
![Le demi-cercle de la couche inférieure ne sera pas repassé](../../../articles/images/ironing_only_highest_layer.png)

**Si une impression comporte plusieurs objets, la couche la plus élevée de chaque objet sera étirée. Cela inclut chaque partie d'une impression à plusieurs zones.**
