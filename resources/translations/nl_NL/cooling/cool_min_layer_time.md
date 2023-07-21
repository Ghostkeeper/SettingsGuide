Minimale Laagtijd
====
De minimale laagentijd bepaalt de kortst toegestane printtijd voor een laag. De printer mag niet sneller dan dit printen.

Dit is nodig om de vorige laag af te laten koelen alvorens de volgende laag erop te leggen. Dit zorgt ervoor dat de vorige laag volledig is uitgehard om uitzakken te voorkomen.

![Welke ventilatorsnelheid wordt waar gebruikt](../../../articles/images/cool_fan_speed.svg)

Deze instelling heeft drie effecten:
* Als een laag sneller print dan de instelling [Drempelwaarde Normale/Maximale Ventilatorsnelheid](cool_min_layer_time_fan_speed_max.md), wordt de ventilatorsnelheid verhoogd naar [Maximale ventilatorsnelheid](cool_fan_speed_max.md). Zodra een laag zo klein is dat het de minimale laagtijd nodig heeft om te printen, wordt de maximale ventilatorsnelheid gebruikt. Tussen deze twee waarden wordt de ventilatorsnelheid geïnterpoleerd.
* Als de laag minder dan de Minimale Verschuivingstijd nodig heeft om te printen, wordt de printsnelheid verlaagd zodat het nog steeds de Minimale Verschuivingstijd kost.
* Als de printkop te veel zou vertragen (langzamer dan de instelling [Minimumsnelheid](cool_min_speed.md)), dan wacht de printkop aan het einde van een laag en brengt de printkop optioneel iets omhoog.

Er is een compromis in het vertragen van nozzle om de laag een betere kans te geven om af te koelen. De minimale laagtijd is bedoeld om het materiaal wat tijd te geven om af te koelen door de beweging van de printkop te vertragen. Gedurende deze tijd zullen de ventilatoren op maximaal vermogen blazen om het materiaal sneller af te koelen, maar de hete nozzle zit nog steeds op het plastic. Voor zeer kleine onderdelen kan de hete nozzle meer warmte in de print overbrengen dan de ventilatoren kunnen afblazen. Hierdoor smelt het plastic nog meer dan wanneer je je niet aan een minimale laagtijd houdt.

Als u relatief koude materialen print of als de ventilatoren op de printkop bijzonder sterk zijn, kan het materiaal een langere minimale schakeltijd verdragen om doorzakken te verminderen. Als de minimale schakeltijd te hoog wordt ingesteld, zal de sproeier steeds vaker vertragen, wat ook op sommige plaatsen klonters en verzakkingen veroorzaakt.