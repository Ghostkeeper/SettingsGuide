Maximale Filamentacceleratie
====
Deze instelling specificeert de maximale acceleratie die de invoermotoren van uw printer aankunnen, volgens de firmware van de printer.

Deze instelling wordt alleen gebruikt om de juiste tijdschattingen te krijgen. De door Cura ingestelde [Printacceleratie](../speed/acceleration_print.md) kent geen limiet, maar Cura gaat ervan uit dat je firmware een specifieke limiet per as instelt. Als de acceleratie voor de feeder deze instelling overschrijdt, wordt de tijdschatting van deze bewegingen aangepast om aan te nemen dat uw firmware de acceleratie beperkt. De totale acceleratie kan nog groter zijn bij diagonaal accelereren met meerdere assen tegelijk.

Het komt vaak voor dat de acceleratiegrenzen voor de feeder worden bereikt omdat (afhankelijk van de firmware) de door Cura ingestelde acceleratie ook de feeder beïnvloedt. Het is dus van cruciaal belang dat deze instelling correct is geconfigureerd om de juiste tijdschattingen voor retraites te krijgen.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**