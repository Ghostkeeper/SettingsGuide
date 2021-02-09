Activer la tour d'amorçage
====
Ce système imprime une tour sur votre plateau d'impression avec un mélange de matériaux. La tour est destinée à être jetée, mais elle sert à amorcer le matériau après chaque changement d'extrudeuse.

![Comment se présente une tour d'amorçage, et ses dimensions](../images/prime_tower_fr.svg)

Pendant que d'autres extrudeuses impriment, il arrive qu'une buse suinte de la matière, laissant la chambre de la buse vide de matière. Il est essentiel d'amorcer le matériau par la suite, sinon le matériau ne s'écoulera pas encore correctement au début.

La tour d'amorçage est constituée d'une enveloppe extérieure qui est entièrement imprimée avec une extrudeuse, chaque couche. Cela est nécessaire pour garantir la stabilité de la tour, mais il faudra parfois recourir à des interrupteurs d'extrudeuse supplémentaires pour certaines impressions. Toutes les autres extrudeuses imprimeront des boucles à l'intérieur de cette enveloppe, en déversant leur matériau à l'intérieur de la tour, de préférence le long des parois intérieures. Ces extrudeuses n'ont pas besoin d'amorçage si elles démarrent sur la couche, car elles ne se mettront pas en veille à ce moment-là.

Le matériau choisi pour l'enveloppe extérieure est celui qui présente la plus grande [tendance à l'adhésion](../material/material_adhesion_tendency.md). C'est un paramètre caché qui ne peut pas être modifié depuis l'interface, qui indique dans quelle mesure les couches adhèrent les unes aux autres. En choisissant le matériau ayant la plus grande adhérence entre les couches, le risque de rupture de la tour d'amorçage est minimisé. Si plusieurs matériaux ont la même tendance à l'adhésion (par exemple, pour les impressions bicolores utilisant le même type de matériau), le numéro d'extrudeuse le plus bas est choisi.

En plus de l'amorçage, la buse effectuera également un mouvement à l'intérieur de la tour pour essuyer tout matériau de la buse qui s'est accumulé pendant la mise en veille. Cela empêche le suintement de coller à l'impression. C'est pourquoi la tour d'amorçage est aussi parfois appelée *tour d'essuyage*.

Les inconvénients de la tour d'amorçage sont qu'elle prend un peu plus de temps pour imprimer et qu'elle prend de la place sur le plateau d'impression.
