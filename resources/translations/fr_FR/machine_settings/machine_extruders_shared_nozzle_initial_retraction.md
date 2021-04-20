Retrait initial de la buse partagée
====
Si les extrudeuses d'une imprimante [partagent une buse](machine_extruders_share_nozzle.md), Cura ne suppose pas que toutes les extrudeuses commencent avec le filament à l'extrémité de la buse. Ce paramètre indique à quelle distance de la buse le filament commence. Le filament peut commencer à une distance différente de la [Distance de rétraction du commutateur de buse](../dual/switch_extruder_retraction_amount.md) parce que le filament peut être stocké plus loin pendant que l'imprimante était inactive que lorsque l'extrudeuse est en attente pendant l'impression.

![Distance du filament inactif avant l'impression](../../../articles/images/machine_extruders_shared_nozzle_initial_retraction.svg)

Cura l'utilisera pour s'assurer que le filament est à l'extrémité de la buse avant de lancer sa procédure d'amorçage pour le premier changement d'extrudeur.
