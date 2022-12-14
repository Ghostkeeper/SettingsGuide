Minimum lijnbreedte even wand
====
Bij het printen van dunne delen past Cura de breedte van de wandlijnen aan de exacte breedte van het model aan. Cura kan er ook voor kiezen om in plaats daarvan minder wandlijnen te gebruiken. Deze instelling is de drempel waarbij Cura twee lijnen samenvoegt tot één. Het kan afzonderlijk worden ingesteld met de [Minimum breedte ongelijkmatige wand](min_odd_wall_line_width.md).

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
Deze instelling kan worden gebruikt om de drempel voor het verwijderen van lijnen specifiek voor een even aantal lijnen aan te passen. Dit is wanneer er twee lijnen in het midden zijn, in plaats van slechts een enkele lijn. Het bepaalt wanneer deze twee lijnen samenkomen in een enkele lijn in het midden.

De minimale breedte van de even wandlijnen kan verschillen van de minimale breedte van de oneven wandlijnen vanwege de manier waarop ze op elkaar aansluiten. De rechte lijnen verbinden aan hun uiteinden door de uiteinden dichter bij elkaar te brengen. Daar snijden deze lijnen elkaar, wat resulteert in een kruising. Dit is anders dan een oneven aantal wanden: de lijn in het midden stopt dan gewoon en laat een gat in de print achter. Het verkleinen van de minimale breedte van de even wandlijnen vermindert over-extrusie bij de even-naar-oneven lijnovergangen. Door de minimale breedte van de oneven wandlijnen te verkleinen, wordt de opening bij de oneven-naar-even lijnovergangen kleiner.

De openingen aan het einde van een oneven lijn zijn beter zichtbaar in het eindresultaat dan een lichte over-extrusie bij een naad, dus het kan helpen om de minimale breedte van de even wandlijn iets hoger te stellen dan de minimale oneven wandlijnbreedte.

Het verlagen van deze instelling resulteert in:
* Vermindering van het overlapgebied waar twee lijnen samenvloeien tot één lijn.
* Verminderde maximale breedte van enkele middellijnen.
* Dunnere lijnen die mogelijk niet goed extruderen.
* Meer regels die langer duren om printen.

**Deze instelling is niet alleen van toepassing op normale wanden, maar ook op wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**