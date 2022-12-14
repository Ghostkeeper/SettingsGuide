Draadprintstrategie
====
Het meest kritieke probleem voor de betrouwbaarheid van draadprinten zijn de verbindingspunten waar de lagen van het frame met elkaar verbonden zijn. Er zijn verschillende strategieën om deze verbindingen te versterken. Met deze instelling kunt u de strategie kiezen die de printer moet gebruiken.

Compenseren
----
Met deze strategie probeert de printer de absorptiefactoren van het model te compenseren. Als het materiaal in gesmolten toestand uit nozzle komt, valt het een beetje naar beneden voordat het stolt en wordt meegesleurd door de bewegingen van nozzle. Deze strategie vervormt het zaagtandpatroon dat de lagen van het frame verbindt op een manier die hopelijk weer op zijn plaats zal eindigen.

Er zijn twee compensatiefactoren beschikbaar: een die het zaagtandpatroon alleen verticaal vervormt tot [Valafstand Draadprinten](wireframe_fall_down.md), en een die het zaagtandpatroon diagonaal vervormt tot [Meegeslepen Draadprinten](wireframe_drag_along.md).

Knooppunt
----
Wanneer deze strategie wordt gekozen, wordt er een kleine heen en weer beweging gemaakt aan de bovenkant van elke zaagtand om daar een "knoop" van materiaal te vormen. Het doel van de knoop is om de horizontale ring boven een gebied te geven om te verbinden met het zaagtandpatroon. De knoop zal van kant tot kant een beetje variëren, dus als de horizontale ring niet erg nauwkeurig is geplaatst, is de kans groter dat ze aan elkaar knopen. Ook trekt de knoop de lijn iets verder omhoog, zodat de horizontale ring eroverheen schuift. En tot slot zal de knoop ook enige lekkage veroorzaken vanwege het ontbreken van inkepingen in deze reisbeweging. Dit creëert een blob

![Waar de knoop is geprint en hoe groot deze is](../../../articles/images/wireframe_top_jump.svg)

De beweging voor dit "knooppunt" bestaat uit een reeks verplaatsbewegingen:
1. Eerst beweegt nozzle iets omhoog en naar achteren.
2. Wanneer er een [Opwaardse Vertraging Draadprinten](wireframe_top_delay.md) in de top is, zal de nozzle pauzeren voor de ingestelde vertragingstijd. Deze pauze wordt gemaakt aan de bovenkant van de beweging van de knoop.
3. Ten derde: nozzle gaat terug naar de normale hoogte. Tegelijkertijd beweegt nozzle naar voren en weg van de verticale lijn.

Intrekken
----
Als voor deze strategie wordt gekozen, wordt het materiaal na elke opwaartse beweging bij het printen van het zaagtandpatroon ingetrokken. Het idee is dat als het materiaal naar binnen wordt getrokken, de draad afbreekt. Dit vermindert het effect van het slepen van het materiaal met de beweging van nozzle, omdat de vorige lijn niet langer aan nozzle is bevestigd. Daarna maakt de nozzle een kleine sprong van 1 millimeter en vervolgt de diagonale beweging naar beneden richting de onderste laag.

Een groot nadeel van deze strategie is dat de diagonale lijn naar beneden ook niet gefixeerd is. Dit maakt extrusie vrijwel nutteloos tijdens deze lijn. Het materiaal komt gewoon in een klodder op de onderste laag terecht. Het maalt het materiaal ook meer omdat het heen en weer wordt getrokken zonder veel tussenkomst van extruderen. Dit alles kost ook veel tijd.