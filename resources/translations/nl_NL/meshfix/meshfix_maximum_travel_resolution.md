Maximale bewegingsresolutie
====
Als het model een zeer hoge resolutie heeft, zal Cura de resolutie verlagen zodat de processor van de printer de verwerking van de G-code-instructies tijdens de uitvoering kan bijhouden. De maximale resolutie van de routes kan bij het printen apart van de [Maximale resolutie](meshfix_maximum_resolution.md) worden bepaald.

Omdat verplaatsingen veel sneller worden uitgevoerd dan printbewegingen, loopt de printkop veel sneller door de lijnsegmenten van het verplaatspad dan andere lijnsegmenten. De CPU zou deze lijnsegmenten veel sneller moeten verwerken om de nozzle bij te houden. Om deze reden moet de resolutie van de verplaatsingen lager zijn dan de resolutie van de langzamere extrusiebewegingen.

Ook de resolutie van de beweging tijdens de verplaatsingen is vaak niet van belang voor de printkwaliteit. Omdat er niet wordt geëxtrudeerd, is er geen oppervlak dat wazig of gekarteld kan worden. Om deze reden heeft het verlagen van de resolutie van de routes geen noemenswaardige invloed op de printkwaliteit.

De meeste verplaatsingen van Cura zijn rechte lijnen. Dit zijn de snelste bewegingen en genereren de minste trillingen. Wanneer Cura echter bedoeld is om botsingen te vermijden, heeft het de neiging om het oppervlak van het te vermijden gebied te volgen. De route rondom dit gebied heeft dan een vergelijkbare resolutie als het te mijden gebied. Daarom heeft deze instelling geen echt effect tenzij [Combing-Modus](../travel/retraction_combing.md) is ingeschakeld.