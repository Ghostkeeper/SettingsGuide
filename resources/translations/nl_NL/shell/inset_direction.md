Wandvolgorde
====
Deze instelling bepaalt welke wanden als eerste worden geprint: de buiten- of binnenwanden.

<!--screenshot {
"image_path": "outer_inset_first_disabled.gif",
"modellen": [{"script": "calendar_holder.scad"}],
"camerapositie": [0, 0, 120],
"instellingen": {
    "skin_outline_count": 0,
    "inset_direction": "inside_out"
},
"laag": 2,
"lijn": [0, 6, 12, 18, 25, 35, 41, 47, 54, 57, 61, 64, 65, 68, 72, 74, 77, 79, 80, 82, 86, 96, 102 , 108, 114, 125, 131, 137, 144],
"vertraging": 125,
"kleuren": 32
}-->
<!--screenshot {
"image_path": "outer_inset_first_enabled.gif",
"modellen": [{"script": "calendar_holder.scad"}],
"camerapositie": [0, 0, 120],
"instellingen": {
    "skin_outline_count": 0,
    "inset_direction": "outside_in"
},
"laag": 2,
"lijn": [0, 6, 12, 18, 25, 35, 41, 47, 54, 58, 61, 63, 64, 66, 70, 72, 76, 79, 80, 83, 88, 97, 103 , 109, 116, 125, 131, 137, 144],
"vertraging": 125,
"kleuren": 32
}-->
![De binnenwand wordt eerst geprint](../../../articles/images/outer_inset_first_disabled.gif)
![De buitenwand wordt eerst geprint](../../../articles/images/outer_inset_first_enabled.gif)

Deze instelling heeft een kleine invloed op de kwaliteit en maatnauwkeurigheid:
* printen van buitenaf verbetert de maatnauwkeurigheid. Aangrenzende wanden hebben de neiging om elkaar een beetje te duwen, vooral wanneer de breedte van de wandlijn kleiner is dan de grootte van de nozzle. De wand die als eerste wordt geprint, is al gestold en zal minder verschuiven. Dus als je eerst de buitenwand print, wordt de buitenwand nauwkeuriger gepositioneerd.
* Als de vulling voor de wanden wordt geprint, zal het printen van buiten naar binnen de doorschijning van de vulling op het oppervlak verminderen. Anders wordt eerst de vulling geprint, dan de binnenwanden, die door de vulling naar buiten worden geduwd, en dan de buitenwand, die door de binnenwanden naar buiten wordt geduwd. Hierdoor kan er aan de buitenkant een patroon zichtbaar zijn. Als de buitenwand eerst wordt geprint, kan de buitenwand stollen voordat de binnenwand erop kan printen.
* Binnenstebuiten printen is beter voor de overhang. De buitenwand ligt verder van de vorige laag dan de binnenwand. Als eerst de buitenwand wordt geprint, heeft de buitenwand nog geen houvast. Als eerst de binnenwand wordt geprint, kan de buitenwand zijdelings tegen de buitenwand aanliggen.