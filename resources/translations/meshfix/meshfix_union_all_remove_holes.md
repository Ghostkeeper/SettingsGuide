Eliminar todos los agujeros
====
Algunos modelos, en particular los realizados para técnicas de fabricación como el moldeo por inyección, tienden a venir con cavidades internas que no son visibles. Si este ajuste está activado, Cura elimina esas cavidades internas.

<!--screenshot {
"image_path": "meshfix_union_all_remove_holes_disabled.png",
"models": [{"script": "foothold.scad"}],
"camera_position": [-68, 40, 46],
"settings": {"meshfix_union_all_remove_holes": false},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_union_all_remove_holes_enabled.png",
"models": [{"script": "foothold.scad"}],
"camera_position": [-68, 40, 46],
"settings": {"meshfix_union_all_remove_holes": true},
"colours": 64
}-->
![Este modelo tiene un agujero en el centro](../images/meshfix_union_all_remove_holes_disabled.png)
![Con este ajuste activado, se elimina el agujero](../images/meshfix_union_all_remove_holes_enabled.png)

Las cavidades en el interior podrían estar diseñadas para ahorrar material, pero con la impresión 3D hay algunas limitaciones que hacen que esos modelos se impriman peor. Por ejemplo, las impresoras 3D no van bien con paredes finas que no sean un múltiplo de la anchura de la línea, y la piel superior tiende a combarse si no se apoya en el relleno. Generalmente es mejor hacer una malla sólida y dejar que el slicer decida cómo rellenarla. Esta configuración de fijación de malla le permite hacer eso sin necesidad de editar la malla.

Cura sólo mirará horizontalmente si una cavidad está cerrada completamente. No mirará si una cavidad es accesible desde la parte superior o inferior. La diferencia podría seguir siendo visible desde la parte superior o inferior.