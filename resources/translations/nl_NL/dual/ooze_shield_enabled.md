Uitloopscherm Inschakelen
====
Bij het printen met meerdere extruders zit er soms nog wat materiaal in de inactieve extruders. Als de nozzles nog heet zijn, heeft dit materiaal de neiging naar buiten te sijpelen. Dit is het probleem dat uitloopscherm is ontworpen om te voorkomen. Het uitloopscherm is een rand rond het object die de afvoer onder de nozzle opvangt.

<!--screenshot {
"image_path": "ooze_shield.png",
"modellen": [
    {
        "script": "rocket_dual.scad",
        "scad_params": ["extruder=0"],
        "object_settings": {
            "extruder_no": 0
        },
        "transformatie": ["schaal(0.5)"]
    },
    {
        "script": "rocket_dual.scad",
        "scad_params": ["extruder=1"],
        "object_settings": {
            "extruder_no": 1
        },
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [-62, 102, 87],
"instellingen": {
    "ooze_shield_enabled": waar,
    "laaghoogte": 0.2,
    "line_width": 0.6
},
"color_scheme": "materiaal_kleur",
"kleuren": 64
}-->
![Het uitloopschermp wordt geprint met de eerste extruder van een laag, wat resulteert in een afwisselend patroon met twee extruders](../../../articles/images/ooze_shield.png)
![Sommige parameters kunnen worden aangepast voor het Uitloopscherm](../../../articles/images/ooze_shield.svg)

De lekbescherming print tot de hoogte van de hoogste extruderschakelaar. Boven deze hoogte wordt er geen nozzle in de print bewogen nadat deze in de standby-modus is geweest, dus het printen van een uitloopschermp is niet nodig. Het uitloopscherm wordt geprint met de extruder beginnend op een laag. Deze extruder wisselt elke laag af, wat een gevaar is bij het werken met twee verschillende materialen die niet goed aan elkaar plakken. Als het echter later wordt geprint, wanneer de andere extruder wordt geactiveerd, wordt het anti-sijpeleffect grotendeels vernietigd.

Het uitloopscherm is dun genoeg om gemakkelijk te breken of te snijden, en houdt afstand tot het model zodat deze kan worden verwijderd zonder de afwerking te beschadigen.