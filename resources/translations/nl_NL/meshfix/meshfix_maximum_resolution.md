Maximale resolutie
====
Hoewel invoer met een hoge resolutie op het eerste gezicht misschien beter lijkt, kan de printer vaak niet goed overweg met G-code met hoge resolutie. Daarom zal Cura de resolutie van de invoer tijdens het slicen verminderen. Deze instelling bepaalt de resolutie die Cura maximaal houdt.

<!--screenshot {
"image_path": "meshfix_maximum_resolution_0.05.png",
"modellen": [{"script": "cilinder.scad"}],
"camerapositie": [40, -20, 116],
"instellingen": {
    "meshfix_maximum_resolution": 0.05
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "meshfix_maximum_resolution_1.png",
"modellen": [{"script": "cilinder.scad"}],
"camerapositie": [40, -20, 116],
"instellingen": {
    "meshfix_maximum_resolution": 4,
    "meshfix_maximum_deviation": 0,5
},
"kleuren": 64
}-->
![Voordat de resolutie wordt verlaagd](../../../articles/images/meshfix_maximum_resolution_0.05.png)
![Na het verlagen van de resolutie (ad extremum)](../../../articles/images/meshfix_maximum_resolution_1.png)

De printer moet de G-code verwerken terwijl deze draait. Als de G-code veel kleine lijnsegmenten bevat, kan de printkop zo snel door de beweging racen dat de processor van de 3D-printer het niet kan bijhouden. Dit zorgt ervoor dat de printkop sporadisch vertraagt, zodat de CPU de achterstand kan inhalen of gewoon wacht op het volgende bewegingscommando. Dit zorgt ervoor dat het oppervlak erg ruw wordt of zelfs kleine klodders krijgt omdat de doorvoer van de sproeikop niet perfect overeenkomt met de sporadische beweging van de sproeier. Soms resulteert een lagere resolutie in een betere printkwaliteit.

Deze instelling specificeert een minimale lengte voor de lijnsegmenten. Lijnsegmenten die korter zijn dan de opgegeven lengte komen in aanmerking voor verbinding met andere lijnsegmenten. Ze worden vervolgens samengevoegd wanneer het nieuwe pad niet meer dan [Maximale afwijking](meshfix_maximum_deviation.md) afwijkt van het oorspronkelijke pad.

Houd er rekening mee dat niet gegarandeerd dezelfde hoekpunten uit elke laag worden verwijderd als de hoekpunten overeenkomen. Resolutiereductie wordt in 2D uitgevoerd door hoekpunten van de vormen van de laag te verwijderen, niet in 3D door hoekpunten van de mesh te verwijderen. Als de resolutie te veel wordt verlaagd, resulteert dit vaak in een onregelmatig oppervlak in plaats van een gekarteld oppervlak.

Het wordt aanbevolen om de resolutie van het model voldoende te verlagen zodat de printkop niet significant vertraagt, zodat de CPU de achterstand kan inhalen. Als de resolutie niet voldoende wordt verlaagd, wordt het oppervlak ruw omdat de printkop langzamer gaat werken terwijl de extrusie doorgaat. Als de resolutie te veel wordt verlaagd, wordt het oppervlak ook ruw omdat de wanden niet overal precies op elkaar liggen.