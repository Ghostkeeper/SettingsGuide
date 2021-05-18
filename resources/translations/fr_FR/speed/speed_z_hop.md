Vitesse du décalage en Z
====
Ce paramètre configure la vitesse de déplacement à laquelle les mouvements verticaux sont effectués dans un Z Hop. Les mouvements horizontaux d'un Z Hop ne sont pas affectés, puisqu'ils sont configurés par la [Vitesse de déplacement](speed_travel.md).

![Le mouvement vertical est effectué à la vitesse du Z Hop](../images/speed_z_hop_fr.svg)

<!--if cura_version >= 4.2-->La vitesse du décalage en Z est également utilisée comme vitesse de déplacement entre les couches. En pratique, cette vitesse importe très peu puisque le mouvement d'une seule épaisseur de couche est si court qu'il est presque toujours limité par l'accélération, et non par la vitesse de déplacement maximale.<!--endif-->

Pour la plupart des imprimantes, l'axe Z est construit pour être robuste mais lent. L'augmentation de la vitesse du décalage en Z permet de tester les limites du mouvement de l'axe Z, ce qui peut faire sauter certains pas au moteur de l'axe Z. Par conséquent, la buse pourrait se retrouver à une hauteur différente après le décalage en Z. Réduire cette vitesse réduit les risques que cela se produise.

D'autre part, une vitesse de décalage en Z plus élevée fera que la buse s'éloignera plus rapidement de la surface imprimée. Cela peut réduire la taille des marques.

En raison des faibles taux d'accélération sur l'axe Z, il est rare que la vitesse de décalage en Z souhaitée soit atteinte, à moins que la hauteur du décalage en Z soit très élevée ou la vitesse très faible.
