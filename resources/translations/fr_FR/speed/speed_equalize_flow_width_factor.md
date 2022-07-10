Rapport d'égalisation des débits
====
Cette fonction vous permet de modifier la méthode utilisée par votre imprimante pour ajuster la largeur de la ligne : au lieu de modifier le débit du matériau à travers la buse, l'imprimante modifie la vitesse à laquelle la buse se déplace.

Les imprimantes FFF sont notoirement incapables de modifier la vitesse à laquelle le matériau sort de la buse. Si l'imprimante modifie la vitesse de l'extrudeur, il faut une fraction de seconde avant que cela ne se traduise réellement par un changement de débit. À ce moment-là, en fonction de la vitesse d'impression, la buse peut déjà avoir dépassé de plusieurs millimètres le point où le débit aurait dû être ajusté. C'est encore pire si votre imprimante a l'extrudeur éloigné de la tête d'impression avec un tube Bowden entre les deux.

Au lieu de modifier la vitesse d'alimentation, l'imprimante peut également modifier la vitesse de déplacement de la tête d'impression. La tête d'impression peut accélérer beaucoup plus rapidement, ce qui permet de mieux contrôler la largeur de la ligne. Si la tête d'impression accélère alors que le débit reste le même, la même quantité de matériau est étirée sur une plus grande longueur, ce qui réduit la largeur de la ligne. Si la tête d'impression ralentit, la même quantité de matériau est regroupée dans un espace plus petit, ce qui augmente la largeur de la ligne.

Ce paramètre est un ratio. Il peut régler le débit (0 %) ou la vitesse d'impression (100 %) ou une combinaison des deux. Le rapport peut même dépasser 100 %, ce qui signifie que le débit est réduit afin de produire des lignes plus épaisses, mais que la vitesse est encore plus réduite pour compenser.

Augmenter ce ratio vers 100% signifie qu'il utilise la vitesse au lieu du débit pour modifier la largeur de la ligne, ce qui a les effets suivants sur l'impression :
* La largeur du trait est probablement plus précise, ce qui améliore la précision dimensionnelle de l'impression.
* Le débit sera maintenu égal, ce qui rend l'impression plus fiable, notamment avec les matériaux exotiques.
* À certains endroits, la tête d'impression se déplace plus rapidement, ce qui peut entrainer des vibrations.

Ce réglage ne s'applique qu'aux variations de la largeur des lignes causées par l'adaptation des lignes à la largeur des parois minces et des angles aigus. Les variations de débit dues à des paramètres tels que des largeurs de ligne différentes pour le remplissage par rapport au parois ne seront pas compensées, ni les fonctions telles que le pontage ou le lissage. Les imprimantes qui mettent en œuvre la fonction Linear Advance ou des fonctions de compensation similaires doivent continuer à les utiliser, même si ce paramètre est réglé sur 100 %, car des changements de débit peuvent toujours se produire en raison de ces paramètres.