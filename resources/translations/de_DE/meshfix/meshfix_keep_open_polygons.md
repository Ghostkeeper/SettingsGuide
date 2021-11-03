Unterbrochene Flächen beibehalten
====
Cura muss wissen, wo sich das Innere Ihres Modells befindet, um das Volumen mit Material füllen zu können. Wenn das Modell nicht richtig geschlossen ist, ist dies nicht eindeutig. Normalerweise wird Cura keine Teile drucken, die nicht richtig geschlossen sind.

Wenn diese Einstellung aktiviert ist, werden Schichten, deren Umfang nicht richtig geschlossen ist, beibehalten. Die Umrandung wird künstlich mit einer geraden Linie geschlossen. Dies kann dazu führen, dass einige Modelle, die kleine Lücken in ihren Oberflächen haben, korrigiert werden. Es kann aber auch zu Fehlinterpretationen der Innenseite Ihres Modells führen.

<!--screenshot {
"image_path": "meshfix_keep_open_polygons_shell.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_disabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
    "meshfix_keep_open_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "meshfix_keep_open_polygons_enabled.png",
"models": [{"script": "cube_missing_corner.py"}],
"camera_position": [85, -55, 75],
"settings": {
    "meshfix_keep_open_polygons": true
},
"colours": 64
}-->
![Bei diesem Würfel fehlt eine Ecke](../../../articles/images/meshfix_keep_open_polygons_shell.png)
![Normalerweise werden die nicht geschlossenen Schichten nicht gedruckt.](../../../articles/images/meshfix_keep_open_polygons_disabled.png)
![Wenn diese Einstellung aktiviert ist, wird die Form künstlich geschlossen.](../../../articles/images/meshfix_keep_open_polygons_enabled.png)

In der Röntgenansicht werden Lücken, die mit dieser Einstellung geschlossen werden können, rot dargestellt.