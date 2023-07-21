Lijnafstand Supportstructuur Eerste Laag
====
De dichtheid van het patroon dat wordt gebruikt om de eerste laag support printen, kan afzonderlijk van de dichtheid van de rest van de support worden ingesteld. Deze instelling configureert de afstand tussen twee aangrenzende lijnen waar de support op het platformrust.

<!--screenshot {
"image_path": "support_initial_layer_line_distance.png",
"modellen": [{"script": "umbrella_square_rounded.scad"}],
"camerapositie": [0, 64, 125],
"instellingen": {
    "support_enable": waar,
    "support_initial_layer_line_distance": 1,333
},
"laag": 160,
"kleuren": 64
}-->
![Het patroon van de eerste laag is twee keer zo dicht als de rest van de support](../../../articles/images/support_initial_layer_line_distance.png)

Deze instelling is handig om de hechting tussen de support en de platformte verbeteren. Door het supportpatroon in de eerste laag dichter te maken, wordt het contactoppervlak tussen de support en de platformvergroot, waardoor het beter hecht. Daaropvolgende lagen kunnen dan op een materiaal worden geplaatst waar ze beter aan hechten.

Omdat deze instelling alleen de eerste laag beïnvloedt, heeft deze geen significante invloed op de supportsterkte of tijd- en materiaalkosten. Het heeft ook geen invloed op de kwaliteit van de overoverhang. Zie de instelling [Lijnafstand supportdak](support_roof_line_distance.md) om de dichtheid van support nabij de uitsteeksels aan te passen.

Het is raadzaam om deze instelling in te stellen op een veelvoud van de regelafstand van het hoofdgedeelte van de support. Op deze manier komen de lijnen van de support in lijn met de lijnen van de eerste laag zodat ze op de eerste laag rusten en niet in de lucht zweven.