Intrekpositie voor voorbereiding van afbreken
====
Bij sommige printers moet het materiaal bij het invoeren schoon worden afgebroken voor een filamentwisseling om het door de feeder te verplaatsen zonder in de war te raken. Deze instelling configureert een deel van de procedure om netjes af te sluiten.

Deze instelling past de tweede positie aan waarnaar het materiaal wordt gevoerd om het materiaal tot een dunne draad uit te rekken. Deze dunne draad steekt uit de verwarmde zone in de matrijs om deze te laten uitdruppelen en stollen. De dunne, harde materiaalstreng kan dan worden afgebroken in de volgende stap van het inrijgen.

![Eerst wordt het materiaal naar binnen getrokken om druppelen te verminderen.](../../../articles/images/filament_switch_anti_ooze.svg)
![Ten tweede wordt het filament langzaam doorgevoerd om een dunne draad te trekken die gemakkelijk te scheiden en te stollen is.](../../../articles/images/filament_switch_break_preparation.svg)
![Ten derde wordt het filament snel verder gevoerd om het filament te snijden.](../../../articles/images/filament_switch_break.svg)

**Deze instelling is momenteel niet zichtbaar in de interface van Cura. Het kan alleen worden ingesteld door de profielen. Het wordt ook niet gebruikt door Cura bij het snijden. Drukkers die het materiaalbestandsformaat van Cura begrijpen, kunnen het echter gebruiken om hun filamentwisselprocedure correct te configureren.**
Een nabewerkingsscript kan worden gebruikt om het commando `M600` in de print in te voegen, waardoor een filamentwisseling wordt geactiveerd.