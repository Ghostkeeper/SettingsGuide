Est l'origine du centre
====
Si ce paramètre est activé, la coordonnée 0,0 de l'imprimante est réglée pour se trouver au milieu du volume de construction, plutôt que dans le coin avant gauche.

Dans certaines imprimantes, le microprogramme considère que la coordonnée 0,0 est au centre du volume de construction. C'est courant pour les imprimantes de type delta, qui ont généralement des volumes de construction cylindriques plutôt que cubiques.

Si la coordonnée zéro de l'imprimante est au centre, le code g final contiendra des coordonnées négatives ainsi que des coordonnées positives. L'origine des coordonnées se trouvera au milieu du volume de construction de Cura. Cura affichera également son marqueur de coordonnées tricolore au centre. Toutefois, les coordonnées des fichiers 3MF seront toujours traitées comme si l'origine des coordonnées se trouvait dans le coin avant gauche de l'imprimante, puisque le format de fichier 3MF l'exige.

*Comme il s'agit d'un réglage de la machine, il ne sera normalement pas répertorié dans la liste normale des réglages. Il existe cependant une case à cocher pour ce paramètre dans la boîte de dialogue des paramètres de l'imprimante, qui se trouve dans la liste des imprimantes ajoutées dans la boîte de dialogue des préférences.*
