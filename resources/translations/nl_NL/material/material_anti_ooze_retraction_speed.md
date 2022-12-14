Intreksnelheid voor niet-uitlopen
====
Bij sommige printers moet het materiaal schoon worden afgebroken wanneer het wordt ingevoerd voor een filamentwisseling, zodat het zonder klitten door de feeder kan worden verplaatst. Deze instelling configureert een deel van de procedure om netjes af te sluiten.

Deze instelling regelt de snelheid waarmee het materiaal naar de eerste positie wordt gevoerd om te voorkomen dat het opraakt. Het materiaal is op dit moment nog niet afgebroken. Het doel is eenvoudig om de druk op de nozzlekamer snel te ontlasten door deze naar binnen te trekken.

![Eerst wordt het materiaal naar binnen getrokken om druppelen te verminderen.](../../../articles/images/filament_switch_anti_ooze.svg)
![Ten tweede wordt het filament langzaam doorgevoerd om een ​​dunne draad te trekken die gemakkelijk te scheiden en te stollen is.](../../../articles/images/filament_switch_break_preparation.svg)
![Ten derde wordt het filament snel verder gevoerd om het filament te snijden.](../../../articles/images/filament_switch_break.svg)

**Deze instelling is momenteel niet zichtbaar in de interface van Cura. Het kan alleen worden ingesteld door de profielen. Het wordt ook niet gebruikt door Cura bij het snijden. Drukkers die het materiaalbestandsformaat van Cura begrijpen, kunnen het echter gebruiken om hun filamentwisselprocedure correct te configureren.**
Een nabewerkingsscript kan worden gebruikt om het commando `M600` in de print in te voegen, waardoor een filamentwisseling wordt geactiveerd.