Printvolgorde van wanden optimaliseren
====
Als dit is ingeschakeld, besteedt Cura wat extra slicing tijd om de volgorde waarin de wanden worden geprint te optimaliseren. Het doel is om het aantal verplaatsingen en intrekkingen te verminderen door wanden te printen die hetzelfde deel na elkaar omringen.
<!--screenshot {
"image_path": "optimize_wall_printing_order_disabled.gif",
"modellen": [
    {
        "script": "plate_with_indent.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 0, 120],
"instellingen": {
    "skin_outline_count": 0,
    "optimize_wall_printing_order": false
},
"laag": 37,
"lijn": [0, 7, 14, 21, 28, 34, 38, 42, 46, 64, 78, 91, 105, 120, 124, 128, 132, 140, 144, 148, 152, 162, 170 , 178, 186, 194, 198, 202, 206, 224, 237, 251, 265, 281, 285, 289, 293, 302, 306, 310, 314],
"vertraging": 125,
"kleuren": 32
}-->
<!--screenshot {
"image_path": "optimize_wall_printing_order_enabled.gif",
"modellen": [
    {
        "script": "plate_with_indent.scad",
        "transformatie": ["schaal(0.5)"]
    }
],
"camerapositie": [0, 0, 120],
"instellingen": {
    "skin_outline_count": 0,
    "optimize_wall_printing_order": true
},
"laag": 37,
"lijn": [0, 4, 8, 12, 16, 21, 25, 29, 33, 42, 46, 50, 54, 59, 63, 67, 71, 97, 110, 123, 138, 153, 166 , 179, 194, 204, 208, 212, 216, 221, 225, 229, 233, 245, 252, 259, 265, 273, 281, 289, 297],
"vertraging": 125,
"kleuren": 32
}-->
![Optimalisatie uitgeschakeld](../../../articles/images/optimize_wall_printing_order_disabled.gif)
![optimalisatie ingeschakeld](../../../articles/images/optimize_wall_printing_order_enabled.gif)

Als deze optimalisatie is ingeschakeld, zal de nozzle eerst alle wanden rond een onderdeel printen voordat het naar het volgende onderdeel gaat, in plaats van eerst alle binnenwanden te printen voordat de buitenwanden worden geprint. Optimalisatie is over het algemeen positief, maar kan de maatnauwkeurigheid voor sommige onderdelen beïnvloeden, omdat de vorige wand nog niet is gestold wanneer de volgende wand ernaast wordt neergezet.