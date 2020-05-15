Topographie ou escalier
====
L'effet "topographie" est obtenu lorsqu'une face supérieure ou inférieure inclinée est imprimée avec une petite quantité de couches, de sorte que les limites entre les couches sont suffisamment espacées pour qu'elles deviennent facilement visibles. Il porte le nom de [cartes topographiques](https://en.wikipedia.org/wiki/Topographic_maps) où les différences d'altitude sont généralement indiquées par des courbes de niveau.

![Vous pouvez voir clairement les bords des couches](../../../articles/images/topography.jpg)

Cet effet est omniprésent dans l'impression 3D, et c'est l'un des moyens les plus faciles de reconnaître qu'un objet a été imprimé en 3D. Il est possible de l'éviter, mais le fait de l'empêcher réduit généralement la productivité de manière significative.

Hauteur de la couche
----
Comme l'effet de topographie se produit lorsque les frontières entre les couches sont très éloignées les unes des autres, il est possible d'éviter cet effet en réduisant la [hauteur de la couche](../resolution/layer_height.md). Lorsque la hauteur de la couche est réduite, les plus petits incréments verticaux entre les couches se traduiront également par des pas horizontaux plus petits, ce qui réduit l'effet de topographie. La réduction de la hauteur de la couche augmente cependant considérablement le temps d'impression.

Au lieu de réduire la hauteur de couche pour l'ensemble de l'impression, vous pouvez également réduire la hauteur de couche uniquement pour les faibles pentes de l'impression en utilisant [Utiliser des couches adaptatives](../experimental/adaptive_layer_height_enabled.md). Cela permet de réduire considérablement l'effet de la topographie tout en ayant un impact minimal sur le temps d'impression. Cependant, il est plus difficile de régler l'impression pour d'autres qualités que celles mentionnées ci-dessus, car le réglage dépend généralement de la hauteur de la couche.

Ajustement de la position du modèle
----
Vous pouvez également envisager de positionner le modèle de manière à ce qu'il n'y ait plus de faible pente dans l'impression. Mais cela implique généralement d'imprimer beaucoup plus de support pour votre modèle, ce qui réduit également la productivité, et les surplombs risquent de ne pas être aussi beaux.
