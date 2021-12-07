Brücken-Außenhautfluss
====
Mit dieser Einstellung wird die Materialmenge eingestellt, die extrudiert wird, um die Unterseiten der Brücken zu drucken.

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
<!--screenshot {
"image_path": "bridge_skin_material_flow_50.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 50,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![Bei 100 % Fluss werden die Linien mit ihrer normalen Linienbreite gezeichnet](../../../articles/images/bridge_skin_density_100.png)
![Bei 50 % Fluss werden die Linien dünner gemacht](../../../articles/images/bridge_skin_material_flow_50.png)

Durch die Verringerung der Materialmenge wird die Leinenbreite auf der Unterseite, die einen Spalt überbrückt, effektiv verringert. Bei verringerter Linienbreite ist das Verhältnis von Oberfläche zu Masse der Linien größer, so dass sie schneller abkühlen können und nicht so stark durchhängen.

Eine zu starke Verringerung der Fließgeschwindigkeit führt jedoch zu einer starken Veränderung der Fließgeschwindigkeit, insbesondere in Verbindung mit einer [langsameren Druckgeschwindigkeit](bridge_skin_speed.md). In der Realität kann das Material seine Fließgeschwindigkeit nicht sehr schnell ändern, was dazu führt, dass die Linien etwas dicker als beabsichtigt sind, wenn die Fließgeschwindigkeit verlangsamt wird, und etwas dünner als beabsichtigt, wenn die Fließgeschwindigkeit beschleunigt wird.