Klodders
====
Klodders zijn kleine vlekjes aan de zijkant van het model. Soms zijn het gewoon punten. Soms zijn er strepen. Ze zijn een optisch oppervlaktedefect en kunnen de wrijving verhogen tussen oppervlakken die in een mechanisme over elkaar moeten schuiven.

![Sommige klodders op dit oppervlak](../../../articles/images/blobs.jpg)

Er zijn verschillende mogelijke oorzaken van klodders. Het is een van de meest voorkomende fouten bij 3D-printen. In dit artikel worden enkele mogelijke oorzaken en hun oplossingen opgesomd.

Nozzle vertraagd
----
Als de nozzle in een bepaalde baan langzamer beweegt dan andere, kan daar meer materiaal worden gestort. Dit materiaal stroomt aan het wandoppervlak naar buiten en vormt een klodder.

Dit zou waarschijnlijk de materiaaltoevoer moeten verminderen. Maar zelfs als de feeder langzamer beweegt, kan het enkele seconden duren voordat de doorvoer uit de nozzleopening dienovereenkomstig is verminderd. Gedurende deze tijd wordt er teveel materiaal geëxtrudeerd, wat resulteert in klodders.

Om dit te voorkomen, dient u de volgende instellingen te maken:
* Pas de snelheid aan voor de [Snelheid Buitenwand](../speed/speed_wall_0.md) zodat deze hetzelfde is als wat ervoor staat (zoals de [Snelheid Binnenwand](../speed/speed_wall_x.md) of [Vulsnelheid](../speed/speed_infill.md)). Dan is er geen vertraging.
* Verhoog de [Schok Buitenwand](../speed/jerk_wall_0.md). Dit voorkomt dat nozzle in bochten vertraagt.
* Verlaag de [Maximale resolutie](../meshfix/meshfix_maximum_resolution.md) en verhoog de [Maximale afwijking](../meshfix/meshfix_maximum_deviation.md) om te voorkomen dat de bewegingsbesturing nozzle vertraagt om gelijke tred te houden met de te verwerken g-codes.
* Schakel de instelling [Gelijkmatige overlappingen van buitenwanden](../shell/travel_compensate_overlapping_walls_0_enabled.md) uit. Deze instelling kan nieuwe bewegingscommando's met verschillende voedingen genereren. Het uitschakelen van deze functie vermindert het aantal bewegingscommando's in de wand.

Nozzle staat stil
----
Als nozzle een beetje pauzeert tijdens het printen van de buitenwand, wacht het waarschijnlijk tot de processor in je 3D-printer nieuwe bewegingsopdrachten verwerkt. De motion planning-software van de printer houdt voor dergelijke gevallen, waarin de bewegingscommando's al zijn verwerkt, meestal een buffer bij van voorbewerkte commando's, zodat de printer precies weet wanneer de stappenmotoren of andere bewegingen moeten worden geactiveerd. Als deze buffer is uitgeput, spreekt men van een "buffer underrun". Hierdoor verschijnen er vlekken op het oppervlak.

Om dit te voorkomen, moet u de resolutie van de G-code verlagen.
* Verhoog de [Maximale resolutie](../meshfix/meshfix_maximum_resolution.md) instelling, waardoor Cura langere lijnsegmenten uitvoert.
* Verhoog de [Maximale afwijking](../meshfix/meshfix_maximum_deviation.md) instelling, waardoor Cura de resolutie verder kan verlagen door verder af te wijken van het oorspronkelijke pad.
* Schakel de instelling [Gelijkmatige overlappingen van buitenwanden](../shell/travel_compensate_overlapping_walls_0_enabled.md) uit. Als de buitenwand overlapt met andere buitenwanden, zou een deel van de wand een ander lijngewicht krijgen, maar dit vereist een extra bewegingscommando. Om het aantal bewegingscommando's te verminderen, kunt u deze functie uitschakelen. Dit kan echter ook leiden tot over-extrusie in deze wanden, wat ook blobs veroorzaakt.
* Verlaag de [Snelheid Buitenwand](../speed/speed_wall_0.md). Dit vermindert de snelheid waarmee de bewegingscommando's moeten worden uitgevoerd, waardoor de CPU de achterstand kan inhalen.

Nozzle verplaatsingen gaan door wanden
----
Hoewel Cura over het algemeen zomin mogelijk de buitenwand oversteekt, is het soms onvermijdelijk. Als nozzle wat doorgesijpeld materiaal draagt terwijl het een buitenwand doorkruist, kan dat materiaal daar worden weggeveegd, waardoor een klodder achterblijft.

Deze oorzaak van klodders kan worden voorkomen door de volgende instellingen:
* Zorg ervoor dat [Combing-modus](../travel/retraction_combing.md) is aangevinkt. Hierdoor gaat nozzle zoveel mogelijk om wanden heen in plaats van erdoorheen.
* Schakel [Z-sprong wanneer ingetrokken](../travel/retraction_hop_enabled.md) in. Wanneer de wanden worden gekruist, beweegt nozzle een beetje omhoog om over de wand te gaan in plaats van er doorheen. Het ingesijpelde materiaal wordt hoogstwaarschijnlijk niet op de wand geveegd, maar waar de nozzle na de rijbeweging terechtkomt. Cura zal altijd proberen om waar mogelijk in de vulling of skin te landen.
* Zorg ervoor dat de [Printvolgorde van wanden optimaliseren](../shell/optimize_wall_printing_order.md) is Dit vermindert het aantal bewegingen bij het printen van wanden, waardoor efficiëntere bewegingen mogelijk zijn en de kans kleiner wordt dat sommige van die bewegingen door een buitenwand moeten gaan.

Opgebouwde druk
----
Als de nozzle te veel wordt geëxtrudeerd, kan de extrusie onregelmatig worden. Deze druk kan plotseling ontsnappen wanneer een bepaalde hoek van uw print wordt geprint (vooral op overhangen). Soms barst deze opgehoopte druk los en laat een grote klodder achter. Meestal wordt de klodder dan gevolgd door een streep van geleidelijk afnemende druk in de nozzle.

Om dit effect te verminderen, moet u enkele instellingen overwegen:
* Verklein de [Lijnbreedte Wand](../resolution/wall_line_width.md). Dit vermindert in het algemeen de druk in de nozzlekamer.
* Verlaag de waarde van [Uitsparing Buitenwand](../shell/wall_0_inset.md). Deze instelling zorgt ervoor dat de buitenwand overlapt met de aangrenzende binnenwand, waardoor de wand strakker tegen de binnenwand wordt geduwd, waardoor de sterkte toeneemt. Dit verhoogt echter ook de druk in de nozzlekamer.

Nat filament
----
Als er zich vocht in het filament heeft opgehoopt terwijl het nog op de spoel zit, zal dit vocht in nozzle boven het kookpunt worden verwarmd. De waterdamp ontsnapt plotseling uit nozzle. Deze kleine explosie kan wat plastic uit de weg blazen, wat resulteert in een kleine klodder op je oppervlak.

Naden
----
Er wordt een naad gecreëerd waar de omtrek van de buitenwand begint en sluit. Dit is niet wat gewoonlijk een klodder wordt genoemd, hoewel het er hetzelfde uitziet. Lees het artikel over [Naden](seam.md) hoe je dit effect kunt verminderen.

Als de [Uitlijning Z-naad](../shell/z_seam_type.md) is ingesteld op "Random", wordt de naad verdeeld over het model, waardoor overal kleine naden worden gemaakt. Dit kan er precies uitzien als een klodder, ook al is het eigenlijk een naad. Wijzig de instelling Z-naaduitlijning om deze naden te verbergen.