Conische supportstructuur inschakelen
====
Wanneer deze instelling is ingeschakeld, staat de draagconstructie aan de zijkanten niet meer volledig verticaal. De support krijgt een conische vorm die naar beneden toe kleiner of groter wordt.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"modellen": [
    {
        "script": "wide_overhang.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [91, -95, 19],
"instellingen": {
    "support_enable": waar,
    "support_conical_enabled": waar,
    "support_conical_angle": 30
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_neg10.png",
"modellen": [
    {
        "script": "wide_overhang.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [91, -95, 19],
"instellingen": {
    "support_enable": waar,
    "support_conical_enabled": waar,
    "support_conical_angle": -10
},
"kleuren": 64
}-->
![De support wordt naar beneden toe kleiner](../../../articles/images/support_conical_enabled.png)
![support neemt toe naar beneden](../../../articles/images/support_conical_angle_neg10.png)

De support zelf kantelt in een bepaalde [Hoek Conische Supportstructuur](support_conical_angle.md). Bij negatieve hoeken wordt de support naar beneden toe groter, wat de support beduidend stabieler maakt. Bij positieve hoeken wordt het naar beneden toe kleiner. Dit bespaart veel materiaal en printtijd. Om te voorkomen dat de support instabiel wordt, kan er ook een [Minimale Breedte Conische Supportstructuur](support_conical_min_width.md) voor de support worden gedefinieerd.

De conische support is de belangrijkste parameter in de afweging tussen printtijd en supportsstabiliteit. Er zijn twee belangrijke use-cases voor conische support:
* Besparing van materiaal en printtijd. Met een conische support bespaart u gemakkelijk de helft van het materiaal dat nodig is voor de support en dus de helft van de tijd die nodig is om te printen. Dit is vooral handig bij grote hoeveelheden support voor grote en hoge printen.
* Gebruik een negatieve hoek om de support stabieler te maken. Als je print kleine high-top elementen bevat die support nodig hebben, resulteert dit meestal in zeer hoge [Pijlers Gebruiken](../support/support_use_towers.md) die gemakkelijk kunnen omvallen tijdens het printen. Met de conische support kunnen deze hoge, dunne draagconstructies aan de onderkant breder gemaakt worden. Dit geeft ze extra stabiliteit. Het printen van deze dragers duurt echter langer omdat er meer materiaal nodig is.

Als de [Plaatsing Supportstructuur](../support/support_type.md) is ingesteld om de support alleen op de platvorm te plaatsen, maakt de conische support het mogelijk om het model te omhelzen om het model ook te ondersupporten op plaatsen die andere delen van het model bedekken. De support rust nog steeds alleen op de platvorm, maar kan door zijn vorm nu ook de overhangende delen in de hoeken bereiken die anders niet ondersupportd zouden worden.

Deze functie is een iets eenvoudigere en minder extreme versie van de<!--if cura_version >= 4.7-->[Tree Support](../support/support_structure.md)<!--endif--><!--if cura_version < 4.7:[Tree Support](../experimental/support_tree_enable.md)-->. Boomsupportsstructuur heeft veel van dezelfde voordelen als conische support. De boomsupportsstructuur gebruikt echter een heel ander algoritme en geeft meer vrijheid in het ontwerp van de support, terwijl de conische support meer het algoritme volgt dat wordt gebruikt om de gewone support te genereren. Dit betekent dat de normale supportsinstellingen de neiging hebben om beter te werken bij gebruik met de conische support, maar ze moeten aanzienlijk worden aangepast voor de boomsupportsstructuur.