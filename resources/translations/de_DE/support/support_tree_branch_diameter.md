Astdurchmesser der Baumstützstruktur
====
Mit dieser Einstellung können Sie die Breite der Zweige der Baumstützstruktur anpassen. Die hier angegebene Breite ist die Breite an der Spitze der Äste des Baums. Die Spitze des Zweigs ist dünner und wird nach unten hin allmählich breiter, wie in der Einstellung [Winkel Astdurchmesser der Baumstützstruktur](support_tree_branch_diameter_angle.md) angegeben.

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
"image_path": "support_tree_branch_diameter_5mm.png",
"models": [{"script": "lantern.scad"}],
"camera_position": [0, 70, 13],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_branch_diameter": 5,
    "support_tree_branch_diameter_angle": 5
},
"structures": ["helpers"],
"colours": 16
}-->
![Die Form eines Astes mit einem Durchmesser von 1.4mm](../../../articles/images/support_tree_branch_diameter_1_4mm_5.png)
![Die Form eines Astes mit einem Durchmesser von 5mm](../../../articles/images/support_tree_branch_diameter_5mm.png)

Breitere Äste sind stabiler und verringern die Gefahr, dass der Baum von der Düse umgeworfen wird, wenn sie darüber fahren muss.

Breitere Äste verbinden sich auch schneller miteinander. Dies spart etwas Material, kann aber auch dazu führen, dass ein Teil des Modells nicht mehr richtig gestützt wird, und zwar auch ein Teil des Supports selbst. Wenn Zweige zusammengeführt werden, haben sie keinen Kontur mehr. Breite Zweige werden am besten entweder mit einem großen [Abstand](support_tree_branch_distance.md) oder einer [Füllung](../support/support_infill_rate.md) kombiniert, um Teile in der Mitte der breiten Zweige richtig zu unterstützen.

Breitere Zweige werden es auch schwerer haben, um Ihr Modell herum zu navigieren. Dies kann dazu führen, dass ein größerer Teil des Supports auf dem Modell und nicht auf der Bauplatte aufliegt. Infolgedessen kann Ihr Modell nach dem Entfernen der Support-Strukturen mehr Narben aufweisen.