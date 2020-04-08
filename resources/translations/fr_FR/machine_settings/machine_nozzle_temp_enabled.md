Activer le contrôle de la température de la buse
====
Si ce paramètre est désactivé, Cura n'enverra aucune commande de température au g-code. Au lieu de cela, Cura laissera au microprogramme de l'imprimante le soin de chauffer les buses avant l'impression.

Ce fonctionnement est similaire à celui de [A un plateau chauffant](machine_heated_bed.md). Si ce paramètre est désactivé, les paramètres de contrôle de la température tels que [Température d'impression](../material/material_print_temperature.md) ne seront pas affichés à l'utilisateur.

La désactivation temporaire de ce paramètre peut être utilisée pour effectuer un essai d'impression à vide. Pour cela, vous devez également [désactiver le chauffage du plateau d'impression](machine_heated_bed.md), le [chauffage du volume de montage](machine_heated_build_volume.md) et régler le [débit](../material/material_flow.md) sur 0%.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
