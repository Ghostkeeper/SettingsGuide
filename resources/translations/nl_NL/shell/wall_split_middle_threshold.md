Drempel voor middenlijn splitsen
====
Bij het printen van dunne delen past Cura de breedte van de wandlijnen aan de exacte breedte van het model aan. Cura kan er ook voor kiezen om in plaats daarvan minder wandlijnen te gebruiken. Deze instelling is de drempel waarbij Cura een enkele regel in tweeën splitst naarmate de breedte van het onderdeel groter wordt. Het kan onafhankelijk van de [drempel waarop een nieuwe middelste regel wordt toegevoegd](wall_add_middle_threshold.md) worden ingesteld.

Deze instelling is hetzelfde als [Min wandlijnbreedte (even)](min_even_wall_line_width.md), maar gebruikt een andere eenheid. De eenheid van deze instelling is de fractie van een lijnbreedte waarmee de breedte van een onderdeel moet toenemen om de middellijn in tweeën te splitsen. Omdat het breedteverschil na de splitsing tussen de twee lijnen in het midden wordt gesplitst, komt een kleinere minimale lijnbreedte voor even wanden overeen met een veel kleinere drempel voor de middellijnsplitsing dan bij het verwijderen van een oneven wand.

<!--screenshot {
"image_path": "min_wall_line_width_0_34.png",
"modellen": [{"script": "moon_sickle.scad"}],
"camera_positie": [0, 0, 63],
"instellingen": {
	"min_wall_line_width": 0,34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"laag": 14,
"kleuren": 32
}-->
<!--screenshot {
"image_path": "min_wall_line_width_even_0_1.png",
"modellen": [{"script": "moon_sickle.scad"}],
"camera_positie": [0, 0, 63],
"instellingen": {
	"min_even_wall_line_width": 0.1,
	"min_wall_line_width": 0,34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"laag": 14,
"kleuren": 32
}-->
![De middellijn is verbreed om te passen](../../../articles/images/min_wall_line_width_0_34.png)
![Als deze instelling wordt verlaagd, worden in plaats daarvan twee regels gebruikt](../../../articles/images/min_wall_line_width_even_0_1.png)

Even versus oneven lijnen
----
Met deze instelling kunt u de drempel voor het toevoegen van regels aanpassen, specifiek wanneer er een even aantal regels is. Dit is wanneer er twee lijnen in het midden zijn, in plaats van slechts een enkele lijn. Het bepaalt wanneer een lijn door het midden in twee lijnen wordt gesplitst.

De drempel voor het splitsen van een middenlijn kan anders zijn dan de drempel voor het toevoegen van een middenlijn omdat de twee lijnen op verschillende manieren met elkaar verbonden zijn. Rechte lijnen verbinden aan hun uiteinden door de uiteinden dichter bij elkaar te brengen. Er is enige overlap met deze lijnen, wat resulteert in over-extrusie. Dit is anders dan bij een oneven aantal wanden: de lijn in het midden blijft gewoon staan en laat een gat in de print achter. Het verlagen van de drempel voor middenlijn verdelen vermindert over-extrusie bij de even-naar-oneven lijnovergangen. Het verlagen van de drempel voor het toevoegen van een middellijn verkleint de grootte van de opening bij de oneven-naar-even lijnovergangen.

De gaten die ontstaan bij het toevoegen van een middellijn zijn beter zichtbaar in het eindresultaat dan een lichte over-extrusie bij een naad, dus het kan helpen om de drempel Middenlijn splitsen iets hoger in te stellen dan de drempel Middenlijn toevoegen.

Het verlagen van deze instelling resulteert in:
* Vermindering van het overlapgebied waar twee lijnen samenvloeien tot één lijn.
* Verminderde maximale breedte van enkele middellijnen.
* Dunnere lijnen die mogelijk niet goed extruderen.
* Meer regels die langer duren om printen.

**Deze instelling is niet alleen van toepassing op normale wanden, maar ook op wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**