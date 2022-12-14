
Materiaal temperatuur invoeren
====
Deze instelling vertelt de slicing-backend of er al dan niet opdrachten moeten worden geschreven voor de temperatuur van de platvorm aan het begin van de print vóór de start-gcode. Het wordt automatisch ingesteld aan het begin van een slice.

Voor de meeste bewerkingen tijdens [Start G-Code](machine_start_gcode.md) is het zinvol om de platvorm op de juiste temperatuur te krijgen voor het printen. Om het voor ontwikkelaars van printerdefinities gemakkelijker te maken, verwarmt Cura automatisch de platvorm voordat de opstart-g-code wordt uitgevoerd. Als de start-G-code echter een verwijzing naar de temperatuur van de platvorm bevat, zal de platvorm niet meer automatisch opwarmen.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst. Het wijzigen heeft ook geen effect omdat Cura het automatisch zal veranderen.**