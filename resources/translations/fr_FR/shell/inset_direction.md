Ordre des parois
====
Ce paramètre détermine quels parois sont imprimées en premier, de l'extérieur vers l'intérieur ou de l'intérieur vers l'extérieur.

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "outer_inset_first": false
},
"layer": 2,
"line": [0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 23, 29, 35, 45, 51, 57, 63, 67, 68, 69, 70, 71, 72, 73, 74, 84, 90, 96, 102, 113, 119, 125, 131],
"delay": 125,
"colours": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"models": [{"script": "calendar_holder.scad"}],
"camera_position": [0, 0, 120],
"settings": {
    "skin_outline_count": 0,
    "outer_inset_first": true
},
"layer": 2,
"line": [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 24, 30, 36, 47, 53, 59, 65, 70, 71, 72, 73, 74, 75, 76, 77, 86, 92, 98, 104, 114, 120, 126, 132],
"delay": 125,
"colours": 32
}-->
![La paroi intérieure est imprimée en premier](../../../articles/images/outer_inset_first_disabled.gif)
![La paroi extérieure est imprimée en premier](../../../articles/images/outer_inset_first_enabled.gif)

Ce paramètre a un léger effet sur la qualité ainsi que sur la précision dimensionnelle:
* L'impression de l'extérieur vers l'intérieur améliore la précision dimensionnelle. Les parois adjacentes se poussent généralement un peu, surtout si la largeur de la ligne de paroi est inférieure à la taille de la buse. La paroi qui est imprimée en premier aura été solidifiée et ne sera donc pas autant poussée. Par conséquent, en imprimant le mur extérieur en premier, vous obtiendrez un emplacement plus précis du mur extérieur.
* Si le remplissage est imprimé avant les murs, l'impression de l'extérieur vers l'intérieur réduira la quantité de remplissage qui transparaît sur la surface. Sinon, le remplissage est imprimé en premier, puis les murs intérieurs qui sont poussés vers l'extérieur par le remplissage, et enfin le mur extérieur qui est poussé vers l'extérieur par les murs intérieurs. Par conséquent, un motif pourrait être visible à l'extérieur. Si la paroi extérieure est imprimée en premier, elle peut se solidifier avant que la paroi intérieure ne puisse la pousser.
* L'impression de l'intérieur vers l'extérieur est meilleure pour la création des surplombs. La paroi extérieure est plus éloignée de la couche précédente que la paroi intérieure. Lorsque la paroi extérieure est imprimée en premier, elle n'a encore rien à quoi s'accrocher. Lorsque la paroi intérieure est imprimée en premier, la paroi extérieure peut se fixer latéralement à la paroi extérieure.