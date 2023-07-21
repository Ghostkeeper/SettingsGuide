Schok (jerk) regulering Inschakelen
====
De jerk bepaalt de snelheid waarmee de nozzle door de bochten kan. Wanneer jerk control is ingeschakeld, bepaalt Cura hoeveel jerk moet worden toegepast tijdens de verschillende delen van de print. Indien uitgeschakeld, kiest de printerfirmware een schokwaarde. De schokwaarde van de printer is meestal vrij hoog om de slicer meer controle te geven, maar hij heeft mogelijk meer informatie over zijn eigen hardware dan Cura.

![De relatie tussen snelheid, acceleratie en schok](../../../articles/images/velocity_acceleration_jerk.svg)

**Een schok in 3D-printen is niet hetzelfde als een schok in de natuurkunde.** De term 'schok (jerk)' is geïntroduceerd door Marlin. Het werd daar ontwikkeld als een remedie voor het inherente probleem om een traject perfect te volgen. Aangezien nozzle (theoretisch) niet van het pad mag afwijken, zou het in elke hoek moeten vertragen tot 0 mm/s. Dit zou uw print verpesten, omdat vertragen tot 0 mm/s een klodder in elke hoek zou veroorzaken. nozzle mag niet buigen om hoeken af te snijden of doorschieten. In plaats daarvan laat Marlin de snelheidsvector onmiddellijk veranderen op elke hoek. De grootte van deze verandering in snelheidsvector wordt "schok" genoemd.

Dus de schok is de maximale momentane verandering in snelheid die optreedt bij elke hoek van de beweging.

Niet-Marlin-gebaseerde firmware, zoals de Sailfish-firmwarefamilie, negeert veranderingen in jerk. Deze instelling heeft dan geen effect.

Voorbeeld van de wiskunde van de schok (jerk)
----
Laten we als voorbeeld een heel eenvoudige print nemen: eerst 100 mm naar rechts, dan 100 mm naar beneden. De printsnelheid is ingesteld op 50 mm/s. acceleratie is ingesteld op 1000 mm/s^2. De schok is ingesteld op 10 mm/s. Dat zal gebeuren:
1. Aan het begin van een print heeft Marlin de helft van de schokwaarde nodig om te starten, dus theoretisch versnelt het onmiddellijk naar 5 mm/s.
2. Met een acceleratie van 1000 mm/s^2 duurt het 0,045 s om van 5 mm/s naar de maximale snelheid van 50 mm/s te accelereren. Gedurende deze tijd beweegt nozzle 1.2375 mm.
3. De nozzle beweegt een tijdje met de maximale printsnelheid van 50 mm/sec.
4. Marlin berekent hoe snel de nozzle door de hoek kan gaan: De nozzle maakt een hoek van 90 graden, eerst naar rechts, dan naar beneden. Om deze snelheidsverandering te beperken, gaat hij de hoek naar rechts in bij cos(90/2) * (10/2) mm/s en terug naar beneden bij cos(90/2) * (10/2) mm/s rijden uit. Hij gaat dus met ongeveer 7,07 mm/s door de hoek.
5. Het duurt 0,043 s om te vertragen van een snelheid van 50 mm/s naar 7,07 mm/s.
6. De bocht wordt genomen met een onmiddellijke snelheidsverandering. De absolute waarde van het verschil tussen de vectoren [7,07, 0] en [0, 7,07] is precies 10 mm/s, zodat de kromme direct kan worden doorlopen.
7. Het duurt 0,043 s om te versnellen van 7,07 mm/s naar 50 mm/s.
8. De nozzle draait weer een tijdje op de maximale printsnelheid van 50 mm/s.
9. Tegen het einde van het printproces wordt nozzle vertraagd van 50 mm/s naar 0 mm/s in 0,05 s.