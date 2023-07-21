Wanddikte
====
Deze instelling bepaalt hoe dik de wand rond de print wordt. Uiteindelijk wordt het aantal binnenwanden aangepast om de gewenste dikte te bereiken.

<!--screenshot {
"image_path": "wall_thickness_0.8.png",
"modellen": [
    {
        "script": "rotary_tumbler_lid.scad",
        "transformatie": ["schaal(0.4)"]
    }
],
"camerapositie": [50, 50, 124],
"instellingen": {
    "skin_outline_count": 0,
    "wall_line_count": 2
},
"kleuren": 32
}-->
<!--screenshot {
"image_path": "wall_thickness_1.6.png",
"modellen": [
    {
        "script": "rotary_tumbler_lid.scad",
        "transformatie": ["schaal(0.4)"]
    }
],
"camerapositie": [50, 50, 124],
"instellingen": {
    "skin_outline_count": 0,
    "wall_line_count": 4
},
"kleuren": 32
}-->
![0,8 mm dikke wanden](../../../articles/images/wall_thickness_0.8.png)
![1,6 mm dikke wanden](../../../articles/images/wall_thickness_1.6.png)

De wanddikte moet een veelvoud zijn van de wandlijnbreedte. Indien dit niet het geval is, wordt er afgerond op een exact veelvoud. Houd er echter rekening mee dat een van de wanden een buitenwand zal zijn en de rest van de wanden een binnenwand. Deze wanden kunnen verschillende lijndiktes hebben.

De dikte van de wanden is een belangrijke factor in hoe sterk de print zal zijn. Doordat de wanden naast elkaar staan, kunnen ze elkaar versterken, wat resulteert in een sterker onderdeel. Voor grotere printen kan dit een veel effectievere manier zijn om een sterk object te krijgen dan de vulling aan te passen aan de vorm.

Bij het vergroten van de wanddikte wordt:
* De sterkte van de print wordt aanzienlijk vergroot.
* Verminderde doorschijning waar het vulpatroon van buitenaf zichtbaar is.
* Verbeterde overhangen omdat wandlijnen meestal meer uitgelijnd zijn met het dichtstbijzijnde supportpunt.
* Maak het model gemakkelijker waterdicht.
* Aanzienlijke toename van printtijd en materiaalverbruik van de print.