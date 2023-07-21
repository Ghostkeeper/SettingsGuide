Pillowing
====
Pillowing is een effect dat kleine bobbels of gaatjes creëert tussen de vullijnen aan de bovenkant van het model. Dit effect komt het meest voor op (anderszins) vlakke bovenzijden bij het printen met hoge stroomsnelheden.

![Bobbels en kleine gaatjes in het oppervlak](../../../articles/images/pillowing.jpg)

Oorzaak
----
Pillowing is een combinatie van meerdere effecten die samenwerken om een uitpuilend effect op de bovenkant van de print te creëren.

De opvallende uitstulping van de skin is eigenlijk een vorm van [Kromtrekken](warping.md), waarbij de skin wordt samengeprint door de omringende wanden en onderliggende vulling. Doordat de wanden en invulling in de onderste lagen eerst worden geprint, koelen en krimpen ze terwijl de buitenskin nog wordt geprint. Terwijl ze krimpen, duwen de wanden en vulling de lijnen van de skin naar binnen totdat ze uitpuilen.

Een andere belangrijke factor bij pillowing is het verslappen van de skin tussen de vullijnen. Afhankelijk van de afstand tussen de vullijnen, moeten de buitenste skinlijnen een bepaalde afstand overbruggen. Als de koeling onvoldoende is, zal het plastic een beetje doorzakken. Als gevolg hiervan plakken de skinen niet zo goed aan elkaar en ontstaan er gaten tussen de vellen. Er zijn een paar skinlagen nodig om dit op te lossen.

Het pillowing buigt naar boven in plaats van naar beneden. Hoewel het zowel omhoog als omlaag kan gaan, komt de uitstulping vaker voor omdat nozzle aan de bovenkant van het plastic trekt terwijl het door de skin gaat, wat een kort moment een opwaartse schuifkracht veroorzaakt. Als de lijnen naar boven buigen, houdt het kromtrekkende effect ze omhoog.

Preventie
----
Er zijn verschillende methoden om pillowing in Cura te voorkomen:
* Het verhogen van [Dikte Bovenkant](../top_bottom/top_thickness.md) is de meest effectieve manier om kussenvorming te voorkomen. Met meer [Bovenlagen](../top_bottom/top_layers.md) kunnen de hogere lagen op de gedeeltelijk gesloten openingen van de vorige lagen rusten. Hierdoor hebben ze een betere kans om de kieren te dichten en een sterke toplaag te vormen die niet doorzakt. Over het algemeen geldt: hoe dunner de lagen, hoe meer toplagen er nodig zijn, aangezien die lagen niet zo sterk zijn.
* Door de [Dichtheid  Vulling](../infill/infill_sparse_density.md) te vergroten, worden de gaten die de skin moet overbruggen kleiner. Dit maakt het gemakkelijker om deze gaten te dichten. Als je dit combineert met [Stappen Geleidelijke Vulling](../infill/gradual_infill_steps.md) kan het grootste deel van de infill-dichtheid hetzelfde blijven. Alleen de bovenkant zal een hogere dichtheid hebben om demping te voorkomen.
* Printen bij een lagere [Printtemperatuur](../material/material_print_temperature.md) verbetert de overbrugging en kromtrekken in het algemeen, inclusief de bovenskin, waardoor het kussen minder wordt.
* Verhoog ook de [Ventilatorsnelheid](../cooling/cool_fan_speed.md) om ook de overbrugging te verbeteren.
* Het verlagen van [Snelheid Boven-/Onderkant](../speed/speed_topbottom.md) verbetert de bypass direct. Bovendien betekent dit dat de hogere lagen van de buitenskin beter op de lagere lagen worden geprint. Hierdoor sluiten de gaten ook sneller.