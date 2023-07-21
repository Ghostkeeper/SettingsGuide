Samenvoegafstand Supportstructuur
====
Dunne supports zijn over het algemeen niet gewenst. Ze hebben de neiging om te kantelen, wat de print kan verpesten. Wanneer meerdere supportstukken naast elkaar worden geplaatst, kunnen ze aan elkaar worden gekoppeld en vormen dan één stuk support dat veel stabieler is.

<!--screenshot {
"image_path": "support_join_distance_low.png",
"modellen": [{"script": "clamp.scad"}],
"camerapositie": [-8, 150, 75],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_join_distance": 0.1
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_join_distance_high.png",
"modellen": [{"script": "clamp.scad"}],
"camerapositie": [-8, 150, 75],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_join_distance": 2
},
"kleuren": 64
}-->
![Twee delen van de support liggen dicht bij elkaar](../../../articles/images/support_join_distance_low.png)
![Als er voldoende afstand is, worden ze samengevoegd.](../../../articles/images/support_join_distance_high.png)

Door supportdelen aan elkaar te zetten, wordt de support stabieler en betrouwbaarder. Dit vermindert ook de printtijd, afhankelijk van het patroon. Bij veel patronen moet een extra wand worden geprint rond de hele of een deel van de omtrek, en het samenvoegen van twee supportstukken vermindert die omtrek.

Als deze instelling te veel wordt verhoogd, kunnen supportdelen die erg ver uit elkaar liggen, met elkaar worden verbonden. Dit kan de printtijd en het materiaalverbruik verhogen.