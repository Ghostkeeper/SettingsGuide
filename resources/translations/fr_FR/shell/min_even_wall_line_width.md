Largeur minimale des lignes de paroi paire
====
Lors de l'impression de pièces fines, Cura ajuste la largeur des lignes de paroi pour s'adapter à la largeur exacte du modèle. Cura peut également décider d'utiliser moins de lignes à la place. Ce paramètre est le seuil à partir duquel Cura combinera deux lignes en une seule. Il peut être réglé séparément du [seuil auquel la ligne centrale est supprimée](min_odd_wall_line_width.md).

![La ligne centrale est élargie pour s'adapter](../../../articles/images/min_wall_line_width_0_34.png)
![En réduisant ce paramètre, il utilise plutôt deux lignes](../../../articles/images/min_wall_line_width_even_0_1.png)

Nombre de lignes paires ou impaires
----
Ce paramètre permet de régler le seuil de suppression des lignes spécifiquement lorsqu'il y a un nombre pair de lignes. C'est le cas lorsqu'il y a deux lignes au centre plutôt qu'une seule ligne. Il détermine le moment où ces deux lignes au centre se combinent en une seule ligne.

La largeur minimale d'une ligne de paroi paire peut être différente de la [largeur minimale de la ligne de paroi impaire](min_odd_wall_line_width.md) en raison de la manière dont elles se rejoignent. Les lignes paires se rejoignent à leurs extrémités en rapprochant les extrémités. Il y a un certain chevauchement avec ces lignes à cet endroit, ce qui entraîne une surextrusion. Ceci est différent de la situation où il y a un nombre impair de cordons : La ligne du milieu s'arrête alors tout simplement, laissant un vide dans l'impression. Réduire la largeur minimale des lignes des parois paires réduit la surextrusion aux transitions entre les lignes paires et impaires. En réduisant la largeur minimale des lignes des murs impairs, on réduit la taille du vide aux transitions entre les lignes paires et impaires.

Les vides laissés à la fin d'une ligne impaire sont plus visibles dans le résultat final qu'un léger dépassement au niveau d'un joint. Il pourrait donc être utile de fixer la largeur minimale des lignes de murs pairs un peu plus haut que la largeur minimale des lignes de murs impairs.

La réduction de ce paramètre conduit à:
* Réduction de la zone de chevauchement où deux lignes se rejoignent pour se fondre en une seule ligne.
* Réduction de la largeur maximale des lignes centrales uniques.
* Des lignes plus fines, qui peuvent ne pas bien s'extruder.
* Plus de lignes, qui prennent plus de temps à imprimer.

**Ce paramètre ne s'applique pas seulement aux parois normales, mais aussi aux parois à contour supplémentaire, aux parois de soutien, aux parois de remplissage et aux motifs concentriques.**