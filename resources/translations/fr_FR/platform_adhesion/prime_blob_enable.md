Activer la goutte de préparation
====
Lorsqu'elle est activée, cette fonction permet à Cura d'envoyer une commande à l'imprimante pour l'amorçage, juste avant que l'extrudeuse ne soit utilisée pour la première fois. L'imprimante s'amorce en créant une petite goutte de matériau sur le plateau d'impression.

L'amorçage a pour but de faire en sorte que le matériau s'écoule correctement. Si la goutte d'amorçage n'est pas activée, l'imprimante amorcera plutôt à la création de la jupe ou de la bordure. C'est d'ailleurs la principale raison d'utilisation de la jupe, mais pour une bordure, cela réduira légèrement sa force d'adhérence.

L'effet de ce réglage sur le G-Code est que Cura placera la commande M280 à un certain endroit. **Cela ne fonctionne actuellement que sur les imprimantes Ultimaker depuis l'Ultimaker 3** car elles sont les seules à mettre en œuvre la commande M280. Pour les autres imprimantes, le paramètre ne sera pas visible.
