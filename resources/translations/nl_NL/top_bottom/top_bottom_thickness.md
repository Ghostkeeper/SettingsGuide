Dikte Boven-/Onderkant
====
Met boven-/onderdikte kunt u instellen hoe dik u wilt dat de skin aan de boven- en onderkant van uw print is.

<!--screenshot {
"image_path": "top_bottom_thickness_0.8.png",
"modellen": [{"script": "stamp.scad"}],
"camerapositie": [0, 203, 30],
"instellingen": {
    "wall_line_count": 0,
    "top_bottom_thickness": 0,8
},
"kleuren": 64
}-->
<!--screenshot {
"image_path": "top_bottom_thickness_3.png",
"modellen": [{"script": "stamp.scad"}],
"camerapositie": [0, 203, 30],
"instellingen": {
    "wall_line_count": 0,
    "top_bottom_thickness": 3
},
"kleuren": 64
}-->

![Normale dikte boven/onder](../../../articles/images/top_bottom_thickness_0.8.png)
![Aanzienlijk dikkere boven- en onderkant](../../../articles/images/top_bottom_thickness_3.png)

Dit heeft invloed op zowel de boven- als onderkant van de print.De boven- en onderkant kunnen ook afzonderlijk worden geconfigureerd met de instellingen [Dikte Bovenkant](top_thickness.md) en [Bodemdikte](bottom_thickness.md).

Als deze instelling geen veelvoud is van de hoogte van de laag, wordt deze afgerond op het dichtstbijzijnde veelvoud. Deze instelling bepaalt alleen hoeveel lagen er aan de boven- en onderkant worden gemaakt.

Het vergroten van de boven- en onderdikte heeft verschillende effecten die positief zijn voor de algehele kwaliteit, maar negatief voor de productiviteit.
* Uw onderdeel zal stabieler zijn. Meer toplagen betekent dat een kleiner deel van je print wordt gevuld met weinig vulling. In plaats daarvan is het volledig ingevuld.
* De bovenkant wordt gladder. Alle oneffenheden in de buitenste skin worden gladgestreken door de lagen erboven.
* Uw model is waarschijnlijk waterdicht. Er zijn meer lagen aan zowel de boven- als onderkant om het binnendringen van water of andere vloeistoffen te voorkomen en om overhangen te egaliseren.
* Uw print zal meer materiaal gebruiken omdat meer lagen volledig worden gevuld.
* Het printen duurt langer omdat er meer materiaal is om aan te brengen en deze lagen printen meestal langzamer dan de vulling.