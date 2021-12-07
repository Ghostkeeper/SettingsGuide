Stützstruktur Füllschichtdicke
====
Da die optische Qualität und Auflösung des Supports nicht wichtig ist, können Sie dickere Schichten für den Support verwenden, um die Druckzeit zu verkürzen. Mit dieser Einstellung legen Sie fest, wie dick die Schichten sein sollen, mit denen der Support gedruckt wird.

In der Schichtansicht sieht es so aus, als ob die Support-Linien viel breiter geworden sind. Wenn sie tatsächlich gedruckt werden, fallen die Support-Linien weiter nach unten, anstatt sich horizontal auszubreiten.

<!--screenshot {
"image_path": "support_infill_sparse_thickness.png",
"models": [
    {
        "script": "calendar_holder.scad",
        "transformation": ["scale(0.5)", "rotateX(90)"]
    }
],
"camera_position": [18, 43, 19],
"settings": {
    "support_enable": true,
    "support_infill_sparse_thickness": 0.24
},
"layer": 148,
"colours": 64
}-->
![Die Dicke der Support-Füllung ist auf das Dreifache der Schichthöhe eingestellt.](../../../articles/images/support_infill_sparse_thickness.png)

Die Dicke der Support-Füllung muss ein Vielfaches der Höhe der normalen Schicht sein. Ist dies nicht der Fall, wird sie auf die nächsthöhere Schicht gerundet.

Diese Einstellung gilt nicht für das Dach oder den Boden des Supports, sondern nur für die Hauptstruktur.

Diese Einstellung ist besonders nützlich, wenn der Support mit einem anderen Material als der Rest des Drucks gedruckt wird, und noch mehr, wenn dieses Material schwer zu extrudieren ist, wie z. B. PVA. Da der Support nicht in jeder Schicht extrudiert wird, muss der Drucker nicht so oft den Extruder wechseln, was viel Zeit spart. Da mehr Material auf die gedruckten Schichten extrudiert wird, werden Materialien, die eine gewisse Zeit brauchen, um den Fluss in Gang zu setzen, zuverlässiger gedruckt.

Seien Sie vorsichtig, diesen Wert nicht zu sehr zu erhöhen. Beim Wechsel zum und vom Support muss die Durchflussrate durch die Düse deutlich beschleunigt und verlangsamt werden. Dies geschieht mit einer gewissen Verzögerung, so dass zu Beginn des Supports zu wenig und nach Ende des Supports zu viel extrudiert wird.