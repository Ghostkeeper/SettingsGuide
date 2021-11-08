Horizontalloch-Erweiterung
====
Dies ist eine Korrekturmaßnahme für einen Druckeffekt, bei dem Löcher tendenziell kleiner gedruckt werden als beabsichtigt. Mit dieser Einstellung können Sie die Größe der vertikalen Löcher in Ihrem Druck vergrößern. Ähnlich wie bei der Einstellung [Horizontale Erweiterung](xy_offset.md) werden die Löcher im Druck in alle Richtungen erweitert.

<!--screenshot {
"image_path": "hole_xy_offset_0.png",
"models": [{"script": "rotary_tumbler_motor_lid.scad"}],
"camera_position": [-30, 30, 111],
"settings": {"hole_xy_offset": 0},
"colours": 64
}-->
<!--screenshot {
"image_path": "hole_xy_offset.png",
"models": [{"script": "rotary_tumbler_motor_lid.scad"}],
"camera_position": [-30, 30, 111],
"settings": {"hole_xy_offset": 0.8},
"colours": 64
}-->
![Die Löcher in diesem Druck müssen für Schrauben und Achsen passen, sie sind aber zu klein gedruckt](../../../articles/images/hole_xy_offset_0.png)
![Die Löcher wurden vergrößert, der Rest der Form wurde nicht verändert.](../../../articles/images/hole_xy_offset.png)

Aufgrund der Viskosität des Materials neigt der Kunststoff beim Drucken einer Linie in einer Kurve dazu, mit der Düse in der Kurve mitgezogen zu werden. Dadurch wird die Kurve etwas kleiner als beabsichtigt, da das Material in das Innere der Kurve gezogen wird. Normalerweise ist dies nicht wirklich sichtbar, aber beim Drucken von Gegenständen, die sehr genau passen müssen, oder beim Drucken von Gegenständen mit sehr kleinen vertikalen Löchern wird dies für die Genauigkeit Ihres Drucks zum Verhängnis. Die Schrauben passen nicht mehr, die Teile gleiten nicht mehr sauber ineinander, und so weiter.

Diese Einstellung kompensiert dies, indem sie alle Löcher etwas größer macht. Im Gegensatz zur [Horizontale Erweiterung](xy_offset.md) betrifft dies jedoch nur geschlossene Löcher. Wenn es auch nur eine winzige Öffnung auf einer Seite gibt (horizontal, auf der gleichen Schicht), dann wird dieser Teil nicht als Loch gewertet und ist von dieser Einstellung nicht betroffen.

Ein positiver Wert macht die Löcher größer. Ein negativer Wert macht die Löcher kleiner. In Kombination mit der horizontalen Erweiterung werden die Löcher zuerst vergrößert, bevor die normale horizontale Erweiterung angewendet wird. Dies kann dazu führen, dass dünne Teile vollständig verschwinden, bevor sie durch die normale horizontale Erweiterung vergrößert werden.