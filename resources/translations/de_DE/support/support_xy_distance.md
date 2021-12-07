X/Y-Abstand der Stützstruktur
====
Sie gibt an, wie groß der horizontale Abstand zwischen dem Support und dem Modell sein muss.

<!--screenshot {
"image_path": "support_xy_distance.png",
"models": [{"script": "clamp.scad"}],
"camera_position": [-8, 185, 42],
"settings": {
    "support_enable": true,
    "support_xy_overrides_z": true,
    "support_xy_distance": 2
},
"colours": 64
}-->
![Eine horizontale Lücke zwischen dem Support und dem Modell](../../../articles/images/support_xy_distance.png)

Der horizontale Abstand soll verhindern, dass der Support gegen das Modell stößt und dort eine Narbe auf der Oberfläche hinterlässt. Allerdings entsteht dadurch auch ein größerer Abstand zwischen dem Modell und der Support-Struktur an der Stelle des Überhangs, so dass kleinere Überhänge nicht unterstützt werden.

X/Y gegenüber Z-Abstand
----
Sowohl der X/Y-Abstand als auch der Z-Abstand sollten genau eingehalten werden, nicht mehr und nicht weniger. Dies ist eine Beschränkung, so dass es eine Präferenz zwischen den beiden geben muss. Dies wird durch die Einstellung [Abstandspriorität der Stützstruktur](support_xy_overrides_z.md) angezeigt. Diese Einstellung ändert das Verhalten der Einstellung X/Y-Abstand der Stützstruktur.

![X/Y hat Vorrang vor Z](../../../articles/images/support_xy_overrides_z.svg)

Wenn X/Y Vorrang vor Z hat, wird der X/Y-Abstand beibehalten, auch wenn dies bedeutet, dass der Z-Abstand zu groß ist. Der Z-Abstand wird weiterhin als Minimum gehalten.

![Z hat Vorrang vor X/Y](../../../articles/images/support_z_overrides_xy.svg)

Wenn Z Vorrang vor X/Y hat, wird der Z-Abstand eingehalten, auch wenn dies bedeutet, dass der X/Y-Abstand zu klein ist. Der X/Y-Abstand hat nur einen Einfluss von der Oberseite des Supports weg, wo der Z-Abstand wiederum keinen Einfluss hat.