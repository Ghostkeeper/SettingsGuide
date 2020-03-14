Le Cross 3D [infill pattern](../infill/infill_pattern.md) a été conçu pour faciliter les impressions flexibles. Le motif contient des croisements à 4 voies qui sont cependant très rigides. Ce réglage permet d'éviter les croisements afin de ne pas être trop rigide à certains endroits. Le motif laissera une poche d'air dans le croisement. Ce réglage détermine la taille de la poche.

![La taille de la poche par défaut est de 2mm](../../../articles/images/infill_pattern_cross_3d.png)
![Un format de poche de 0,5mm](../../../articles/images/cross_infill_pocket_size_0_5.png)

Le modèle fait varier la distance autour du passage à quatre voies. Ce réglage détermine la taille de la poche dans les couches lorsque les lignes se touchent complètement. La taille maximale de la poche est déterminée par la densité de remplissage. La taille de la poche ne sera pas plus grande que la racine carrée de 2 fois la distance entre les lignes de remplissage. Si une valeur plus grande est saisie, cela n'aura aucun effet, mais des valeurs plus grandes peuvent toujours être saisies pour faciliter des tailles de poche plus grandes dans le cas où [remplissage progressif](../infill/gradual_infill_steps.md) ou [densité de remplissage variable](cross_infill_density_image.md) est utilisé.

L'augmentation de la valeur de ce paramètre rend le remplissage plus faible dans la direction verticale et permet de mieux répartir la force pour créer une distribution plus uniforme de la force.
