Printkop Optillen
====
Wanneer de [Minimale Laagtijd](cool_min_layer_time.md) is bereikt, vertraagt ​​de printkop om te voorkomen dat er sneller dan de minimale laagtijd wordt geprint. Dit geeft de vorige laag voldoende tijd om af te koelen en uit te harden voordat de volgende laag wordt aangebracht. De printkop vertraagt ​​totdat hij [Minimumsnelheid](cool_min_speed.md) bereikt.

Als deze instelling is ingeschakeld en de printkop is ingesteld om langzamer te bewegen dan de minimumsnelheid om aan de minimale laagtijd te voldoen, zal de printkop iets omhoog bewegen nadat de laag is geprint. Hij wacht dan een tijdje totdat de minimumtijd voor de laag is bereikt voordat hij aan de volgende laag begint.

Als deze instelling is uitgeschakeld, gaat de printer onmiddellijk door naar de volgende laag. Het wacht niet op de minimale laagtijd, dus lagen worden geprint op lagen die mogelijk niet volledig zijn uitgehard.

![Als de minimale schakeltijd is bereikt, kan de printkop omhoog gaan](../../../articles/images/cool_fan_speed.svg)

De printkop wordt altijd 3 mm verhoogd. Er is momenteel geen manier om dit te configureren.

Kcompromissen
----
Er is een compromis in het vertragen van nozzle om de laag een betere kans te geven om af te koelen. De minimale laagtijd is bedoeld om het materiaal wat tijd te geven om af te koelen door de beweging van de printkop te vertragen. Gedurende deze tijd zullen de ventilatoren op maximaal vermogen blazen om het materiaal sneller af te koelen, maar de hete nozzle zit nog steeds op het plastic. Voor zeer kleine onderdelen kan de hete nozzle meer warmte in de print overbrengen dan de ventilatoren kunnen afblazen. Hierdoor smelt het plastic nog meer dan wanneer je geen minimale laagtijd zou hebben.

Dit compromis wordt opgelost door de printkop op te tillen. Je kunt nog steeds tot op zekere hoogte vertragen, maar bij hele kleine lagen wordt de hete nozzle weggeschoven, zodat deze geen warmte meer in de print overdraagt. De printkop blijft zo dichtbij dat eventuele ventilatoren op de printkop op de print blijven blazen.

Het nadeel van deze techniek is dat het effectief een [Hoogte Z-sprong](../travel/retraction_hop.md) uitvoert, wat op zijn beurt resulteert in [Stringing](../troubleshooting/stringing.md). Hoewel het optillen van de printkop doorhangen en klodderen kan verbeteren, veroorzaakt het een andere reeks problemen. Een beetje handmatig afwerken met een mes kan de snaren die dit veroorzaakt elimineren.