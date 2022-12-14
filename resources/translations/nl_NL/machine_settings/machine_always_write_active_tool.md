Tool voor altijd actief schrijven
====
Deze instelling specificeert hoe bepaalde G-code-commando's met een gereedschapsparameter door de printer worden geïnterpreteerd. Sommige G-code-opdrachten kunnen een parameter bevatten die aangeeft op welke extruder het van toepassing is. Sommige firmware interpreteert deze parameter als een opdracht om naar die tool over te schakelen en vervolgens de G-code uit te voeren, terwijl sommige firmware deze parameter interpreteert als een opdracht om de G-code toe te passen op een andere extruder dan de momenteel actieve.

De enige commando's waarvoor dit geldt en die relevant zijn voor 3D printen zijn de commando's voor het verwarmen van de nozzles, `M104` en `M109`. Laten we het volgende voorbeeld nemen van een warmteopdracht die wordt uitgevoerd terwijl de eerste extruder (`T0`) aan het printen is:

`M104 S210 T1`

Er zijn twee mogelijke interpretaties van dit commando:
* Terwijl de eerste extruder doorgaat met printen, verwarmt u de tweede extruder tot 210°C. Dit is de interpretatie die wordt bepleit door Marlin, Reprap, Sailfish en hun afgeleide firmwarepakketten.
* Schakel eerst over naar de tweede extruder, verwarm vervolgens de tweede extruder tot 210°C. Dit is de interpretatie van Smoothieware en zijn afgeleide firmware.

Vanwege Cura's strategie voor temperatuurbeheersing is het nooit nodig om de tweede interpretatie uit te voeren. Als de printer het g-code-commando op de tweede manier interpreteert, schrijft Cura in plaats daarvan de volgende g-code:

`M104 S210 T1`

`T0`

In wezen weet hij dat de printer als gevolg van deze opdracht naar de tweede extruder zal overschakelen, dus hij moet terugschakelen naar de eerste extruder om daar verder te gaan met printen.

**Omdat dit een machine-instelling is, wordt deze normaal gesproken niet vermeld in de normale lijst met instellingen.**