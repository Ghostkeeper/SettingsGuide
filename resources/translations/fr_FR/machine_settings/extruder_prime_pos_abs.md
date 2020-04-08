La position d'amorçage absolue de l'extrudeuse
====
Si l'option [Activer la goutte de préparation](../platform_adhesion/prime_blob_enable.md) est utilisée, la position de cette procédure d'amorçage peut être ajustée avec une position [X](../platform_adhesion/extruder_prime_pos_x.md) et [Y](../platform_adhesion/extruder_prime_pos_y.md). Ce paramètre détermine s'il s'agit de la position sur le plateau d'impression ou d'une position relative à la position actuelle de l'imprimante.

Si ce paramètre est activé, les coordonnées X et Y se rapportent à une certaine position fixe sur le plateau d'impression. L'extrudeuse se déplacera toujours à cet endroit afin de créer une goutte de plastique d'amorçage.

Si ce paramètre est désactivé, les coordonnées X et Y sont relatives à la position que la buse occupe lors du premier passage à cette extrudeuse. Pour la première extrudeuse, il s'agit de la coordonnée [0,0]. Pour les autres extrudeuses, il s'agit de leur position de départ telle que définie dans le fichier de définition de l'extrudeuse. Cette position de départ peut également être relative.

Il est fortement conseillé d'utiliser une position première absolue. Une position initiale absolue est garantie sans collision avec d'autres parties de l'impression, puisque vous ne pouvez pas placer d'objets à cet endroit sur la plaque de montage. Une position première relative peut se trouver n'importe où sur la plaque de montage et, par conséquent, vous pourriez vous retrouver avec une couche d'apprêt quelque part au-dessus de votre première couche. L'utilisation d'une position première relative pourrait permettre de gagner du temps de déplacement, mais cela ne vaut vraiment pas la peine de courir ce risque.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
