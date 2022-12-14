Wandvolgorde
====
Deze instelling bepaalt welke wanden het eerst worden geprint, de buiten- of binnenwanden.

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"modellen": [{"script": "calendar_holder.scad"}],
"camerapositie": [0, 0, 120],
"instellingen": {
    "skin_outline_count": 0,
    "outer_inset_first": false
},
"laag": 2,
"lijn": [0, 1, 2, 3, 4, 5, 6, 7, 8, 17, 23, 29, 35, 45, 51, 57, 63, 67, 68, 69, 70, 71, 72 , 73, 74, 84, 90, 96, 102, 113, 119, 125, 131],
"vertraging": 125,
"kleuren": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"modellen": [{"script": "calendar_holder.scad"}],
"camerapositie": [0, 0, 120],
"instellingen": {
    "skin_outline_count": 0,
    "outer_inset_first": true
},
"laag": 2,
"lijn": [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 24, 30, 36, 47, 53, 59, 65, 70, 71, 72, 73, 74, 75 , 76, 77, 86, 92, 98, 104, 114, 120, 126, 132],
"vertraging": 125,
"kleuren": 32
}-->
![De binnenwand wordt eerst geprint](../../../articles/images/outer_inset_first_disabled.gif)
![De buitenwand wordt eerst geprint](../../../articles/images/outer_inset_first_enabled.gif)

Het inschakelen van deze instelling heeft een kleine invloed op de kwaliteit en maatnauwkeurigheid:
* Het verbetert de maatnauwkeurigheid. Aangrenzende wanden verschuiven over het algemeen een beetje, vooral als de breedte van de wandlijn kleiner is dan de maat van de nozzle. De wand die het eerst wordt geprint is al gestold en zal dus niet zo veel verschoven worden. Dus als je eerst de buitenwand print, komt de buitenwand nauwkeuriger te staan.
* Als de vulling voor de wanden wordt geprint, is de vulling niet zo zichtbaar op het oppervlak. Anders wordt eerst de vulling geprint, dan de binnenwanden, die door de vulling naar buiten worden geduwd, en dan de buitenwand, die door de binnenwanden naar buiten wordt geduwd. Hierdoor kan er aan de buitenkant een patroon zichtbaar zijn. Als de buitenwand eerst wordt geprint, kan de buitenwand stollen voordat de binnenwand erop kan printen.
* Het is over het algemeen slechter voor de overhang als eerst de buitenwand wordt geprint. De buitenwand ligt verder van de vorige laag dan de binnenwand. Als eerst de buitenwand wordt geprint, heeft de buitenwand nog geen houvast. Als de binnenwand eerst wordt geprint, kan de buitenwand zijdelings aan de buitenwand plakken.