Stufenweise Füllungsschritte Stützstruktur
====
Der stufenweise Support reduziert die Menge des verwendeten Support-Materials, indem er die Support-Dichte in den unteren Schichten verringert. Dies spart Druckzeit und Material, ohne die Qualität des Überhangs zu beeinträchtigen. Der Hauptzweck des Supports besteht darin, überhängende Bereiche zu stützen. Mit dieser Funktion wird der Support nur auf diesen Zweck ausgerichtet.

Diese Einstellung gibt an, in wie vielen Schritten die Support-Dichte reduziert wird. Bei jedem Schritt wird die Dichte des Supports halbiert. Bei einer Dichte von 20 % und zwei Stufen beträgt die Support-Dichte in den unteren Bereichen beispielsweise 10 % bzw. 5 %.

<!--screenshot {
"image_path": "gradual_support_infill_step_height_1mm.png",
"models": [
    {
        "script": "stair.scad",
        "transformation": ["rotateY(-90)", "scaleZ(0.5)"]
    }
],
"camera_position": [49, 91, -38],
"settings": {
    "support_enable": true,
    "support_pattern": "grid",
    "support_wall_count": 0,
    "support_infill_rate": 50,
    "gradual_support_infill_steps": 3,
    "gradual_support_infill_step_height": 1
},
"colours": 64
}-->
![Der Support wird in 3 Stufen auf eine geringere Dichte reduziert](../../../articles/images/gradual_support_infill_step_height_1mm.png)

Wenn Sie die Anzahl der Schritte erhöhen, wird die Dichte immer mehr halbiert, was zu einem Support mit geringerer Dichte führt. Das spart eine Menge Material und Druckzeit, macht den Support aber schwächer.

Ein Teil des Supports wird in der Luft schweben. In der Praxis wird sich dies jedoch bei den meisten Support-Mustern schnell von selbst beheben, da sich die Schichten selbst auf geschwächten unteren Schichten gut aufbauen können. Der Zweck der [Höhe in den stufenweisen Füllungsschritten der Stützstruktur](gradual_support_infill_step_height.md) ist es, den Schichten genügend Zeit zu geben, sich selbst zu reparieren, bevor die nächste stufenweise Füllung aufgetragen wird.

Diese Einstellung wird am besten mit mindestens einer [Anzahl der Wandlinien der Stützstruktur](support_wall_count.md) kombiniert. Dies gibt den Support-Linien etwas, an dem sie haften können, anstatt in der Luft zu schweben.