Onvoltooide Print
====
Soms is een print niet helemaal af. Hier kunnen een aantal redenen voor zijn, en sommige kunnen worden verholpen door de instellingen van Cura aan te passen.

![Het filament stopte met stromen halverwege de print.](../../../articles/images/unfinished_print.jpg)

Printerfout
----
Soms is de oorzaak van een onvoltooide print een printerfout waarbij de printer niet doet wat hij moet doen. Cura kan daar meestal weinig aan doen. Hier zijn enkele veelvoorkomende oorzaken.
* Stroomstoring. Cura kan hier weinig aan doen, behalve sneller printen om de kans op een stroomstoring halverwege de print te verkleinen.
* Stroomstoring. Als een van de temperaturen (ofwel de [Platvormtemperatuur](../material/material_bed_temperature.md) of de [Printtemperatuur](../material/material_print_temperature.md)) te hoog is, hebben sommige printers een storingsmodus wanneer de voeding raakt oververhit of de temperatuursensoren melden fouten. Hierdoor wordt de printer uitgeschakeld en wordt het printen niet voltooid.
* Firmware loopt vast. Vanwege bugs in de firmware reageert de printer mogelijk niet meer. Als u begrijpt waar in de g-code de printer vastloopt (meestal aan het begin of einde van het printproces), kunt u wellicht achterhalen welke g-code de oorzaak is. Misschien moet begin-g-code of eind-g-code worden aangepast.
* De filamentspoel is verward. Het is een goed idee om *altijd* het uiteinde van het filament vast te houden wanneer het niet stevig vastzit in de feeder of in een van de gaten in de spoel (als uw spoel dergelijke gaten heeft). Als u het filament loslaat en het uiteinde van het filament terug op de spoel springt, kan het onder een van de andere wikkels glijden en verstrikt raken. Omdat de draad typisch honderden meters lang is, is deze knoop erg moeilijk los te maken als hij eenmaal in de knoop raakt.

Filament slijpen
----
De feeder duwt het filament soms heel hard om het door de extruderstreng te duwen. Dit beschadigt het filament. Als de feeder heel vaak aan hetzelfde stuk filament duwt en trekt, kan het zo erg beschadigd raken dat de feeder het filament niet meer kan pakken. Het materiaal stopt dan met stromen en de rest van de print wordt geprint met lucht in plaats van plastic.

![Het filament is uitgeslepen door de feeder](../../../articles/images/grinding.jpg)

Dit kun je tijdens het printen zien door een vinger op de opening te leggen waar het filament de feeder binnenkomt. U zou de vinger moeten voelen bewegen terwijl u drukt. Als het niet beweegt, is het hoogstwaarschijnlijk het materiaal vermalen en kan het er geen vat op krijgen. Je kunt het filament ook uit de printer trekken en kijken waar het beschadigd is.

Om dit probleem te voorkomen, kun je de volgende aanpassingen maken in de instellingen van Cura:
* Verlaag het [Maximaal Aantal Intrekbewegingen](../travel/retraction_count_max.md) of verhoog het [Minimaal Afstandsgebied voor Intrekken](../travel/retraction_extrusion_window.md). Dit beperkt het aantal voedingen dat wordt uitgevoerd tijdens de extrusie van een gegeven filamentlengte. Dit beperkt het aantal keren dat de feeder heen en weer kan rollen over elk stuk filament.
* Verklein de [Intrekafstand](../travel/retraction_amount.md). Dit beperkt ook het aantal voorwaartse en achterwaartse verplaatsingen van de feeder over hetzelfde stuk filament.
* Verlaag de [Intreksnelheid](../travel/retraction_speed.md). Als het materiaal snel beweegt maar ergens onderweg wordt belemmerd, zal de feeder het materiaal malen. Als het materiaal langzamer beweegt, is de kans kleiner dat dit gebeurt.
* Print langzamer door [Laaghoogte](../resolution/layer_height.md), [Lijnbreedte](../resolution/line_width.md) of [Printsnelheid](../speed/speed_print.md ) te verminderen. Dit vermindert de kracht die de feeder op het filament moet uitoefenen, waardoor het risico op slijpen wordt verminderd.