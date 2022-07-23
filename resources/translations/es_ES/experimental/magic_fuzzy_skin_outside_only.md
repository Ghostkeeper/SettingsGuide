Pieles peludas sólo en el exterior
====
Si esta opción está activada, el efecto [piel difusa](magic_fuzzy_skin_enabled.md) sólo se aplicará a las paredes exteriores de la impresión.

<!--screenshot {
"image_path": "magic_fuzzy_skin_outside_only.png",
"models": [{"script": "watch_strap_keeper.scad"}],
"camera_position": [-52, -37, 37],
"settings": {
    "magic_fuzzy_skin_enabled": true,
    "magic_fuzzy_skin_outside_only": true
},
"colours": 32
}-->
![El exterior es borroso, pero el interior no lo es](../images/magic_fuzzy_skin_outside_only.png)

Una piel borrosa puede ser un buen efecto para dar al modelo algo de textura o mayor agarre, pero destruye por completo cualquier precisión dimensional que se pueda esperar de la impresión. Esto es un problema si la impresión necesita ser montada en algo, como un asa o unos tornillos. Para estos casos, puedes desactivar el efecto de piel difusa en los contornos interiores de la impresión, limitándolo sólo a los exteriores.