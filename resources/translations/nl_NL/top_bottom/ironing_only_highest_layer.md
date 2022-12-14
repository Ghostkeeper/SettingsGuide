Alleen hoogste laag strijken
====
Als deze instelling is ingeschakeld, wordt strijken alleen toegepast op de bovenste laag van het object. Als uw model veel verschillende bovenvlakken heeft, maar alleen de bovenste zichtbaar is of alleen de bovenste moet worden gladgemaakt, kan deze instelling u veel printtijd besparen.

<!--screenshot {
"image_path": "ironing_only_highest_layer.png",
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
    "ironing_only_highest_layer": true
},
"kleuren": 64
}-->
![De halve cirkel in de onderste laag is niet gladgestreken.](../../../articles/images/ironing_only_highest_layer.png)

**Als er meerdere objecten in een print zijn, wordt de bovenste laag van elk object gestreken. Dit geldt ook voor alle onderdelen van een multi-extrusie print.**