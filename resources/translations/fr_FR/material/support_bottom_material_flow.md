Débit du bas de support
===

Ce réglage permet d'ajuster le débit pour le plancher de support uniquement. Le débit du plancher porteur peut être réglé séparément du débit du reste du support.

Le réglage du débit pendant le plancher de support est une méthode d'arrêt de l'espace pour régler les problèmes de taux d'extrusion ou d'adhérence entre le modèle et le support. Le même effet peut être obtenu en ajustant la [largeur de ligne](../resolution/support_bottom_line_width.md) ou [espacement des lignes](../support/support_bottom_line_distance.md) du plancher de support, mais l'ajustement du débit peut être plus intuitif.

En cas de problème de vitesse d'extrusion, il est préférable d'examiner les [vitesses d'impression](../speed/speed_support_bottom.md), [température](material_print_temperature.md) et [largeur de ligne](../resolution/support_bottom_line_width.md). Il y a peut-être une trop grande différence entre le débit du plancher de support et les autres structures de la couche. Peut-être que la largeur de la ligne est trop fine pour être extrudée correctement. Si l'interface est imprimée avec un [matériau différent](../support/support_interface_extruder_nr.md), un problème courant est que le matériau avec lequel l'interface est imprimée n'a pas assez de temps pour commencer à couler correctement. Ce problème peut être résolu en utilisant une [tour principale](../dual/prime_tower_enable.md) ou en augmentant la [surface du plancher de support](../support/support_bottom_offset.md).

Si le support colle trop bien au modèle, le réglage de la [largeur de ligne](../resolution/support_bottom_line_width.md) sera généralement plus efficace car il permet également de rapprocher les lignes pour obtenir la même densité de remplissage du support.
