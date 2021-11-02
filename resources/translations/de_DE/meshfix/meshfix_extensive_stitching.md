Extensives Stitching
====
Cura muss wissen, wo sich das Innere des Modells befindet, um es mit Material füllen zu können. Wenn die Oberfläche Ihres Modells nicht vollständig geschlossen ist oder Innenwände hat, kann es unklar sein, wo sich das Innere des Modells befindet.

Ein häufiger Fall, in dem das Modell nicht vollständig ist, ist, wenn ein zusätzliches Stück des Modells an ein ansonsten geschlossenes Teil angefügt wird. Dies geschieht häufig bei der Bearbeitung von Netzen mit CAD-Software, die nicht für die Fertigung (sondern nur für das digitale Rendering) entwickelt wurde, wie z. B. Blender oder SketchUp. Ein Beispiel dafür sehen Sie in den folgenden Bildern.

<!--screenshot {
"image_path": "meshfix_extensive_stitching_xray.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_disabled.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"settings": {
    "meshfix_extensive_stitching": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_enabled.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"settings": {
    "meshfix_extensive_stitching": true
},
"colours": 32
}-->
![Die Röntgenaufnahme zeigt eine zusätzliche Oberfläche auf der Innenseite](../../../articles/images/meshfix_extensive_stitching_xray.png)
![Wenn diese Einstellung ausgeschaltet ist, wird nur der vollständig geschlossene Objekt gedruckt.](../../../articles/images/meshfix_extensive_stitching_disabled.png)
![Wenn diese Einstellung aktiviert ist, wird das zusätzliche Stück entsprechend hinzugefügt.](../../../articles/images/meshfix_extensive_stitching_enabled.png)

Diese Einstellung bewirkt, dass Cura versucht, Lücken im Netz besser zu schließen, wenn es nicht vollständig geschlossen ist. Dies erhöht die Chancen auf einen guten Druck, verlängert aber die Slicing-Zeit und kann manchmal falsche Oberflächen miteinander verbinden.