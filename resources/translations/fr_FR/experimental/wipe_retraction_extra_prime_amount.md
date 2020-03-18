Degré supplémentaire de rétraction d'essuyage primaire
===

Si [rétraction pendant la procédure d'essuyage](./wipe_retraction_enable.md), le matériau ne sera pas rétracté après la fin de la procédure d'essuyage. Dans ce cas, vous pouvez souhaiter que le matériau soit poussé un peu plus loin que la [distance de rétraction](./wipe_retraction_amount.md) initiale pour compenser la perte de matériau malgré la rétraction. Cette distance peut être configurée séparément du [montant normal de la rétraction](../travel/retraction_extra_prime_amount.md).

La procédure d'essuyage fait que la buse va jusqu'au côté de l'imprimante, se déplace d'avant en arrière, puis se déplace jusqu'à l'arrière. Il s'agit essentiellement d'un déplacement très long. Comme ce déplacement est plus long que les déplacements moyens tout au long de l'impression, il est possible que davantage de matière ait été perdue à cause du suintement. Pour compenser cela, il se peut que vous deviez amorcer davantage après la procédure d'essuyage qu'après les déplacements normaux.

Si trop de matériau supplémentaire est amorcé, il y aura une surextrusion. Celle-ci se manifeste par une tache à l'endroit où la buse atterrit après la procédure d'essuyage.
