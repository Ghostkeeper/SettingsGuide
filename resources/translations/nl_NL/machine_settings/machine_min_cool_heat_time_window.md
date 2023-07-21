Minimale tijd stand-by temperatuur
====
Deze instelling configureert de minimale stand-bytijd voor nozzle om af te koelen tot de stand-bytemperatuur. Als nozzle is ingesteld op een kortere periode dan deze stand-bytijd, wordt het niet afgekoeld maar blijft het op de [Eindtemperatuur voor printen](../material/material_final_print_temperature.md).

Uw nozzle heeft een PID-controller die regelt hoeveel energie wordt gebruikt om uw nozzle te verwarmen om de juiste temperaturen te bereiken. Wanneer nozzle wordt bevolen om snel achter elkaar af te koelen en op te warmen met grote temperatuurverschillen, heeft de PID-regelaar de neiging om het vereiste verwarmingsvermogen verkeerd te voorspellen. Dit leidt tot grote schommelingen in de werkelijke nozzle-temperatuur. Dit kan worden gebruikt om te voorkomen dat de [Stand-bytemperatuur](../material/material_standby_temperature.md) wordt bereikt wanneer nozzle voor een zeer korte tijd inactief is.

De optimale waarde voor deze instelling hangt af van de instelling van uw PID-regelaar. Sommige regelaars kunnen snellere veranderingen in de doeltemperatuur beter aan dan andere, en deze zijn mogelijk beter in staat om een korte standby-periode aan te kunnen. Een lagere instelling zou dan helpen voorkomen dat het materiaal in nozzle vergaat.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**