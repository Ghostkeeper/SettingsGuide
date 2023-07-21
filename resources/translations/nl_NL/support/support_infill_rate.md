Dichtheid Supportstructuur
====
Deze instelling bepaalt de snelheid waarmee de supportconstructies met materiaal worden gevuld. Bij hoge opvulsnelheden worden de supportlijnen zeer dicht bij elkaar geplaatst. Bij lage opvulsnelheden worden de lijnen verder uit elkaar geplaatst.

<!--screenshot {
"image_path": "support_infill_rate_low.png",
"modellen": [{"script": "spiral_stair.scad"}],
"camerapositie": [-95, 18, 116],
"instellingen": {
    "support_enable": waar,
    "support_infill_rate": 10
},
"laag": 256,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "support_infill_rate_high.png",
"modellen": [{"script": "spiral_stair.scad"}],
"camerapositie": [-95, 18, 116],
"instellingen": {
    "support_enable": waar,
    "support_infill_rate": 20
},
"laag": 256,
"kleuren": 64
}-->
![Lage support percentage](../../../articles/images/support_infill_rate_low.png)
![Hoog support percentage](../../../articles/images/support_infill_rate_high.png)

Het verhogen van de supportdichtheid heeft zowel positieve als negatieve effecten. Hier zijn enkele van de implicaties om te overwegen:
* Omdat de afstand tussen de supportlijnen kleiner is, zal het oppervlak dat op die support rust minder doorzakken.
* De support is stabieler, wat de betrouwbaarheid van het printen verhoogt.
* Het is moeilijker om het support te verwijderen omdat het kleefoppervlak groter is.
* Er is meer materiaal nodig om de drager printen.
* printen duurt langer.