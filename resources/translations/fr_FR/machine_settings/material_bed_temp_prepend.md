Inclure la température du plateau
====
Ce paramètre indique au générateur de code si il doit ou non écrire les commandes de température de la buse pour le début de l'impression avant le G-Code de début. Il est automatiquement défini au démarrage d'un fichier.

Pour la plupart des opérations effectuées pendant le [G-Code de démarrage](machine_start_gcode.md), il est judicieux que la buse soit à la bonne température pour l'impression. Pour faciliter la conception des définitions d'imprimante, Cura chauffe automatiquement la buse avant que le [G-Code de démarrage](machine_start_gcode.md) ne soit exécuté. Toutefois, si le code g de démarrage contient une référence à un réglage de la température de la buse, celle-ci ne sera plus chauffée automatiquement.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages. Le modifier n'a pas non plus d'effet puisqu'il sera modifié automatiquement par Cura.*
