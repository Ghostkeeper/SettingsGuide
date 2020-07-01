Inclure les températures du matériau
====
Ce paramètre indique au générateur de code s'il doit ou non écrire les commandes de température d'impression pour le début de l'impression avant le code g de démarrage. Il est automatiquement défini lors du démarrage d'une impression.

Pour la plupart des opérations effectuées pendant le [G-code de démarrage](machine_start_gcode.md), il est utile que la buse d'impression soit à la bonne température pour l'impression. Pour faciliter la tâche des concepteurs de définitions d'imprimantes, Cura chauffe automatiquement la buse avant que le [G-code de démarrage](machine_start_gcode.md) ne soit exécuté. Toutefois, si le G-code de départ contient une référence à un réglage de la température, celle-ci ne sera plus chauffée automatiquement.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages. Le modifier n'a pas non plus d'effet puisqu'il sera modifié automatiquement par Cura.*
