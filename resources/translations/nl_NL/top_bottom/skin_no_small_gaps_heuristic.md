Geen skin in Z-gaten
====
Als uw model een kleine horizontale opening heeft die kleiner is dan de boven-/onderskindikte, zal deze instelling de boven- en onderskin niet volledig vullen. Dit bespaart tijd bij het slicen en printen, maar kan ertoe leiden dat er vulmateriaal uitlekt.

<!--screenshot {
"image_path": "skin_no_small_gaps_heuristic_disabled.png",
"modellen": [
    {
        "script": "small_z_gap.scad",
        "scad_params": ["gap_size=0.06"]
    }
],
"camerapositie": [-21, -62, 25],
"instellingen": {
    "wall_line_count": 0,
    "skin_no_small_gaps_heuristic": false
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "skin_no_small_gaps_heuristic_enabled.png",
"modellen": [
    {
        "script": "small_z_gap.scad",
        "scad_params": ["gap_size=0.06"]
    }
],
"camerapositie": [-21, -62, 25],
"instellingen": {
    "wall_line_count": 0,
    "skin_no_small_gaps_heuristic": true
},
"kleuren": 32
}-->

![Er is meestal skin rond de kleine horizontale opening.](../../../articles/images/skin_no_small_gaps_heuristic_disabled.png)
![Als deze functie is geactiveerd, zal de skin niet goed sluiten.](../../../articles/images/skin_no_small_gaps_heuristic_enabled.png)

Het belangrijkste doel van deze instelling is om de printtijd te verkorten. Deze instelling vermindert effectief de resolutie waarmee Cura controleert waar de skin moet worden geplaatst. Afhankelijk van de vorm van het model kan dit tussen de 5% en 30% aan printtijd besparen. Het bespaart ook printtijd wanneer er kleine openingen zijn, omdat de vulling wordt geprint in plaats van de buitenskin.

Als het model geen horizontale openingen heeft die kleiner zijn dan de skindikte, is de enige impact een kortere printtijd.

Als het model echter dergelijke horizontale gaten heeft, is de vulling zichtbaar in de opening. Als de opening echter klein genoeg is, zou de overhang de wanden voldoende doorhangen om toch niet zichtbaar te zijn.