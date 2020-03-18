Montant de l'amorce supplémentaire lors d'un changement de buse
===

Ce paramètre vous permet de configurer l'imprimante pour purger un peu de matière supplémentaire à chaque fois que l'on change d'extrudeuse. Il est destiné à rétablir la pression sur la buse après qu'elle ait suinté pendant que d'autres extrudeuses impriment ou lors d'un changement d'extrudeuse.

Pendant que d'autres extrudeuses sont en train d'imprimer, cette extrudeuse aura été en attente. Mais pendant ce temps, elle va suinter de la matière. Cette perte de matière peut être compensée en faisant passer de la matière supplémentaire. La pression est alors rétablie dans la chambre de la buse. La matière qui a suinté reste cependant sur l'embout de la buse, de sorte qu'à moins d'utiliser une [tour d'amorçage](prime_tower_enable.md) ou une [protection contre le suintement](ooze_shield_enabled.md), elle se retrouvera sur le côté de votre empreinte. 

**Ce paramètre est configurable par extrudeuse. La quantité de matière configurée est purgée au *début* du plan de cette extrudeuse, avant d'imprimer avec la matière.**
