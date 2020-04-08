Attendre le chauffage de la buse
====
La couche initiale peut avoir une [Température d’impression couche initiale](../material/material_print_temperature_layer_0.md) différente de la [Température d’impression par défaut](../material/material_print_temperature.md). Si ce paramètre est activé, l'imprimante attendra que cette température soit atteinte avant de poursuivre l'impression.

Elle attendra que la température soit réchauffée ou refroidie à la température appropriée. Bien que l'étiquette de ce paramètre indique qu'elle attendra d'être chauffée, elle se refroidira tout aussi bien. La buse n'attendra pas d'autres changements de température, comme la [Température d'impression initiale](../material/material_initial_print_temperature.md), la [Température d'impression finale](../material/material_final_print_temperature.md) ou la [Température de veille](../material/material_standby_temperature.md). Si l'impression se fait en mode d'impression [Un à la fois](../blackmagic/print_sequence.md), la buse attendra également que la température de la couche initiale soit atteinte lorsqu'elle devra revenir à la première couche pour les objets suivants.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
