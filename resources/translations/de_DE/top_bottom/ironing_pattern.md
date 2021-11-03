Glättungsmuster
====
Beim Glätten wird die Oberseite mit einem Muster versehen. Diese Einstellung legt fest, welches Muster zum Glätten der Oberseite verwendet wird.

Das Ziel des Musters ist es, eine glatte, durchgehende Oberfläche zu schaffen. Wenn das Muster unterbrochen wird, entsteht ein sichtbarer Rand auf der Oberfläche. Es sind zwei Muster verfügbar.
<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true
},
"colours": 64
}-->
Zigzag
----
![Zigzag Glättungsmuster](../../../articles/images/ironing_enabled_enabled.png)

Dadurch wird die Düse über die Oberfläche hin- und herbewegt. Das funktioniert bei den meisten Oberflächen gut und zuverlässig, verursacht aber etwas mehr Ränder als nötig.

<!--screenshot {
"image_path": "ironing_pattern.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true,
    "ironing_pattern": "concentric"
},
"colours": 64
}-->
Konzentrisch
----
![Konzentrisches Glättungsmuster](../../../articles/images/ironing_pattern.png)

Dadurch erzeugt die Düse Kreise von innen nach außen. Dadurch werden die Ränder auf ein Minimum reduziert, wenn aber die konzentrischen Ringe in der Mitte sehr klein werden, wird sich die Qualität verschlechtern, weil die Düse zu lange an der gleichen Stelle verweilt. Dies hinterlässt einen sichtbaren Makel auf der Oberfläche. Daher funktioniert dies am besten bei langen und dünnen Flächen und nicht bei Flächen, die ebenso breit wie hoch sind.