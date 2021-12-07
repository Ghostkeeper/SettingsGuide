Linienabstand der ursprünglichen Stützstruktur
====
Die Dichte des Musters, mit dem die erste Schicht des Supports gedruckt wird, kann getrennt von der Dichte des restlichen Supports eingestellt werden. Mit dieser Einstellung wird der Abstand zwischen zwei benachbarten Linien konfiguriert, an denen der Support auf der Bauplatte aufliegt.

<!--screenshot {
"image_path": "support_initial_layer_line_distance.png",
"models": [{"script": "umbrella_square_rounded.scad"}],
"camera_position": [0, 64, 125],
"settings": {
    "support_enable": true,
    "support_initial_layer_line_distance": 1.333
},
"layer": 160,
"colours": 64
}-->
![Das Muster der ersten Schicht ist doppelt so dicht wie der Rest des Supports](../../../articles/images/support_initial_layer_line_distance.png)

Diese Einstellung ist nützlich, um die Haftung zwischen Support und Bauplatte zu verbessern. Wenn Sie das Stützmuster in der ersten Schicht dichter machen, wird die Kontaktfläche zwischen dem Support und der Bauplatte vergrößert, so dass es besser haftet. Die nachfolgenden Schichten können dann auf ein Material gelegt werden, auf dem sie besser haften.

Da sich diese Einstellung nur auf die erste Schicht auswirkt, hat sie keinen wesentlichen Einfluss auf die Festigkeit des Supports oder die Zeit- und Materialkosten. Sie hat auch keinen Einfluss auf die Qualität der Überhänge. Um die Dichte des Supports in der Nähe der Überhänge anzupassen, sehen Sie sich die Einstellung [Linienabstand der Dachstruktur](support_roof_line_distance.md) an.

Es ist ratsam, diese Einstellung auf ein Vielfaches des Linienabstands des Hauptkörpers des Supports festzulegen. Auf diese Weise stimmen die Linien des Supports mit den Linien der ersten Schicht überein, so dass sie auf der ersten Schicht aufliegen und nicht in der Luft schweben.