Brim nur an Außenseite
====
Wenn Ihr Modell in der ersten Schicht auf der Bauplatte Löcher hat, verhindert diese Einstellung, dass ein Brim an der Innenseite des Lochs gedruckt wird.

<!--screenshot {
"image_path": "brim_outside_only_original.png",
"models": [{"script": "holes_in_panel.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "adhesion_type": "brim",
    "brim_line_count": 10,
    "brim_outside_only": false
},
"layer": 1,
"colours": 32
}-->
<!--screenshot {
"image_path": "brim_outside_only_enabled.png",
"models": [{"script": "holes_in_panel.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "adhesion_type": "brim",
    "brim_line_count": 10,
    "brim_outside_only": true
},
"layer": 1,
"colours": 32
}-->
![Brim überall gedruckt.](../../../articles/images/brim_outside_only_original.png)
![Brim nur auf der Außenseite](../../../articles/images/brim_outside_only_enabled.png)

Der Brim auf der Innenseite sorgt in der Regel nur für eine sehr geringe zusätzliche Haftkraft zwischen dem Druck und der Bauplatte und hat keinen Einfluss auf die Vermeidung von Schrumpfung. Das Entfernen des Brims auf der Innenseite kann Ihnen nach dem Drucken etwas Zeit ersparen, da Sie den Brim nicht von den Innenlöchern entfernen müssen.

**Befindet sich ein anderes Objekt im Loch, kann der Brim aus technischen Gründen nicht entfernt werden.**