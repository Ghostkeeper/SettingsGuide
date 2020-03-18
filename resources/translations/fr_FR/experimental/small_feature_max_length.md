Longueur max de petite structure
====
Les petits détails de l'empreinte sont souvent très critiques sur le plan dimensionnel. Ce réglage fait que les petits trous dans l'impression sont imprimés plus lentement afin d'obtenir une plus grande précision.

Si un trou a une circonférence inférieure à celle indiquée par ce paramètre, la vitesse à laquelle le périmètre de ce trou est imprimé sera multipliée par un facteur de [Vitesse de petite structure](small_feature_speed_factor.md) (réduit, normalement). Ce paramètre est une façon différente d'aborder le paramètre [Taille maximale des petits trous](small_hole_max_size.md), qui est plus générique que pour les trous circulaires.

Un cas d'utilisation courant de cette fonction est l'impression de trous de vis à des dimensions très précises. Lors de l'impression de petits trous, la bille a tendance à être tirée avec la buse dans le coin. Si le coin est très pointu, comme c'est le cas pour les petits trous, cela a pour effet de rendre le trou plus petit. Lorsque l'impression est plus lente, cette traction est réduite parce que le matériau a plus de temps pour s'installer et parce que la traction mécanique est simplement plus faible.

En augmentant ce réglage, on obtient davantage de contours marqués comme "petits éléments". Une plus grande partie des trous de l'impression sera imprimée plus lentement. Ces trous seront donc imprimés avec plus de précision, mais le temps d'impression sera plus long.
