Eind G-code
====
Met deze instelling kan een stukje g-code worden geschreven om aan het einde van elke print te worden uitgevoerd. Met deze g-code kan de printer zijn componenten afsluiten en opruimen na het printen.

Enkele voorbeelden van dingen die vaak worden gedaan in de eind-g-code zijn:

* Intrekken van het materiaal.
* Koeling van de nozzle(s).
* Koeling van de platform.
* Zet de ventilatoren uit.

Voor een redelijk uitgebreide lijst van beschikbare g-codes om hier te schrijven, zie de [RepRap Wiki](https://reprap.org/wiki/G-code).

Verwijzingen naar instellingen
----
Bij het bewerken van de eind-G-code kunt u verwijzen naar de waarden van andere instellingen. Hiervoor wordt een specifieke syntaxis gebruikt. Er wordt naar instellingen verwezen met hun *sleutel*. Deze sleutel is een interne naam in Cura. Het is niet zichtbaar in de gebruikersinterface. Voor een volledige lijst van alle sleutels, zie [dit document](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) in de Cura-broncode.

De syntaxis om de waarde van een globale instelling te krijgen is als volgt:

`{setting_key}`

Met andere woorden, schrijf de sleutel van de instelling tussen accolades. Zo wordt de globale waarde van een instelling bepaald. Veel instellingen kunnen echter voor elke extruder anders zijn. Deze moeten als volgt worden aangeduid:

`{setting_key, #}`

Hier moet u in plaats van het "#"-symbool het nummer van de extruder schrijven waarvan u de instelling wilt krijgen. Extruders beginnen te tellen vanaf 0. Algemene instellingen kunnen ook worden verkregen door een extruder op te geven, maar deze zullen voor alle extruders hetzelfde zijn. Als u een extruderspecifieke temperatuur probeert te krijgen zonder het extrudernummer op te geven, krijgt u de waarde voor de eerste extruder die niet is uitgeschakeld.

U kunt deze referenties b.v. Gebruik het bijvoorbeeld om af te koelen tot een stand-bytemperatuur of om de standaardversnelling en schok van de printer te herstellen. Hier zijn enkele voorbeelden:

`M104 T0 S{material_standby_temperature, 0} ;standby voor de volgende print`

`M104 T1 S{material_standby_temperature, 1}`

`M204 P{machine_acceleration} T{machine_acceleration}`

Wees voorzichtig met de snelheidsinformatie. G-code accepteert doorgaans doorvoersnelheden in millimeters per *minuut*, terwijl instellingen in millimeters per *seconde* zijn. Er is momenteel geen manier om de juiste voedingssnelheid te selecteren. Met deze referenties is het onmogelijk om berekeningen te maken.

Andere informatie
----
Er is ook wat aanvullende informatie beschikbaar met dezelfde syntaxis als voor verwijzingen naar instellingen:

* `{time}` verwijst naar de skinige lokale tijd van de dag waarop het werd gesneden.
* `{date}` verwijst naar de datum waarop het werd gesneden.
* `{day}` verwijst naar de dag van de week waarop het werd gesneden.
* `{initial_extruder_nr}` verwijst naar de extruder die gaat printen.
<!--if cura_version>=4.12-->
* `{material_id}` verwijst naar een unieke identificatie voor het actieve materiaal. Specificeer de extruder vergelijkbaar met andere instellingen.
* `{material_name}` verwijst naar de naam van het actieve materiaal. Dit is meestal de naam die je aantreft op een website waar het materiaal wordt verkocht.
* `{material_type}` verwijst naar de actieve materiaalklasse, zoals PLA of ABS.
* `{material_brand}` verwijst naar de fabrikant van het materiaal.
<!--endif-->

**Deze instelling is een apparaatinstelling en komt daarom niet voor in de normale lijst met instellingen. Het kan worden gewijzigd door op "Apparaatinstellingen" te klikken in de lijst met printers in het instelling