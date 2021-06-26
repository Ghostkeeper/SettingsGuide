Décalage en Z lors d’une rétraction
====
Si ce réglage est activé, la buse sera légèrement soulevée au-dessus de l'impression lorsque la buse doit se déplacer d'un endroit à l'autre. L'objectif est que la buse passe au-dessus de l'impression au lieu de frotter les parties précédemment imprimées avec la buse.

![Déplacement vers le haut lorsque les sauts Z sont activés](../images/retraction_hop_enabled_fr.svg)

Chaque fois qu'un retrait est effectué, la buse est relevée (ou le plateau d'impression abaissée) pour créer un espace entre la buse et l'impression. Cela présente plusieurs avantages :
* Il empêche la buse de heurter l'impression pendant les déplacements. Lorsque la buse frotte l'impression, elle laisse une cicatrice visible, ce qui devrait améliorer la qualité visuelle des parois de l'impression.
* Si la matière suinte de la buse pendant les déplacements, l'exsudat se dépose à l'endroit où la buse se pose après le déplacement, souvent dans le remplissage où il n'est pas visible. Cela permet de réduire les défauts à la surface.
* Les frottements sur la surface ont une chance de faire tomber votre impression, donc activer ce paramètre peut améliorer la fiabilité de l'impression.

Cependant, le déplacement de la buse de haut en bas prend un peu plus de temps, de sorte que votre impression sera plus longue à réaliser. L'axe Z de l'imprimante peut également s'user plus rapidement, selon la conception de l'imprimante.
