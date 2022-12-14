Nozzle afvegen tussen lagen
====
Met deze instelling kan aan het einde van elke laag een procedure worden uitgevoerd om al het materiaal van de nozzle te vegen. Als u een printer heeft met een ingebouwde veegborstel, zorgt het inschakelen van deze instelling ervoor dat Cura de printer vertelt dat hij periodiek nozzle met die borstel moet afvegen.

![Visualisatie van de bewegingen tijdens het wissen](../../../articles/images/clean_between_layers.svg)

Deze wisprocedure bestaat uit een reeks stappen:
1. Als [Intrekken voor afvegen ingeschakelen](wipe_retraction_enable.md), wordt het materiaal ingetrokken.
2. Als [Z-Sprong afvegen](wipe_hop_enable.md) is ingeschakeld, gaat nozzle omhoog of gaat de platvorm omlaag.
3. nozzle beweegt voorbij de [X-positie afveegborstel](wipe_brush_pos_x.md).
4. nozzle wordt [Aaantal afveegbewegingen](wipe_repeat_count.md) op de borstel afgeveegd.
5. nozzle wordt teruggezet in zijn oorspronkelijke positie.
6. Z-Jump wordt beëindigd als deze is geactiveerd. Het materiaal wordt teruggeduwd.
7. Het printen pauzeert voor een [afvegen pauzeren](wipe_pause.md).

Het doel van dit proces is om regelmatig vervuiling van de nozzle te verwijderen. Sommige materialen hebben de neiging naar de nozzle te stijgen vanwege de hoge oppervlaktespanning door capillaire werking. Deze kunnen in de printkop komen en zich daar ophopen, wat de printkop kan beschadigen. Andere materialen die vezels of andere vulstoffen bevatten, kunnen ervoor zorgen dat de vulstof tijdens het printen op de nozzle spuit. Dit zal het materiaal wegvegen.

De afveegmethode is nu echter niet erg configureerbaar. Het veegt altijd in de X-richting, waarbij de Y-positie van de laatste positie in de print behouden blijft. Dit betekent dat een printer met een borstel in een hoek niet goed zal werken met deze functie. Je zou een borstel langs een hele kant van het bouwvolume nodig hebben.