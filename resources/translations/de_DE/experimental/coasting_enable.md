Coasting aktivieren
====
Wenn diese Einstellung aktiviert ist, hört die Düse kurz vor dem Schließen einer Wandkontur auf, Material zu extrudieren. Der Gedanke dahinter ist, dass sich die Düsenkammer dann auf dem letzten Stück der Linie entleeren kann, wodurch der Druck auf die Düse verringert wird und sie durch den Beginn der Kontur blockiert werden kann. Dies führt dann zu einer geringeren Naht am Beginn der Kontur und reduziert das Stringing in der nachfolgenden Fahrbewegung.

<!--screenshot {
"image_path": "coasting_enable.png",
"models": [{"script": "phone_holder.scad"}],
"camera_position": [0, -215, 117],
"minimum_layer": 1,
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
    "coasting_enable": true,
    "coasting_volume": 0.06
},
"colours": 32
}-->
![In der Schicht-Ansicht ist die Naht leicht zu erkennen, wenn Coasting aktiviert ist, weil es dann eine Fahrbewegung gibt](../../../articles/images/coasting_enable.png)

Die Aktivierung von Coasting soll die Sichtbarkeit der Naht in den Wänden verringern. Wenn Sie normalerweise große, dicke Nähte haben, kann die Aktivierung dieser Funktion diesen Effekt verringern. Es ist im Grunde das Gegenteil von dem, was der [Wipe-Abstand der Außenwand](../shell/wall_0_wipe_dist.md) tut, daher ist es eine gute Idee, zuerst zu versuchen, den Wipe zu reduzieren, bevor man Coasting ausprobiert.

Coasting führt theoretisch immer zu Unterextrusion. Ob dies beim Drucken sichtbar ist oder nicht, hängt von den jeweiligen Umständen ab. Coasting ist bei Druckern mit Direktantrieb in der Regel etwas effektiver. Wenn Ihr Drucker über einen Direktantrieb verfügt, sollten Sie das [Coasting-Volumen](coasting_volume.md) auf einen niedrigeren Wert setzen als bei der Verwendung von Bowdenzügen oder flexiblen Antriebswellen, da die Reaktion der Durchflussmenge dann viel schneller erfolgt. Bei Bowden-Fördersystemen ist es außerdem viel schwieriger, die Coasting-Menge so zu steuern, dass die Sichtbarkeit der Naht effektiv reduziert wird.