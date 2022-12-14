Buitencontour Spiraliseren
====
Het spiraliseren van de buitencontour is een speciaal geval.

Als u laag voor laag print, moet de nozzle normaal gesproken van de ene laag naar de volgende gaan. Deze beweging zorgt ervoor dat nozzle bijna een fractie van een seconde stilstaat, waardoor een naad op het oppervlak achterblijft die bekend staat als de Z-naad. Deze instelling is ontworpen om dat en meer te voorkomen. Het vereenvoudigt het printproces aanzienlijk door veel aspecten van het proces te elimineren.

Bij het spiraliseren van het model krijgt het model geen vulling of toppen. Er wordt slechts één wand en één verdieping verkregen. Wanneer de optie [Gespiraliseerde contouren effenen](smooth_spiralized_contours.md) is ingeschakeld, wordt de hoogte van nozzle geleidelijk verhoogd over de hoogte van één laag. Hierdoor ontstaat een spiraal die de contouren van het model volgt. Er is geen beweging van de ene laag naar de volgende omdat de nozzle al geleidelijk naar de volgende laag is verplaatst.

Spiralize-modus is gebruikelijk op veel slicers. Het wordt ook wel "vaasmodus" genoemd omdat het goed is voor het printen van vazen. Enkele andere eigenschappen zijn:
* Drukt extreem snel af.
* Het oppervlak wordt zeer glad. Er is niet langer een [Naden](../troubleshooting/seam.md) die deze naar de volgende laag verplaatst wanneer [Gespiraliseerde contouren effenen](smooth_spiralized_contours.md) is ingeschakeld.
* De druk zal niet erg stabiel zijn. Als het model te groot is, heeft het de neiging om te breken [Laag Splitsing](../troubleshooting/layer_splitting.md) vanwege de dunne wand.
*Terwijl het verwijderen van de stiksels de print waterdicht maakt, is het moeilijk om hem waterdicht te krijgen als de print eenmaal een bepaalde grootte heeft. Daarom is het aan te raden om minimaal 2 wanden te hebben. Het is dan niet meer mogelijk om de buitencontour te spiraliseren.

**Spiraliseren werkt niet goed op prints met veel horizontale vlakken. Het kan geen overhangen aan en geprint geen toppen, dus niets kan tegen een horizontaal oppervlak rusten. Het werkt ook niet goed als er meerdere delen op een laag staan.**