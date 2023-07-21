Verwarmingssnelheid
====
Deze instelling vertelt Cura hoe snel uw printer dat nozzle kan opwarmen. Het wordt gebruikt om te voorspellen wanneer nozzle moet worden voorverwarmd voordat van extruder wordt gewisseld.

![De nozzles worden verwarmd voordat de extruder wordt omgeschakeld.](../../../articles/images/temperature_regulation.svg)

Bij het wisselen van nozzles zal Cura de volgende nozzle voorverwarmen voordat deze moet worden gebruikt, zodat deze klaar is voor gebruik wanneer de andere extruder net klaar is. Het doet dit door het verschil tussen de skinige nozzletemperatuur en de doelnozzletemperatuur te nemen en dit te delen door de verwarmingssnelheid om een tijdsduur te krijgen voor het voorverwarmen van nozzle.

Als de nozzle inderdaad sneller opwarmt dan deze instelling aangeeft, zal de nozzle enige tijd op de doeltemperatuur zijn voordat de andere extruder klaar is met printen. Gedurende deze tijd zal er wat materiaal uitlekken en kan het plastic een beetje in de nozzle degraderen, wat resulteert in [Onder-extrusie](../troubleshooting/underextrusion.md).

Als de nozzle inderdaad langzamer opwarmt dan deze instelling aangeeft, zal de printer bij de extruderschakelaar moeten wachten tot de nozzle de gewenste temperatuur heeft om te printen. Dit zal wat extra tijd kosten. Ook wordt tijdens dit wachten de vorige extruder op de uiteindelijke printtemperatuur gehouden, waardoor deze meer materiaal aanzuigt en het plastic in de nozzle weer afbreekt. Dit is nodig om te voorkomen dat het materiaal tijdens het snijden verder afkoelt dan Cura verwachtte, waardoor het temperatuurverschil groter zou zijn dan Cura verwacht en dus de volgende keer nog langer wachten. Dit zou resulteren in een op hol geslagen effect, waarbij de voorspelling met elke laag slechter wordt, dus Cura moet het vorige materiaal warm houden,

De werkelijke verwarmingssnelheid is geen constante snelheid in graden per seconde. Het hangt veeleer af van het verschil tussen de skinige nozzletemperatuur en de temperatuur van het bouwvolume. Als de printer koud is, warmt hij sneller op en als hij dichter bij de doeltemperatuur komt, warmt hij langzamer op. Ook de PID-controller van de printer speelt hierin een grote rol. De meeste regelaars vertragen de verwarming net voordat de doeltemperatuur wordt bereikt om doorschieten te voorkomen. Als je dit instelt, probeer dan de tijd te meten die nodig is om van [Stand-bytemperatuur](../material/material_standby_temperature.md) naar [Starttemperatuur voor printen](../material/material_initial_print_temperature.md) te gaan om op te warmen. Dit is het belangrijkste stukje informatie dat Cura probeert te voorspellen.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**