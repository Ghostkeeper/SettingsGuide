Max. Stufenhöhe der Stützstruktur
====
Wenn die Einstellung [Platzierung Stützstruktur](support_type.md) auf "Überall" gesetzt ist, darf der Support auf dem Modell aufliegen. Sie folgt jedoch nicht exakt den Konturen des Modells. Stattdessen wird die Unterseite des Supports mit einem Treppenstufenmuster versehen. Auf diese Weise stellt die Stütze nur an wenigen Stellen eine Verbindung zum Modell her.

Diese Einstellung bestimmt die maximale Breite dieser Stufen. Normalerweise folgt die Breite der Stufe der Oberfläche des Modells mit einem vorgegebenen Wert von der [Stufenhöhe der Stützstruktur](support_bottom_stair_step_height.md). Wenn dies jedoch zu breit ist, wird die Breite auf die maximale Breite der Support-Treppenstufe begrenzt. Sie folgt dann für den Rest der Stufe der Oberfläche des Modells.

<!--screenshot {
"image_path": "support_bottom_stair_step_width.png",
"models": [{"script": "standing_ring.scad"}],
"camera_position": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"settings": {
    "support_enable": true,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_width": 0.7
},
"colours": 64
}-->
![Begrenzte Breite der Treppenstufen, so dass der Support dem Modell folgt](../../../articles/images/support_bottom_stair_step_width.png)

Diese Einstellung sollte normalerweise auf den maximalen Abstand eingestellt werden, der vom Material überbrückt werden kann, ohne die Stabilität der darüber liegenden Support-Linien zu beeinträchtigen. Eine niedrigere Einstellung bewirkt, dass der Support dem Modell häufiger folgt, was die Stabilität des Supports erhöht. Eine Erhöhung der Einstellung bewirkt, dass der Support den eingestellten Wert für die Höhe der Stütztreppe häufiger einhält, wodurch der Support leichter vom Modell entfernt werden kann.