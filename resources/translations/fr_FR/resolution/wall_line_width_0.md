La largeur de la ligne de la paroi extérieure peut être ajustée séparément de celle des parois intérieures. Ce réglage indique la largeur de la ligne de la paroi extérieure.

![Le contour de la paroi extérieure est beaucoup plus large que le reste](../../../articles/images/wall_line_width_0.png)

On sait que la réduction de la paroi extérieure à une largeur de ligne légèrement inférieure à la taille de la buse est bénéfique pour la résistance. La buse extrudera un peu moins de matière, mais son ouverture chevauchera la paroi intérieure adjacente. Le matériau est alors repoussé par la paroi précédemment placée à son emplacement correct. Mais cela permettra également au plastique de mieux fusionner avec les parois adjacentes. Ainsi, la paroi extérieure fusionne mieux avec les parois intérieures, de sorte que celles-ci puissent combiner leurs forces. Cela améliore considérablement la résistance des murs.

La réduction de la largeur de la ligne de la paroi extérieure permet également à la buse d'imprimer des détails plus fins, car la ligne plus fine s'adaptera mieux aux petits détails.

L'augmentation de la largeur de la ligne de la paroi extérieure peut réduire le temps d'impression. Vous pouvez obtenir une paroi d'épaisseur similaire avec moins de parois intérieures. La résistance sera tout de même quelque peu réduite car la paroi extérieure ne fusionnera pas aussi bien avec les parois intérieures.

Ajuster les lignes
----
Lors de l'impression de pièces fines, le réglage de la largeur des lignes de la paroi est un outil important pour obtenir des pièces précises et solides. Cura ne dessine jamais que des contours complets, donc si un contour n'est pas adapté, un espace va tomber dans les parois, ce qui compromet grandement la solidité et la précision de la pièce.

Cura tentera de combler ces vides entre les murs si [Remplir les vides entre les murs](../shell/fill_perimeter_gaps.md) est activé, mais cette technique est loin d'être idéale pour les formes arbitraires et prend souvent beaucoup de temps d'impression. Lorsque deux murs se chevauchent, la fonction [Compenser les chevauchements de murs](../shell/travel_compensate_overlapping_walls_enabled.md) réduit la largeur de la ligne de mur pour s'assurer que la pièce est dimensionnellement précise, mais cela entraîne des changements de flux qui réduisent également la qualité et la résistance de l'impression.

Pour un ajustement idéal, il faut que la pièce soit un multiple exact de la largeur de la ligne de paroi afin que les parois s'adaptent précisément à la pièce. Si vous connaissez la largeur de votre pièce, cela peut facilement se faire en ajustant la largeur des parois. Vous voyez d'abord combien de contours vous voulez ajuster de manière à ce que les lignes aient encore une largeur raisonnable. Ensuite, vous pouvez voir de combien vous devez ajuster la largeur des lignes des murs pour que les lignes s'ajustent correctement. Gardez à l'esprit que vous pouvez ajuster la [Largeur de la ligne de mur extérieure](./largeur_ligne_mur_0.md) et la [Largeur de la ligne de mur intérieure](./wall_line_width_x.md) séparément. Comptez soigneusement le nombre de fois que chaque type de mur sera dessiné pour prévoir l'effet de la modification de la largeur de la ligne de mur.

L'ajustement des lignes de mur est une compétence importante pour l'impression 3D qui distingue les opérateurs experts d'imprimantes 3D des autres. Une certaine pratique est nécessaire.
