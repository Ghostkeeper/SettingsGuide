Kromtrekken
====
Kromtrekken is een probleem met de uiteindelijke print waarbij de print opkrult na het printen, waardoor het voltooide object wordt vervormd. Meestal krullen de hoeken aan de onderkant van de print omhoog of worden dunne delen van de print golvend.

![De punten krullen omhoog](../../../articles/images/warping.jpg)

Oorzaak
----
De vervorming wordt veroorzaakt door een combinatie van effecten, maar voornamelijk interne spanningen die worden veroorzaakt door nozzle dat aan het gesmolten plastic trekt. Tijdens de glasovergang gedraagt ​​plastic zich een beetje als rubber of kauwgom. Als je eraan trekt, rekt het materiaal uit, maar als je stopt met trekken, keert het terug naar zijn oorspronkelijke vorm. Hetzelfde gebeurt ook bij het printen. Wanneer u een lange lijn print, trekt nozzle aan de plastic lijn, waardoor de lengte van de lijn wordt uitgerekt. Wanneer nozzle weg beweegt en stopt met trekken, zal de plastic lijn samentrekken. Deze samentrekking veroorzaakt een trekkracht op alles wat eraan vastzit. Als er genoeg plastic lijnen naar elkaar toe trekken, kunnen ze de print vervormen. Dit is vooral vaak het geval wanneer veel lijnen evenwijdig lopen, b.v. B. aan de buitenskin.

Een tweede effect dat tot vervorming leidt, is de krimp van het materiaal als het afkoelt. De meeste materialen hebben de neiging om te krimpen als ze afkoelen. Als het object ongelijkmatig afkoelt, zullen sommige delen van de print meer krimpen dan andere delen van de print, waardoor het object kromtrekt. Naarmate het object verder afkoelt, zal het blijven stollen en zal de vervorming permanent zijn.

Sommige materialen zijn meer vatbaar voor krimp dan andere vanwege hun kristalliniteit. Hieronder staan ​​enkele krimpcoëfficiënten voor veelgebruikte 3D-printmaterialen. Dit is de geschatte hoeveelheid die materiaal krimpt als het afkoelt van de glasovergangstemperatuur naar kamertemperatuur. Er zijn bepaalde afwijkingen tussen de afzonderlijke mengsels. Grotere krimp leidt tot grotere vervorming.
* PLA: 0,21%
* ABS: 0,70%
* TPU: 0,63%
* HIPS: 0,64%
* PETG en CPE: 0,45%
* Nylon: 0,62%
* PC's: 0,70%
* PP: 1,2%

Ook kan kromtrekken worden voorkomen wanneer ander materiaal in de weg zit. Als een deel van de print volledig dicht is, kan het omringende materiaal minder of helemaal niet krimpen. Als andere delen niet helemaal strak zitten, is de print gedeeltelijk gekskinen. Het gekskinen deel van de print trekt aan de rest, wat ook kan leiden tot kromtrekken. Dit is vaak het geval op het grensvlak tussen de buitenskin en de vulling, aangezien de buitenskin volledig strak is, maar de vulling niet.

Kromtrekken komt het meest voor aan de onderkant van de print. Hier is de temperatuurgradiënt het grootst, omdat de onderkant van de print vaak wordt verwarmd door een verwarmd platform, maar de rest van de print niet. Ook de onderzijde bestaat meestal uit vele lange skinlijnen. Als [Patroon Boven-/Onderkant](../top_bottom/top_bottom_pattern.md) is ingesteld op Lijnen of Zigzag, zijn deze lijnen lang, recht en evenwijdig, zodat ze in dezelfde richting samentrekken om het object te vervormen.

Vermijden
----
* Als het kromtrekken zich aan de onderkant van de print voordoet, stelt u [Eerste laag patroon onderkant](../top_bottom/top_bottom_pattern_0.md) in op concentrisch. Op deze manier zal de samentrekking van de onderste skinlijnen niet meer in de pas lopen. De interne spanning wordt gelijkmatig verdeeld over de binnenkant van de onderlaag. Als dit niet genoeg is om kromtrekken te voorkomen, kunt u ook het normale [Patroon Boven-/Onderkant](../top_bottom/top_bottom_pattern.md) op Concentric zetten.
* Om de temperatuurgradiënten binnen de print te verminderen, verlaagt u de [Platformtemperatuur](../material/material_bed_temperature.md). Het object moet dan gelijkmatiger afkoelen.
* Afhankelijk van uw printerhardware kan printen in een gesloten, verwarmde kamer ook kromtrekken voorkomen. Dit verkleint enerzijds het temperatuurverschil tussen het bouwvolume en de platvorm en het verschil tussen het bouwvolume en de nozzle. Het zorgt er ook voor dat het plastic langer kan uitharden (https://en.wikipedia.org/wiki/Annealing_%28glass%29), waardoor de interne spanningen en dus het trekken aan de geprinte lijnen die kromtrekken veroorzaken, worden verminderd. Als uw printer dit ondersteund, moet u de [Temperatuur werkvolume](../material/build_volume_temperature.md) verhogen.
* Om te voorkomen dat de bodem kromtrekt, is een goede hechting van de platvorm handig. Dit verhoogt de kracht die nodig is om het materiaal te laten kromtrekken. Vergroot bijvoorbeeld [Breedte Brim](../platform_adhesion/brim_width.md) of [Extra Marge Raft](../platform_adhesion/raft_margin.md).
* Het gebruik van een [(Raft i.p.v. Brim)Type Hechting aan Platform](../platform_adhesion/adhesion_type.md) haalt de print van het platvorm en plaatst er een stevig stuk plastic tussen dat bestand is tegen kromtrekken.
* Probeer te printen met een [Tochtscherm Inschakelen](../experimental/draft_shield_enabled.md). Dit creëert een beschermende kamer rond uw print, waardoor tocht van buitenaf uw print afkoelt voordat deze klaar is. Houd er echter rekening mee dat het tochtscherm zelf ook kan krimpen. Als het tochtscherm faalt, ziet u mogelijk veel stringing of spaghetti in uw print.
* Print met een materiaal dat minder krimpt, zoals: PLA.
* Als u de mogelijkheid heeft om het geprinte model aan te passen, probeer dan zeer scherpe buitenste hoeken op de platvorm te vermijden. U kunt bepaalde buitenhoeken afronden. Dit voorkomt dat alle kracht van interne spanning op één punt wordt geconcentreerd, waardoor de kans op kromtrekken wordt verkleind.