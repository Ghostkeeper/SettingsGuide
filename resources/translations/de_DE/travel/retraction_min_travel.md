Mindestbewegung für Einzug
====
Diese Einstellung verhindert, dass das Material bei sehr kurzen Fahrwegen eingezogen wird. Während dieser Fahrwege hat das Material ohnehin nur sehr wenig Zeit, um aus der Düse auszutreten, so dass ein Einziehen mehr schaden als nutzen würde.

<!--screenshot {
"image_path": "retraction_min_travel.png",
"models": [{"script": "spike_curve.scad"}],
"camera_position": [0, -31, 79],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_min_travel": 12},
"minimum_layer": 303,
"layer": 550,
"line": 337,
"colours": 64
}-->
![Beim kurzen Fahrweg in der Mitte wird nicht eingezogen.](../../../articles/images/retraction_min_travel.png)

Das Einziehen des Materials soll ein Stringing verhindern. Sehr kurze Fahrwege führen nicht zu Stringing, da das Material noch nicht aus der Düse fließen konnte. Bei extrem kurzen Fahrwegen von etwa einer Linienbreite überlagern sich die Linien sogar vollständig, so dass für ein Stringing kein Platz mehr ist. Beim Einziehen hingegen steht die Düse kurzzeitig still, während das Material in Bewegung ist. Dadurch kann etwas Material fließen und es entsteht ein Klecks. Aus diesen Gründen ist es besser, bei kurzen Strecken nicht einzuziehen, auch wenn sich diese Wege auf sichtbaren Teilen des Modells befinden.

Wenn Sie diese Einstellung zu sehr erhöhen, führt dies zu Stringing in detailreichen Teilen des Modells oder dort, wo Teile eng beieinander liegen.