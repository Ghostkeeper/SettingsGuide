Débit du fond de la Couche initiale
====
L'écoulement de la couche initiale peut être modifié avec le paramètre [Débit de la couche initiale](material_flow_layer_0.md), mais ce paramètre permet de contrôler les détails les plus fins de la couche initiale en modifiant uniquement l'écoulement de la peau de la première couche.

Certaines parties de la couche initiale sont plus susceptibles de se détacher de la plaque de construction que d'autres. Les premières lignes de l'impression sont les plus risquées. En utilisant ce paramètre, vous pouvez réduire le débit de la peau pour éviter d'obtenir une surextrusion à cet endroit, tout en gardant le débit des parois de l'impression plus élevé.

Si le débit de la couche initiale est trop élevé, la peau peut onduler, ce qui donne un effet laid sur le bas de l'impression et peut entraîner l'arrachement de l'impression du plateau d'impression. Ce n'est pas un problème aussi important pour les murs. Il est conseillé de garder ce débit plus bas que le débit des [parois extérieures](wall_0_material_flow_layer_0.md) et des [parois intérieures](wall_x_material_flow_layer_0.md).