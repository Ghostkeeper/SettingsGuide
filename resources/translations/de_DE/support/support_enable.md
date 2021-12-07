Stützstruktur generieren
====
3D-FFF Drucker arbeiten, indem sie einen Strang aus geschmolzenem Kunststoff an den richtigen Stellen platzieren. Wenn dieser Kunststoff nicht gestützt wird, sackt er nach unten, weil er mit erheblicher Kraft und aufgrund der Schwerkraft aus der Düse gedrückt wird. Wenn das Modell nicht darunter liegt, um die neue Schicht zu stützen, muss sie durch eine zusätzliche Support-Struktur gestützt werden, die nach dem Drucken des Modells entfernt und entsorgt wird.

Diese Einstellung ermöglicht das Erstellen von Support-Strukturen, um das Objekt zu stützen, während es gedruckt wird. Cura aktiviert diesen Support nicht standardmäßig, aber es markiert die Oberfläche des Modells rot, wenn es denkt, dass das Material dort stark durchhängen könnte, wenn der Support nicht aktiviert ist.

<!--screenshot {
"image_path": "support_enable_prepare_mode.png",
"models": [{"script": "pipe_corner.scad"}],
"camera_position": [77, 197, 40],
"layer": -1
}-->
<!--screenshot {
"image_path": "support_enable.png",
"models": [{"script": "pipe_corner.scad"}],
"camera_position": [77, 197, 40],
"settings": {"support_enable": true},
"colours": 64
}-->
![Rote Markierung des Modells, wo Support erforderlich ist](../../../articles/images/support_enable_prepare_mode.png)
![Support-Struktur (in Cyan) zum Stützen des Modells während des Druckens](../../../articles/images/support_enable.png)

Das Drucken von Support erfordert einen erheblichen Zeit- und Materialaufwand. An den Stellen, an denen der Support das Modell berührt, muss er später, nachdem der Druckvorgang abgeschlossen ist, abgebrochen oder abgeschnitten werden. Dies hinterlässt in der Regel eine Narbe auf der Oberfläche.

Manchmal ist der Support jedoch absolut notwendig. Wenn das Modell zum Beispiel ein Stück hat, das nach unten zur Bauplatte zeigt, würde dieses Stück sonst einfach in der Luft hängen.

Design zur Vermeidung von Support
----

Auch wenn es manchmal notwendig ist, sollte das Drucken von Support nach Möglichkeit vermieden werden. Es gibt zahlreiche Techniken, um zu verhindern, dass Support gedruckt werden muss. Dies ist ein wichtiger Teil des Modelldesigns für den 3D-Druck. Im Folgenden finden Sie einige Techniken, mit denen Sie Ihr 3D-Modell so verändern können, dass kein Support erforderlich ist.
* Richten Sie Ihr Modell so aus, dass es keine flachen Oberflächen gibt, die höher als die Bauplatte sind.
* Vermeiden Sie so weit wie möglich die Konstruktion von Überhängen.
* Wenn sich eine Fläche direkt über der Bauplatte befindet, ziehen Sie sie nach unten auf die Bauplatte.
* Kleine Vorsprünge können mit einem 45-Grad-Winkel unterstützt werden, indem der Überhang in das Modell übertragen wird.
* Größere Überhänge können überbrückt werden, wenn sie auf beiden Seiten gestützt werden. Cura wird die Linien der Unterseite des Überhangs automatisch so ausrichten, dass sie in einer geraden Linie über die Brücke laufen. Während des Druckens dieser Linien hält die Düse die Spannung auf dem Streifen aufrecht, so dass er nicht herunterhängt. So hat er genug Zeit, um sich zu verfestigen, so dass er sich selbständig halten kann.
* Wenn es eine Lücke im Überhang gibt, kann eine sogenannte Opferbrücke eingeplant werden. Dabei handelt es sich um eine Schicht, in der die Lücke geschlossen wird. Dies ermöglicht eine gute Überbrückung, so dass die zweite Schicht die richtigen Wände der Lücke darüber aufbauen kann. Nach dem Drucken kann der Spalt mit einem Messer geöffnet werden, da er nur eine Schicht dick ist.