Minimale Doorvoersnelheid
====
De Marlin-firmware voor 3D-printers, waarvan de meeste printerfirmwares zijn afgeleid, heeft een minimumsnelheid voor al zijn bewegingen. Deze instelling geeft aan wat deze minimumsnelheid is voor de firmware van uw printer.

De minimale snelheid is een aanpassing om fouten in de firmware door deling door nul te voorkomen. De firmware moet de tijdsintervallen tussen stappen berekenen om een signaal met de juiste timing naar de motoren te sturen. Als de motor met 0 snelheid moet bewegen (d.w.z. stilstand), zou dat een oneindig tijdsinterval zijn dat de firmware niet goed aankan. Dit is echter alleen het geval als geen van de motoren van de printer daadwerkelijk draait. Bij beweging in de X-richting bijvoorbeeld draait de Y-as motor nog niet, maar door de fijne kneepjes van stappenmotoren is de minimale voeding hier niet van toepassing.

Cura gebruikt dit minimale voorschot om correcte tijdsinschattingen te maken. Het wordt toegepast bij het versnellen aan het begin van een print of na een pauze, en bij het vertragen tot stilstand aan het einde van een print of voor een pauze.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**