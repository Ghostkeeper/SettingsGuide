Taille maximale des petits trous
===

Les petits détails de l'empreinte sont souvent très critiques sur le plan dimensionnel. Ce réglage fait que les petits trous dans l'impression sont imprimés plus lentement afin d'obtenir une plus grande précision.

Si un trou circulaire a un diamètre inférieur à la valeur de ce paramètre, la vitesse à laquelle le périmètre de ce trou est imprimé sera multipliée par un facteur de la [Vitesse de petite structure](./small_feature_speed_factor.md) (réduit, normalement). Pour les trous qui ne sont pas circulaires, ils seront imprimés à une vitesse différente si la circonférence est inférieure à un cercle ayant le diamètre spécifié ici. Voir aussi [Longueur max de petite structure](./small_feature_max_length.md); c'est le réglage qui sera effectivement utilisé pour le découpage.

Un cas d'utilisation courant de cette fonction est l'impression de trous de vis à des dimensions très précises. Lors de l'impression de petits trous, le cordon a tendance à être tiré avec la buse dans le coin. Si le coin est très pointu, comme c'est le cas pour les petits trous, cela a pour effet de rendre le trou plus petit. Lorsque l'impression est plus lente, cette traction est réduite parce que le matériau a plus de temps pour s'installer et parce que la traction mécanique est simplement plus faible.

En augmentant ce réglage, on obtient davantage de contours marqués comme "petits éléments". Une plus grande partie des trous de l'impression sera imprimée plus lentement. Ces trous seront donc imprimés avec plus de précision, mais le temps d'impression sera plus long.
