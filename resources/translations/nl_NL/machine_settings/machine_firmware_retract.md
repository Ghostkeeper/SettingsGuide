Intrekken via firmware
====
Normaal gesproken veroorzaakt Cura een feed door de beweging van de feeder te regelen en hem te vertellen het filament een beetje naar binnen te trekken. Als deze instelling is ingeschakeld, wordt in plaats daarvan een `G10`-commando geschreven, wat betekent dat de printer het filament moet invoeren, of een `G11`-commando om verder te gaan.

Als u ervoor kiest om firmware-feeds te gebruiken, bepaalt de firmware van de printer hoe ver en hoe snel het filament moet worden ingevoerd. De printer weet misschien meer over zijn eigen geometrie dan Cura, waardoor hij beter kan beslissen hoe het filament moet worden ingevoerd. Hierdoor heeft Cura echter geen controle meer over deze inkepingen en weet Cura meer over de print zelf. Kortom, de slicer en de firmware hebben verschillende informatie, en deze instelling bepaalt welke van de twee de keuze heeft.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**