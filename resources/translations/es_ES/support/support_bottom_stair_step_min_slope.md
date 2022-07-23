Ángulo de pendiente mínimo del escalón de la escalera de soporte
====
Con este ajuste puede desactivar el paso de escalera en la parte inferior del soporte, hasta que la pendiente del modelo tenga un determinado ángulo.

<!--screenshot {
"image_path": "support_bottom_stair_step_min_slope_10.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 82, 10],
"camera_lookat": [0, 0, 10],
"settings": {
    "support_enable": true,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_min_slope": 10
},
"layer": 250,
"colours": 64
}-->
<!--screenshot {
"image_path": "support_bottom_stair_step_min_slope_30.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 82, 10],
"camera_lookat": [0, 0, 10],
"settings": {
    "support_enable": true,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_min_slope": 30
},
"layer": 250,
"colours": 64
}-->
![Escalera desactivada hasta que la pendiente sea de 10°](../images/support_bottom_stair_step_min_slope_10.png)
![Escalera desactivada hasta que la pendiente sea de 30°](../images/support_bottom_stair_step_min_slope_30.png)

En pendientes poco pronunciadas, los peldaños de la parte inferior pueden ser muy anchos. Nunca pueden ser más anchos de lo que indica la [anchura máxima](support_bottom_stair_step_width.md), pero como esa distancia se mantiene desde todos los lados, los peldaños de la escalera pueden llegar a ser tan anchos que haya una distancia considerable que el soporte tenga que salvar. Si hay un pequeño valle en el que se apoya el soporte, puede incluso hacer que se salte toda la parte inferior, haciendo que todo el soporte se apoye sólo en las esquinas de los peldaños.

Para esos casos, puede limitar los peldaños de la escalera para que sólo se produzcan en las pendientes más pronunciadas. Este ajuste decide lo que constituye una pendiente "empinada" en ese sentido.

Aumentando este ajuste evitará que Cura genere los peldaños de la escalera en superficies poco profundas. Esto hará que el soporte sea más resistente, pero más difícil de eliminar. El soporte dejará más cicatrices en la superficie. Reducirlo hará que el soporte sea más fácil de quitar y dejará una superficie más bonita donde se apoyaba el soporte, pero en algunos casos puede hacer que el soporte tenga que salvar largas distancias o incluso que parezca colgar en el aire completamente.

Para obtener una superficie agradable, es mejor dejar este ajuste en un ángulo bajo conservador, 5° o 10° más o menos. Si el soporte se apoya en una superficie poco profunda pero no completamente plana, inspeccione la vista de la capa y aumente el ángulo si encuentra que el soporte parece muy precario.