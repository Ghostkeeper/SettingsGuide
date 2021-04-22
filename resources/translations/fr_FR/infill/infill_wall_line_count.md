Nombre de parois de remplissage supplémentaire
====
Ce réglage ajoute un certain nombre de contours autour des zones de remplissage. Cela revient à augmenter le [nombre de lignes de la paroi](../shell/wall_line_count.md), mais les contours ne font pas le tour de la peau et les parois seront également entre la peau et le remplissage. C'est également similaire à l'ajout de [supplémentaire de parois extérieures](../top_bottom/skin_outline_count.md), mais autour du remplissage plutôt qu'autour de la peau.

Ces parois sont imprimées avec les paramètres de remplissage.

![Deux parois supplémentaires autour du remplissage](../../../articles/images/infill_wall_line_count.png)

Par rapport à l'ajout de parois supplémentaires extérieures, ce réglage augmente considérablement la résistance du modèle et réduit la visibilité du remplissage à travers la peau, mais augmente également le temps d'impression et l'utilisation du matériau. Alors que des parois extérieures supplémentaires remplaceront le matériau qui aurait été imprimé comme peau de toute façon, ce réglage ajoute en fait du matériau à moins que la densité de remplissage ne soit déjà de 100 %.

Cela ressemble beaucoup à l'ajout de parois extérieures supplémentaires. Cependant, il est conseillé d'ajouter au moins une paroi supplémentaire autour du remplissage ou extérieure, car cela empêche les lignes de peau de se terminer dans le vide.
