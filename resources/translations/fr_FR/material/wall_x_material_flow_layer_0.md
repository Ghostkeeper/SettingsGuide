Débit Couche initiale Paroi intérieure 
====
L'écoulement de la couche initiale peut être modifié avec le paramètre [Débit de la couche initiale](material_flow_layer_0.md), mais ce paramètre permet de contrôler les détails les plus fins de la couche initiale en modifiant uniquement l'écoulement des parois internes de la première couche.

Certaines parties de la couche initiale sont plus susceptibles de se détacher du plateau d'impression que d'autres. Les premières lignes de l'impression sont les plus dangereuses. Ce paramètre vous permet de modifier les parois intérieures pour qu'elles aient un débit plus élevé afin de mieux les fixer au plateau d'impression. Ceci est particulièrement utile lorsque vous imprimez les parois intérieures avant la paroi extérieure, car la première paroi intérieure est alors imprimée en une seule ligne lâche avant de s'attacher à la paroi extérieure et au bord.

En ne modifiant que le débit de la paroi interne, les problèmes liés à un débit élevé tels que le [Pied d'éléphant](../troubleshooting/elephants_foot.md) peut être évitée.