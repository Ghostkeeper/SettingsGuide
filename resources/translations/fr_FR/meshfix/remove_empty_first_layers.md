Lorsque cette option est activée, les couches vides sur la face inférieure de l'impression seront supprimées. L'ensemble de l'impression se déplacera vers le bas jusqu'à ce qu'elle repose sur la plaque de construction. Au lieu d'avoir des couches vides qui font échouer l'impression, l'impression sera légèrement plus basse.

Si la préférence de Cura pour "Déposer automatiquement les modèles sur la plaque de montage" est activée, ce paramètre n'aura probablement que très peu d'effet. Il peut néanmoins avoir un effet. Lorsque vous déposez automatiquement des modèles sur la plaque de montage, les modèles sont exactement alignés avec la plaque de montage. Cependant, si la ou les premières couches ne contiennent que des éléments trop petits pour être imprimés (peut-être parce que le fond n'est pas entièrement lisse), la première couche peut être encore vide dans l'impression finale. Ce réglage permet d'éviter cela en déplaçant les autres couches d'une couche vers le bas.

Après avoir déplacé l'impression vers le bas, les paramètres qui s'appliquent à la première couche sont toujours appliqués. Ainsi, même si la première couche originale est supprimée, la [Température d'impression de la couche initiale](../material/material_print_temperature_layer_0.md) et les paramètres similaires sont toujours appliqués à la nouvelle première couche.

Normalement, ce paramètre devrait toujours être activé pour éviter que les impressions ne tombent en panne parce que le fond n'est pas entièrement lisse ou parce qu'elles sont mal alignées sur la plaque de montage. Toutefois, vous pouvez choisir de désactiver ce paramètre si vous effectuez un travail d'impression en plusieurs étapes qui doit commencer en plein vol.

Si [support est activé](../support/support_enable.md), ce support s'étendra jusqu'à la plaque de montage, de sorte que les premières couches ne seront plus vides. Aucune couche ne sera enlevée et l'impression ne se déplacera pas vers le bas.

Si le paramètre [Tolérance de découpage](../experimental/slicing_tolerance.md) est réglé sur "Exclusif", la première couche sera toujours vide. Si ce paramètre n'est pas activé, la première couche sera en fait vide et votre impression échouera très probablement.


