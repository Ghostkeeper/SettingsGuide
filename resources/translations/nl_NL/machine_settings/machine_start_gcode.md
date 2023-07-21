Start G-code
====
Met deze instelling kan een stukje G-code worden geschreven om aan het begin van elke print te worden uitgevoerd. Deze G-code kan worden gebruikt om de printer klaar te maken om printen.

Enkele voorbeelden van dingen die vaak worden gedaan in de opstart-g-code zijn:
* Prime de nozzle(en).
* Opwarmen van de platform.
* Opwarmen van de nozzle(s).
* Zorg ervoor dat de juiste extruder is geselecteerd.
* Configureer ventilatoren, acceleratie of schok.
* Automatische bednivellering.
* Lineaire voeding configureren.

Voor een redelijk uitgebreide lijst van beschikbare g-codes om hier te schrijven, zie de [RepRap Wiki](https://reprap.org/wiki/G-code).

Verwijzingen naar instellingen
----
Bij het bewerken van de start-G-code kunt u verwijzen naar de waarden van andere instellingen. Hiervoor wordt een specifieke syntaxis gebruikt. Er wordt naar instellingen verwezen met hun *sleutel*. Deze sleutel is een interne naam in Cura. Het is niet zichtbaar in de gebruikersinterface. Voor een volledige lijst van alle sleutels, zie Cura's broncode in [dit document](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json).

De syntaxis om de waarde van een globale instelling te krijgen is als volgt:

`{setting_key}`

Met andere woorden, schrijf de sleutel van de instelling tussen accolades. Zo wordt de globale waarde van een instelling bepaald. Veel instellingen kunnen echter voor elke extruder anders zijn. Deze moeten als volgt worden aangeduid:

`{setting_key, #}`

Hier moet u in plaats van het "#"-symbool het nummer van de extruder schrijven waarvan u de instelling wilt krijgen. Extruders beginnen te tellen vanaf 0. Algemene instellingen kunnen ook worden verkregen door een extruder op te geven, maar deze zijn hetzelfde voor alle extruders. Als u een extruderspecifieke temperatuur probeert te krijgen zonder het extrudernummer op te geven, krijgt u de waarde voor de eerste extruder die niet is uitgeschakeld.

Deze referenties kun je bijvoorbeeld gebruiken voor het voorverwarmen tot de juiste temperatuur of het instellen van versnellingen. Hier zijn enkele voorbeelden:

`M104 S{material_print_temperature_layer_0, 0} ;voorverwarmen`

`M140 S{material_bed_temperature_layer_0} ;heat bed`

`M204 P{acceleration_print, 0} T{acceleration_travel, 0}`

`M205 X{jerk_print, 0}`

Wees voorzichtig met de snelheidsinformatie. G-code accepteert doorgaans doorvoersnelheden in millimeters per *minuut*, terwijl instellingen in millimeters per *seconde* zijn. Er is momenteel geen manier om de juiste voedingssnelheid te selecteren. Met deze referenties is het niet mogelijk om berekeningen uit te voeren.

Andere informatie
----
Sommige aanvullende informatie is ook beschikbaar via dezelfde syntaxis als de verwijzingen naar de instellingen:

* `{time}` verwijst naar de lokale tijd van de dag waarop het werd gesneden.
* `{date}` verwijst naar de datum waarop het werd gesneden.
* `{day}` verwijst naar de dag van de week waarop het werd gesneden.
* `{initial_extruder_nr}` verwijst naar de extruder die gaat printen.
<!--if cura_version>=4.12-->
* `{material_id}` verwijst naar een unieke identificatie voor het actieve materiaal. Specificeer de extruder vergelijkbaar met de andere instellingen.
* `{material_name}` verwijst naar de naam van het actieve materiaal. Dit is meestal de naam die je aantreft op een website waar het materiaal wordt verkocht.
* `{material_type}` verwijst naar de actieve materiaalklasse, zoals PLA of ABS.
* `{material_brand}` verwijst naar de fabrikant van het materiaal.
* `{print_time}` verwijst naar de geschatte duur van de print (opgemaakt volgens ISO-8601).
* `{filament_amount}` verwijst naar de gebruikte filamentlengte in meters, voor elke extruder afzonderlijk. Dit is opgemaakt als een lijst met vierkante haken.
* `{filament_weight}` verwijst naar het gewicht van het gebruikte filament in grammen, voor elke extruder afzonderlijk, opgemaakt als een lijst met vierkante haken. Als het spoelgewicht niet bekend is, is dit 0.
* `{filament_cost}` verwijst naar de kosten van het gebruikte filament, afzonderlijk voor elke extruder. De eenheid van de kosten is dezelfde als gespecificeerd op de materiaalbeheerpagina in de instellingen. Als de eenheid onbekend is, wordt deze op 0 gezet.
<!--endif-->

Warmte voor start G-code
----
Cura geeft automatisch verwarmingsopdrachten voordat uw opstart-G-code begint. Zo hoeft de opstart G-code er geen rekening mee te houden dat de nozzle verwarmd moet worden. U kunt direct beginnen met het verwarmen van nozzle. Als uw start-gcode een verwijzing naar een temperatuur bevat (voor nozzle of bed), wordt deze uitgeschakeld (respectievelijk voor nozzle of het bed).