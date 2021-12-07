Kollisionsauflösung der Baumstützstruktur
====
Ein großer Nachteil der Baumstützstruktur ist, dass die Berechnung sehr lange dauert, wenn sie aktiviert ist. Die meisten Berechnungen, die für die Baumunterstützung erforderlich sind, beziehen sich auf die Vermeidung von Kollisionen zwischen den Ästen des Baums und dem Netz. Diese Einstellung bestimmt die Genauigkeit dieser Kollisionsvermeidungsberechnungen. Eine höhere Auflösung (geringere Genauigkeit) spart viel Zeit bei den Berechnungen, führt aber auch dazu, dass der Support gezackt erscheint, wenn er sich in der Nähe des Meshes befindet.

<!--screenshot {
"image_path": "support_tree_collision_resolution_lo.png",
"models": [{"script": "castle_low.scad"}],
"camera_position": [-128, -63, 30],
"settings": {
    "z_seam_position": "backright",
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "support_tree_collision_resolution_hi.png",
"models": [{"script": "castle_low.scad"}],
"camera_position": [-128, -63, 30],
"settings": {
    "z_seam_position": "backright",
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.02
},
"colours": 32
}-->
![Eine niedrige Auflösung (0,2 mm) führt dazu, dass die Äste kantig werden.](../../../articles/images/support_tree_collision_resolution_lo.png)
![Eine hohe Auflösung (0,02 mm) erzeugt glatte Äste](../../../articles/images/support_tree_collision_resolution_hi.png)

Der technische Hintergrund dieser Einstellung ist wie folgt. Um bei aktivierter Kollisionsauflösung der Baumstützstruktur mit dem gedruckten Objekt zu vermeiden, berechnet Cura 3-dimensionale Volumina, in die die Zentren der Äste des Baumes nicht eindringen dürfen. Für jeden möglichen Durchmesser der Äste des Baumes wird ein solches Volumen berechnet, was sehr viel Zeit in Anspruch nimmt. Die Anzahl der möglichen Astdurchmesser nimmt mit zunehmender Höhe des Baumes und mit großen Werten für die [Winkel der Astdurchmesser für die Baumstützstruktur](support_tree_branch_diameter_angle.md) drastisch zu. Aus diesem Grund wird der Durchmesser auf das nächste Vielfache dieser Auflösungseinstellung gerundet. An einigen Stellen entlang der Baumhöhe wird die Kollision, der der Zweig ausweichen muss, jedoch auf das nächste Muster eines Zweigdurchmessers begrenzt, wodurch der Zweig plötzlich mehr Platz zum Bewegen hat. Dies lässt den Baum kantig erscheinen.

Wenn Sie diese Einstellung erhöhen, wird der Schnitt in Cura weniger Zeit in Anspruch nehmen. Dadurch wird auch der Support kantiger, was seine Festigkeit beeinträchtigt und die Wahrscheinlichkeit erhöht, dass der Support während des Druckens abbricht, was zum Scheitern des Drucks führen kann.