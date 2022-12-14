Extruder supportvloer
====
Als uw printer is uitgerust met meerdere extruders, kan de onderkant van de support, waar de support op het model rust, worden geprint met een andere extruder dan de bovenkant van de support, waar het model op de support rust. Met deze instelling kunt u kiezen welke extruder wordt gebruikt voor de supportvloer.

<!--screenshot {
"image_path": "support_bottom_extruder_nr.png",
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
    "support_bottom_extruder_nr": 2
},
"color_scheme": "materiaal_kleur",
"kleuren": 64
}-->
![De supportbodem is in rood geprint, de supportbovenkant in wit.](../../../articles/images/support_bottom_extruder_nr.png)

Sommige materialen bieden betere overhangeigenschappen dan andere materialen wanneer ze als support worden gebruikt. Ze kunnen bijvoorbeeld dichter bij het oppervlak worden geprint omdat ze niet chemisch aan het oppervlak hechten of omdat ze in water oplosbaar zijn. Dergelijke materialen zijn echter vaak duur en het printen duurt langer. Met deze instelling kunt u de supportbasis printen met een andere extruder. Dit kan een deel van het dure of langzaam printende materiaal besparen.

Voor de kwaliteit van de oversoverhang is de supportvloer minder belangrijk dan het supportdak. Als een duur materiaal spaarzaam moet worden gebruikt, is de ondergrond een goede kandidaat om met het goedkopere materiaal te printen.