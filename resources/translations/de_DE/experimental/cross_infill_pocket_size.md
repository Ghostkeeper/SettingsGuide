Größe 3D-Kreuztasche
====
Das Kreuz 3D [Füllmuster](../infill/infill_pattern.md) wurde erstellt, um flexible Drucke zu ermöglichen. Das Muster enthält jedoch 4-Wege-Kreuzungen, die sehr starr sind. Diese Einstellung bewirkt, dass das Muster die Kreuzungen vermeidet, um an bestimmten Stellen nicht zu starr zu sein. Sie bewirkt, dass das Muster eine Lufttasche in der Kreuzung hinterlässt. Diese Einstellung bestimmt die Größe der Tasche.

<!--screenshot {
"image_path": "infill_pattern_cross_3d.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d",
    "cross_infill_pocket_size": 2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "cross_infill_pocket_size_0_5.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d",
    "cross_infill_pocket_size": 0.5
},
"colours": 32
}-->
![Die Standardtaschengröße von 2 mm](../../../articles/images/infill_pattern_cross_3d.png)
![Eine Taschengröße von 0,5 mm](../../../articles/images/cross_infill_pocket_size_0_5.png)

Das Muster variiert den Abstand um die 4-Wege-Kreuzung. Diese Einstellung bestimmt die Größe der Tasche in den Schichten, wenn sich die Linien vollständig berühren. Die maximale Größe der Tasche wird durch die Dichte der Füllung bestimmt. Die Taschengröße wird nicht größer gezeichnet als die Quadratwurzel aus dem 2-fachen Abstand der Füllung. Wenn ein größerer Wert eingegeben wird, hat das keine Auswirkung, kann aber trotzdem eingegeben werden, um größere Taschengrößen zu ermöglichen, falls die Funktion [Stufenweise Füllungsschritte](../infill/gradual_infill_steps.md) oder [Kreuzfülldichte Bild](cross_infill_density_image.md) verwendet wird.

Wenn Sie den Wert für diese Einstellung erhöhen, wird die Füllung in vertikaler Richtung schwächer und verteilt die Stärke besser, so dass eine gleichmäßigere Stärkeverteilung entsteht.