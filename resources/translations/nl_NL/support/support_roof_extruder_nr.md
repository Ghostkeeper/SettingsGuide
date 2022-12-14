Extruder supportdak
====
Als uw printer is uitgerust met meerdere extruders, kan de bovenkant van de support, waar het model op de support rust, worden geprint met een andere extruder dan de onderkant van de support, waar de support op het model rust. Met deze instelling kunt u kiezen welke extruder wordt gebruikt voor het supportdak.

<!--screenshot {
"image_path": "support_roof_extruder_nr.png",
"modellen": [
    {
        "script": "question_stick_clip.scad",
        "transformatie": ["roterenY(90)"],
        "object_settings": {"extruder_nr": 1}
    }
],
"camerapositie": [134, 134, 113],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_use_towers": false,
    "support_extruder_nr": 3,
    "support_roof_extruder_nr": 2
},
"color_scheme": "materiaal_kleur",
"kleuren": 64
}-->
![Het supportdak is in rood geprint, de supportbodem in wit.](../../../articles/images/support_roof_extruder_nr.png)

Sommige materialen hebben betere overhangeigenschappen dan andere materialen wanneer ze als support worden gebruikt. Ze kunnen bijvoorbeeld dichter bij het oppervlak worden geprint omdat ze niet chemisch aan het oppervlak hechten of omdat ze in water oplosbaar zijn. Dergelijke materialen zijn echter vaak duur en het printen duurt langer. Met deze instelling kunt u het supportdak printen met een andere extruder dan de supportvloer. Op deze manier wordt het dure of trage materiaal spaarzaam gebruikt, maar is het nog steeds in staat om goede ondersteuning te produceren.

Het supportdak is belangrijker voor de kwaliteit van de overhang dan de supportvloer. Daarom, als een duur materiaal spaarzaam moet worden gebruikt, is het het beste om het op zijn minst te gebruiken voor het supportdak.