Lijnrichting supportvloer
====
De supportvloer wordt meestal zo loodrecht mogelijk georiënteerd op de support erboven en het model eronder. Als de uitlijning van de bovenvlaklijnen of de supportlijnen is aangepast, is het raadzaam om ook de uitlijning van de supportvloerlijnen aan te passen. Met deze instelling kunt u de uitlijning van de supportgrondlijnen aanpassen.

<!--screenshot {
"image_path": "support_interface_angles_0.png",
"modellen": [
    {
        "script": "plug.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 36, 92],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_interface_pattern": "lijnen",
    "support_interface_angles": [0, 90]
},
"laag": 118,
"kleuren": 128
}-->
<!--screenshot {
"image_path": "support_interface_angles_45.png",
"modellen": [
    {
        "script": "plug.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 36, 92],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_interface_pattern": "lijnen",
    "support_interface_angles": [45, 135]
},
"laag": 118,
"kleuren": 128
}-->
![Zowel het dak als de vloer zijn hellend op 0° en 90°](../../../articles/images/support_interface_angles_0.png)
![Zowel het dak als de vloer hellen onder 45° en 135°](../../../articles/images/support_interface_angles_45.png)

Voor deze instelling kunnen meerdere hoeken, gescheiden door komma's, worden ingevoerd. Cura wisselt van hoek in lagen.

De supportgrondlijnen zijn ideaal uitgelijnd zodat ze loodrecht staan ​​op de modellijnen waarop ze rusten en de supportlijnen die erop rusten. Wanneer ze loodrecht georiënteerd zijn, wordt de afstand die deze lijnen moeten overspannen kleiner, waardoor de doorbuiging wordt verminderd en de supportstabiliteit wordt verbeterd.