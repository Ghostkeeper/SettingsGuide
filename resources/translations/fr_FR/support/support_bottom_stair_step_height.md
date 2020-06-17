Hauteur de la marche de support
====
Si [Positionnement des supports](support_type.md) est réglé sur "Partout", le support est autorisé à reposer sur le modèle. Il ne suivra cependant pas exactement les contours du modèle. Au lieu de cela, le côté inférieur du support est doté d'un modèle en escalier. De cette façon, le support n'établit un lien avec le modèle qu'à quelques endroits.

Ce réglage détermine la hauteur de ces marches.

![Marches d'escalier se formant au bas du support](../../../articles/images/support_bottom_stair_step_height.png)

La hauteur des marches de l'escalier est comptée par la distance à la surface du modèle. Cela signifie que si vous avez défini une distance verticale dans le paramètre [Distance inférieure des supports](support_bottom_distance.md), celle-ci est soustraite de la hauteur et la connexion entre le modèle et le support sera plus grande. De même, le paramètre [Activer les bas de support](support_bottom_enable.md) permet également de réduire l'effet des marches d'escalier.

Le paramètre [Largeur maximale de la marche de support](support_bottom_stair_step_width.md) limite la largeur des marches. Si la surface du modèle est si peu profonde qu'une petite hauteur de marche entraînerait une grande largeur de marche, le support suivra la surface du modèle pour le reste de la hauteur de marche.

En réduisant ce paramètre, le bas du support sera plus lisse. Cela augmente l'adhérence entre le support et le modèle, ce qui rend le retrait du support plus difficile mais aussi le support plus stable.
