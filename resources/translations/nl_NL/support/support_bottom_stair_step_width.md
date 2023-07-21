Maximale breedte traptreden supportstructuur
====
Als de instelling [Plaatsing Supportstructuur](support_type.md) is ingesteld op Overal, mag de support op het model rusten. Het volgt echter niet precies de contouren van het model. In plaats daarvan is de onderzijde van de support voorzien van een traptredepatroon. Zo sluit de support maar op een paar plekken aan op het model.

Deze instelling bepaalt de maximale breedte van deze treden. Normaal gesproken volgt de breedte van de trede het oppervlak van het model met een gegeven waarde van de [Hoogte Traptreden Supportstructuur](support_bottom_stair_step_height.md). Is deze echter te breed, dan wordt de breedte beperkt tot de maximale breedte van de supporttraptrede. Het volgt dan het oppervlak van het model voor de rest van het podium.

<!--screenshot {
"image_path": "support_bottom_stair_step_width.png",
"modellen": [{"script": "standing_ring.scad"}],
"camerapositie": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"instellingen": {
    "support_enable": waar,
    "support_bottom_stair_step_height": 1,
    "support_bottom_stair_step_width": 0.7
},
"kleuren": 64
}-->
![Beperkte breedte van de traptreden zodat de support het model volgt](../../../articles/images/support_bottom_stair_step_width.png)

Deze instelling moet normaal gesproken worden ingesteld op de maximale afstand die het materiaal kan overbruggen zonder de stabiliteit van de supportlijnen erboven op te offeren. Een lagere instelling zorgt ervoor dat de support het model vaker volgt, waardoor de stabiliteit van de support toeneemt. Door de instelling te verhogen, voldoet de support vaker aan de ingestelde waarde voor de supporttraphoogte, waardoor de support gemakkelijker uit het model kan worden verwijderd.