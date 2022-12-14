Afvoersnelheid flush
====
Wanneer de printer het filament voor een nozzle moet vervangen, moet hij het resterende materiaal dat zich nog in de nozzlekamer bevindt, wegspoelen. Deze instelling bepaalt hoe snel het filament door de feeder wordt geduwd om het oude materiaal weg te spoelen.

Dit geldt alleen na het overstappen op een andere materiaalsoort. Als hetzelfde materiaaltype opnieuw wordt geladen (bijvoorbeeld omdat de vorige spoel leeg was), wordt een andere [Afvoersnelheid einde van filament](material_end_of_filament_purge_speed.md) gebruikt.

**Deze instelling is momenteel niet zichtbaar in de interface van Cura. Het kan alleen worden ingesteld door de profielen. Het wordt ook niet gebruikt door Cura bij het snijden. Drukkers die het materiaalbestandsformaat van Cura begrijpen, kunnen het echter gebruiken om hun filamentwisselprocedure correct te configureren.**
Een nabewerkingsscript kan worden gebruikt om het commando `M600` in de print in te voegen, waardoor een filamentwisseling wordt geactiveerd.