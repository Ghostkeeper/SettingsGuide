Nombre de distributions des parois
====
Cura peut ajuster la largeur des lignes des parois pour mieux s'adapter à la forme que vous imprimez, mais il n'est pas obligé d'ajuster chaque cordon de la même manière. Il préfère modifier la largeur des cordons plus vers l'intérieur du modèle. Ce paramètre détermine le nombre de cordons, en comptant de l'intérieur vers l'extérieur, qui sont ajustés pour s'adapter à l'espace disponible.

![Concentré au milieu, avec de grandes variations dans les largeurs de ligne à cet endroit.](../../../articles/images/wall_distribution_count_1.png)
![Répartis sur plusieurs cordons](../../../articles/images/wall_distribution_count_5.png)

Les cordons à largeur variable sont plus difficiles à imprimer que les simples cordons à largeur constante. Il faut un certain temps pour ajuster le débit de la buse, et pour faire la transition, il faut aussi faire quelques angles aigus qui peuvent provoquer des vibrations parasites. Il est préférable de faire tout cela le plus loin possible de l'extérieur, là où cela serait visible sur la surface de l'impression. Cura concentrera donc les ajustements de largeur de ligne sur les cordons les plus internes.

D'un autre côté, la concentration de la variation signifie également que les lignes du milieu auront des largeurs très divergentes. En répartissant cette variation sur un plus grand nombre de lignes, l'amplitude des variations peut être plus faible, ce qui réduit l'impact de la largeur variable des lignes au lieu de la cacher à l'intérieur.

Ce paramètre permet de sélectionner un certain nombre de cordons de l'intérieur parmi lesquels la largeur de ligne peut être ajustée pour remplir l'espace disponible. Cela compte dans les deux sens à partir du centre, donc si ce paramètre est réglé sur 2, jusqu'à 4 cordons peuvent être ajustés au centre. L'ajustement n'est pas non plus réparti uniformément entre ces cordons. Les cordons du centre seront toujours légèrement plus ajustés que les cordons plus proches de l'extérieur.

Dans la mesure du possible, le cordon extérieure est toujours maintenu à la largeur de ligne nominale. Ce cordon a une telle influence sur la qualité de l'impression qu'il est maintenue à une largeur de ligne constante afin de rendre la surface aussi lisse que possible. Ce n'est que si la pièce devient si mince qu'elle n'est constituée que de cordons extérieures que ceux-ci seront ajustés.

En pratique, cacher les imperfections au centre est presque toujours une meilleure stratégie que de les répartir sur plusieurs cordons. Par conséquent, il est préférable de maintenir ce paramètre aussi bas que possible. Lorsque vous travaillez avec des matériaux difficiles à extruder ou à modifier, comme les matériaux flexibles, il est utile d'augmenter ce paramètre pour réduire les changements de flux. Cependant, il ne peut jamais empêcher complètement ces changements de flux.

**Ce paramètre ne s'applique pas seulement aux parois normales, mais aussi aux parois à contour supplémentaire, aux parois de soutien, aux parois de remplissage et aux motifs concentriques.**
