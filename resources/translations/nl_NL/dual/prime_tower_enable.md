Primepijler Inschakelen
====
Hiermee wordt een toren van een mix van materialen op je platform geprint. De toren is bedoeld om weggegooid te worden, maar dient om het materiaal voor te bereiden na elke extruderwissel.

![Hoe een Primepijler eruit ziet en wat de afmetingen zijn](../../../articles/images/prime_tower.svg)

Terwijl andere extruders aan het printen zijn, kan een nozzle wat materiaal uitstoten, waardoor de nozzlekamer leeg blijft. Een latere voorbereiding van het materiaal is essentieel, anders zal het materiaal in het begin niet goed vloeien.

De primepijler bestaat uit een buitenschil die per laag volledig geprint wordt met een extruder. Dit is nodig om de torenstabiliteit te garanderen, maar vereist soms extra extruderveranderingen voor sommige printen. Alle andere extruders printen in lussen in deze schaal en voeren hun materiaal af in de toren, bij voorkeur langs de binnenwanden. Deze extruders hoeven niet te primen als ze toevallig in de laag beginnen, omdat ze dan niet in de stand-bymodus gaan.

Het materiaal dat voor de buitenschaal is gekozen, is het materiaal met de grootste [Hechtingsgevoeligheid](../material/material_adhesion_tendency.md). Dit is een verborgen instelling die niet kan worden gewijzigd via de gebruikersinterface en bepaalt hoe goed de lagen aan elkaar blijven plakken. Door het materiaal te kiezen met de grootste hechting tussen de lagen, wordt het risico op het breken van de primepijler geminimaliseerd. Als meerdere materialen dezelfde hechtingsneiging hebben (bijvoorbeeld bij tweekleurenprints met hetzelfde type materiaal), wordt het laagste aantal extruders gekozen.

Naast het primen maakt nozzle ook een beweging in de toren om materiaal van nozzle weg te vegen dat zich tijdens de standby-modus heeft opgehoopt. Dit voorkomt dat het slib aan het geprinte materiaal blijft kleven. Om deze reden wordt de primepijler ook wel eens *veegtoren* genoemd.

De nadelen van de primepijler zijn dat het extra tijd kost om te printen en wat ruimte in beslag neemt op de platform.