Horizontale Uitbreiding
====
Deze instelling zorgt ervoor dat het hele model iets breder of smaller wordt. Dit is een compenserende maatregel voor maatonnauwkeurigheden in het printproces.

<!--screenshot {
"image_path": "xy_offset_neutral.png",
"modellen": [{"script": "flipper_grip.scad"}],
"camerapositie": [62, -91, 176],
"instellingen": {"xy_offset": 0},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "xy_offset_wider.png",
"modellen": [{"script": "flipper_grip.scad"}],
"camerapositie": [62, -91, 176],
"instellingen": {"xy_offset": 1},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "xy_offset_slimmer.png",
"modellen": [{"script": "flipper_grip.scad"}],
"camerapositie": [62, -91, 176],
"instellingen": {"xy_offset": -1},
"kleuren": 32
}-->
![Het originele model](../../../articles/images/xy_offset_neutral.png)
![Horizontaal uitgevouwen, de schroefgaten zijn nu kleiner](../../../articles/images/xy_offset_wider.png)
![Een negatieve waarde verkleint het model en maakt de schroefgaten groter.](../../../articles/images/xy_offset_slimmer.png)

Een positieve waarde maakt de print vetter. Hierdoor worden de holtes kleiner. Een negatieve waarde maakt de print slanker en vergroot de holtes.

Als de tolerantie van een print belangrijk is, kan deze instelling erg handig zijn. Door een lichte vervorming van kunststoffen is het mogelijk dat de werkelijke afmetingen van de print niet volledig overeenkomen met de afmetingen van het digitale model. Versterkingsfouten kunnen worden gecompenseerd door het model eenvoudig op de platform te schalen met de schaaltool, maar offsetfouten als gevolg van het printproces kunnen met deze instelling worden gecompenseerd.

Als je weet dat je printer altijd te breed print door over-extrusie of een onnauwkeurige beweging, dan kun je deze instelling ook gebruiken om dat te compenseren.