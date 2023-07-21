Temperatuur voor voorbereiding van afbreken
====
Bij sommige printers moet het materiaal schoon worden afgebroken wanneer het wordt ingevoerd voor een filamentwisseling, zodat het zonder klitten door de feeder kan worden verplaatst. Deze instelling configureert een deel van de procedure om netjes af te sluiten.

Deze instelling past de temperatuur van nozzle aan wanneer het materiaal naar de tweede positie wordt teruggetrokken om het materiaal tot een dunne draad uit te rekken. Deze dunne draad steekt uit de verwarmde zone in de nozzle om deze te laten uitdruppelen en stollen. De dunne, harde materiaalstreng kan dan in de volgende fase van het intrekken worden afgebroken.

![Eerst wordt het materiaal naar binnen getrokken om druppen te verminderen.](../../../articles/images/filament_switch_anti_ooze.svg)
![Ten tweede wordt het filament langzaam doorgevoerd om een dunne draad te trekken die gemakkelijk te scheiden en te stollen is.](../../../articles/images/filament_switch_break_preparation.svg)
![Ten derde wordt het filament snel verder gevoerd om het filament te snijden.](../../../articles/images/filament_switch_break.svg)

**Deze instelling is momenteel niet zichtbaar in de interface van Cura. Het kan alleen worden ingesteld door de profielen. Het wordt ook niet gebruikt door Cura bij het snijden. Drukkers die het materiaalbestandsformaat van Cura begrijpen, kunnen het echter gebruiken om hun filamentwisselprocedure correct te configureren.**
Een nabewerkingsscript kan worden gebruikt om het commando `M600` in de print in te voegen, waardoor een filamentwisseling wordt geactiveerd.