Knoopgrootte Draadprinten
====
Wanneer de [Draadprint Strategie](wireframe_strategy.md) is ingesteld op Nodes, wordt een kleine op- en neergaande beweging uitgevoerd aan het uiteinde van elke zaagtand. Deze instelling configureert de hoeveelheid van deze beweging.

![Waar het knooppunt is geplaatst en hoe groot het is](../../../articles/images/wireframe_top_jump.svg)

De beweging voor dit "knooppunt" bestaat uit een reeks verplaatsingen:
1. Eerst beweegt nozzle omhoog over de afstand die is opgegeven in deze instelling. Tegelijkertijd beweegt nozzle de helft van deze afstand naar achteren.
2. Als er een [Opwaardse Vertraging Draadprinten](wireframe_top_delay.md) bovenaan staat, zal de nozzle gedurende de ingestelde tijd pauzeren. Deze pauze wordt gemaakt aan de bovenkant van de beweging van de knoop.
3. Ten derde: nozzle gaat terug naar de normale hoogte. Tegelijkertijd beweegt nozzle 1,5 keer de knoopgrootte naar voren en eindigt op de afstand die in deze instelling is opgegeven vanaf de verticale lijn.

Het doel van de knoop is om de horizontale ring boven een oppervlak te geven om te verbinden met het zaagtandpatroon. De knoop zal van kant tot kant een beetje variëren, dus tenzij de horizontale ring heel nauwkeurig wordt geplaatst, is de kans groter dat ze aan elkaar blijven kleven. Ook trekt de knoop de lijn iets verder omhoog, zodat de horizontale ring eroverheen schuift. En tot slot zal de knoop ook enige lekkage veroorzaken vanwege het ontbreken van inkepingen in deze reisbeweging. Hierdoor ontstaat een klodder waarop de horizontale ring beter kan rusten.