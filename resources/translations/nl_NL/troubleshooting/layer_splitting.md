Laag Splitsing
====
Hechting tussen de lagen is vaak de zwakste schakel in de structuur van 3D-geprinte objecten. Wanneer de hechting tussen de lagen tijdens of kort na het printen wegvalt, wordt dit laagsplitsing, delaminatie genoemd.

![De lagen zijn gesplitst aan de zijkant van deze container.](../../../articles/images/layer_splitting.jpg)

Laagsplitsingen kunnen moeilijk zijn om mee om te gaan, omdat de print altijd op het zwakste punt splitst. De volgende suggesties zijn bedoeld om de print consistenter en de extrusie betrouwbaarder te maken om zwakke punten in de hechting van de lagen te elimineren.

Kromtrekken
----
De meeste laagsplitsingen worden veroorzaakt door [Kromtrekken](warping.md). Dit komt vooral veel voor bij semi-kristallijne polymeren. Als ze afkoelen, vormen ze microscopisch kleine kristalstructuren en krimpen ze aanzienlijk. De meest voorkomende vorm van kromtrekken is wanneer het onderste deel van de print naar boven vervormt, wat niet leidt tot delaminatie. Wanneer de vervorming zich echter verder op de print voordoet, zorgt dit ervoor dat de lagen wegbuigen van de aangrenzende lagen en uit elkaar splijten.

Om kromtrekken in hogere lagen te voorkomen, kan men een paar dingen doen om de kans op laagsplitsing te verkleinen:
* Gebruik een concentrisch [Patroon Boven-/Onderkant](../top_bottom/top_bottom_pattern.md). Een lineair patroon heeft lijnen die allemaal in dezelfde richting krimpen, waardoor de lagen in dezelfde richting worden getrokken. Het concentrische patroon verdeelt deze kracht.
* Het verhogen van [Temperatuur werkvolume](../material/build_volume_temperature.md) vermindert de vervorming door [uitharding](https://en.wikipedia.org/wiki/Annealing_%28glass%29) van het plastic. Hiervoor heeft de printer een gesloten volume nodig waarin de warmte wordt vastgehouden.
* Het gebruik van een [Tochtscherm Inschakelen](../experimental/draft_shield_enabled.md) houdt ook een deel van de warmte binnen, zij het minder effectief dan een gesloten bouwvolume.
* Voorkom scherpe hoeken in 3D-model. Door een ronde aan een scherpe hoek toe te voegen, wordt voorkomen dat de lijnen van de skin direct tegen de onderliggende wanden aanliggen. Dit is vaak een plek waar de laag wordt gesplitst.
* Gebruik een materiaal dat niet zo veel krimpt. PLA vervormt bijvoorbeeld minder dan polypropyleen. De meeste mensen kiezen hun materiaal echter op basis van specifieke vereisten, dus dit is voor hen uitgesloten.

Onvoldoende druk
----
Om de lagen goed aan elkaar te laten plakken, helpt het om het plastic stevig op de vorige laag te printen. Als de nozzle niet genoeg materiaal uitwerpt, of het materiaal niet hard genoeg tegen de vorige laag wordt geprint, neemt de houdkracht tussen de lagen af, waardoor ze gemakkelijker kunnen scheiden. Hoewel dit de laag niet onmiddellijk doet barsten, vermindert het de sterkte van het voltooide onderdeel.

Dit is vooral een probleem voor de wanden. De buitenskin heeft zo'n groot oppervlak dat deze niet scheurt. Tussen de vulling en de wanden zorgen de wanden voor het grootste deel van de laaghechting, omdat de vulling vaak zeer snel wordt geprint, met dun uit elkaar geplaatste lijnen en vaak niet verticaal gestapeld.

Zorg ervoor dat er geen [Onder-extrusie](underextrusion.md) is om ervoor te zorgen dat er voldoende wordt geprint. Er zijn allemaal oorzaken van onder-extrusie, maar sommige zijn met name relevant voor het splitsen van lagen:
* Als u halverwege stopt met printen, duurt het even voordat de extrusie weer op gang komt. Het "Pauze op hoogte script" heeft een optie om <!--if cura_version >= 4.7-->één laag te herhalen<!--endif--><!--if cura_version < 4.7: de laatste lagen te herhalen --> . Dit bereidt het materiaal voor voordat het naar boven gaat en voorkomt een slappe laag met onvoldoende nozzledruk.
* Als u de [Wandsnelheid](../speed/speed_wall.md) verlaagt, worden de wanden gelijkmatiger geprint. Dit verkleint de kans op het ontwikkelen van zwakke punten en vermindert tegelijkertijd onder-extrusie op de wanden.
* Verlaag de [laaghoogte](../resolution/layer_height.md) of de [Lijnbreedte Wand](../resolution/wall_line_width.md). Hoge doorvoersnelheden vereisen een hogere druk. Als de printer deze print niet kan produceren, wordt er niet genoeg materiaal geëxtrudeerd om de dikke lagen of brede lijnen te vullen. Dit vermindert de druk.
* Verhoog de [Printtemperatuur](../material/material_print_temperature.md) om ervoor te zorgen dat het materiaal breder uitvloeit en het contactgebied volledig benut in plaats van geconcentreerd te blijven in het midden van de lijn.
* Verklein de [Intrekafstand](../travel/retraction_amount.md). Lange terugtrekafstanden zorgen ervoor dat er meer materiaal naar buiten kan stromen tijdens het terugtrekken, wat later leidt tot onder-extrusie. Bovendien onderbreken ze de doorvoer meer. Het duurt dan langer voordat de stroming weer stabiliseert. Het verminderen van de terugtreklengte vermindert het risico dat zich een zwakke schakel vormt langs de hoogte van de druk als gevolg van een niet-uniforme stroming.

Onvoldoende oppervlakte
----
Hechting tussen lagen is een functie van de sterkte van de hechting tussen de materialen vermenigvuldigd met de hoeveelheid oppervlakte waarop kan worden gelijmd. Hoe groter het oppervlak, hoe kleiner de kans dat de lagen zullen splijten.

De belangrijkste parameter hiervoor is de [Wanddikte](../shell/wall_thickness.md). Meer wanden vergroten het oppervlak drastisch. De wanden worden langzamer geprint en bevinden zich op het punt waar het splijten begint; ze zijn daarom een ​​zeer effectief middel om de hechting van de lagen te vergroten. Het printen van meer wanden verhoogt echter ook de printtijd en het materiaalverbruik drastisch.

Onvoldoende oppervlak is vaak een probleem bij het printen van grote prints met slechts één wand en zonder vulling waar de vervorming ernstig is. De wand zal door de vervorming gaan knikken en er is geen manier om dit te voorkomen. Dit zou een reden kunnen zijn om het gebruik van [Buitenbcontour Spiraliseren](../blackmagic/magic_spiralize.md) uit te schakelen, omdat het slechts een enkele wand print en voorkomt dat er infill wordt gemaakt. In plaats daarvan moet u mogelijk met twee wanden printen en de opvuldichtheid handmatig op 0% instellen om een ​​soortgelijk effect te bereiken.

Materialen die niet met elkaar samengaan
----
Let er bij het printen met verschillende kunststoffen op dat de kunststoffen aan elkaar kleven. Kunststoffen met zeer verschillende krimpverhoudingen kunnen over het algemeen niet aan elkaar kleven. Verschillende chemische effecten zorgen er ook voor dat de kunststoffen elkaar afstoten en niet aan elkaar kleven. Als dit in een groot vlak gebied in het midden van je print gebeurt, bestaat het risico dat de print daar uit elkaar valt.
