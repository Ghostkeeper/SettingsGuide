Relatif à la jointure en Z
====
Lorsque la couture est placée à un endroit spécifié par l'utilisateur conformément au paramètre [Alignement de la jointure en Z](z_seam_type.md), vous pouvez saisir les coordonnées de l'endroit où la couture doit être placée. Normalement, ces coordonnées indiquent un emplacement sur le plateau d'impression, par exemple au dos de l'imprimante. Si ce paramètre est activé, ces coordonnées seront prises par rapport à la position du modèle.

![Désactivé : Les coordonnées indiquent une position absolue au centre de la plaque de montage, de sorte que toutes les bandes blanches pointent vers le milieu](../../../articles/images/z_seam_relative_disabled.png)
![Activé : Les coordonnées sont relatives au modèle, donc chaque modèle aura les bandes blanches dans le même coin](../../../articles/images/z_seam_relative_enabled.png)

Lorsqu'un maillage est dupliqué sur le plateau d'impression, ce réglage fait que la couture est positionnée exactement au même endroit pour chacun des duplicatas, plutôt que de les faire pointer vers le même point sur le plateau. Cela vous permet d'imprimer chaque copie exactement de la même manière, quelle que soit sa position sur le plateau d'impression.
