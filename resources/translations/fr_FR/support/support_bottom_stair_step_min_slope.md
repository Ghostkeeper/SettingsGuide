Marche de l'escalier de soutien Angle de pente minimum
====
Avec ce réglage, vous pouvez désactiver le fait de marcher sur le bas du support, jusqu'à ce que la pente du modèle ait un certain angle.

![Marche d'escalier désactivée jusqu'à ce que la pente soit de 10°](../../../articles/images/support_bottom_stair_step_min_slope_10.png)
![Marche d'escalier désactivée jusqu'à ce que la pente soit de 30°](../../../articles/images/support_bottom_stair_step_min_slope_30.png)

En cas de faible pente, les marches de l'escalier du bas peuvent être très larges. Elles ne peuvent jamais être plus larges que ce que la [largeur maximale] (support_bottom_stair_step_width.md) indique, mais comme cette distance est maintenue de tous les côtés, les marches peuvent devenir si larges qu'il y a une distance importante que le support devra franchir. Si le support repose dans un petit creux, il peut même faire sauter tout le bas de l'escalier, ce qui fait que le support entier ne repose que sur les coins des marches.

Dans ce cas, vous pouvez limiter les marches de l'escalier aux seules pentes les plus raides. Ce réglage détermine ce qui constitue une pente "raide" à cet égard.

Augmenter ce paramètre empêchera Cura de générer les marches d'escalier sur des surfaces peu profondes. Cela rendra le support plus solide, mais plus difficile à enlever. Votre support laissera plus de cicatrices sur la surface. En le réduisant, le support sera plus facile à enlever et laissera une plus belle surface où le support reposait, mais dans certains cas, le support peut devoir parcourir de longues distances ou même sembler complètement suspendu en l'air.

Pour obtenir une belle surface, il est préférable de laisser ce réglage à un angle bas conservateur, de 5° ou 10° environ. Si le support repose sur une surface peu profonde mais pas complètement plane, inspectez la vue de la couche et augmentez l'angle si vous trouvez que le support semble très précaire.
