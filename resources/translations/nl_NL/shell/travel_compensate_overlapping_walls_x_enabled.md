Gelijkmatige overlappingen van binnenwanden
====
Bij het printen van zeer dunne delen kunnen de tegenoverliggende wanden zo dicht bij elkaar staan ​​dat ze elkaar overlappen. Als beide wanden met hun normale lijnbreedte zouden worden geprint, zouden ze over-extruderen. Deze instelling voorkomt deze over-extrusie door de breedte van een van de lijnen te verkleinen, waardoor deze over-extrusie wordt voorkomen en een betere maatnauwkeurigheid wordt verkregen.

![Alle lijnen worden over hun volle breedte geëxtrudeerd, waardoor een deel te breed is.](../../../articles/images/travel_compensate_overlapping_walls_x_enabled_disabled.png)
![De helft van de regels is verkleind in breedte, wat resulteert in een nauwkeuriger printen.](../../../articles/images/travel_compensate_overlapping_walls_x_enabled_enabled.png)

Deze instelling geldt alleen voor de binnenwanden. Compensatie voor de overlap in de binnenwanden is aan de buitenzijde minder zichtbaar omdat er minder artefacten van doorvoersnelheidsveranderingen zichtbaar worden, maar het vermindert evenzeer het effect van over-extrusie doordat de binnenwanden minder naar buiten worden geduwd.

De lijnbreedte van de wand die een andere wand overlapt, wordt verminderd met het overlapgebied. Dit compenseert de over-extrusie.

Zoals hierboven beschreven, heeft dit de neiging de maatnauwkeurigheid te verbeteren. Het nadeel is echter dat de doorvoersnelheid ongelijker wordt, wat resulteert in onder-extrusie op sommige plaatsen en over-extrusie op andere. Ook kan de doorvoersnelheid onder de minimale doorvoersnelheid van nozzle en de extruderinstelling komen, wat resulteert in een onregelmatige doorvoer en druppelen. Om dit effect te verminderen, kunt u de [minimale wanddoorvoer](wall_min_flow.md) instellen, waardoor enkele van de dunste wanden in verplaatsingen worden omgezet ten koste van de maatnauwkeurigheid.

**Deze instelling ziet er nogal lelijk uit in de laagweergave. Bij echt printen zijn er geen grenzen tussen de regels. In de laagweergave worden alleen de paden van de G-code weergegeven, maar in werkelijkheid wordt het materiaal opzij geschoven door de andere wand waarmee het overlapt. Zelfs kleine verminderingen van de doorvoer worden niet weerspiegeld in de daadwerkelijke print, omdat de doorvoersnelheid door nozzle zich niet zo snel kan aanpassen. Deze effecten zorgen ervoor dat de daadwerkelijke print vloeiender is dan de plakweergave laat zien.**