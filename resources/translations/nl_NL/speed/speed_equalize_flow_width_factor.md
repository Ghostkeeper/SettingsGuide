Verhouding voor afstemmen doorvoer
====
Met deze functie kunt u de manier wijzigen waarop uw printer de lijnbreedte aanpast: in plaats van de doorvoer van het materiaal door de nozzle te veranderen, verandert de printer de snelheid waarmee nozzle beweegt.

FFF-printers zijn notoir slecht in het veranderen van de snelheid waarmee materiaal uit nozzle stroomt. Wanneer de printer de snelheid van de doorvoer verandert, duurt het een fractie van een seconde voordat dit zich daadwerkelijk vertaalt in een verandering in de doorvoer. Afhankelijk van de printsnelheid kan de nozzle tegen die tijd al enkele millimeters voorbij het punt zijn waar de doorvoer had moeten worden aangepast. Het is nog erger met Bowden-buisprinters.

In plaats van de doorvoersnelheid te wijzigen, kan de printer ook de verplaatsingssnelheid van de printkop wijzigen. De printkop kan veel sneller accelereren, wat een betere controle geeft over de breedte van de lijn. Als de printkop met dezelfde invoersnelheid versnelt, wordt dezelfde hoeveelheid materiaal over een grotere lengte uitgerekt, waardoor de lijnbreedte kleiner wordt. Wanneer de printkop langzamer print, wordt dezelfde hoeveelheid materiaal in een kleinere ruimte geprint, waardoor de lijnbreedte toeneemt.

Deze instelling is een relatie. Het kan de doorvoer (0%) of de printsnelheid (100%) of een combinatie van beide instellen. De verhouding kan zelfs meer dan 100% zijn, wat betekent dat nozzle wordt verlaagd om dikkere lijnen te creëren, maar de snelheid nog meer wordt verlaagd om te compenseren.

Het verhogen van deze verhouding naar 100% betekent dat snelheid wordt gebruikt in plaats van doorvoer om de lijnbreedte te veranderen, wat de druk als volgt beïnvloedt:
* De lijndikte is waarschijnlijk nauwkeuriger, wat de maatnauwkeurigheid van de print verbetert.
* De doorvoer blijft hetzelfde, waardoor het printen betrouwbaarder wordt, vooral voor exotische materialen.
* Op sommige plaatsen beweegt de printkop sneller, waardoor rimpelen ontstaat.

Deze instelling is alleen van toepassing op de variaties in lijndikte die worden veroorzaakt door het aanpassen van de lijnen aan de breedte van dunne delen en scherpe hoeken. Veranderingen in de doorvoer als gevolg van instellingen zoals verschillende lijnbreedtes voor vulling versus wanden worden niet gecompenseerd, evenmin als functies zoals overbrugging of strijken. Printers die Linear Advance of soortgelijke compensatiefuncties gebruiken, moeten deze ook gebruiken als deze instelling is ingesteld op 100%, omdat doorvoer veranderingen als gevolg van deze instellingen nog steeds kunnen optreden.