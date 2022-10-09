Débit Couche initiale Paroi extérieure
====
Le débit de la couche initiale peut être modifié avec la fonction [Débit de la couche initiale](material_flow_layer_0.md) mais ce paramètre permet de contrôler les détails les plus fins de la couche initiale en ne modifiant que le débit de la paroi extérieure de la première couche.

Certaines parties de la couche initiale sont plus susceptibles de se détacher du plateau d'impression que d'autres. Les premières lignes de l'impression sont les plus dangereuses. Ce paramètre vous permet de modifier la paroi extérieure pour qu'elle ait un débit plus élevé afin de mieux la fixer au plateau d'impression. C'est utile lorsque l'impression n'a pas de bord, car la paroi extérieure est alors imprimée comme une seule ligne lâche sur le plateau d'impression avec relativement peu de surface à laquelle adhérer.

En ne modifiant que le débit de la paroi extérieure, les problèmes liés à un débit élevé tels que la [Surextrusion](../troubleshooting/overextrusion.md) peuvent être évités.