Aantal wanden voor distributie
====
Cura kan de breedte van de wandlijnen aanpassen om beter te passen bij de vorm die wordt geprint, maar niet elke wand hoeft in dezelfde mate te worden aangepast. Cura geeft er de voorkeur aan om de breedte van de wanden verder in het model te veranderen. Deze instelling bepaalt het aantal wanden, van binnen naar buiten geteld, dat wordt aangepast aan de beschikbare ruimte.

<!--screenshot {
"image_path": "wall_distribution_count_1.png",
"modellen": [
	{
		"script": "misaligned_ring.scad",
		"transformatie": ["schaal(2)"]
	}
],
"camera_positie": [-11, 0, 111],
"instellingen": {
	"wall_line_count": 5,
	"wall_distribution_count": 1
},
"color_scheme": "line_width",
"kleuren": 128
}-->
<!--screenshot {
"image_path": "wall_distribution_count_5.png",
"modellen": [
	{
		"script": "misaligned_ring.scad",
		"transformatie": ["schaal(2)"]
	}
],
"camera_positie": [-11, 0, 111],
"instellingen": {
	"wall_line_count": 5,
	"wall_distribution_count": 5
},
"color_scheme": "line_width",
"kleuren": 128
}-->
![Geconcentreerd in het midden, daar met grote verschillen in lijndikte ](../../../articles/images/wall_distribution_count_1.png)
![Verdeeld over vele wanden](../../../articles/images/wall_distribution_count_5.png)

Wanden met verschillende breedtes zijn moeilijker te printen dan eenvoudige wanden met constante breedte. Het kost wat tijd om de doorvoer van nozzle aan te passen, en de overgang moet ook enkele scherpe hoeken maken die rinkelen kunnen veroorzaken. Dit alles kan het beste zo ver mogelijk van de buitenkant worden gedaan, waar het zichtbaar is op het oppervlak van de print. Daarom richt Cura de aanpassing van de lijnbreedte op de binnenste wanden.

Aan de andere kant betekent de concentratie van variatie ook dat de lijnen in het midden heel verschillende breedtes zullen hebben. Omdat ze over meerdere lijnen zijn verspreid, kan de amplitude van de variaties kleiner zijn, waardoor de effecten van de variabele lijnbreedte worden verminderd in plaats van deze aan de binnenkant te verbergen.

Deze instelling selecteert een aantal wanden aan de binnenkant waartussen de lijndikte kan worden aangepast om de beschikbare ruimte te vullen. Dit werkt vanuit het midden twee kanten op, dus bij een instelling van 2 tot 4 wanden kunnen in het midden worden aangepast. Zelfs binnen deze wanden is de aanpassing niet gelijkmatig verdeeld. De wanden in het midden zijn altijd iets meer aangepast dan de wanden aan de buitenkant.

De buitenwand wordt zoveel mogelijk op de nominale lijnbreedte gehouden. Deze wand heeft zo'n grote invloed op de printkwaliteit dat deze op een constante lijnbreedte wordt gehouden om het oppervlak zo glad mogelijk te maken. Pas als het stuk zo dun wordt dat het alleen nog maar uit buitenwanden bestaat, worden deze wanden aangepast.

In de praktijk is het bijna altijd beter om de onvolkomenheden in het midden te verbergen dan ze over meerdere wanden te verspreiden. Het is dus het beste om deze instelling zo laag mogelijk te houden. Bij het werken met materialen die moeilijk te extruderen zijn of waarvan het vloeigedrag moeilijk te veranderen is, zoals: B. flexibele materialen, het is handig om deze instelling te verhogen om stroomvariaties te verminderen. Deze stromingsveranderingen kunnen echter niet geheel worden voorkomen.

**Deze instelling is niet alleen van toepassing op normale wanden, maar ook op wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**