Draadprinten
====
Deze instelling maakt een heel ander soort printen mogelijk, genaamd draadprinten. Bij draadprinten drukt de printer geen vast object af, maar alleen een driehoekig netwerk van dunne draden dat zich aan de buitenvorm aanpast.

Deze techniek heeft een aantal voordelen:
* Het drukt veel sneller af dan een vast object.
* Het gebruikt slechts een fractie van het materiaal dat bij normaal printen zou worden gebruikt.
* Het lijkt alsof het met de hand is gemaakt met een 3D-printpen.

Het resulterende object is echter niet functioneel. Het is ongeveer de juiste maat, wat het handig maakt voor prototyping om een idee te krijgen van de schaal van de print, hoewel de maat ook niet erg nauwkeurig is. Het resulterende object is uiterst kwetsbaar, niet alleen tijdens het printen maar ook daarna. Het is moeilijk om het van de platform te halen zonder het te beschadigen. Ook verliest het model de meeste details.

Bij het printen met draadstructuur worden ringen van materiaal aangebracht met een relatief grote verticale afstand van enkele millimeters. Tussen deze ringen wordt een zaagtandvorm geprint, waardoor de volgende ring op de vorige kan rusten. Waar het oppervlak van het model horizontaal is, wordt een vergelijkbare techniek gebruikt om de bovenkant te sluiten. Binnen het dak bevinden zich concentrische ringen die bij elkaar worden gehouden door een zaagtandvorm die zorgvuldig in de lucht wordt opgehangen door van buitenaf (waar het tegen een wand kan stoten) naar binnen te bouwen.

Wireframe-printen werkt alleen betrouwbaar op vormen die bijna volledig verticaal zijn, vergelijkbaar met het type modellen dat goed zou werken met [Buitencontour Spiraliseren](../blackmagic/magic_spiralize.md). Als het oppervlak over grote vlakken horizontaal is, moet de dakafsluittechniek een extreem grote afstand overbruggen. Dit zal dan hoogstwaarschijnlijk mislukken. Als het model vervolgens halverwege een horizontaal vlak omhoog gaat, zal het vrijwel zeker in de lucht printen.

**Cura's laagweergave geeft het printen van draad direct na het snijden niet correct weer. Het resultaat kan echter nog steeds worden bekeken door de G-code op schijf op te slaan en die G-code opnieuw te openen met Cura.**