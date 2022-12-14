Begin laag Y
====
Als er meerdere onderdelen op één laag moeten worden geprint, optimaliseert Cura de volgorde waarin deze onderdelen worden geprint. Om het onderdeel te laten afkoelen voordat de volgende laag wordt geprint, wordt elke laag in ongeveer dezelfde volgorde geprint. De instellingen [Begin laag X](layer_start_x.md) en Begin Laag Y bepalen welk onderdeel het eerst wordt geprint: het gedeelte dat dichtst bij de opgegeven coördinaten. Deze instelling bepaalt de Y-coördinaat van dit onderdeel.

Dit is een andere instelling dan de Z-naad. De instellingen voor Z-naaduitlijning bepalen alleen waar de printer de omtrek van een onderdeel begint printen, terwijl deze instelling bepaalt met welk onderdeel het begint.

Als uw printer iets specifieks doet bij het starten van een nieuwe laag of het wijzigen van de extruder, is het een goed idee om deze coördinaten in te stellen op de positie waar de printkop zal eindigen wanneer deze klaar is om door te gaan met printen. Dit minimaliseert verplaatsafstanden en vuil.

Deze coördinaten bevinden zich in het G-code coördinatensysteem, dat verschilt van het coördinatensysteem dat Cura gebruikt om de positie van objecten weer te geven.