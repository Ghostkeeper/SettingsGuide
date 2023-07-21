Stapgrootte variatie adaptieve lagen
====
Wanneer de gewenste laaghoogte van een laag sterk afwijkt van die van een aangrenzende laag, zal er een groot verschil zijn in doorvoersnelheid vanaf de nozzle, wat kan leiden tot over- of onder-extrusie. Deze instelling zorgt ervoor dat het verschil in laaghoogte een geleidelijke verandering is om dit te voorkomen. Met deze instelling kunt u de maximale verandering in laaghoogte tussen twee aangrenzende lagen instellen.

<!--screenshot {
"image_path": "adaptive_layer_height_variation_step_0_05.png",
"modellen": [{"script": "barn.scad"}],
"camerapositie": [-108, -229, 118],
"instellingen": {
    "adaptive_layer_height_enabled": waar,
    "adaptive_layer_height_variation_step": 0.05,
    "layer_height": 0.2
},
"color_scheme": "laaghoogte",
"kleuren": 128
}-->
<!--screenshot {
"image_path": "adaptive_layer_height_enabled.png",
"modellen": [{"script": "barn.scad"}],
"camerapositie": [-108, -229, 118],
"instellingen": {
    "adaptive_layer_height_enabled": waar,
    "layer_height": 0.2
},
"color_scheme": "laaghoogte",
"kleuren": 128
}-->
![Een grote stapgrootte maakt zeer plotselinge laaghoogteveranderingen mogelijk](../../../articles/images/adaptive_layer_height_variation_step_0_05.png)
![Een kleine toename vereist een soepelere verandering in laaghoogte](../../../articles/images/adaptive_layer_height_enabled.png)

Als u deze instelling verlaagt, wordt de overgang van de laaghoogte geleidelijker. Dit heeft een aantal effecten op het printen:
* Er is minder over-extrusie bij overgang naar een lagere laaghoogte, omdat de doorvoer uit de nozzle tijd heeft om zich aan te passen aan een lagere doorvoersnelheid. Dit voorkomt vlekken op het oppervlak.
* Er is minder onder-extrusie bij de overgang naar een dikkere laaghoogte omdat de doorvoer uit de nozzle zich geleidelijk kan aanpassen aan een grotere doorvoersnelheid.
* De strepen zullen minder zichtbaar zijn. Terwijl gebieden met verschillende laaghoogtes nog steeds een verschillende textuur en kleur hebben, liggen deze gebieden nu verder uit elkaar, waardoor ze moeilijker te zien zijn.
* Het topografische effect komt terug op plaatsen in het model waar een scherpe hoek een plotselinge overgang naar dunnere lagen zou moeten veroorzaken. Dit komt omdat de laaghoogte niet zo snel kan worden aangepast, dus voor vlakke ondergronden moeten dikkere lagen worden gebruikt.
* Evenzo, als het model een scherpe hoek heeft die een plotselinge overgang naar dikkere lagen zou moeten veroorzaken: de printer maakt onnodig dunne lagen, waardoor de printtijd wordt verspild waar dit niet nodig is.

Door de implementatie van het matching slice-algoritme vindt de geleidelijke overgang naar een andere laaghoogte altijd *boven* de hoek in het model plaats die de overgang veroorzaakt.