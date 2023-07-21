Hoek overhang bliksemvulling
====
De Bliksem-infill ondersteund alleen de bovenkant van het model van binnenuit waar deze overhangt. Deze instelling bepaalt de hoek van de overhang die door de bliksem wordt ondersteund vanuit de binnenkant van het model.

<!--screenshot {
"image_path": "lightning_infill_support_angle_30.png",
"modellen": [{"script": "half_sphere.scad"}],
"camerapositie": [130, 87, 47],
"instellingen": {
    "infill_pattern": "bliksem",
    "wall_line_count": 0,
    "top_lagen": 0,
    "lightning_infill_support_angle": 30
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "lightning_infill_overhang_angle_70.png",
"modellen": [{"script": "half_sphere.scad"}],
"camerapositie": [130, 87, 47],
"instellingen": {
    "infill_pattern": "bliksem",
    "wall_line_count": 0,
    "top_lagen": 0,
    "lightning_infill_support_angle": 30,
    "lightning_infill_overhang_angle": 70
},
"kleuren": 64
}-->
![Overhang tot 30° wordt niet ondersteund](../../../articles/images/lightning_infill_support_angle_30.png)
![Tot 70° wordt niet ondersupportd, dus alleen het bovenste deel van de bol wordt ondersteund.](../../../articles/images/lightning_infill_overhang_angle_70.png)

Door de hoek te vergroten, wordt de geproduceerde hoeveelheid vulling verminderd. De top wordt minder ondersupport, tenzij het een zeer steile overhang is. Dit bespaart tijd en materiaal, maar kan er ook voor zorgen dat het blad op sommige plaatsen doorzakt. Het resultaat kan [Pillowing](../troubleshooting/pillowing.md) of een over het algemeen ruwer oppervlak zijn.

In tegenstelling tot de bovenliggende instelling [Hoek supportstructuur bliksemvulling](lightning_infill_support_angle.md) heeft deze instelling geen invloed op de overhang in het vulpatroon zelf.