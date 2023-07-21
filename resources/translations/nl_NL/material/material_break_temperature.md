Temperatuur voor afbreken
====
Bij sommige printers moet het materiaal schoon worden afgebroken wanneer het wordt ingevoerd voor een filamentwisseling, zodat het zonder klitten door de feeder kan worden verplaatst. Deze instelling configureert een deel van de procedure om netjes af te sluiten.

Deze instelling stelt de temperatuur in waarop moet worden afgekoeld voordat het filament afbreekt. Deze afkoeling vindt plaats tussen de tweede en derde fase (zoals weergegeven in de onderstaande afbeeldingen). Het doel is om het filament te laten uitharden zodat de printer het netjes kan afbreken, in plaats van het eruit te trekken in een lange streng die in de feeder zou kunnen blijven haken.

![Eerst wordt het materiaal naar binnen getrokken om druppelen te verminderen.](../../../articles/images/filament_switch_anti_ooze.svg)
![Ten tweede wordt het filament langzaam doorgevoerd om een dunne draad te trekken die gemakkelijk te scheiden en te stollen is.](../../../articles/images/filament_switch_break_preparation.svg)
![Ten derde wordt het filament snel verder gevoerd om het filament te snijden.](../../../articles/images/filament_switch_break.svg)

**Deze instelling is momenteel niet zichtbaar in de interface van Cura. Het kan alleen worden ingesteld door de profielen. Het wordt ook niet gebruikt door Cura bij het snijden. Drukkers die het materiaalbestandsformaat van Cura begrijpen, kunnen het echter gebruiken om hun filamentwisselprocedure correct te configureren.**
Een nabewerkingsscript kan worden gebruikt om het commando `M600` in de print in te voegen, waardoor een filamentwisseling wordt geactiveerd.