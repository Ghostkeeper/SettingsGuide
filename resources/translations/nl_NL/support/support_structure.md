Supportstructuur
====
Met deze instelling kunt u kiezen welk algoritme u wilt gebruiken voor het construeren van de draagconstructie. Deze constructies hebben heel verschillende eigenschappen, dus de keuze van een algoritme heeft grote invloed op hoe goed je print wordt onderteund. Er zijn twee opties beschikbaar.

<!--screenshot {
"image_path": "support_type_everywhere.png",
"modellen": [{"script": "duct.scad"}],
"camerapositie": [56, 127, 60],
"instellingen": {
    "support_enable": waar,
    "support_type": "overal"
},
"kleuren": 32
}-->
Normale supportstructuur
----
![Normale supportstructuur](../../../articles/images/support_type_everywhere.png)

Dit is de traditionele supportstructuur die de meeste mensen gewend zijn. De structuur wordt onder de overhangen gemaakt en is meestal gevuld met een patroon dat de overshang direct ondersteund. Van daaruit valt het recht naar beneden totdat het de platform bereikt of een deel van het model dat het ondersteund.

Normale supportconstructie is de standaard geweest voor het grootste deel van de geschiedenis van 3D-printen en werkt op dezelfde manier in alle slicers. Dit is de gouden standaard, en niet zonder reden:
* Door zijn stabiele structuur met grote contactvlakken op het model en het platform is hij zeer betrouwbaar. Het kompenseerd heel goed slechte instellingen of een slecht afgestelde printer.
* Omdat de vorm eenvoudig is, kan deze snel worden gesneden.
* De rechte supportstructuur is eenvoudig aan te passen door de gebruiker, omdat direct duidelijk is welke randen worden ondersteund en welke niet.

De belangrijkste nadelen vloeien voort uit dezelfde kenmerken:
* Door de grote contactoppervlakken is de support vaak moeilijk te verwijderen en kan het aanzienlijke littekens achterlaten op het aangeraakte oppervlak.
* Hoewel het stabiel is, kan het veel materiaal verbruiken en kan het lang duren om printen. Dit kan tot op zekere hoogte worden tegengegaan door [Overhang Printbaar Maken](../experimental/conical_overhang_enabled.md) te gebruiken.

Aangezien de support meestal groot en breed is, is een [Patroon Supportstructuur](support_pattern.md) nodig om het oppervlak goed te ondersteunen. De zigzagvulling kan worden gebruikt om het grootste deel van de support van een enkele lijn printen en voor eenvoudiger verwijderen. Andere patronen kunnen worden gecombineerd met een extra [Aantal wandlijnen supportstructuur](support_wall_count.md) om de support extra stabiel te maken.

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
Boom ondersteunde structuur
----
![boom ondersupportende structuur](../../../articles/images/support_structure_tree.png)

Met boomsupport begint de supportstructuur klein op de platformen groeit vervolgens naar de delen van de print die support nodig hebben.

De boomsupportsstructuur kan obstakels vermijden als deze naar de overhangende gebieden groeit, omdat de supportstructuur niet recht naar beneden hoeft te vallen. Waar mogelijk zal de support alleen op de platform rusten om beschadiging van het oppervlak waarop de support rust te voorkomen. Als er geen pad is van de platform naar de overhang, zal de support op een oppervlak zo dicht mogelijk bij de overhang rusten om het materiaalverbruik te minimaliseren. De takken van de support van de boom worden beperkt door de [Hoek van takken van boomsupportstructuur](support_tree_angle.md) zodat ze niet te steil overhangen. Dit beperkt het vermogen om rond obstakels te groeien en bepaalt ook de hoogte waarop stammen beginnen te vertakken.

De boomdraagconstructie heeft een aantal grote voordelen ten opzichte van de normale draagconstructie:
* De boomdraagconstructie verbruikt vaak veel minder materiaal dan de normale draagconstructie. Tussen 25% en 50% van het materiaalverbruik is gebruikelijk. Dit bespaart veel tijd en verlaagt de printkosten.
* Door het kleine contactoppervlak ziet de overhang er vaak beter uit bij gebruik van de boomdraagstructuur.
* Door het kleine contactoppervlak is de support ook makkelijker te verwijderen.
* Het laat minder littekens achter op het oppervlak dan normale support, omdat het vanaf de platformrond het model naar de overhang kan grijpen.

De belangrijkste nadelen zijn echter:
* Slicen duurt aanzienlijk langer dan normale support. Geduld is vereist, vooral bij grote modellen.
* Er zijn veel stromingsonderbrekingen wanneer de kleinste takken worden geprint, waardoor de boomdraagstructuur ongeschikt is voor het printen van moeilijk te extruderen materialen, zoals PVA of flexibele materialen.
* De boomsupportsstructuur is niet goed geschikt om sommige mechanische modellen te ondersteunen. In het bijzonder heeft hij de neiging om te weinig takken te plaatsen om vlakke, hellende overstekken te ondersteunen.

De boomsupportsstructuur is standaard hol. De knopen hebben een kleine punt, dus een opvulpatroon biedt geen extra support voor het overhangende oppervlak van het geprinte object. Door zijn gekartelde vorm is de boomsupport meestal vrij stabiel. De normale supportsinstellingen zijn echter nog steeds van toepassing op het gebied dat wordt omsloten door de takken van de boom. De [Dichtheid Supportstructuur](support_infill_rate.md) kan worden gebruikt om meer structurele sterkte aan de support toe te voegen.