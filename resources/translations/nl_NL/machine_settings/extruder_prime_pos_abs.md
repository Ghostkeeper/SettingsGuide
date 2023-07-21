Absolute Positie voor Primen Extruder
====
Wanneer de [Primeblob inschakelen](../platform_adhesion/prime_blob_enable.md) wordt gebruikt, kan de positie van deze indent-methode worden ingesteld met een [X](../platform_adhesion/extruder_prime_pos_x.md) en [Y](.. /platform_adhesion/ extruder_prime_pos_y.md) positie kan worden ingesteld. Deze instelling bepaalt of het de positie op de platform is of een positie ten opzichte van de skin printerpositie.

Als deze instelling is ingeschakeld, zijn de X- en Y-coördinaten relatief ten opzichte van een specifieke vaste positie op de platform. De extruder zal altijd daarheen bewegen om een Primeblob te creëren.

Als deze instelling is uitgeschakeld, verwijzen de X- en Y-coördinaten naar de positie waarin de nozzle zich bevindt wanneer deze voor het eerst naar die extruder overschakelt. Voor de eerste extruder zou dit de coördinaat [0,0] zijn. Voor de andere extruders zou dit hun startpositie zijn zoals gedefinieerd in het definitiebestand van de extruder. Deze uitgangspositie kan ook relatief zijn.

Het wordt sterk aanbevolen om een absolute startpositie te gebruiken. Een absolute startpositie is gegarandeerd vrij van botsingen met andere delen van de print, aangezien je op die plek geen objecten op de platform kunt plaatsen. Een relatieve inspringpositie kan overal op de platform zijn, waardoor u ergens op de eerste laag kunt beginnen. Het gebruik van een relatieve inspringpositie kan wat tijd besparen, maar het is het risico niet waard.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**