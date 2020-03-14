Ce réglage ajuste le débit pour la paroi extérieure uniquement. Le débit de la paroi extérieure peut être réglé séparément du débit des parois intérieures.

Le réglage du débit de la paroi extérieure est une méthode d'arrêt de l'espace pour résoudre les problèmes de débit d'extrusion ou de précision dimensionnelle. Le même effet peut également être obtenu en ajustant les paramètres [Outer Wall Line Width](../resolution/wall_line_width_0.md) et [Outer Wall Inset](../shell/wall_0_inset.md), mais ce paramètre pourrait être une façon plus intuitive de procéder au réglage initial.

S'il y a un problème de vitesse d'extrusion uniquement au niveau de la paroi extérieure, il est préférable d'examiner les paramètres [vitesses d'impression](../speed/speed_wall_0.md) et [température d'impression](material_print_temperature.md). Peut-être que le matériau ne reçoit pas assez d'impulsion de la buse et qu'une plus grande vitesse d'impression pourrait aider. Peut-être que les lignes sont trop fines pour être extrudées correctement. Peut-être que le matériau est trop froid ou trop chaud.

S'il y a un problème de précision dimensionnelle, il est préférable d'examiner les [largeurs de ligne](../resolution/wall_line_width_0.md), [expansion horizontale](../shell/xy_offset.md) et l'[ordre d'impression](../shell/outer_inset_first.md).
