Épaisseur de la couche de remplissage de support
====
La qualité visuelle et la résolution du support n'étant pas importantes, vous pouvez utiliser des couches plus épaisses pour le support afin de réduire le temps d'impression. Ce paramètre permet de configurer l'épaisseur des couches avec lesquelles le support sera imprimé.

En vue par couches, on aura l'impression que les lignes du support sont devenues beaucoup plus larges. Lorsqu'elles seront imprimées, les lignes de support descendront davantage au lieu de s'étendre horizontalement.

![L'épaisseur de la couche de remplissage du support est définie à trois fois la hauteur de la couche](../../../articles/images/support_infill_sparse_thickness.png)

L'épaisseur de la couche de remplissage du support doit être un multiple de la hauteur de la couche ordinaire. Si elle ne l'est pas, elle sera arrondie à la hauteur de couche la plus proche.

Ce réglage ne s'applique pas au toit ou au plancher du support, mais uniquement à la structure principale du support.

Ce réglage est particulièrement utile lorsque le support est imprimé avec un matériau différent du reste de l'impression, et encore plus lorsque ce matériau est difficile à extruder, comme le PVA. Comme le support n'est pas extrudé sur chaque couche, l'imprimante n'aura pas besoin de changer d'extrudeuse aussi souvent, ce qui permet de gagner beaucoup de temps. Étant donné que davantage de matériau est extrudé sur les couches qui sont imprimées, les matériaux qui mettent un certain temps à démarrer le flux seront imprimés de manière plus fiable.

Faites attention à ne pas trop augmenter ce débit. Lors du changement de support, le débit à travers la buse doit être accéléré et décéléré de manière significative. Il peut y avoir un certain retard sur ce point, de sorte que le débit sera trop faible au début du support et trop important après la fin du support.
