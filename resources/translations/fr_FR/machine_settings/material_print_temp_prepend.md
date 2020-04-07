Inclure la température de la plaque de construction
====
Ce paramètre indique au back-end de découpe s'il doit ou non écrire les commandes de température de la plaque de montage pour le début de l'impression avant le code g de démarrage. Il est automatiquement défini lors du démarrage d'une tranche.

Pour la plupart des opérations effectuées pendant le [G-code de démarrage](machine_start_gcode.md), il est utile que la plaque de montage soit à la bonne température pour l'impression. Pour faciliter la tâche des concepteurs de définitions d'imprimantes, Cura chauffe automatiquement la plaque de montage avant que le [G-code de démarrage](machine_start_gcode.md) ne soit exécuté. Toutefois, si le code g de départ contient une référence à un réglage de la température de la plaque de montage, celle-ci ne sera plus chauffée automatiquement.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages. Le modifier n'a pas non plus d'effet puisqu'il sera modifié automatiquement par Cura.*
