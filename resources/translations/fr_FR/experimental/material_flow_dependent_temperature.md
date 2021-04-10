Température auto
====
Pour imprimer plus vite, il est préférable d'imprimer à une température légèrement plus élevée. Cela rend le thermoplastique plus fluide, ce qui lui permet de s'écouler plus rapidement par l'ouverture de la buse. Ce réglage ajuste automatiquement la température en fonction du débit moyen du matériau hors de la buse.

Pour savoir dans quelle mesure la température doit être ajustée, le [graphique de la température du flux](material_flow_temp_graph.md) est référencé. Le débit est calculé en millimètres cubes par seconde. Si l'on met cela en relation avec la température du flux, on obtient une certaine température. Cette température sera utilisée comme température d'impression. Lorsque ce réglage est activé, le réglage ordinaire [température d'impression](../material/material_print_temperature.md) ne sera plus utilisé en faveur de la température calculée à partir du débit.

Le but de ce réglage est d'obtenir une meilleure qualité d'impression, en réduisant la sur-extrusion et la sous-extrusion, s'il y a de grands changements de débit dans une impression. Un cas fréquent est celui de la frontière entre la peau et le remplissage. Comme la peau est normalement imprimée beaucoup plus lentement que le matériau de remplissage, les couches où il y a beaucoup de matériau de remplissage doivent être imprimées à une température légèrement plus élevée afin que le matériau puisse être correctement extrudé pendant l'impression de ce matériau de remplissage.

Pour de nombreuses imprimantes, le régulateur PID qui régule les températures dans la buse de l'imprimante a tendance à réagir de manière excessive lorsqu'il y a de nombreux changements de température en peu de temps. La température d'impression peut donc être très imprécise lorsque ce réglage est utilisé.

**Ce réglage n'est actuellement pas visible dans l'interface de Cura et ne peut pas être activé.**
