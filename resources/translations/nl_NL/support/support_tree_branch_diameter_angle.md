Hoek van Takdiameter van boomsupportsstructuur
====
De takken van de boomsupport zijn aan de onderkant breder dan aan de bovenkant. Dit houdt de takken stabiel, hoe hoog de support ook wordt. Met deze instelling kunt u de intensiteit regelen waarmee de support zich verspreidt.

<!--screenshot {
"image_path": "support_tree_branch_diameter_1_4mm_5.png",
"modellen": [{"script": "lantaarn.scad"}],
"camera_positie": [0, 70, 13],
"instellingen": {
    "support_enable": waar,
    "support_structure": "boom",
    "support_tree_branch_diameter": 1.4,
    "support_tree_branch_diameter_angle": 5
},
"structuren": ["helpers"],
"kleuren": 16
}-->
<!--screenshot {
"image_path": "support_tree_branch_diameter_angle_10.png",
"modellen": [{"script": "lantaarn.scad"}],
"camera_positie": [0, 70, 13],
"instellingen": {
    "support_enable": waar,
    "support_structure": "boom",
    "support_tree_branch_diameter": 1.4,
    "support_tree_branch_diameter_angle": 10
},
"structuren": ["helpers"],
"kleuren": 16
}-->
![De vorm van een tak met een diameterhoek van 5°](../../../articles/images/support_tree_branch_diameter_1_4mm_5.png)
![De vorm van een tak met een diameterhoek van 10°](../../../articles/images/support_tree_branch_diameter_angle_10.png)

Hoe groter de hoek, hoe breder de onderkant van de boomsupport zal zijn, vooral bij hoge modellen. Dit heeft verschillende implicaties:
* De bredere onderkant zorgt ervoor dat de support minder snel omvalt. Dit verhoogt de betrouwbaarheid van de boomsupport.
* De bredere onderkant vereist meer materiaal en tijd om te printen.
* De supporthoek is additief aan de maximale [Hoek van takken van boomsupportstructuur](support_tree_angle.md) waarbij de takken kunnen overhangen, dus zeer hoge waarden kunnen ertoe leiden dat de boomsupport in sommige gevallen ook minder stabiel is.
* De bredere takken kunnen moeilijker door het raster navigeren, waardoor het moeilijker is om sommige delen van de overhang vanaf de platvorm te bereiken. Als gevolg hiervan moet de support mogelijk op het model rusten in plaats van op de platvorm, waardoor littekens toenemen.
* Het vermijden van botsingen met bomen is moeilijker te berekenen voor Cura, wat resulteert in een langere snijtijd. Dit kan worden tegengegaan door de instelling [Resolutie bij botsingen van de boomsupportstructuur](support_tree_collision_resolution.md) te verhogen, maar dit vermindert ook de structurele integriteit van de boomsupport.

Over het algemeen moet de hoek zo worden gekozen dat de boomsupport net breed genoeg is om zichzelf op elke hoogte te ondersupporten zonder te wiebelig te worden.