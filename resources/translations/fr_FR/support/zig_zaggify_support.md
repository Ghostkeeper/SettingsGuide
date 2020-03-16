Relier les lignes de support
===

Avec certains modèles de support, le support peut devenir très instable lorsque de fines bandes de support sont nécessaires. Ce réglage entraînera la connexion des extrémités des lignes de support entre elles. Cela leur donne plus de stabilité. Cela permet également au support de s'imprimer avec un flux plus continu. Moins de déplacements seront nécessaires.

![Lignes de support déconnectées](../../../articles/images/zig_zaggify_support_disabled.png)
![Lignes de support connectées](../../../articles/images/zig_zaggify_support_enabled.png)

Lorsqu'une ligne de soutien est tracée, au lieu de se rendre à la ligne suivante, une ligne sera tracée le long de la frontière de la zone de soutien vers la ligne suivante. Cela permet de convertir l'ensemble de la zone de soutien en une seule ligne ou en très peu de lignes. La conversion en une seule ligne n'est pas toujours possible. Le point de départ de cette ligne est arbitraire, de sorte que très souvent, il y aura des lignes suspendues en l'air parce que dans une couche, deux lignes peuvent être connectées à un point final, tandis que dans la couche suivante, elles sont connectées de l'autre côté. Cela rend le support un peu plus faible mais toujours stable et cela permet d'éviter les interruptions de flux. Le comportement de ce paramètre est le même que celui de [Relier les lignes de remplissage](../infill/zig_zaggify_infill.md).

La connexion des lignes de soutien présente quelques avantages, mais aussi quelques inconvénients :
* Le support sera plus stable, moins susceptible de basculer pendant l'impression.
* Le débit sera maintenu plus constant, ce qui vous permettra d'imprimer le support à une plus grande vitesse sans problème de débit. Ceci est particulièrement important pour les supports qui sont difficiles à extruder correctement.
* Si des retraits sont effectués pendant le support, il y aura beaucoup moins de retraits nécessaires pendant l'impression du support, ce qui empêche le matériau de se broyer.
* Il faut plus de matériau pour imprimer le support.
* Il faut généralement plus de temps pour imprimer le support, car les mouvements de déplacement sont normalement plus rapides que l'impression des lignes de support.

Le motif de support en zigzag est toujours relié (selon une technique légèrement différente). Ce réglage n'est pas disponible pour le motif en zigzag.
