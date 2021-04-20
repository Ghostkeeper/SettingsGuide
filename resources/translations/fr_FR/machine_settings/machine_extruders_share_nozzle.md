Les extrudeuses partagent une buse
====
Avec ce paramètre, vous pouvez indiquer que votre imprimante ne possède qu'une seule buse, et que tout le filament est poussé par cette même buse. Cura modifiera alors sa stratégie d'amorçage.

Normalement, Cura suppose qu'après l'exécution du [G-Code de démarrage](machine_start_gcode.md), tous les extrudeurs ont leur filament à l'extrémité de la buse, prêt à être imprimé. Lorsque les extrudeurs partagent une buse, cela n'est pas possible car un seul filament peut se trouver dans la buse à la fois. Au lieu de la procédure d'amorçage normale avec l'[activation de la goutte de préparation](../platform_adhesion/prime_blob_enable.md) ou des lignes de jupe supplémentaires, la buse doit s'amorcer comme pour un changement d'extrudeur complet. Cela implique l'impression dans la [tour d'amorçage](../dual/prime_tower_enable.md), si elle est activée.

Si toutes les extrudeuses partagent une seule buse, il est logique qu'elles [partagent le chauffage](machine_extruders_share_heater.md). Cependant, Cura ne fait aucun lien entre les deux de lui-même, donc assurez-vous d'activer les deux si votre imprimante a une seule buse et un seul élément chauffant pour toutes les extrudeuses.

**Comme il s'agit d'un paramètre machine, il ne sera pas normalement listé dans la liste normale des paramètres. Il existe cependant une case à cocher pour ce paramètre dans la boîte de dialogue des paramètres de l'imprimante, qui se trouve dans la liste des imprimantes ajoutées dans la boîte de dialogue des préférences**.
