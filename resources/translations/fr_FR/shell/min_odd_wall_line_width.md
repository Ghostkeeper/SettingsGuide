Largeur minimale des lignes de paroi impaire
====
Lors de l'impression de pièces fines, Cura ajuste la largeur des lignes des parois pour s'adapter à la largeur exacte du modèle. Cura peut également décider d'utiliser moins de lignes pour les parois à la place. Ce paramètre est le seuil à partir duquel Cura supprime une ligne au centre. Il peut être ajusté séparément du [seuil auquel les deux lignes centrales se combinent](min_even_wall_line_width.md).

![Lorsque la ligne centrale est trop petite, les deux lignes qui l'entourent sont élargies.](../../../articles/images/min_wall_line_width_0_34.png)
![En réduisant ce réglage, la ligne centrale commence et finit beaucoup plus petit](../../../articles/images/min_wall_line_width_odd_0_1.png)

Nombre de lignes paires ou impaires
----
Ce paramètre permet d'ajuster le seuil de suppression des lignes spécifiquement lorsqu'il y a un nombre impair de lignes. C'est-à-dire lorsqu'il y a une seule ligne au centre plutôt que deux. Il détermine le moment où cette ligne unique est supprimée au profit des deux lignes qui l'entourent, légèrement plus larges.

La largeur minimale d'une ligne de paroi impaire peut être différente de la largeur minimale d'une ligne paire en raison de la manière dont elles se transforment. Lorsqu'une ligne impaire est supprimée, elle s'arrête avant la transition et laisse les parois environnantes se rapprocher. Pendant la transition, il y a un petit espace où les lignes environnantes ne se sont pas encore rapprochées. C'est différent de ce qui se passe lorsqu'il y a un nombre pair de cordons : Les deux lignes du milieu se rapprochent alors, en se chevauchant légèrement. Réduire la largeur minimale des lignes des parois impairs réduit la taille de l'écart aux transitions entre les lignes paires et impaires. La réduction de la largeur minimale des lignes des parois pairs réduit la surextrusion aux transitions entre les lignes paires et impaires.

Les vides laissés à la fin d'une ligne impaire sont plus visibles dans le résultat final qu'un léger dépassement au niveau d'un joint. Il pourrait donc être utile de fixer la largeur minimale des lignes de parois impairs un peu plus bas que la largeur minimale des lignes de parois pairs.

La réduction de ce paramètre conduit à:
* Espaces plus petits lorsqu'une ligne centrale se termine.
* Largeur maximale réduite d'une paire de lignes centrales paires.
* Des lignes plus fines, qui risquent de ne pas bien s'extruder.
* Des lignes plus longues, qui prennent plus de temps à imprimer.

**Ce paramètre ne s'applique pas seulement aux parois normales, mais aussi aux parois à contour supplémentaire, aux parois de soutien, aux parois de remplissage et aux motifs concentriques.**