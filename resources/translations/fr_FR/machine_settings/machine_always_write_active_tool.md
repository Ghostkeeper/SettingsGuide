Toujours écrire Outil actif
====
Ce paramètre indique comment certaines commandes G-Code avec un paramètre d'outil sont interprétées par l'imprimante. Certaines commandes G-Code peuvent inclure un paramètre pour indiquer à quelle extrudeuse il s'applique. Certains microprogrammes interprètent ce paramètre comme une commande permettant de passer à cet outil et d'exécuter ensuite le G-Code, tandis que d'autres interprètent ce paramètre comme une commande permettant d'appliquer le G-Code à une extrudeuse différente de celle qui est actuellement active.

Les seules commandes auxquelles cela s'applique et qui sont pertinentes pour l'impression 3D sont les commandes de chauffage de la buse, "M104" et "M109". Prenons l'exemple suivant d'une commande de chauffage, exécutée pendant que la première extrudeuse (`T0`) est en cours d'impression :

`M104 S210 T1`

Il y a deux interprétations possibles de ce commandement :
* Tout en continuant à imprimer sur la première extrudeuse, commencez à chauffer la deuxième extrudeuse à 210°C. C'est l'interprétation retenue par Marlin, Reprap, Sailfish et leurs progiciels dérivés.
* Commencez par passer sur la deuxième extrudeuse, puis chauffez la deuxième extrudeuse à 210°C. C'est l'interprétation de Smoothieware et de ses microprogrammes dérivés.

En raison de la stratégie de régulation de la température de Cura, il n'est jamais nécessaire d'exécuter la deuxième interprétation. Si l'imprimante interprète la commande g-code de la seconde manière, Cura écrira le g-code suivant à la place :

`M104 S210 T1`

`T0`

Elle sait essentiellement que l'imprimante passera à la deuxième extrudeuse en raison de cette commande, et qu'elle doit donc repasser à la première extrudeuse pour continuer à y imprimer.
