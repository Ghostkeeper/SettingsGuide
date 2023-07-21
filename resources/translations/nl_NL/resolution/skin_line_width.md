Lijnbreedte Boven-/onderkant
====
De breedte van de lijn aan de boven- en onderkant. De breedte van een lijn kan variëren ondanks de grootte van het nozzle door simpelweg meer of minder materiaal te extruderen dan nodig is. Naarmate er meer materiaal wordt geëxtrudeerd, zal het plastic naar de zijkanten stromen, waardoor de lijn dikker wordt. Als er minder materiaal wordt geëxtrudeerd, trekt de oppervlaktespanning van het materiaal het materiaal naar de hartlijn van het nozzlepad.

<!--screenshot {
"image_path": "skin_line_width.png",
"modellen": [
    {
        "script": "flipper_grip.scad",
        "transformatie": ["schaal(0.6)"]
    }
],
"camerapositie": [0, 37, 107],
"instellingen": {"skin_line_width": 0.8},
"laag": 300,
"kleuren": 64
}-->
![De skinlijnen zijn aanzienlijk breder dan de rest](../../../articles/images/skin_line_width.png)

Het breder maken van de skinlijnen is een gemakkelijke manier om de printtijd te verkorten, omdat er minder lijnen nodig zijn om de boven- en onderkant van het object printen. Te veel vergroting kan echter leiden tot grote extrusievariaties. Dit resulteert in onder-extrusie bij het printen van de skinlijn en over-extrusie bij het printen van het volgende deel omdat de doorvoer door het nozzle zich niet snel genoeg kan aanpassen. Het vergroten van de breedte van de skinlijn vergroot ook de kans op het maken van gaten in het oppervlak, wat niet mooi is en voorkomt dat het waterdicht is.

Het verkleinen van de breedte van de skinlijn resulteert meestal in een mooiere top, maar dit gaat ten koste van de printtijd. Het is vaak effectiever om een andere techniek te gebruiken, zoals [Strijken](../top_bottom/ironing_enabled.md) of gewoon de [Lijnbreedte bovenskin](../experimental/roofing_line_width.md) aan te passen.