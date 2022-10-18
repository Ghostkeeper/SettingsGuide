Altura del protector contra corrientes de aire
====
Si el ajuste [Limitación del protector contra corrientes de aire](draft_shield_height_limitation.md) está establecido en "Limitado", este ajuste le permite especificar a qué altura debe limitarse el protector contra corrientes de aire.

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
![El protector contra corrientes de aire está limitado a 20 mm de altura](../images/draft_shield_height_limitation.png)

La parte inferior de la impresión tiende a ser más sensible a las fluctuaciones de temperatura. Aquí es donde se produce la mayor parte del alabeo si la habitación está fría, y este alabeo puede hacer que la impresión se suelte de la placa de impresión. Con este ajuste, puedes elegir a qué altura limitar la impresión. Bajar la altura del protector contra corrientes de aire puede ahorrar algo de tiempo y material. El protector contra corrientes de aire seguirá protegiendo la parte inferior de la impresión y también bloqueará la convección del aire debido al ascenso del aire caliente (hasta cierto punto).

El protector contra corrientes de aire nunca puede imprimirse más alto que el propio objeto.