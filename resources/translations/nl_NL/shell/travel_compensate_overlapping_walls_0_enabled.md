Gelijkmatige overlappingen van buitenwanden
====
Bij het printen van zeer dunne delen kunnen de tegenover elkaar liggende buitenwanden zo dicht bij elkaar staan ​​dat ze elkaar overlappen. Als beide wanden met hun normale lijnbreedte zouden worden geprint, zouden ze over-extruderen. Deze instelling voorkomt deze over-extrusie door de breedte van een van de lijnen te verkleinen, waardoor deze over-extrusie wordt voorkomen en een betere maatnauwkeurigheid wordt verkregen.

![Waar de lijndikte wordt verkleind](../../../articles/images/travel_compensate_overlapping_walls_enabled_schematic.svg)
![Alle lijnen worden over hun volle breedte geëxtrudeerd, waardoor een deel te breed is.](../../../articles/images/travel_compensate_overlapping_walls_enabled_disabled.png)
![De helft van de lijnen is verkleind in de breedte, wat resulteert in nauwkeuriger printen.](../../../articles/images/travel_compensate_overlapping_walls_enabled_enabled.png)

De lijnbreedte van de buitenwand die een andere buitenwand overlapt, wordt verminderd met het overlapgebied. Dit compenseert de over-extrusie.

Zoals hierboven beschreven, heeft dit de neiging de maatnauwkeurigheid te verbeteren. Het nadeel is echter dat de doorvoersnelheid ongelijker wordt, wat resulteert in onder-extrusie op sommige plaatsen en over-extrusie op andere. Ook kan de doorvoersnelheid onder de minimale doorvoersnelheid van nozzle en de extruderinstelling komen, wat resulteert in een onregelmatige doorvoer en druppelen. Om dit effect te verminderen, kunt u de [Minimale wandstroom](wall_min_flow.md) instellen, waardoor enkele van de dunste wanden in verplaatsingen worden omgezet ten koste van de maatnauwkeurigheid.

**Deze instelling ziet er nogal lelijk uit in de laagweergave. Bij echt printen zijn er geen grenzen tussen de regels. In de laagweergave worden alleen de paden van de G-code weergegeven, maar in werkelijkheid wordt het materiaal opzij geschoven door de andere wand waarmee het overlapt. Zelfs kleine verminderingen van de doorvoer worden niet weerspiegeld in de daadwerkelijke print, omdat de doorvoersnelheid door nozzle zich niet zo snel kan aanpassen. Deze effecten zorgen ervoor dat de daadwerkelijke print vloeiender is dan de plakweergave laat zien.**