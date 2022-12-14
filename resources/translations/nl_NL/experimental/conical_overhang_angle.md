Maximale Modelhoek
====
Deze instelling configureert de overhanghoek (in graden) die wordt gegenereerd om [Overhang Printbaar Maken](conical_overhang_enabled.md). Het vergroten van deze hoek zorgt voor meer overhang, waardoor Cura het model minder hoeft te veranderen. Als je deze hoek verkleint, heeft het object nauwelijks overhang.

<!--screenshot {
"image_path": "conical_overhang_enabled_enabled.png",
"modellen": [{"script": "kasteel.scad"}],
"camerapositie": [0, 189, 25],
"instellingen": {
    "conical_overhang_enabled": waar,
    "conical_overhang_angle": 50
},
"kleuren": 8
}-->
<!--screenshot {
"image_path": "conical_overhang_angle_20.png",
"modellen": [{"script": "kasteel.scad"}],
"camerapositie": [0, 189, 25],
"instellingen": {
    "conical_overhang_enabled": waar,
    "conische_overhang_hoek": 20
},
"kleuren": 8
}-->
![Een maximale modelhoek van 50°](../../../articles/images/conical_overhang_enabled_enabled.png)
![Een maximale modelhoek van 20°](../../../articles/images/conical_overhang_angle_20.png)

In een hoek van 90° blijft het model zoals het was, met al zijn overhangen. Het model wordt niet gewijzigd. Bij een hoek van 0° worden alle hellingen volledig verticaal.

Door deze hoek te verkleinen, wordt de overhang van het model kleiner. Hierdoor is het model makkelijker printen. Het zakt niet meer zo veel door en het oppervlak aan de onderzijde wordt gladder. Het geprinte object komt dan echter niet meer exact overeen met het oorspronkelijke model. Het kost ook wat meer tijd en materiaal om het printen.

De hoek kan ook negatief zijn. Hierdoor wordt de hele print kegelvormig en heeft een brede basis. Dit kan tot interessante effecten leiden, maar heeft geen echt praktisch nut.