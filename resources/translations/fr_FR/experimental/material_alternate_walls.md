Alterner les directions des parois
====
S'il est activé, ce paramètre fait alterner le sens d'enroulement des parois entre le sens horaire et le sens antihoraire.

La première paroi intérieure sera imprimée dans le sens inverse de la paroi extérieure, et la deuxième paroi intérieure sera à nouveau imprimée dans le sens inverse. De plus, sur la couche suivante, le sens sera également opposé, de sorte que les parois empilés les uns sur les autres seront également alternés.

L'alternance de la direction d'impression réduit l'effet des contraintes internes à l'intérieur du modèle, ce qui réduit l'effet de [Décollement](../troubleshooting/warping.md). Lors de l'impression d'une ligne, la buse tire assez fort sur le cordon de matière fondue, ce qui étire le plastique. Pendant la solidification, cette contrainte peut déformer le modèle. Si la ligne adjacente est imprimée dans la direction opposée, cette contrainte est contrecarrée par les lignes adjacentes qui tirent dans la direction opposée. La force de la contrainte est contrée par la contrainte dans la direction opposée.

L'inconvénient de l'alternance du sens des parois provient de l'hystérésis du portique de l'imprimante. S'il y a du jeu dans les axes ou les poulies de l'imprimante, les lignes diagonales seront placées à un endroit légèrement différent lors de l'impression dans la direction opposée. En conséquence, la paroi devient moins lisse et les dimensions de l'impression moins précises. Une imprimante bien réglée ne montrera pas cet effet, donc si l'imprimante a des courroies, des poulies et des composants précis serrés, l'alternance des directions des parois ne donnera probablement que des avantages.

Lors de [l'impression de l'intérieur vers l'extérieur](../shell/inset_direction.md), ce paramètre rend la couture des parois plus visible et provoque un certaine vibrations, car la buse fait un tour complet de 180° juste avant le début des parois extérieur, ce qui provoque des vibrations. Ce n'est pas un effet marquant lorsque l'on imprime de l'extérieur vers l'intérieur.
