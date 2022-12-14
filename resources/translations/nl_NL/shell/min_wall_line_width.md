Minimumbreedte wandlijn
====
Bij het printen van dunne delen past Cura de breedte van de wandlijnen aan de exacte breedte van het model aan. Cura kan er ook voor kiezen om in plaats daarvan minder wandlijnen te gebruiken. Deze instelling bepaalt bij welke drempel Cura besluit een wand te verwijderen in plaats van de bestaande wanden te verdunnen.

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
"image_path": "min_wall_line_width_0_1.png",
"modellen": [{"script": "moon_sickle.scad"}],
"camera_positie": [0, 0, 63],
"instellingen": {
	"min_wall_line_width": 0.1,
	"wall_line_count": 3,
	"wall_transition_angle": 20
},
"laag": 14,
"kleuren": 32
}-->
![Meestal worden de lijnen breder gemaakt om te passen](../../../articles/images/min_wall_line_width_0_34.png)
![Door de minimale lijndikte te verkleinen, worden meer lijnen gebruikt.](../../../articles/images/min_wall_line_width_0_1.png)

Ander aantal wanden
----
Als er maar één centrale lijn is en [Aantal wanden voor distributie](wall_distribution_count.md) is ingesteld op 1, werkt deze instelling precies zoals vermeld. Wanneer de lijn in het midden dunner wordt dan een bepaalde breedte, wordt deze verwijderd om andere lijnen breder te maken. In andere gevallen is de berekening wat ingewikkelder.

De exacte berekening is complex, maar een intuïtief begrip kan nuttig zijn. In principe kun je de totale breedte van het model delen door de [Lijnbreedte Wand](../resolution/wall_line_width.md) om een ​​specifiek aantal wanden te krijgen. Dit kan ook een breuk zijn (bijvoorbeeld 5,3 wandlijnbreedtes). De minimale wandlijnbreedte neemt alleen die fractie (0,3 lijnbreedtes) en voegt een extra wand toe als deze de minimale wandlijnbreedte overschrijdt. Als het aantal wanden bekend is, wordt de breedte van elke lijn bepaald volgens het wandverdelingsnummer.

![Min wand lijndikte verschuift de drempel voor het toevoegen van een nieuwe lijn naar links of rechts](../../../articles/images/min_wall_line_width.svg)

Dit betekent dat voor meerdere lijnen waarvan de breedte is aangepast, de lijnbreedte nooit zo extreem zal zijn als de minimale wandlijnbreedte zou toestaan. als bijv. Als bijvoorbeeld de middelste twee lijnen worden aangepast, zal de lijndikte niet onder het gemiddelde van de normale lijndikte en de minimale wandlijnbreedte komen.

De instelling kan afzonderlijk worden aangepast voor [Minimum lijnbreedte even wand](min_even_wall_line_width.md) en [Minimum breedte ongelijkmatige wandlijn ](min_odd_wall_line_width.md) aantal wanden. Het aantal 0 wanden is ook een apart geval dat kan worden aangepast met de instelling [Minimum elementgrootte](min_feature_size.md).

Afstemmen
----
In theorie zorgt een instelling van 50% van de lijndikte ervoor dat de lijndikte het dichtst bij de normale lijndikte ligt. Het is echter beter om iets hoger te zitten. Het is voor een printer gemakkelijker om lijnen af ​​te printen die breder zijn dan de nozzles dan om dunnere lijnen ​te printen, en minder lijnen betekent ook dat de print sneller gaat.

Bij zeer stroperige materialen of bij sneller printen moet de minimale wanddikte worden verkleind om te brede lijnen te voorkomen. Deze zijn moeilijk te printen als het materiaal niet genoeg tijd heeft om naar de zijkanten te vloeien. Als de minimale wandlijnbreedte te hoog is, zullen de wanden niet goed aan elkaar hechten, waardoor de print bros wordt.

**Deze instelling is niet alleen van toepassing op normale wanden, maar ook op wanden met extra skinen, supportwanden, vullingen en concentrische patronen.**