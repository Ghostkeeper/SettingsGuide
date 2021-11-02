Brim Einzugsturm
====
Der Einzugsturm Brim ist ein zusätzlicher Brim, ähnlich der Brim-Option in der Einstellung [Druckplattenhaftungstyp](../platform_adhesion/adhesion_type.md). Diese Umrandung kann getrennt von der normalen Haftung aktiviert und deaktiviert werden. Wenn sie aktiviert ist, wird ein zusätzlicher Rand um den Einzugsturm gedruckt. Bei diesem Rand handelt es sich um eine flache Schicht um den Einzugsturm, die die Haftung des Einzugsturm auf der Bauplatte verbessert.

<!--screenshot {
"image_path": "prime_tower_brim_enable.png",
"models": [
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 0
        }
    },
    {
        "script": "cube.scad",
        "object_settings": {
            "extruder_nr": 1
        },
        "transformation": ["translateX(40)"]
    }
],
"camera_position": [50, -32, 133],
"camera_lookat": [93, -122, 5],
"settings": {
    "prime_tower_enable": true,
    "prime_tower_brim_enable": true,
    "prime_tower_position_x": 600,
    "prime_tower_position_y": 600,
    "adhesion_type": "skirt"
},
"colours": 16
}-->
![Die Haftung ist auf "skirt" eingestellt, aber es gibt immer noch einen Rand um den Einzugsturm](../../../articles/images/prime_tower_brim_enable.png)

Durch das Aktivieren des Einzugsturm-Brim erhält der Einzugsturm mehr Oberfläche, um sich mit der Bauplatte zu verbinden. Da der Einzugsturm ziemlich hoch und schlank werden kann, kann er bei sehr hohen Drucken umkippen. Der Einzugsturm-Brim soll dies verhindern, was allerdings einen geringen Aufwand an Druckzeit, Material und Platz auf der Bauplatte bedeutet.

Der Einzugsturm erhält die Breite, die in der Einstellung [Breite des Brim-Elements](../platform_adhesion/brim_width.md) definiert ist. Wenn der "Druckplattenhaftungstyp" auf "Brim" eingestellt ist, verdoppelt diese Einstellung effektiv die Breite des Randes um den Einzugsturm.

Der Rand des Einzugsturm kann nicht mit einem "Raft" kombiniert werden.