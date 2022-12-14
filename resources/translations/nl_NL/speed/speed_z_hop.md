Snelheid Z-sprong
====
Deze instelling configureert de verplaatsingssnelheid waarmee de verticale bewegingen worden uitgevoerd bij het uitvoeren van een Z-sprong. De horizontale bewegingen van een z-sprong worden niet beïnvloed omdat deze worden geconfigureerd door de [Bewegingssnelheid](speed_travel.md).

![De verticale beweging is met de z-hop snelheid](../../../articles/images/speed_z_hop.svg)

<!--if cura_version >= 4.2-->De z-sprongsnelheid wordt ook gebruikt als de snelheid voor het verplaatsen tussen lagen. In de praktijk speelt deze snelheid slechts een ondergeschikte rol, aangezien de beweging van een enkele laag zo kort is dat deze bijna altijd wordt beperkt door de acceleratie en niet door de maximale verplaatsingssnelheid.<!--endif-->

Voor de meeste printers is de Z-as robuust maar traag. Door de Z-sprongsnelheid te verhogen, worden de limieten van de Z-beweging getest, waardoor de Z-motor een paar stappen kan overslaan. Hierdoor zou de nozzle na de Z-sprong op een andere hoogte kunnen landen. Het verlagen van deze snelheid verkleint de kans dat dit gebeurt.

Aan de andere kant zorgt een hogere Z-sprongsnelheid ervoor dat nozzle sneller van het geprinte oppervlak weg beweegt. Dit kan de grootte van de klodders verkleinen.

Vanwege de lage acceleratiessnelheden op de Z-as wordt de gewenste Z-sprongsnelheid zelden bereikt, tenzij de Z-spronghoogte erg hoog of de snelheid erg laag is.