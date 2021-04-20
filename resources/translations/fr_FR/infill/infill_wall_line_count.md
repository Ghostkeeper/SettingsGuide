Nombre de parois de remplissage supplémentaire
====
Ce réglage ajoute un certain nombre de contours autour des zones de remplissage. Cela revient à augmenter le [nombre de lignes de la paroi](../shell/wall_line_count.md), mais les contours ne font pas le tour de la peau et les murs seront également entre la peau et le remplissage. C'est également similaire à l'ajout de [parois de peau supplémentaires](../top_bottom/skin_outline_count.md), mais autour du remplissage plutôt qu'autour de la peau.

Ces parois sont imprimées avec les paramètres de remplissage.

![Deux murs supplémentaires autour du remplissage](../../../articles/images/infill_wall_line_count.png)

Par rapport à l'ajout de parois supplémentaires autour de la peau, ce réglage augmente considérablement la résistance du modèle et réduit la visibilité du remplissage à travers la peau, mais augmente également le temps d'impression et l'utilisation du matériau. Alors que des parois de peau supplémentaires remplaceront le matériau qui aurait été imprimé comme peau de toute façon, ce réglage ajoute en fait du matériau à moins que la densité de remplissage ne soit déjà de 100 %.

Cela ressemble beaucoup à l'ajout de parois supplémentaires autour de l'ensemble de l'impression. Cependant, il est conseillé d'ajouter au moins une paroi supplémentaire autour du remplissage ou de la peau, car cela empêche les lignes de peau de se terminer en plein air.
