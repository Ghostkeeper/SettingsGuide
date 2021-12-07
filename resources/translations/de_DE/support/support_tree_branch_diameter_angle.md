Winkel Astdurchmesser der Baumstützstruktur
====
Die Äste der Baumstützen sind unten breiter als oben. Dadurch bleiben die Äste stabil, egal wie hoch der Support wird. Mit dieser Einstellung können Sie die Intensität steuern, mit der der Support breiter wird.

<!--screenshot {
"image_path": "support_tree_branch_diameter_1_4mm_5.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_diameter": 1.4,
    "support_tree_branch_diameter_angle": 5
},
"structures": ["helpers"],
"colours": 16
}-->
<!--screenshot {
"image_path": "support_tree_branch_diameter_angle_10.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_diameter": 1.4,
    "support_tree_branch_diameter_angle": 10
},
"structures": ["helpers"],
"colours": 16
}-->
![Die Form eines Astes mit einem Durchmesserwinkel von 5°](../../../articles/images/support_tree_branch_diameter_1_4mm_5.png)
![Die Form eines Astes mit einem Durchmesserwinkel von 10°](../../../articles/images/support_tree_branch_diameter_angle_10.png)

Je größer der Winkel ist, desto breiter wird die Unterseite des Baumsupports, insbesondere bei hohen Modellen. Dies hat mehrere Auswirkungen:
* Die breitere Unterseite sorgt dafür, dass der Support nicht so leicht umkippt. Dies erhöht die Zuverlässigkeit des Baumsupports.
* Der breitere Boden erfordert mehr Material und Zeit zum Drucken.
* Der Support-Winkel addiert sich zum maximalen [Winkel](support_tree_angle.md), bei dem die Äste überhängen können, so dass sehr hohe Werte dazu führen können, dass der Baumsupport in einigen Fällen auch weniger stabil ist.
* Die breiteren Äste haben es schwerer, um das Netz herum zu navigieren, wodurch es schwieriger wird, einige Teile des Überhangs von der Bauplatte aus zu erreichen. Infolgedessen kann es vorkommen, dass der Support auf dem Modell statt auf der Bauplatte aufliegen muss, wodurch die Narbenbildung zunimmt.
* Die Kollisionsvermeidung des Baums ist für Cura schwieriger zu berechnen, was zu einer erhöhten Slicing-Zeit führt. Dem kann man entgegenwirken, indem man die [Kollisionsauflösung der Baumstützstruktur](support_tree_collision_resolution.md) Einstellung erhöht, aber das reduziert auch die strukturelle Integrität des Baumsupport.

Im Allgemeinen sollte der Winkel so gewählt werden, dass der Baumsupport gerade breit genug ist, um sich in jeder Höhe zu halten, ohne zu wackelig zu werden.