Overlapercentage Skin
====
In deze setting overlapt de skin de aangrenzende structuren enigszins. Hierdoor hecht de buitenskin beter aan deze structuren.

De overlap in deze instelling wordt uitgeprint als een percentage van de gemiddelde lijndikte tussen de skinlijnen en de binnenste wandlijnen.

<!--screenshot {
"image_path": "skin_overlap_none.png",
"modellen": [{"script": "mounting_plate.scad"}],
"camerapositie": [0, 0, 84],
"instellingen": {
    "skin_outline_count": 0,
    "skin_overlap": 0
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "skin_overlap_20.png",
"modellen": [{"script": "mounting_plate.scad"}],
"camerapositie": [0, 0, 84],
"instellingen": {
    "skin_outline_count": 0,
    "skin_overlap": 40
},
"kleuren": 64
}-->

![Geen overlap.](../../../articles/images/skin_overlap_none.png)
![Lichte overlap](../../../articles/images/skin_overlap_20.png)

Deze overlap resulteert technisch in over-extrusie, maar het is zo klein dat je het niet kunt zien. Het heeft echter een aanzienlijke invloed op de sterkte omdat de buitenskin beter kan hechten aan de wanden en opvulling. Deze constructies voegen immers alleen sterkte toe aan het model als ze houvast hebben.

Enige overlap kan ook helpen het optreden van skinhiaten te verminderen.