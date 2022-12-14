Printschok (jerk)
====
De jerk bepaalt de snelheid waarmee de nozzle door de bochten kan. Bij hoge schokniveaus zal nozzle niet zo veel vertragen bij het naderen van een bocht, wat resulteert in een meer constante snelheid maar ook meer trillingen.

**Schok (Jerk) in 3D-printen is niet hetzelfde als jerk in de natuurkunde.** De term 'jerk(schok)' is geïntroduceerd door Marlin. Het werd daar ontwikkeld als een remedie voor het inherente probleem om te proberen een pad perfect te volgen. Aangezien nozzle (theoretisch) niet van het pad mag afwijken, zou het in elke hoek moeten vertragen tot 0 mm/s. Dit zou uw print verpesten, omdat vertragen tot 0 mm/s een klodder in elke hoek zou veroorzaken. nozzle mag niet buigen om hoeken af ​​te snijden of doorschieten. In plaats daarvan laat Marlin de snelheidsvector onmiddellijk veranderen op elke hoek. De grootte van deze verandering in snelheidsvector wordt "Schok" genoemd. Dus de schok is de maximale momentane verandering in snelheid op elke hoek van de beweging.

Het verhogen van de jerk heeft een aantal positieve en enkele negatieve effecten op je druk:
* De printtijd wordt verkort doordat de nozzle minder vertraagt ​​in de hoeken.
* Doordat de nozzle niet afremt tot stilstand, krijg je minder klodders in de hoeken. nozzle beweegt in een meer constant tempo, zodat het niet in de hoek blijft hangen terwijl het materiaal uit de opening blijft stromen.
* De printer trilt over het algemeen meer bij elke hoek omdat de printkop de instructie krijgt om onmiddellijk van richting te veranderen met een theoretisch oneindige acceleratie. Deze trillingen hebben de neiging om hobbels in uw print te veroorzaken, wat resulteert in verminderde maatnauwkeurigheid.
* Bij extreme waarden bestaat de kans dat je motoren wat stappen in de bochten verliezen, waardoor er een laagverschuiving kan ontstaan.