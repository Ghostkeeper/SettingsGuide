Pour imprimer plus vite, il est préférable d'imprimer à une température légèrement plus élevée. Cela rend le thermoplastique plus fluide, ce qui lui permet de s'écouler plus rapidement par l'ouverture de la buse. Lorsque [Auto Temperature](material_flow_dependent_temperature.md) est activé, ce paramètre spécifie pour chaque débit à quelle température le matériau doit être imprimé. Le débit est ensuite moyenné pour chaque couche afin de déterminer une température pour cette couche.

Le débit est calculé en millimètres cubes par seconde, moyenné pour une couche entière. La température est exprimée en degrés Celsius. La valeur de ce paramètre doit être une liste de coordonnées séparées par des virgules. Chaque coordonnée est de la forme `[<débit>, <température>]`.

Le but de ce réglage est d'obtenir une meilleure qualité d'impression, en réduisant la sur-extrusion et la sous-extrusion, s'il y a de grands changements de flux dans une impression. Un cas fréquent est celui de la frontière entre la peau et le remplissage. Comme la peau est normalement imprimée beaucoup plus lentement que le matériau de remplissage, les couches où il y a beaucoup de matériau de remplissage doivent être imprimées à une température légèrement plus élevée afin que le matériau puisse être correctement extrudé pendant l'impression de ce matériau de remplissage.

Pour de nombreuses imprimantes, le régulateur PID qui régule les températures dans la buse de l'imprimante a tendance à réagir de manière excessive lorsqu'il y a de nombreux changements de température en peu de temps. La température d'impression peut donc être très imprécise lorsque ce réglage est utilisé.

**Ce réglage n'est actuellement pas visible dans l'interface de Cura et ne peut pas être activé.**
