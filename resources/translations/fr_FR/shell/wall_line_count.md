Nombre de lignes de la paroi
====
Ce paramètre détermine le nombre de contours qui seront dessinés autour de l'impression sur chaque couche.

![Deux murs](../../../articles/images/wall_thickness_0.8.png)
![Quatre murs](../../../articles/images/wall_thickness_1.6.png)

Un seul des murs sera un mur extérieur (affiché en rouge de le rendu Cura), il sera imprimé en utilisant les paramètres du mur extérieur. Le reste des murs sera imprimé avec les paramètres de la paroi intérieure.

Le nombre de murs est un facteur important dans la résistance d'une pièce. Comme les murs sont adjacents, ils peuvent se renforcer mutuellement, ce qui donne un ensemble plus solide. Pour des impressions plus grandes, cela peut être un moyen beaucoup plus efficace d'obtenir un objet résistant plutôt que d'ajuster le remplissage, en fonction de la forme.

Augmenter le nombre de parois fera :
* Augmenter considérablement la résistance de la pièce.
* Réduire l'effet de brillance lorsque le motif de remplissage est visible à l'extérieur.
* Améliorera les surplombs, car les lignes des murs sont généralement plus orientées vers leur point d'appui le plus proche.
* Rendra le modèle étanche plus facilement.
* Augmentera le temps d'impression et l'utilisation de matière.
