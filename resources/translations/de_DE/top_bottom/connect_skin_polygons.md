Polygone oben/unten verbinden
====
Bei der Verwendung eines konzentrischen Oben/Unten-Musters (ein Muster, das aus geschlossenen Konturen besteht, auch bekannt als Polygone), verbinden Sie alle Konturen so miteinander, dass sie einen einzigen Pfad ergeben.

<!--screenshot {
"image_path": "connect_skin_polygons_original.png",
"models": [
    {
        "script": "web.scad",
        "scad_params": ["stakes=1", "line_width=4"]
    }
],
"camera_position": [10, 5, 111],
"settings": {
    "top_bottom_pattern": "concentric",
    "connect_skin_polygons": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "connect_skin_polygons_enabled.png",
"models": [
    {
        "script": "web.scad",
        "scad_params": ["stakes=1", "line_width=4"]
    }
],
"camera_position": [10, 5, 111],
"settings": {
    "top_bottom_pattern": "concentric",
    "connect_skin_polygons": true
},
"colours": 64
}-->
![Das konzentrische Muster erzeugt separate Konturen](../../../articles/images/connect_skin_polygons_original.png)
![Alle Konturen werden zu einer einzigen Kurve verbunden](../../../articles/images/connect_skin_polygons_enabled.png)

Dadurch werden Fahrwege größtenteils vermieden. Allerdings entstehen dadurch neue scharfe Ecken, in denen die Düse stark beschleunigen und abbremsen muss, was den Gewinn an Druckzeit wieder zunichte macht. Das verschnörkelte Muster wird auch auf der Außenseite sichtbar sein, was einen interessanten optischen Effekt ergibt.

Die durch [Linienanzahl der zusätzlichen Außenhaut](../../../articles/top_bottom/skin_outline_count.md) erzeugten Konturen sind nicht miteinander verbunden.