Vulpolygonen Verbinden
====
Als de vulling uit gesloten lijnen bestaat, kunnen deze gesloten lijnen worden samengevoegd tot één lijn. Als u deze functie activeert, worden er kleine verbindingen gemaakt tussen aangrenzende polygonen.

Deze instelling is alleen beschikbaar als de vulling uit aangrenzende lijnen bestaat. Dit betekent dat ofwel:
* Het [Vulpatroon](infill_pattern.md) is ingesteld op Kruis of Kruis 3D.
* De infill-lijnen zijn [Vermenigvuldiging Vullijn ](infill_multiplier.md) met een even getal.
* Er zijn minstens 2 [Aantal Extra Wanden Rond vulling](infill_wall_line_count.md).

![Met meerdere opvullijnen zijn er veel lussen in dit opvulpatroon.](../../../articles/images/connect_infill_polygons_disabled.png)
![Schakel deze instelling in om de lussen met elkaar te verbinden.](../../../articles/images/connect_infill_polygons_enabled.png)

Het doel van deze functie is het voorkomen van teveel nozzle bewegingen. De laatste lijn bestaat uit een enkele lus voor elk verbonden stuk infill, dus er zijn extra geen nozzle bewegingen. Dit maakt het gemakkelijker om met flexibele filamenten te werken omdat ze moeilijker te voeden zijn en het beste werken als ze door nozzle mogen blijven stromen.

Het verbinden van deze lussen kan de vulling ook sterker maken omdat de verbinding tussen de lussen binnenin wordt verbeterd. Wanneer de polygonen echter zijn aangesloten, moet de printkop vlak voor een aansluiting vaak 180 graden draaien. Deze wendingen zorgen er soms voor dat de verbinding niet volledig tot stand komt. In sommige gevallen kan dit er ook toe leiden dat de vulling zwakker wordt. Het hangt allemaal af van hoe de lussen door de vorm van uw model verstrengelen.