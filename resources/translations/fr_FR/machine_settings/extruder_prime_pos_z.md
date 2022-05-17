Extrudeuse Position d'amorçage Z
====
Si la fonction [Activer la goutte de préparation](../platform_adhesion/prime_blob_enable.md) est activée, ce paramètre indique la coordonnée Z à laquelle le mouvement de génération de la première goutte commence. Cura se déplacera vers cette position avant que la goutte de départ ne soit extrudée.

Contrairement aux coordonnées X et Y, il s'agit d'un réglage machine. Cela est dû au fait que l'acte d'amorçage est supposé avoir une coordonnée Z fixe. Pour créer une goutte d'amorçage, la buse devra se déplacer vers le plateau d'impression et peut-être se déplacer un peu de haut en bas. Les paramètres [X](../platform_adhesion/extruder_prime_pos_x.md) et [Y](../platform_adhesion/extruder_prime_pos_y.md) peuvent être choisis avec des réglages normaux pour déplacer la position de la goutte d'amorçage dans le cas où l'espace sur le plateau d'impression est limité, mais pas la coordonnée Z.

La seule chose que cela change est la coordonnée Z à laquelle Cura commandera à la buse de se déplacer avant que la commande de la goutte de départ ne soit exécutée.

*Comme il s'agit d'un réglage de machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
