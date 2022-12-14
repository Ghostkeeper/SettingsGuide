Prioriteit Afstand Supportstructuur
====
Zowel de [X/Y-afstand van de Supportstructuur](support_xy_distance.md) als de [Z-afstand Supportstructuur](support_z_distance.md) van de support moeten exact worden gevolgd, niet meer en niet minder. Dit is een beperking, dus er moet een voorkeur zijn tussen de twee. Deze instelling stelt die voorkeur in.

X/Y heeft voorrang op Z
----
![X/Y heeft voorrang op Z](../../../articles/images/support_xy_overrides_z.svg)

Als de X/Y-afstand voorrang heeft op de Z-afstand, dan wordt de X/Y-afstand altijd constant gehouden, zelfs als dat betekent dat de Z-afstand groter is dan gewenst. De Z-afstand wordt echter nog steeds als de minimale afstand aangehouden. Dus als de overhang erg horizontaal is, heeft de Z-afstand nog steeds een effect, waardoor de X/Y-afstand groter wordt dan gewenst.

Z heeft voorrang op X/Y
----
![Z heeft voorrang op X/Y](../../../articles/images/support_z_overrides_xy.svg)

Als de Z-afstand voorrang heeft op de X/Y-afstand, dan wordt de Z-afstand altijd constant gehouden, zelfs als dat betekent dat de X/Y-afstand kleiner is dan gewenst. De X/Y-afstand heeft dan alleen invloed op de print waar de Z-afstand niet in het spel is, dus niet bovenop de draagconstructies, alleen aan de zijkanten.

Er wordt echter nog steeds een minimale X/Y-afstand aangehouden. Als de overhang erg verticaal is, zou de X/Y-afstand zo klein worden dat de support zou kunnen versmelten met de zijkanten van het model. De [Minimale X/Y-afstand Supportstructuur](support_xy_distance_overhang.md) voorkomt dit.