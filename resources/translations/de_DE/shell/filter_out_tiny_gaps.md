Kleine Lücken ausfiltern
====
Das Füllen von Lücken zwischen Wänden führt zu zusätzlichen Fahrwegen. Wenn die Lücken extrem klein sind, hat das Material normalerweise nicht genug Zeit, um ausreichend aus der Düse zu fließen. Wenn diese Einstellung aktiviert ist, macht sich der Drucker nicht die Mühe, einige der kleinsten Lücken zu füllen.
<!--screenshot {
"image_path": "filter_out_tiny_gaps_disabled.png",
"models": [
    {
        "script": "gear_hollow.scad",
        "scad_params": ["radius=10", "teeth_depth=1.5", "teeth=50"]
    }
],
"settings": {"filter_out_tiny_gaps": false},
"camera_position": [0, 0, 80],
"colours": 64
}-->
<!--screenshot {
"image_path": "filter_out_tiny_gaps_enabled.png",
"models": [
    {
        "script": "gear_hollow.scad",
        "scad_params": ["radius=10", "teeth_depth=1.5", "teeth=50"]
    }
],
"settings": {"filter_out_tiny_gaps": true},
"camera_position": [0, 0, 80],
"colours": 64
}-->
![Winzige Lücken an den Zahnspitzen werden gefüllt](../../../articles/images/filter_out_tiny_gaps_disabled.png)
![Winzige Lücken werden gefiltert, so dass sie nicht ausgefüllt werden.](../../../articles/images/filter_out_tiny_gaps_enabled.png)

Lücken, die kleiner als 2 quadratische Außenwandlinienbreiten sind, gelten als "kleine" Lücken. Wenn zum Beispiel Ihre [Breite der äußeren Wandlinien](../resolution/wall_line_width_0.md) Einstellung auf 0.4mm gesetzt ist, werden Lücken mit einer Fläche von 0.4mm * 0.4mm * 2 = 0.32mm^2 nicht mehr gefüllt.