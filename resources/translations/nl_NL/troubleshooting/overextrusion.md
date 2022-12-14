Over-extrusie
====
Over-extrusie is een term die wordt gebruikt wanneer de printer te veel materiaal op één plaats extrudeert. Hierdoor stroomt het materiaal naar de zijkanten of omhoog, waardoor het oppervlak erg ruw en onregelmatig wordt. Het kan ook resulteren in [Stringing](stringing.md) en veel [Klodders](blobs.md).

![Deze print resulteerde in massale over-extrusie](../../../articles/images/overextrusion.jpg)

Temperatuurregeling
----
De meest voorkomende oorzaak van over-extrusie is te heet printen. Als de [Printtemperatuur](../material/material_print_temperature.md) te hoog wordt ingesteld, zal het materiaal een lagere viscositeit hebben, waardoor het ongecontroleerd uit de nozzle vloeit. Het resultaat is meestal over-extrusie in sommige gebieden, zoals de buitenwanden, maar onder-extrusie in andere gebieden, zoals de vulling.

Om dit op te lossen, moet u de temperatuur geleidelijk verlagen. Kijk goed naar het gegevensblad van het materiaal waarmee u print om te bepalen welk temperatuurbereik acceptabel is, en verlaag de printtemperatuur naar de onderkant van dat bereik.

Diameter van het filament
----
Er zijn verschillende normen voor de diameter van filamenten. De meest voorkomende zijn 1,75 mm en 2,85 mm, maar ook 3,00 mm zijn nog in omloop. Overigens produceren niet alle fabrikanten hun filament met een uniforme diameter. Als je filament breder is dan Cura verwacht, extrudeer je te veel materiaal omdat Cura de printer vertelt een bepaalde lengte filament te extruderen, wat dan te veel volume zal hebben.

Om dit op te lossen, meet u eerst de werkelijke diameter van het filament met een schuifmaat. Het is het beste om dit op meerdere plaatsen te meten als het varieert en onder verschillende hoeken rond de omtrek. Vind het gemiddelde van deze metingen. Deze gemiddelde waarde kan in Cura op de pagina Materiaalbeheer worden ingevoerd als eigenschap van het materiaal. Als de diameter niet kan worden bewerkt omdat het een vooraf gedefinieerd materiaal is, moet u het materiaal mogelijk eerst dupliceren. Dan moet het mogelijk zijn om de diameter te bewerken.

Extruderkalibratie
----
Soms is het probleem dat de hardware niet overeenkomt met wat de firmware verwacht. Als de extrudermotor een stappenmotor is (wat gebruikelijk is bij 3D-printers), moet de firmware weten hoeveel stappen de motor neemt om een ​​bepaalde afstand te bereiken. De firmware heeft hiervoor een instelling die de nauwkeurigheid van de voeding meet in stappen per millimeter. Als deze instelling verkeerd is geconfigureerd, kan de transportband te snel of te langzaam bewegen. Deze instelling kunt u het beste in de firmware maken. Als dit echter niet mogelijk is, kan de [Doorvoer](../material/material_flow.md) in Cura worden aangepast om te compenseren. Pas dan ook de [Intrekafstand](../travel/retraction_amount.md) en [Intreksnelheid](../travel/retraction_speed.md) aan.

Wand overlapt
----
Normaal gesproken tekent Cura alleen de contouren van de print met een bepaalde lijndikte. Als de wanden op bepaalde punten in je print dicht bij elkaar staan, krijg je overlappende lijnen. Deze lijnen worden dik en creëren klodders omdat daar tot twee keer zoveel materiaal kan worden aangebracht als nodig is. Bij een grote overlap wordt voorkomen dat de tweede lijn extrudeert, waardoor de druk in de nozzlekamer toeneemt totdat deze wordt uitgeworpen, waardoor een klodder ontstaat.

Dit kan worden voorkomen door [Gelijkmatige wandoverlappingen](../shell/travel_compensate_overlapping_walls_enabled.md) in te schakelen. De extrusie van de tweede lijn wordt verminderd, zodat slechts zoveel materiaal wordt geëxtrudeerd als nodig is om de resterende ruimte van de wand te vullen, waardoor over-extrusie wordt voorkomen.

Als de wanden elkaar overlappen vanwege de instelling [Uitsparing Buitenwand](../shell/wall_0_inset.md), kunt u proberen deze parameter te verminderen om overlapping te voorkomen. Je kunt ook proberen om de [Wandvolgorde](../shell/outer_inset_first.md) printen. Het overtollige materiaal wordt vervolgens in het model geduwd waar het onzichtbaar is.

Pas de doorvoer direct aan
----
Als de oorzaak van de over-extrusie niet bekend is, kunt u de [Doorvoer](../material/material_flow.md) ook direct aanpassen. Verlaag de doorvoer totdat uw oppervlak weer glad lijkt. Dit kan een aantal onbekende factoren direct compenseren.