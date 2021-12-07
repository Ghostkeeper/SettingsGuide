Dichte der Brücken-Außenhaut
====
Diese Einstellung steuert die Dichte der Unterseite des Drucks, wo er eine Lücke überbrückt. Bei einer Dichte von 100 % werden die Linien direkt nebeneinander platziert. Bei geringerer Dichte sind die Linien weiter voneinander entfernt.

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
"image_path": "bridge_skin_density_50.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 50,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![Bei einer Dichte von 100 % sind die Linien direkt nebeneinander angeordnet.](../../../articles/images/bridge_skin_density_100.png)
![Bei einer Dichte von 50 % ist ein gewisser Abstand zwischen den Linien vorhanden.](../../../articles/images/bridge_skin_density_50.png)

Bei dieser Einstellung spielen zwei wesentliche Effekte eine Rolle: Die Haftung zwischen den Linien und die Abkühlung.

Wenn Sie die Linien der Außenhaut direkt nebeneinander anordnen, haften sie aneinander. Dadurch sieht die Unterseite des überbrückten Spalts schöner aus, da die Oberfläche durchgängig ist und nicht wie ein Faden wirkt. Außerdem kann sich die zweite Linie beim Überbrücken etwas an die erste Linie anlehnen, wodurch die Brücke etwas weniger durchhängt.

Es gibt jedoch noch einen weiteren Effekt: die Abkühlung. Wenn die Leinen weiter voneinander entfernt sind, können sie schneller abkühlen und hängen dann auch nicht so stark durch. Dies gilt natürlich nur, wenn der Lüfter eingeschaltet ist; bei Materialien mit hohen Temperaturen wird diese Strategie also nicht funktionieren.

Welcher dieser Effekte stärker ist, hängt von der Viskosität des Materials ab, wie schnell es erstarrt und von der Lüftergeschwindigkeit. Eine gewisse Abstimmung ist immer erforderlich.

**Wenn die Einstellung [Brücken-Außenhautfluss](bridge_skin_material_flow.md) kleiner als 100% ist, gibt es auch bei einer Dichte von 100% einen gewissen Abstand zwischen den Linien, weil die Linien dann dünner sind.**