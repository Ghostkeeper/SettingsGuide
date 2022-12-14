Grafiek Doorvoertemperatuur 
====
Als je sneller wilt printen, kun je het beste op een iets hogere temperatuur printen. Hierdoor wordt het thermoplastische materiaal vloeibaarder en kan het sneller uit de nozzle stromen. Als [Automatische Temperatuurinstelling](materiaaldoorvoer_afhankelijke_temperatuur.md) is ingeschakeld, specificeert deze instelling bij welke temperatuur het materiaal moet worden geprint voor elke doorvoersnelheid. nozzle wordt dan gemiddeld voor elke laag om een ​​temperatuur voor die laag te bepalen.

Doorvoer wordt berekend in kubieke millimeters per seconde, gemiddeld over een hele laag. De temperatuur wordt gegeven in graden Celsius. De waarde van deze instelling moet een door komma's gescheiden lijst van coördinaten zijn. Elke coördinaat heeft de vorm `[<flow>, <temperatuur>]`.

Het doel van deze instelling is om een ​​betere printkwaliteit te bereiken door over- en onder-extrusie tijdens grote doorvoerveranderingen binnen een print te verminderen. Een veelvoorkomend geval hiervoor is de grens tussen de buitenskin en de vulling. Omdat de skin meestal veel langzamer wordt geprint dan de infill, moeten de lagen met veel infill op een iets hogere temperatuur worden geprint, zodat het materiaal goed kan extruderen terwijl de infill wordt geprint.

In veel printers heeft de PID-controller die de temperaturen in nozzle van de printer regelt de neiging om overdreven te reageren wanneer er in korte tijd veel temperatuurveranderingen zijn. Hierdoor kan de printtemperatuur erg onnauwkeurig zijn bij gebruik van deze instelling.

**Deze instelling is momenteel niet zichtbaar in de interface van Cura en kan niet worden geactiveerd.**