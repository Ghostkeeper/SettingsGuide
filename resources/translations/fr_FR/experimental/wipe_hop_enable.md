Décalage en Z d'essuyage lors d’une rétraction
====
Avec ce réglage, la procédure d'effacement se fera pendant que Z saute. Il peut être configuré séparément du [Décalage en Z lors d’une rétraction](../travel/retraction_hop_enabled.md) ordinaire.

La procédure d'effacement contient deux déplacements très longs qui vont jusqu'au côté du volume de construction. Pendant ces déplacements, la tête d'impression peut prendre de la vitesse car elle a beaucoup de temps pour accélérer. À grande vitesse, il y a un risque accru que la tête d'impression renverse accidentellement des parties déjà imprimées. C'est pourquoi vous pouvez activer les sauts en Z même si vous ne le feriez pas pour le processus d'impression ordinaire.

Dans cette procédure, le saut Z est exécuté indépendamment du fait que [les sauts Z ne sont effectués que sur des parties précédemment imprimées](../travel/retraction_hop_only_when_collides.md) ou qu'il y ait des parties imprimées entre les deux.
