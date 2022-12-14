Strijken inschakelen
====
Gladmaken zorgt ervoor dat de printer nog een keer over de bovenkant gaat om het extra glad te maken. Deze extra stap heeft een zeer kleine lijnbreedte en print bijzonder langzaam.

<!--screenshot {
"image_path": "ironing_enabled_disabled.png",
"modellen": [
    {
        "script": "dial_brace.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 14, 83],
"instellingen": {
    "laaghoogte": 0.2,
    "ironing_enabled": false
},
"kleuren": 64
}-->
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
![Een normale print van bovenaf gezien](../../../articles/images/ironing_enabled_disabled.png)
![Let op de dunne lijnen bovenaan wanneer vloeiend maken is ingeschakeld..](../../../articles/images/ironing_enabled_enabled.png)


Strijken print een lijnenpatroon af op de bovenkant van de print. Dit heeft twee belangrijke positieve effecten:
* Het smelt het oppervlak opnieuw door er meerdere keren met een hete nozzle overheen te gaan. Vandaar de naam "strijken". Omdat de verplaatsingssnelheid zo laag is en de lijnbreedte zo klein is, verwarmt de nozzle het oppervlak veel. Het platte deel van nozzle maakt ze vervolgens glad.
* Het vult de gaten in het oppervlak. De beweging vindt plaats op hetzelfde niveau als de laag zelf, de flux is minder dan die van een volledige laag, maar is er nog steeds. In theorie kan de doorvoer nergens heen, maar in de praktijk handhaaft het de druk in de nozzlekamer. Telkens wanneer nozzle over een hobbel in het oppervlak gaat, doorvoert het materiaal in nozzle in die opening.

Strijken heeft echter ook enkele nadelen:
* Het verhoogt de printtijd aanzienlijk.
* Als het patroon breuken heeft (omdat het naar verschillende delen moet), laat het een zichtbare lijn achter tussen het deel dat eerder is gladgestreken en het deel dat daarna is gladgestreken. Dit kan soms worden vermeden door [Strijkpatroon](ironing_pattern.md) op een ander patroon in te stellen, b.v. Concentrisch.
* Afgeschuinde oppervlakken of oppervlakken met veel detail kunnen ook worden gladgemaakt, waardoor het topografische effect wordt vergroot. De grenzen tussen de lagen worden duidelijker. Dit kan worden voorkomen door [Alleen hoogste laag strijken](ironing_only_highest_layer.md) in te schakelen.