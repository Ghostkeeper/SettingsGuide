Ordre des parois
====
Ce paramètre détermine quels parois sont imprimées en premier, de l'extérieur vers l'intérieur ou de l'intérieur vers l'extérieur.

![La paroi intérieure est imprimée en premier](../../../articles/images/outer_inset_first_disabled.gif)
![La paroi extérieure est imprimée en premier](../../../articles/images/outer_inset_first_enabled.gif)

Ce paramètre a un léger effet sur la qualité ainsi que sur la précision dimensionnelle:
* L'impression de l'extérieur vers l'intérieur améliore la précision dimensionnelle. Les parois adjacentes se poussent généralement un peu, surtout si la largeur de la ligne de paroi est inférieure à la taille de la buse. La paroi qui est imprimée en premier aura été solidifiée et ne sera donc pas autant poussée. Par conséquent, en imprimant le mur extérieur en premier, vous obtiendrez un emplacement plus précis du mur extérieur.
* Si le remplissage est imprimé avant les murs, l'impression de l'extérieur vers l'intérieur réduira la quantité de remplissage qui transparaît sur la surface. Sinon, le remplissage est imprimé en premier, puis les murs intérieurs qui sont poussés vers l'extérieur par le remplissage, et enfin le mur extérieur qui est poussé vers l'extérieur par les murs intérieurs. Par conséquent, un motif pourrait être visible à l'extérieur. Si la paroi extérieure est imprimée en premier, elle peut se solidifier avant que la paroi intérieure ne puisse la pousser.
* L'impression de l'intérieur vers l'extérieur est meilleure pour la création des surplombs. La paroi extérieure est plus éloignée de la couche précédente que la paroi intérieure. Lorsque la paroi extérieure est imprimée en premier, elle n'a encore rien à quoi s'accrocher. Lorsque la paroi intérieure est imprimée en premier, la paroi extérieure peut se fixer latéralement à la paroi extérieure.

Lorsqu'il y a un nombre impair de murs, le mur du centre sera toujours imprimé en dernier.