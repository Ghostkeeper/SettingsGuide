Ce paramètre configure la vitesse de déplacement à laquelle les mouvements verticaux sont effectués dans un Z Hop. Les mouvements horizontaux d'un Z Hop ne sont pas affectés, puisqu'ils sont configurés par la [Vitesse de déplacement](speed_travel.md).

![Le mouvement vertical est effectué à la vitesse du Z Hop](../../../articles/images/speed_z_hop.svg)

Pour la plupart des imprimantes, l'axe Z est construit pour être robuste mais lent. L'augmentation de la vitesse de saut de l'axe Z permet de tester les limites du mouvement de l'axe Z, ce qui peut faire sauter certaines étapes au moteur de l'axe Z. Par conséquent, la buse pourrait se retrouver à une hauteur différente après le saut en Z. Réduire cette vitesse réduit les chances que cela se produise.

D'autre part, une vitesse de saut Z plus élevée fera que la buse s'éloignera plus rapidement de la surface imprimée. Cela peut réduire la taille des taches.

En raison des faibles taux d'accélération sur l'axe Z, il est rare que la vitesse de saut en Z souhaitée soit atteinte, à moins que la hauteur du saut en Z soit très élevée ou la vitesse très faible.
