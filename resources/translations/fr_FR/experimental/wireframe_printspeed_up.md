Vitesse d’impression filaire ascendante
===

Ce réglage précise la vitesse à laquelle la buse se déplacera vers le haut tout en effectuant un mouvement vertical dans la configuration en dents de scie. La vitesse de déplacement vers le haut peut être configurée séparément du reste de la vitesse d'impression du fil.

![Où les différentes vitesses d'impression à fil s'appliquent](../images/wireframe_printspeed_fr.svg)

Le mouvement ascendant n'aura pas la vitesse spécifiée pour l'ensemble du mouvement. Pour le bit le plus bas du mouvement ascendant, tel que défini par le paramètre [Écart ascendant de l'impression filaire](wireframe_up_half_speed.md), la tête d'impression se déplacera à la moitié de cette vitesse.

Un mouvement vers le haut plus lent prendra plus de temps mais donnera plus de temps au matériau pour se solidifier. De cette façon, il ne sera pas traîné autant dans la direction de la diagonale. Cependant, un déplacement trop lent poussera également la ligne vers le bas en raison de l'inertie du filament avec la pression dans la chambre de la buse. Le filament a alors tendance à osciller, ce qui rend moins probable que la prochaine ligne horizontale puisse établir une connexion correcte.
