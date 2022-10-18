El borde sustituye al soporte
====
Si esta opción está activada, el borde continuará siguiendo el modelo por debajo del soporte, en lugar de rodearlo. El soporte se imprimirá encima del borde, en la siguiente capa. También habrá un borde alrededor del soporte.

<!--screenshot {
"image_path": "brim_replaces_support_disabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 100, -136],
"settings": {
    "adhesion_type": "brim",
    "support_enable": true,
    "brim_replaces_support": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "brim_replaces_support_enabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 100, -136],
"settings": {
    "adhesion_type": "brim",
    "support_enable": true,
    "brim_replaces_support": true
},
"colours": 64
}-->
![Desactivado, el borde va alrededor del soporte](../images/brim_replaces_support_disabled.png)
![Activado, el borde va por debajo del soporte](../images/brim_replaces_support_enabled.png)

Si se activa esta opción, el borde seguirá mejor al modelo. Como resultado, el modelo se mantiene mejor hasta la placa de construcción, lo que evita el alabeo.

En algunos casos, esto reducirá el ancho total del borde para algunas piezas de soporte. Sin embargo, en esos casos, el soporte estará lo suficientemente cerca del modelo como para que el borde se funda con el del modelo, por lo que apenas habrá problemas de adherencia allí.