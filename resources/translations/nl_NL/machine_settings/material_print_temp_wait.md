Wachten op verwarmen van nozzle
====
De eerste laag kan een andere [Printtemperatuur van de eerste laag](../material/material_print_temperature_layer_0.md) hebben dan de [Printtemperatuur](../material/material_print_temperature.md). Als deze instelling is ingeschakeld, wacht de printer totdat deze temperatuur is bereikt voordat hij verder gaat met printen.

Het wacht tot de temperatuur is opgewarmd of afgekoeld tot de juiste temperatuur. Terwijl de identificatie van deze instelling zegt dat je moet wachten om op te warmen, koelt het ook af. nozzle wacht niet op andere temperatuurveranderingen, zoals: de [Starttemperatuur voor printen](../material/material_initial_print_temperature.md), de [Eindtemperatuur voor printen](../material/material_final_print_temperature.md) of de [Stand-bytemperatuur](../material/material_standby_temperature.md ). Wanneer u printt in [Printvolgorde](../blackmagic/print_sequence.md) zal de nozzle ook wachten tot de temperatuur van de eerste laag is bereikt als het moet terugkeren naar de eerste laag voor de volgende objecten.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**