Uitsparing strijken
====
Normaal gesproken maakt strijken niet glad tot naar de buitenrand. Als dit het geval zou zijn, zou de continue druk in de nozzlekamer ervoor zorgen dat het materiaal over de rand vloeit, waardoor een soort rimpeleffect ontstaat. Deze instelling bepaalt hoe ver van de rand wordt gestreken.

<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"modellen": [
    {
        "script": "dial_brace.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 14, 83],
"instellingen": {
    "laaghoogte": 0.2,
    "ironing_enabled": true
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "ironing_inset.png",
"modellen": [
    {
        "script": "dial_brace.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 14, 83],
"instellingen": {
    "laaghoogte": 0.2,
    "strijken_enabled": waar,
    "strijkinzet": 1.2
},
"kleuren": 64
}-->
![Standaard gebruik van halve lijndikte](../../../articles/images/ironing_enabled_enabled.png)
![Een grotere inzet van 1,2 mm](../../../articles/images/ironing_inset.png)

Er zijn twee belangrijke gebruiksscenario's voor deze instelling:
* Om ervoor te zorgen dat het materiaal zich niet over de rand verspreidt.
* Als een manier om dunne strepen uit te filteren die normaal gesproken zouden worden gladgestreken. Als u een vlakke helling heeft, wilt u misschien niet dat elke laagstap in die helling wordt afgevlakt. Het verhogen van deze instelling kan de dunste strepen wegfilteren, maar heeft ook tot gevolg dat de grotere delen niet tot aan de rand worden gladgestreken.