Minimale hellingshoek traptreden supportstructuur
====
Met deze instelling kunt u de traptreden aan de onderkant van de support uitschakelen totdat de helling van het model een bepaalde hoek bereikt.

<!--screenshot {
"image_path": "support_bottom_stair_step_min_slope_10.png",
"modellen": [{"script": "standing_ring.scad"}],
"camerapositie": [0, 82, 10],
"camera_lookat": [0, 0, 10],
"instellingen": {
    "support_enable": waar,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_min_slope": 10
},
"laag": 250,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_bottom_stair_step_min_slope_30.png",
"modellen": [{"script": "standing_ring.scad"}],
"camerapositie": [0, 82, 10],
"camera_lookat": [0, 0, 10],
"instellingen": {
    "support_enable": waar,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_min_slope": 30
},
"laag": 250,
"kleuren": 64
}-->
![Traptreden uitgeschakeld totdat de helling 10° is](../../../articles/images/support_bottom_stair_step_min_slope_10.png)
![Traptreden uitgeschakeld totdat de helling 30° is](../../../articles/images/support_bottom_stair_step_min_slope_30.png)

Op niet zo steile hellingen kunnen de treden aan de onderkant erg breed zijn. Ze kunnen nooit breder zijn dan de [Maximale breedte traptreden supportstructuur](support_bottom_stair_step_width.md), maar omdat deze afstand van alle kanten wordt aangehouden, kunnen de traptreden zo breed worden dat de support een aanzienlijke afstand moet overspannen. Als er een kleine vallei is waar de kolom rust, kan dit er zelfs toe leiden dat de hele onderkant overslaat en de hele kolom alleen op de hoeken van de traptreden rust.

Voor deze gevallen kunt u de traptreden beperken tot de steilere hellingen. Deze instelling bepaalt wat een "steile" helling in dit opzicht is.

Als u deze instelling verhoogt, zal Cura voorkomen dat de traptreden worden gegenereerd op vlakke oppervlakken. Dit maakt de support stabieler maar moeilijker te verwijderen. Uw support zal meer littekens op het oppervlak achterlaten. Door de instelling te verlagen, is de support gemakkelijker te verwijderen en blijft er een mooiere afwerking achter waar de support rust, maar in sommige gevallen kan dit ertoe leiden dat de support lange afstanden moet afleggen of zelfs volledig in de lucht lijkt te hangen.

Om een ​​mooie afwerking te krijgen, kunt u deze instelling het beste op een conservatieve, lage hoek van 5° of 10° laten staan. Als de support op een vlak maar niet geheel vlak oppervlak rust, moet u de laag controleren en de hoek vergroten als u merkt dat de support er erg onstabiel uitziet.