Hoogte Traptreden Supportstructuur
====
Als [Plaatsing Supportstructuur](support_type.md) is ingesteld op Overal, kan de support bovenop het model rusten. Het volgt echter niet precies de contouren van het model. In plaats daarvan is de onderzijde van de support voorzien van een traptredepatroon. Zo sluit de support maar op een paar plekken aan op het model.

Deze instelling bepaalt de hoogte van deze niveaus.

<!--screenshot {
"image_path": "support_bottom_stair_step_height.png",
"modellen": [{"script": "standing_ring.scad"}],
"camerapositie": [0, 136, 10],
"camera_lookat": [0, 0, 10],
"instellingen": {
    "support_enable": waar,
    "support_bottom_stair_step_height": 1
},
"kleuren": 64
}-->
![Trapvorming onderaan de support](../../../articles/images/support_bottom_stair_step_height.png)

De hoogte van de traptreden wordt berekend op basis van de afstand tot het oppervlak van het model. Dat wil zeggen, als u een verticale afstand heeft ingesteld in de instelling [Afstand van Onderkant Supportstructuur](support_bottom_distance.md) wordt deze afgetrokken van de hoogte en wordt de verbinding tussen het model en de support groter. Evenzo zorgt de instelling [Supportvloer inschakelen](support_bottom_enable.md) ervoor dat het effect van de traptreden wordt verminderd.

De [Maximale breedte traptreden supportstructuur](support_bottom_stair_step_width.md) beperkt de breedte van treden. Als het oppervlak van het model zo vlak is dat een kleine staphoogte zou resulteren in een grote stapbreedte, volgt de support het oppervlak van het model voor de rest van de staphoogte.

Als u deze instelling verlaagt, wordt de onderkant van de support gladder. Dit vergroot de hechting tussen de drager en het model, waardoor het moeilijker wordt om de drager te verwijderen, maar ook de stabiliteit van de drager.