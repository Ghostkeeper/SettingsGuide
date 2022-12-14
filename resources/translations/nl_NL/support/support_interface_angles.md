Lijnrichting interface Supportstructuur
====
De supportstructuur is typisch zo loodrecht mogelijk op het model en het omringende supportlichaam georiënteerd. Als de oriëntatie van de boven-/onderlijnen of de supportlijnen is aangepast, is het raadzaam om ook de oriëntatie van de supportstructuurlijnen aan te passen. Met deze instelling kunt u de richting van de supportstructuurlijnen aanpassen.

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
![Hoeken op 0° en 90°](../../../articles/images/support_interface_angles_0.png)
![Gehoekt op 45° en 135°](../../../articles/images/support_interface_angles_45.png)

Voor deze instelling kunnen meerdere hoeken, gescheiden door komma's, worden ingevoerd. Cura zal deze hoeken tussen de lagen afwisselen.

De supportstructuurlijnen zijn ideaal uitgelijnd zodat ze loodrecht staan ​​op de lijnen waarop ze rusten en de lijnen waarop ze rusten. Door ze loodrecht uit te lijnen, verkleint u de afstand die deze lijnen moeten overbruggen, waardoor de doorbuiging wordt verminderd en de kwaliteit van de overhangen wordt verbeterd. Dit is vooral van belang wanneer de support niet helemaal gesloten is.