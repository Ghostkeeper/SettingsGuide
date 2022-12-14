Inactive Nozzle vegen op primepijler
====
Indien ingeschakeld, veegt de printer het vorige nozzle af na het voorbereiden van het volgende nozzle in de primepijler.

De volgorde van gebeurtenissen is als volgt wanneer dit is ingeschakeld:
1. De printer schakelt over naar de nieuwe extruder.
2. De nieuwe extruder wordt voorbereid door een primepijler te printen.
3. nozzle dat vóór de extruderwissel actief was, wordt op de primepijler afgeveegd.
4. De printer blijft het onderdeel printen met de nieuwe extruder.

Houd er rekening mee dat wanneer u dit doet, de printer nozzle zal wissen dat actief was vóór de extruderwissel, niet het momenteel actieve nozzle. Als uw printer meerdere nozzles heeft die op een bepaalde afstand van elkaar staan, ziet u mogelijk enige beweging in de slice-weergave die nutteloos lijkt. Dit komt omdat het verplaatsen naar deze positie ervoor zorgt dat het vorige nozzle over de primepijler beweegt (die niet wordt weergegeven in de plakweergave).

Nadat een nozzle op stand-by gaat, is hij nog een tijdje behoorlijk heet. Terwijl het heet is, heeft er wat materiaal de neiging om eruit te sijpelen. Tijdens het primen van het volgende nozzle op de primepijler, heeft het de kans gehad om een beetje af te koelen, dus het sijpelen is vertraagd. Deze instelling zorgt ervoor dat het materiaal dat naar buiten drupt in het midden van de primepijler wordt weggeveegd, zodat het niet op de zijkant van je afgedrukte model terechtkomt.