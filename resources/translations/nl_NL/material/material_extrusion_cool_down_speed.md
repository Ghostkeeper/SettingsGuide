Aanpassing Afkoelsnelheid Doorvoer
====
Als [Automatische Temperatuurinstelling](../experimental/material_flow_dependent_temperature.md) is ingeschakeld, wordt de printtemperatuur aangepast aan de hoeveelheid geëxtrudeerd materiaal.

Wanneer het materiaal in de nozzlekamer opwarmt, onttrekt het warmte aan de nozzle. Hoe sneller het materiaal wordt geëxtrudeerd, hoe meer warmte er uit nozzle wordt gehaald. Als de temperatuursonde niet precies op de punt van de nozzle zit, zal de nozzle bij het extruderen van materiaal een iets lagere temperatuur hebben dan wanneer deze stationair draait, zelfs met een goede PID-regelaar.

Deze instelling beschrijft hoeveel warmte er tijdens het printen in de nozzle verloren gaat. De extra warmte die verloren gaat tijdens extrusie wordt dan gecompenseerd door de gewenste printtemperatuur uit de G-code te verhogen. De waarde van de instelling hangt af van het ontwerp van de nozzle, de warmtecapaciteit van het geprinte materiaal en de extrusiesnelheid.