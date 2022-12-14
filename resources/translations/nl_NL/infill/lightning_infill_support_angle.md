Hoek supportstructuur bliksemvulling
====
Het Bliksemvulling-patroon is alleen bedoeld om van binnenuit te helpen printen. Deze instelling bepaalt de maximale hoek van de overhang, niet alleen van de oppervlakken die het ondersupportt, maar ook binnen de vulling zelf. Als u deze instelling verlaagt, wordt er meer vulling gecreëerd. Als u deze instelling verhoogt, neemt de hoeveelheid vulling af.

Het patroon onderssteund de bovenkant van de print van binnenuit, maar alleen de bovenkant, die aanzienlijk meer overhangt dan deze hoek. Het patroon heeft ook eindpunten die onder een bepaalde hoek uitsteken om een ​​vertakkende boomstructuur te creëren, en de zijkanten van deze vertakkende structuur hebben een binnenhoek om verder in bepaalde gebieden te reiken. Deze drie aspecten van de overhang kunnen ook afzonderlijk worden geregeld met de instellingen [Hoek overhang bliksemvulling](lightning_infill_overhang_angle.md), [Snoeihoek bliksemvulling](lightning_infill_prune_angle.md) en [Rechtbuighoek bliksemvulling](lightning_infill_straightening_angle.md).

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
"image_path": "lightning_infill_support_angle_60.png",
"modellen": [{"script": "half_sphere.scad"}],
"camerapositie": [130, 87, 47],
"instellingen": {
    "infill_pattern": "bliksem",
    "wall_line_count": 0,
    "top_lagen": 0,
    "lightning_infill_support_angle": 60
},
"kleuren": 64
}-->
![Bij een kleine overhanghoek is veel support nodig](../../../articles/images/lightning_infill_support_angle_30.png)
![Steile overhangen zijn toegestaan ​​met een hoge overhanghoek](../../../articles/images/lightning_infill_support_angle_60.png)

Als u deze instelling verhoogt, is er aanzienlijk minder materiaal nodig en wordt de printtijd verkort. Dit leidt echter ook tot vervorming. Deze vervorming zit aan de binnenkant van het model en is dus niet direct zichtbaar. Als de [Dikte Bovenkant](../top_bottom/top_thickness.md) echter onvoldoende is, kan [Pillowing](../troubleshooting/pillowing.md) optreden. Omdat de binnenhoeken in het paneel ook meer mogen overhangen, is het waarschijnlijk dat het paneel hoger op de wanden zal beginnen.