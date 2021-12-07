Winkel für Überhänge Stützstruktur
====
Der Überhangwinkel beeinflusst, wie viel Material nach unten abgelegt wird, um den Druck zu unterstützen. Der Winkel gibt den Mindestwinkel an, der unterstützt werden soll.

**Eine Verringerung des Wertes dieser Einstellung führt zu mehr Support.**

<!--screenshot {
"image_path": "support_angle_low.png",
"models": [{"script": "duct.scad"}],
"camera_position": [136, 10, 10],
"camera_lookat": [0, 10, 10],
"settings": {
    "support_enable": true,
    "support_join_distance": 0.1,
    "support_angle": 40
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_angle_high.png",
"models": [{"script": "duct.scad"}],
"camera_position": [136, 10, 10],
"camera_lookat": [0, 10, 10],
"settings": {
    "support_enable": true,
    "support_join_distance": 0.1,
    "support_angle": 75
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_angle_prepare_mode.png",
"models": [{"script": "duct.scad"}],
"camera_position": [113, 77, 0],
"layer": -1
}-->
![Ein niedriger Überhangwinkel erzeugt mehr Support](../../../articles/images/support_angle_low.png)
![Ein hoher Überhangwinkel erzeugt weniger Support](../../../articles/images/support_angle_high.png)
![Die unterstützten Bereiche sind in rot dargestellt](../../../articles/images/support_angle_prepare_mode.png)

Wenn Sie diese Einstellung verringern, unterstützt der Drucker einen größeren Teil des gedruckten Objekts, sogar Oberflächen, die steiler sind und während des Drucks nicht stark durchhängen. Wenn der Support Teile stützt, die nicht gestützt werden müssen, verlängert sich die Druckzeit und der Materialverbrauch unnötig und es entstehen Narben an den Stellen, an denen der Support den Druck berührt.

Eine Verringerung des Support-Winkels ist jedoch manchmal notwendig, um zu verhindern, dass das Material zu sehr durchhängt. Dies verbessert im Allgemeinen die Maßhaltigkeit des fertigen Teils und lässt auch die Überhänge besser aussehen.

Wenn Sie mit Support arbeiten, sollten Sie sich in der Vorschau ansehen, wie der Support aussehen wird. Dort können Sie sehen, wo der Support tatsächlich erzeugt wird. Die Anpassung dieser Einstellung ist dann eines der Werkzeuge, die Ihnen zur Verfügung stehen, um zu filtern, wo genau der Support erzeugt wird.