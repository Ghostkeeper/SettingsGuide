Facteur de compensation du débit
===

La compensation du débit est une expérience similaire à la fonctionnalité [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) de Marlin. Le but de la compensation du débit est de compenser la sous-extrusion et la surextrusion lorsque le débit de la matière sortant de la buse change. Ce réglage permet de configurer l'ampleur de l'effet.

La compensation du débit fait avancer le filament de la matière supplémentaire nécessaire dans la seconde qui suit, à chaque mouvement. Entre chaque mouvement, il y a trois scénarios possibles.
* Si les deux commandes de mouvement adjacentes ont le même débit (parce que leur largeur de ligne, leur hauteur de couche et leur vitesse sont les mêmes), alors l'avancement sera également le même. Le filament ne sera déplacé dans aucune direction entre ces lignes.
* Si le débit augmente avec la ligne suivante, le filament est déplacé plus loin vers l'avant pendant la deuxième ligne. Cela augmente la pression dans la chambre de la buse, de sorte que le matériau peut alors extruder plus rapidement pendant l'impression de la ligne et des lignes suivantes.
* Si le débit diminue avec la ligne suivante, le filament est déplacé vers l'arrière pendant la deuxième ligne. La pression dans la chambre de la buse est ainsi réduite, de sorte que le matériau ralentit pendant l'impression de la deuxième ligne et des lignes suivantes.

La distance sur laquelle le filament est déplacé est égale à la quantité de matière qui serait extrudée chaque seconde pendant la ligne (si la ligne était assez longue pour imprimer une seconde entière). Toutefois, grâce à ce réglage, cette distance peut être ajustée. En augmentant le facteur, l'effet de compensation sera plus fort. Le réduire rendra l'effet de compensation plus faible. Des facteurs plus élevés nécessiteront également plus de temps pour l'impression, car le filament doit être déplacé davantage vers le haut et vers le bas.

Si cette compensation de débit est activée, la pression à l'intérieur de la chambre de la buse devrait être mieux équipée pour gérer le débit à venir. Cela peut réduire à la fois la sous-extrusion et la sur-extrusion et donnera à l'objet des dimensions plus précises.

Cependant, la compensation est appliquée pendant une seule ligne. Il peut parfois s'agir d'une ligne courte, au cours de laquelle le filament doit se déplacer très rapidement. La tête d'impression peut avoir besoin de ralentir pour que le chargeur puisse suivre, ce qui provoquera l'apparition d'une tache. Parfois, il peut s'agir d'une longue ligne, ce qui réduit la force de l'effet. Cela rend toute la fonction de compensation des taux d'extrusion peu fiable, et c'est la raison pour laquelle ce réglage est encore expérimental.
