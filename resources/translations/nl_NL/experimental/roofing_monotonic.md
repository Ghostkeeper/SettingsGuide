Monotone volgorde bovenlaag
====
Normaal gesproken regelt Cura lijnen zo dat de afstand ertussen klein is. Als deze instelling is geactiveerd, worden de lijnen op het oppervlak zo gerangschikt dat aangrenzende lijnen altijd overlappend in dezelfde richting worden geprint.

Wanneer lijnen op het oppervlak worden geprint, overlappen de lijnen meestal een beetje de aangrenzende lijnen omdat de vorm van een lijn geen perfecte rechthoek is. Deze overlap geeft de lijnen een lichte schuine stand, waardoor ze licht in verschillende richtingen anders weerkaatsen. Wanneer aangrenzende lijnen elkaar anders overlappen, verandert deze reflectie. Dit zie je terug in het eindresultaat. Het geeft een andere glans aan verschillende delen van het oppervlak. Door in een gelijkmatige volgorde te printen, is de overlap over het oppervlak gelijk, dus er zijn geen verschillen in lichtreflectie. Hierdoor ziet het oppervlak er egaler en gladder uit.

<!--screenshot {
"image_path": "skin_monotonic_disabled.gif",
"modellen": [
    {
        "script": "yen.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 0, 130],
"instellingen": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": false
},
"laag": 1,
"lijn": [29, 45, 61, 77, 93, 109, 125, 141, 157, 161, 177, 193, 199, 211, 231, 246, 262, 280, 296, 312, 326, 342, 358 , 374, 397, 417, 433, 449, 464, 480, 499],
"vertraging": 125,
"kleuren": 32
}-->
<!--screenshot {
"image_path": "skin_monotonic_enabled.gif",
"modellen": [
    {
        "script": "yen.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 0, 130],
"instellingen": {
    "wall_line_count": 1,
    "skin_outline_count": 0,
    "travel_compensate_overlapping_walls_enabled": false,
    "skin_monotonic": waar
},
"laag": 1,
"lijn": [31, 47, 63, 77, 93, 109, 115, 131, 147, 163, 181, 197, 213, 229, 244, 263, 281, 296, 319, 340, 356, 372, 379 , 395, 411, 427, 443, 459, 475, 491, 507, 511],
"vertraging": 125,
"kleuren": 32
}-->
![Niet-gelijke volgorde](../../../articles/images/skin_monotonic_disabled.gif)
![Monotone volgorde, altijd beginnend vanaf de rechter benedenhoek](../../../articles/images/skin_monotonic_enabled.gif)

De gelijkmatige volgorde vergroot de lengte van de nozzle bewegingen enigszins, maar dit effect is zeer minimaal. Het beïnvloedt alleen de print visueel. De gelijkmatige volgorde heeft geen mechanische voordelen.

Om een glad oppervlak te krijgen, moet u deze instelling combineren met de instelling [Combing-modus](../travel/retraction_combing.md) om skinbewegingen te voorkomen, en misschien [Hoogte Z-sprong](../enable travel/retraction_hop.md ). Als alternatief kunt u ook [Strijken inschakelen](../top_bottom/ironing_enabled.md) inschakelen, maar dat doet het nut van deze instelling volledig teniet. Gladmaken heeft zijn eigen [Monotone strijkvolgorde](../top_bottom/ironing_monotonic.md).