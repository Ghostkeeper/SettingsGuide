Mindestwandfluss
====
Durch die Kompensation von Überschneidungen in Wandlinien wird die Durchflussrate einiger Wände reduziert.Dies kann problematisch sein, da die Durchflussrate beliebig niedrig sein kann, bis zu 1 %, wenn sich die Wände fast vollständig überlappen. Das Drucken bei extrem niedrigen Durchflussraten funktioniert nicht gut. Er neigt dazu, ein Tropfenmuster zu erzeugen, anstatt kontinuierlich Linien zu extrudieren.

Mit dieser Einstellung werden diese Linien mit extrem niedriger Fließgeschwindigkeit zu Fahrwegen, indem ihre Fließgeschwindigkeit auf 0 % reduziert wird. Das Material wird immer noch wie bei normalen Fahrwegen austreten, aber es werden keine Tropfen entstehen.

<!--screenshot {
"image_path": "wall_min_flow_0.png",
"models": [
    {
        "script": "sprocket.scad",
        "transformation": ["scale(0.4)"]
    }
],
"camera_position": [0, 0, 50],
"settings": {
    "z_seam_type": "shortest",
    "wall_min_flow": 0
},
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"minimum_layer": 2,
"layer": 2,
"colours": 32
}-->
<!--screenshot {
"image_path": "wall_min_flow_50.png",
"models": [
    {
        "script": "sprocket.scad",
        "transformation": ["scale(0.4)"]
    }
],
"camera_position": [0, 0, 50],
"settings": {
    "z_seam_type": "shortest",
    "wall_min_flow": 50
},
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"minimum_layer": 2,
"layer": 2,
"colours": 32
}-->
![Überschneidungen zwischen Wänden werden normalerweise ausgeglichen](../../../articles/images/wall_min_flow_0.png)
![Wände mit weniger als 50% Extrusion werden in Fahrwege umgewandelt](../../../articles/images/wall_min_flow_50.png)

Die Düse wird weiterhin dem Verlauf der Wand folgen, um an der richtigen Stelle zu tropfen.

Wenn Sie diese Einstellung erhöhen, werden Ihre Wände dünner als gewünscht. Anstatt sehr dünne Linien zu zeichnen, zeichnen Sie gar nichts mehr. Technisch gesehen handelt es sich um Unterextrusion, d. h. Ihr Teil ist dünner als gewünscht. Allerdings wäre die Wand ohnehin nicht gut gedruckt worden. Anstatt eine lange Reihe von Punkten oder Tropfen quer über die Wand zu zeichnen, wird nichts gedruckt, wodurch die Wand etwas glatter wird.

Stellen Sie diese Einstellung auf den minimalen Wanddurchsatz ein, den Ihre Düse erreichen kann, ohne dass sich Tropfen bilden. Normalerweise liegt dieser Wert bei etwa 60 %. Wenn die Linienbreite unter 60 % sinkt, würden Tropfen entstehen, so dass es besser ist, diese Linien in Fahrwege umzuwandeln. Wenn Sie mit größeren Schichthöhen oder dickwandigeren Linien drucken, können Sie diese Einstellung möglicherweise etwas verringern, um eine höhere Maßgenauigkeit zu erzielen.