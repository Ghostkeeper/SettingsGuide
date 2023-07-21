Lijnrichting supportdak
====
Het supportdak wordt meestal zo loodrecht mogelijk georiënteerd op het model hierboven en het supportlichaam eronder. Als de uitlijning van de grondlijnen of de supportlijnen is aangepast, is het raadzaam om ook de uitlijning van de supportdaklijnen aan te passen. Met deze instelling kunt u de richting van de ondersupportende daklijnen aanpassen.

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
![Zowel het dak als de bodem zijn 0° en 90° gedraaid.](../../../articles/images/support_interface_angles_0.png)
![Zowel het dak als de vloer zijn 45° en 135° gedraaid.](../../../articles/images/support_interface_angles_45.png)

Voor deze instelling kunnen meerdere hoeken, gescheiden door komma's, worden ingevoerd. Cura zal deze hoeken afwisselend gebruiken in de lagen.

De supportdaklijnen zijn ideaal uitgelijnd zodat ze loodrecht staan op de supportlijnen waarop ze rusten en de modellijnen waarop ze rusten. Bij een loodrechte oriëntatie wordt de afstand die deze lijnen moeten overspannen kleiner, waardoor de doorbuiging wordt verminderd en de kwaliteit van de overhangen wordt verbeterd. Dit is vooral van belang wanneer de support niet helemaal gesloten is.