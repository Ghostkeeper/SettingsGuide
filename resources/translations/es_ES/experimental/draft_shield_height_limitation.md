Limitación del protector contra corrientes de aire
====
El protector contra corrientes de aire puede imprimirse hacia toda la altura del modelo o sólo hasta una altura determinada. Este ajuste le permite elegir la altura del protector contra corrientes de aire.

<!--screenshot {
"image_path": "draft_shield_enabled.png",
"models": [{"script": "headphone_hook.scad"}],
"camera_position": [-56, 139, 305],
"settings": {
    "draft_shield_enabled": true
},
"colours": 32
}-->
<!--screenshot {
"image_path": "draft_shield_height_limitation.png",
"models": [{"script": "headphone_hook.scad"}],
"camera_position": [-56, 139, 305],
"settings": {
    "draft_shield_enabled": true,
    "draft_shield_height_limitation": "limited",
    "draft_shield_height": 20
},
"colours": 32
}-->
![El escudo contra corrientes de aire es igual de alto que el modelo](../images/draft_shield_enabled.png)
![El protector contra corrientes de aire está limitado a 20 mm de altura](../images/draft_shield_height_limitation.png)

La parte inferior de la impresión tiende a ser más sensible a las fluctuaciones de temperatura. Aquí es donde se produce la mayor parte del alabeo si la habitación está fría, y este alabeo puede hacer que la impresión se suelte de la placa de impresión. Con este ajuste, puedes elegir limitar la altura del protector contra corrientes de aire a una altura determinada. Esto puede ahorrar algo de tiempo y material. El protector contra corrientes de aire seguirá protegiendo la parte inferior de la impresión y también bloqueará la convección del aire debido al ascenso del aire caliente (hasta cierto punto).

El protector contra corrientes de aire nunca puede imprimirse más alto que el propio objeto.