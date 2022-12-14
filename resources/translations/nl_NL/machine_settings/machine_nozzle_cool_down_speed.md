Afkoelsnelheid
====
Deze instelling vertelt Cura hoe snel je nozzle afkoelt als het niet wordt verwarmd. Het wordt gebruikt om te voorspellen wanneer nozzle moet worden gekoeld voordat de extruder wordt omgeschakeld.

![De nozzles worden verwarmd voordat de extruder wordt omgeschakeld.](../../../articles/images/temperature_regulation.svg)

Wanneer de extruder wordt gewisseld, zal Cura de actieve nozzle voorkoelen net voordat deze klaar is, zodat deze tijdens het wachten iets minder zal sijpelen. Cura probeert ook te voorspellen hoeveel de nozzle is afgekoeld terwijl deze inactief was. Zo weet hij hoeveel moeite hij moet doen om ze daarna weer op te warmen.

Als de nozzle daadwerkelijk sneller afkoelt dan deze instelling aangeeft, komt de nozzle sneller op de gereedtemperatuur dan Cura voorspelt. Hierdoor kan het langer duren voordat de nozzle is opgewarmd dan Cura voorspelt en wacht de printer bij de nozzle-schakelaar totdat de nozzle verder is verwarmd.

Als de nozzle inderdaad langzamer afkoelt dan deze instelling aangeeft, kan de nozzle nog warm zijn als Cura een commando stuurt om de nozzle voor te verwarmen, waardoor deze te snel opwarmt. De nozzle zal een tijdje op printtemperatuur zijn voordat het zijn beurt is om te printen. Gedurende deze tijd zal het een beetje druppelen en zal het plastic iets meer degraderen.

De werkelijke koelsnelheid is geen constante snelheid in graden per seconde. Het hangt veeleer af van het verschil tussen de skinige nozzletemperatuur en de temperatuur van het bouwvolume. Wanneer nozzle heet is, koelt het sneller af, en wanneer het de gereedtemperatuur nadert, koelt het langzamer af. Als u dit instelt, kunt u proberen de tijd te meten die nodig is om van [Eindtemperatuur voor printen](../material/material_final_print_temperature.md) naar [Stand-bytemperatuur](../material/material_standby_temperature.md) af te koelen. Dit is het belangrijkste stukje informatie dat Cura probeert te voorspellen. Als je kleine printen maakt, wil je misschien de afkoelsnelheid iets verhogen om te compenseren dat je vaker warm blijft.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**