Intreksnelheid voor afbreken
====
Bij sommige printers moet het materiaal schoon worden afgebroken wanneer het wordt ingevoerd voor een filamentwisseling, zodat het zonder klitten door de feeder kan worden verplaatst. Deze instelling configureert een deel van de procedure om netjes af te sluiten.

Deze instelling regelt de snelheid waarmee het materiaal wordt aangezogen, waardoor uiteindelijk het filament van het bit afbreekt dat onvermijdelijk in nozzle achterblijft. Hoewel het stuk in nozzle niet kan worden uitgetrokken vanwege de gesmolten toestand, mag het deel dat wordt uitgetrokken geen dunne draad aan de punt hebben, omdat deze vast kan komen te zitten in de feeder. Deze laatste trekkracht zal het filament breken, maar hopelijk zal het dankzij de vorige twee stappen schoon breken.

![Eerst wordt het materiaal naar binnen getrokken om druppelen te verminderen.](../../../articles/images/filament_switch_anti_ooze.svg)
![Ten tweede wordt het filament langzaam doorgevoerd om een ​​dunne draad te trekken die gemakkelijk te scheiden en te stollen is.](../../../articles/images/filament_switch_break_preparation.svg)
![Ten derde wordt het filament snel verder gevoerd om het filament te snijden.](../../../articles/images/filament_switch_break.svg)

**Deze instelling is momenteel niet zichtbaar in de interface van Cura. Het kan alleen worden ingesteld door de profielen. Het wordt ook niet gebruikt door Cura bij het snijden. Drukkers die het materiaalbestandsformaat van Cura begrijpen, kunnen het echter gebruiken om hun filamentwisselprocedure correct te configureren.**
Een nabewerkingsscript kan worden gebruikt om het commando `M600` in de print in te voegen, waardoor een filamentwisseling wordt geactiveerd.