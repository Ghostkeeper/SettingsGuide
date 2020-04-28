Spiraliser le contour extérieur
====
Spiraliser le contour extérieur est une astuce.

Lors de l'impression couche par couche, la buse doit normalement se déplacer d'une couche à l'autre. Ce mouvement fait que la buse reste presque immobile pendant une fraction de seconde, ce qui laisse une couture sur la surface appelée la couture Z. Ce réglage est destiné à empêcher cela et bien plus encore.

Lors de la mise en spirale du modèle, le modèle n'aura aucun remplissage ni aucun sommet. Il n'aura qu'une paroi et un fond. Il est essentiel que si [Lisser les contours spiralisés](smooth_spiralized_contours.md) est activé, la hauteur de la buse sera progressivement augmentée sur l'épaisseur d'une couche. De cette façon, une spirale est créée en suivant le contour du modèle. Il n'y aura aucun mouvement d'une couche à l'autre, car la buse s'est déjà déplacée progressivement vers la couche suivante. 

Le mode spirale est courant chez de nombreux trancheurs.  Il est aussi parfois appelé "mode vase", car c'est un bon moyen d'imprimer des vases.  Parmi les autres propriétés, on peut citer 
* Imprime extrêmement rapidement. 
* La surface devient très lisse. 
* Elle ne sera pas très résistante. 
* Il est difficile de rendre l'impression étanche si elle a un seul contour.  Pour cela, il est conseillé d'avoir au moins 2 murs. 

*La spiralisation ne fonctionnera pas bien avec des impressions ayant beaucoup de surfaces horizontales.  Elle ne gère pas du tout les surplombs et n'imprime pas les surfaces supérieures, donc rien ne pourra s'appuyer sur une surface horizontale.  Elle ne fonctionne pas bien non plus lorsqu'il y a plusieurs zones sur une couche.* 
