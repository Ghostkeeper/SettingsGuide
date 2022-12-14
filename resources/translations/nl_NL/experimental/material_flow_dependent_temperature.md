Automatische Temperatuurinstelling
====
Als je sneller wilt printen, kun je het beste op een iets hogere temperatuur printen. Hierdoor wordt het thermoplastische materiaal vloeibaarder en kan het sneller uit de nozzle stromen. Deze instelling past automatisch de temperatuur aan, afhankelijk van de gemiddelde doorvoer van het materiaal uit de nozzle.

Raadpleeg de [Grafiek Doorvoertemperatuur](material_flow_temp_graph.md) om te weten hoeveel de temperatuur moet worden aangepast. De doorvoer wordt berekend in kubieke millimeters per seconde. Als je dit in de printtemperatuur relatie zet, krijg je een bepaalde temperatuur. Deze temperatuur wordt dan gebruikt als printtemperatuur. Als deze instelling geactiveerd is, wordt de normale [Printtemperatuur](../material/material_print_temperature.md) niet meer gebruikt, maar de temperatuur berekend uit de doorvoer.

Het doel van deze instelling is om een ​​betere printkwaliteit te bereiken door over- en onder-extrusie tijdens grote stroomveranderingen binnen een print te verminderen. Een veelvoorkomend geval hiervoor is de grens tussen de buitenskin en de vulling. Omdat de skin meestal veel langzamer wordt geprint dan de infill, moeten de lagen met veel infill op een iets hogere temperatuur worden geprint, zodat het materiaal goed kan extruderen terwijl de infill wordt geprint.

In veel printers heeft de PID-controller die de temperaturen in nozzle van de printer regelt de neiging om overdreven te reageren wanneer er in korte tijd veel temperatuurveranderingen zijn. Hierdoor kan de printtemperatuur erg onnauwkeurig zijn bij gebruik van deze instelling.

**Deze instelling is momenteel niet zichtbaar in de interface van Cura en kan niet worden geactiveerd.**