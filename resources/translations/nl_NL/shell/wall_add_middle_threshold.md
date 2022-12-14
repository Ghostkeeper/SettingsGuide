Drempel voor het toevoegen van een middellijn
====
Bij het printen van dunne delen past Cura de breedte van de wandlijnen aan de exacte breedte van het model aan. Cura kan er ook voor kiezen om in plaats daarvan minder wandlijnen te gebruiken. Deze instelling is de drempel waarop Cura een lijn in het midden zal toevoegen. Het kan afzonderlijk worden ingesteld van de [drempel waar de twee middelste lijnen samenkomen](wall_split_middle_threshold.md).

Deze instelling is hetzelfde als [Minimale lijndikte wand (oneven)](min_odd_wall_line_width.md), maar gebruikt een andere eenheid. De eenheid van deze instelling is in fracties van een lijnbreedte, die de breedte van een onderdeel moet vergroten om een ​​nieuwe middellijn toe te voegen.

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
"image_path": "min_wall_line_width_odd_0_1.png",
"modellen": [{"script": "moon_sickle.scad"}],
"camera_positie": [0, 0, 63],
"instellingen": {
	"min_odd_wall_line_width": 0.1,
	"min_wall_line_width": 0,34,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"laag": 14,
"kleuren": 32
}-->
![Als de middellijn te klein is, worden de twee lijnen eromheen breder gemaakt](../../../articles/images/min_wall_line_width_0_34.png)
![Als deze instelling wordt verlaagd, begint en eindigt de middellijn veel kleiner](../../../articles/images/min_wall_line_width_odd_0_1.png)

Even versus oneven lijnen
----
Met deze instelling kan de drempel voor het toevoegen van regels specifiek worden aangepast wanneer het aantal regels oneven is. Dit is wanneer er een enkele regel in het midden is in plaats van twee. Het bepaalt wanneer een nieuwe regel wordt toegevoegd tussen de twee middelste regels.

De drempel voor het toevoegen van een middellijn kan anders zijn dan de drempel om de middellijn in tweeën te delen, omdat de twee lijnen anders in elkaar overlopen. Wanneer een oneven lijn wordt toegevoegd, begint deze pas als de twee omringende lijnen hem ruimte hebben gegeven. Er is een kleine opening tijdens de overgang waar de omringende lijnen nog niet genoeg ruimte hebben gemaakt. Dit is anders dan een even aantal wanden: de lijn in het midden splitst zich dan in tweeën, en deze twee lijnen overlappen elkaar enigszins totdat ze ver genoeg van elkaar verwijderd zijn. Als u de drempel voor middenlijn toevoegen verlaagt, wordt de opening bij de even-naar-oneven lijnovergangen kleiner.

De gaten die ontstaan ​​wanneer een oneven lijn begint, zijn beter zichtbaar in het eindresultaat dan een lichte over-extrusie bij een naad, dus het kan helpen om de drempel voor middenlijn toevoegen iets lager dan de drempel voor middenlijn splitsen in te stellen.

Het verlagen van deze instelling resulteert in:
* Kleinere openingen wanneer een middenlijn eindigt.
* Verminderde maximale breedte van een paar even hartlijnen.
* Dunnere lijnen die mogelijk niet goed extruderen.
* Langere regels die langer duren om printen.

**Deze instelling is niet alleen van toepassing op normale wanden, maar ook op wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**