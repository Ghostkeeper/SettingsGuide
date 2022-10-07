Mindestbreite konische Stützstruktur
====
Wenn die konische Unterstützung aktiviert ist und die Unterstützungsstruktur schrumpfen soll, bestimmt diese Einstellung die Mindestbreite, auf die die konische Unterstützung die Unterstützung schrumpfen lässt. Der Support wird nicht dünner, es sei denn, der Überhangbereich, der gestützt werden muss, ist bereits dünner.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_min_width_20.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30,
    "support_conical_min_width": 20
},
"colours": 64
}-->
![Eine Mindestbreite von 5 mm](../../../articles/images/support_conical_enabled.png)
![Eine Mindestbreite von 20 mm](../../../articles/images/support_conical_min_width_20.png)

Wenn ein großes Support-Volumen auf einem kleinen Support-Pfeiler ruht, ist dieser Support sehr kippanfällig. Eine Erhöhung der Mindestbreite vergrößert die Breite der Basissäule des Supports, an der sich der Kegel festhalten kann. Dies erhöht die Zuverlässigkeit des Drucks, kostet aber zusätzliches Material. Alles in allem wird der konische Support die Druckzeit weniger effektiv verkürzen.