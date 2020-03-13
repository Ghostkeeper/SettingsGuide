Ce paramètre vous permet de modifier la direction dans laquelle les lignes du haut et du bas sont imprimées. Vous pouvez spécifier une liste d'angles séparés par des virgules (en degrés), et les lignes alterneront les directions par couche.

![Motif de lignes avec des angles de 0°, 60° et 120° alternés](../../../articles/images/skin_angles.gif)

Par défaut, le motif des lignes s'imprime dans les deux directions diagonales. Pour les systèmes à portique cartésien, c'est le plus précis, car l'imprimante peut utiliser les moteurs X et Y pour accélérer la buse lors du retournement pour la ligne suivante.

Il peut y avoir plusieurs raisons de changer ces directions :
* Pour obtenir un effet optique.
* Pour optimiser la force. L'impression sera normalement plus résistante lorsqu'elle est soumise à une poussée et à une traction parallèles aux lignes de la peau (et de remplissage).
* Pour réduire le surplomb. Si une impression est très fine dans une direction, faire un pont de peau dans cette direction peut être un moyen efficace d'économiser de la matière sur le remplissage. Aucun remplissage ne sera nécessaire pour combler l'écart. De même, vous pouvez également choisir une direction perpendiculaire au remplissage afin de réduire au minimum le débordement sur le remplissage. Cela permet d'obtenir une meilleure qualité de surface.
* Pour optimiser la précision si votre imprimante ne dispose pas d'un moteur pour la direction X et d'un moteur pour la direction Y, comme une imprimante avec un portique en H ou une imprimante delta.

Plusieurs nombres peuvent être saisis pour changer la direction de chaque couche. Par exemple, la saisie de `[0, 30, 60]` fait alterner entre 0 degré de distance de l'axe X, 30 degrés de distance et 60 degrés de distance.
