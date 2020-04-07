Décalage avec l'extrudeuse
====
Ce paramètre décide si Cura doit écrire les coordonnées de la tête d'impression ou de la buse.

Si votre imprimante n'a qu'une seule buse, le système de coordonnées de votre imprimante est très probablement aligné sur votre buse. Cela signifie qu'en se déplaçant vers la position [50,50], la pointe de la buse se déplace effectivement vers cette position. Si votre imprimante a plusieurs buses et que ces buses sont côte à côte dans la tête d'impression, alors c'est important.

Certaines imprimantes déplacent la tête d'impression au même endroit, quelle que soit la buse actuellement activée. Alors que le code g peut ordonner à l'imprimante de se placer en position [50,50], l'extrémité de la buse actuellement active peut être placée en position [68,50] puisqu'elle se trouve, par exemple, à 18 mm à droite de la première buse. Si c'est le cas, ce paramètre doit être activé.

D'autres imprimantes ajustent automatiquement la position de la tête d'impression de telle sorte que la buse active soit déplacée à la position indiquée dans le code g. Cela signifie que si le code g commande à l'imprimante de se déplacer en position [50,50], l'extrudeuse actuellement active se déplacera dans cette position. La tête d'impression elle-même se déplacerait un peu sur le côté pour y positionner l'extrudeuse active. Si votre imprimante se comporte de cette manière, ce paramètre doit être désactivé.

*Comme il s'agit d'un réglage de machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
