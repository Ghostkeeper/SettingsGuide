Hoek van takken van boomsupportsstructuur
====
Deze instelling definieert de maximale overhanghoek die de takken van de boomsupport mogen hebben. Door de hoek te vergroten, kunnen de takken meer horizontaal worden geprint, waardoor ze verder kunnen reiken.

<!--screenshot {
"image_path": "support_tree_angle_20.png",
"modellen": [{"script": "over_t.scad"}],
"camerapositie": [-23, 124, 45],
"instellingen": {
    "support_enable": waar,
    "support_structure": "boom",
    "support_tree_collision_resolution": 0.02,
    "support_tree_angle": 20
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_tree_angle_40.png",
"modellen": [{"script": "over_t.scad"}],
"camerapositie": [-23, 124, 45],
"instellingen": {
    "support_enable": waar,
    "support_structure": "boom",
    "support_tree_collision_resolution": 0.02,
    "support_tree_angle": 40
},
"kleuren": 64
}-->
![Een aftakhoek van 20°](../../../articles/images/support_tree_angle_20.png)
![Een aftakhoek van 40°](../../../articles/images/support_tree_angle_40.png)

Door de vertakkingshoek te verkleinen, worden de takken meer verticaal. Naarmate het toeneemt, worden ze meer horizontaal. Omdat de takken een grotere overhanghoek mogen hebben, kunnen ze verder rond obstakels reiken, waardoor de support vaker op de platvorm kan rusten in plaats van op het model. Bovendien kunnen de takken op een later tijdstip van elkaar scheiden.

De belangrijkste effecten van het vergroten van de vertakkingshoek voor boomsupport zijn onder meer:
* Minder littekens omdat er minder support is om op het model te rusten en niet op de platvorm. Als [Plaatsing Supportstructuur](../support/support_type.md) is ingesteld op "Bed Touch", kan een groter deel van het model worden ondersteund.
* Verminderde printtijd en materiaalverbruik omdat de knopen zich op grotere hoogte afsplitsen. De takken worden net op tijd afgesplitst om de hele overhang te bereiken.
* Lagere betrouwbaarheid. Als de overhanghoek te groot wordt, wordt de support ernstig verzwakt, waardoor de kans groter wordt dat de support breekt of omvalt.

Grote vertakkingshoeken kunnen het beste worden gecombineerd met lage waarden voor de instelling [Resolutie bij botsingen van de boomsupportstructuur](support_tree_collision_resolution.md). Dit vermindert de positieverschuivingen van de boom als gevolg van het vermijden van botsingen. Dit voorkomt dat de overhangafstand te groot wordt wanneer de botsafstand wordt aangepast.