Lorsqu'elle est activée, cette fonction permet à Cura d'envoyer une commande à l'imprimante pour l'amorçage, juste avant que l'extrudeuse ne soit utilisée pour la première fois. L'imprimante s'amorce en créant une petite goutte de matériau sur la plaque de montage.

L'amorçage a pour but de faire en sorte que le matériau s'écoule correctement. Si la goutte d'amorçage n'est pas activée, l'imprimante amorcera plutôt pendant la jupe ou le bord. C'est le principal cas d'utilisation de la jupe en premier lieu, mais pour un bord, cela réduira légèrement la force d'adhérence du bord.

L'effet de ce réglage sur le g-code est que Cura placera la commande M280 à un certain endroit. **Cela ne fonctionne actuellement que sur les imprimantes Ultimaker depuis l'Ultimaker 3** car elles sont les seules à mettre en œuvre la commande M280. Pour les autres imprimantes, le paramètre ne sera pas visible.
