Horizontale Erweiterung erste Schicht
====
Diese Einstellung erweitert nur die erste Schicht, die auf der Bauplatte (oder auf dem Floß) aufliegt. Ähnlich wie bei [Horizontale Erweiterung](xy_offset.md) erweitert ein positiver Wert die erste Schicht, während ein negativer Wert die erste Schicht verringert.

<!--screenshot {
"image_path": "xy_offset_layer_0_original.png",
"models": [
    {
        "script": "d1.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"settings": {"xy_offset_layer_0": 0},
"colours": 16
}-->
<!--screenshot {
"image_path": "xy_offset_layer_0_enabled.png",
"models": [
    {
        "script": "d1.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"settings": {"xy_offset_layer_0": -0.6},
"colours": 16
}-->
![Das originale Modell](../../../articles/images/xy_offset_layer_0_original.png)
![Die erste Schicht wird verkleinert.](../../../articles/images/xy_offset_layer_0_enabled.png)

Die erste Schicht wird häufig auf einer beheizten Bauplatte gedruckt, wodurch sie in einem leicht flüssigen Zustand gehalten wird, um die Haftung auf der Bauplatte zu verbessern. Die erste Schicht ist normalerweise auch viel dicker als die übrigen Schichten. So bleibt genügend Zeit und Material, damit die Schicht seitlich absinken kann, wodurch das Phänomen des "Elefantenfußes" entsteht, bei dem die Unterseite des Drucks eine etwas breitere Kante aufweist. Mit dieser Einstellung kann der Elefantenfuß kompensiert werden, indem die erste Schicht von vornherein dünner gemacht wird. Geben Sie dieser Einstellung einen kleinen negativen Wert, um den Elefantenfuß zu kompensieren.

Sie können diese Einstellung auch mit einem hohen Wert versehen, um einen Pseudorand um Ihren Druck zu erzeugen, der mit anderen Haftungstechniken wie dem Raft kombiniert werden kann. Denken Sie daran, dass sich dadurch auch die Außenhaut ausdehnt, so dass sich unter den Wänden der zweiten Schicht Außenhaut befindet.

**Die Kombination dieser Einstellung mit einem brim ist unwirksam, da der Brim ohnehin einen großen Rand um die erste Schicht erzeugt.**