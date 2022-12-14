Strijkpatroon
====
Bij het gladstrijken krijgt de bovenkant een patroon. Deze instelling bepaalt welk patroon wordt gebruikt om de bovenkant glad te maken.

Het doel van het patroon is om een ​​glad, doorlopend oppervlak te creëren. Wanneer het patroon wordt verbroken, verschijnt er een zichtbare rand op het oppervlak. Er zijn twee patronen beschikbaar.
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
Zigzag
----
![Zigzag gladmakend patroon](../../../articles/images/ironing_enabled_enabled.png)

Hierdoor beweegt de nozzle heen en weer over het oppervlak. Dit werkt goed en betrouwbaar op de meeste oppervlakken, maar veroorzaakt iets meer randjes dan nodig is.

<!--screenshot {
"image_path": "strijkpatroon.png",
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
    "ironing_pattern": "concentrisch"
},
"kleuren": 64
}-->
Concentrisch
----
![Concentrisch gladstrijkpatroon](../../../articles/images/ironing_pattern.png)

Dit zorgt ervoor dat nozzle cirkels van binnenuit creëert. Dit houdt de randjes tot een minimum beperkt, maar als de concentrische ringen in het midden erg klein worden, gaat de kwaliteit achteruit omdat de nozzle te lang op dezelfde plek blijft. Dit laat een zichtbare vlek op het oppervlak achter. Daarom werkt dit het beste op lange en dunne oppervlakken in plaats van oppervlakken die even breed als hoog zijn.