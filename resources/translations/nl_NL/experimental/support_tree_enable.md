Boom supporttructuur
====
De boomsupportstructuur biedt een alternatieve benadering om het model te ondersteunen in vergelijking met de traditionele supporttechniek. Boomsupport creëert een vertakkende structuur die begint op de platvorm met een kleine basis, maar groeit naar de delen die support nodig hebben.

<!--screenshot {
"image_path": "support_structure_tree.png",
"modellen": [{"script": "duct.scad"}],
"camerapositie": [56, 127, 60],
"instellingen": {
    "support_enable": waar,
    "support_structure": "boom",
    "support_tree_collision_resolution": 0.05
},
"kleuren": 32
}-->
![Een boomachtige structuur ondersteund de overhang](../../../articles/images/support_structure_tree.png)

De boomsupportstructuur kan obstakels vermijden als ze naar de overhangende gebieden groeien. Waar mogelijk zal de boom vanaf de platvorm omhoog groeien om het oppervlak waarop de support rust niet te beschadigen. Als dit niet mogelijk is, zal de boom op het oppervlak van het model rusten, zo dicht mogelijk bij de overhang om verspilling van tijd en materiaal te minimaliseren. De takken van de support van de boom worden beperkt door de [Tree Support Branch Angle](../support/support_tree_angle.md) zodat ze niet te steil overhangen. Dit beperkt het vermogen om rond obstakels te groeien en bepaalt ook de hoogte waarop takken beginnen te vertakken.

De boomsupportstructuur is standaard hol. De normale supportinstellingen zijn echter nog steeds van toepassing op het gebied dat wordt omsloten door de takken van de boom. In het bijzonder kan de [Support Density](../support/support_infill_rate.md) worden gebruikt om meer structurele stijfheid aan de support toe te voegen. Omdat de supportstructuur van de boom inherent kronkelig is, heeft deze gewoonlijk voldoende sterkte voor zijn doel.

De boomdraagconstructie biedt een aantal voordelen ten opzichte van de normale draagconstructie, om er een paar te noemen:
* Voor een boomdraagconstructie is over het algemeen veel minder materiaal nodig dan voor een reguliere draagconstructie. Doorgaans wordt tussen 25% en 50% van het materiaalverbruik bespaard. Dit bespaart veel tijd en materiaalkosten.
* Wanneer geprint met hetzelfde materiaal als de print, ziet de overhang er meestal beter uit bij gebruik van de boomdraagstructuur.
* De boomdraagconstructie is makkelijker te verwijderen dan een normale draagconstructie.
* De supportstructuur voor bomen laat minder littekens achter op het oppervlak dan normale support, omdat deze rond het model naar de platvorm kan reiken.

Dit heeft echter ook enkele nadelen:
* De boomsupportstructuur kost veel meer tijd om te snijden. Geduld is vereist, vooral bij grote modellen.
* Er zijn veel stromingsonderbrekingen bij het printen van de kleinste takken, waardoor de boomdraagstructuur ongeschikt is voor het printen van moeilijk te extruderen materialen, zoals PVA of flexibele materialen.
* De structuur van de boomsupport is niet erg goed voor het ondersupporten van sommige mechanische modellen. In het bijzonder heeft hij de neiging om te weinig takken te plaatsen om vlakke, hellende overstekken te ondersupporten.

Hoewel de boomsupportstructuur tegelijk met de normale support kan worden geactiveerd, is dit over het algemeen niet wenselijk. De twee soorten support overlappen elkaar en resulteren in overexpansie.