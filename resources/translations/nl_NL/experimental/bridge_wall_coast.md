Coasting brugwand
====
Bij het overbruggen met wandlijnen stopt de materiaaltoevoer even voordat een brug wordt geprint. Gedurende deze tijd laat men het resterende materiaal in de nozzlekamer naar buiten stromen om de druk in de nozzlekamer te verminderen. Deze techniek wordt [Coasting Inschakelen](coasting_enable.md) genoemd. Deze instelling kan worden gebruikt om de hoeveelheid overschrijding te regelen. Dit bepaalt in wezen hoe ver voor een brug het materiaal stopt met stromen.

Nadat de brug is voltooid, wordt het niet-geëxtrudeerde materiaal nog steeds uitgeworpen. De totale hoeveelheid geëxtrudeerd materiaal blijft hetzelfde. Hierdoor wordt de druk op nozzle hersteld, waardoor onder-extrusie wordt voorkomen.

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"modellen": [{"script": "bridge.scad"}],
"laag": 80,
"instellingen": {
    "bridge_settings_enabled": waar,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camerapositie": [0, 18, 79],
"kleuren": 64
}-->
![Geen extrusie aan de ene kant van de brug en extra extrusie aan de andere kant](../../../articles/images/bridge_skin_density_100.png)

De eenheid van deze instelling is niet intuïtief te begrijpen. De afstand tot de brug waarop het materiaal stopt met stromen, is afhankelijk van een aantal factoren:
* De lengte van de vorige wand tot aan de brug. Hoe langer de wand, hoe meer hij kan lekken.
* De doorvoer uit de nozzle tijdens de normale wand, bepaald door de [Wandsnelheid](../speed/speed_wall.md), de [Lijnbreedte Wand](../resolution/wall_line_width.md), de [Wanddoorvoer](../material/wall_material_flow.md) en de [Laaghoogte](../resolution/layer_height.md) van deze wanden. Hoe groter de doorvoer in normale wanden, hoe langer de uitloopafstand.
* De filament doorvoer tijdensprinten van de overbrugde wand hangt af van de [Snelheid brugwand](bridge_wall_speed.md) en [Doorvoer brugwand](bridge_wall_material_flow.md) van die wanden. Hoe groter de doorvoer in overbrugde wanden, hoe *korter* de uitloopafstand.

Deze instelling is een vermenigvuldigingsfactor voor de uiteindelijke lengte.

Het doel van deze vertraging is om de druk in de nozzlekamer te verlagen. Dit is nodig omdat een eventuele restdruk in de nozzlekamer ervoor zorgt dat het materiaal over een aanzienlijke afstand naar beneden wordt geprint voordat het stolt nadat de tegendruk is verwijderd. Dit naar beneden printen van het materiaal veroorzaakt doorbuiging. In wezen worden de overhangende lijnen naar beneden geduwd door de rest van het materiaal dat zich nog in nozzle bevindt. Wanneer de druk in de nozzlekamer wordt verlaagd, neemt ook deze kracht af en treedt er minder doorbuiging op.

Door de vertraging te vergroten, wordt de druk in de nozzlekamer verminderd tegen de tijd dat de brug moet worden geprint, waardoor de doorbuiging wordt verminderd. De print is dan nauwkeuriger. Als u de vertragingstijd echter te veel verlengt, zal er een fase van onder-extrusie zijn net voordat de brug wordt geprint. Aangezien deze onder-extrusie in de wanden van de print zit, zal deze duidelijk zichtbaar zijn aan de zijkant van de print.