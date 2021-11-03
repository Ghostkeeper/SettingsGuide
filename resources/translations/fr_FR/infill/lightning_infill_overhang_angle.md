Angle de surplomb du remplissage éclair
====
Le remplissage de type Eclair ne soutiendra que la face supérieure du modèle depuis l'intérieur où elle est dans le vide. Ce paramètre détermine l'angle du surplomb qui est soutenu par le remplissage Eclair depuis l'intérieur du modèle.

![Le surplomb jusqu'à 30° n'est pas soutenu.](../../../articles/images/lightning_infill_support_angle_30.png)
![Jusqu'à 70° n'est pas soutenu, laissant seulement le sommet de la sphère soutenu.](../../../articles/images/lightning_infill_overhang_angle_70.png)

Increasing this angle will reduce the amount of infill generated. Less of the top surface will get supported, if it's not a very steep overhang. This saves time and material, but may also cause the top surface to sag in places. Le résultat pourrait être un défaut de type [matelassage](../troubleshooting/pillowing.md) ou généralement une surface plus rugueuse.

Contrairement au réglage parent [Angle Support Remplissage Eclair](lightning_infill_support_angle.md), ce paramètre n'a pas d'influence sur le surplomb dans le motif de remplissage lui-même.
