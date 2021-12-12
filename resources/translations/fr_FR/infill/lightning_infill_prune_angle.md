Angle d'élagage du remplissage Eclair
====
Le motif de remplissage Eclair produit une structure arborescente à l'intérieur de l'impression, très réduite au départ, mais se ramifie pour atteindre toutes les parties du haut de l'impression qui doivent être soutenues de l'intérieur. Ce paramètre indique dans quelle mesure les branches de l'arbre peuvent etre créées avec une certaine dépouille.

![A 40°, le remplissage Eclair est assez stable.](../../../articles/images/lightning_infill_prune_angle_40.png)
![A 70°, les branches débordent assez fortement.](../../../articles/images/lightning_infill_prune_angle_70.png)

En augmentant l'angle de ramification, le remplissage pourra commencer plus petit en bas tout en atteignant la totalité de la surface supérieure. Dans de nombreux cas, il n'est même plus nécessaire de commencer par le bas, il suffit de s'accrocher aux côtés. Les principaux effets de l'augmentation de cet angle sont les suivants :

* Réduction du temps d'impression et de l'utilisation des matériaux.
* Des murs plus lisses, parce qu'il n'y aura pas autant de remplissage touchant les murs de l'intérieur.
* Résistance légèrement réduite.
* Plus de risques de défaillance de l'impression. Si le surplomb est trop important, il y aura un surplomb significatif à l'extrémité de chaque ligne, qui s'affaissera et pourrait se détacher.

En pratique, l'angle de ramification peut être plus élevé que les angles de surplomb normaux ou que les autres [angles de saillie du remplissage Eclair](lightning_infill_overhang_angle.md). Comme les lignes sont bien soutenues sur la couche inférieure, avoir un peu plus de dépouille n'est pas vraiment un problème.
