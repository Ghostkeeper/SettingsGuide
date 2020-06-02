Hauteur de la couche initiale
====
Ce paramètre définit l'épaisseur de la première couche de votre impression. La couche initiale est normalement imprimée plus épaisse que le reste afin de créer une adhérence plus forte avec le plateau d'impression. Avec ce réglage, l'épaisseur de la couche initiale peut être augmentée sans réduire la résolution du reste de l'impression.

![La couche initiale est plus épaisse que le reste des couches](../../../articles/images/layer_height_0.png)

L'augmentation de l'épaisseur de la couche initiale fait que la buse extrude plus de matière sur la même distance. Cela demande une force supplémentaire, car le matériau s'étale sur les côtés pour remplir toute la largeur de la ligne. Cette force supplémentaire fait que le matériau adhère mieux au plateau d'impression. De plus, la couche plus épaisse permet de rattraper les irrégularités de la planéité de la surface. Si le plateau d'impression est légèrement tordu, la variabilité sera absorbée par l'épaisseur de la première couche, alors qu'autrement la buse pourrait le racler dans la deuxième couche.

Une épaisseur trop importante de la première couche entraîne un affaissement plus important de la première couche, ce qui provoque des pattes d'éléphant. Le paramètre [Expansion horizontale de la couche initiale](../shell/xy_offset_layer_0.md) peut empêcher cela en lui donnant une petite valeur négative.
