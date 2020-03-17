Débit de remplissage
===

Ce réglage ajuste le débit pour le remplissage uniquement. Le débit de la recharge peut être réglé séparément du débit du reste de l'impression.

L'ajustement du débit pendant le remplissage est une méthode d'arrêt de l'espace pour régler les problèmes de vitesse d'extrusion ou de résistance. Le même effet peut être obtenu en ajustant la [distance entre les lignes](../infill/infill_line_distance.md) et la [largeur de ligne](../resolution/infill_line_width.md) du remplissage, mais ce réglage peut être plus intuitif.

Les problèmes de vitesse d'extrusion ou de résistance du remplissage sont généralement dus à l'une des deux causes suivantes Des croisements dans le modèle de remplissage, ou un trop grand changement de débit entre le remplissage et d'autres structures. Plutôt que d'ajuster ce débit, il peut être plus efficace d'ajuster le [schéma de remplissage](../infill/infill_pattern.md) ou la [largeur_ligne](../resolution/infill_line_width.md). Choisissez un motif de remplissage qui ne se croise pas, comme le zigzag, et choisissez une largeur de ligne plus proche du taux d'extrusion des parois et de la peau. Si la largeur de la ligne doit être augmentée pour des raisons de résistance mais que le débit est limité, il est conseillé d'utiliser le [multiplicateur de remplissage](../infill/infill_multiplier.md) plutôt que d'augmenter le débit.
