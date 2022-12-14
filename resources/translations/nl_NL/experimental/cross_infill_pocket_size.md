Luchtbelgrootte bij Kruis3D
====
Het cross 3D [Vulpatroon](../infill/infill_pattern.md) is gemaakt om flexibele prints mogelijk te maken. Het patroon bevat echter 4-weg kruisingen die erg rigide zijn. Deze instelling zorgt ervoor dat het patroon de kruisingen vermijdt om op bepaalde plaatsen niet te rigide te zijn. Het zorgt ervoor dat het patroon een luchtzak achterlaat in de kruising. Deze instelling bepaalt de maat van de bel.

<!--screenshot {
"image_path": "infill_pattern_cross_3d.png",
"modellen": [{"script": "hexagonal_prism.scad"}],
"camera_positie": [0, 0, 180],
"instellingen": {
    "top_lagen": 0,
    "infill_pattern": "cross_3d",
    "cross_infill_pocket_size": 2
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "cross_infill_pocket_size_0_5.png",
"modellen": [{"script": "hexagonal_prism.scad"}],
"camera_positie": [0, 0, 180],
"instellingen": {
    "top_lagen": 0,
    "infill_pattern": "cross_3d",
    "cross_infill_pocket_size": 0,5
},
"kleuren": 32
}-->
![De standaard belmaat van 2 mm](../../../articles/images/infill_pattern_cross_3d.png)
![Een belformaat van 0,5 mm](../../../articles/images/cross_infill_pocket_size_0_5.png)

Het patroon varieert de afstand rond de 4-weg kruising. Deze instelling bepaalt de grootte van de bel in de lagen wanneer de lijnen elkaar volledig raken. De maximale grootte van de bel wordt bepaald door de dichtheid van de vulling. De belkmaat wordt niet groter geprint dan de vierkantswortel van 2 keer de opvulafstand. Het invoeren van een grotere waarde heeft geen effect, maar kan nog steeds worden ingevoerd om grotere belformaten mogelijk te maken als de [Stappen Geleidelijke vulling](../infill/gradual_infill_steps.md) of [Dichtheid kruisvulling afbeelding](cross_infill_density_image.md ) is gebruikt.

Als u de waarde van deze instelling verhoogt, wordt de vulling verticaal zwakker en wordt de kracht gelijkmatiger verdeeld, wat resulteert in een meer gelijkmatige verdeling van de kracht.