Initiële terugtrekking gedeelde nozzle
====
Wanneer de extruders van een printer [Extruders delen nozzle](machine_extruders_share_nozzle.md), gaat Cura er niet vanuit dat alle extruders beginnen met het filament aan de punt van nozzle. Deze instelling geeft aan hoe ver het filament vanaf nozzle begint. Het filament kan op een andere afstand beginnen dan de [Intrekafstand bij Wisselen Nozzles](../dual/switch_extruder_retraction_amount.md) omdat het filament mogelijk verder weg is opgeslagen terwijl de printer inactief was dan toen de extruder inactief was tijdens het printen.

![afstand van inactief filament voor printen](../../../articles/images/machine_extruders_shared_nozzle_initial_retraction.svg)

Cura gebruikt dit om ervoor te zorgen dat het filament zich bij de nozzlepunt bevindt voordat het materiaal begint te verzamelen voor de eerste extruderwissel.