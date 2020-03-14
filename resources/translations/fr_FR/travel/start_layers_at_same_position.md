À l'origine, ce paramètre faisait que l'imprimante commençait chaque couche avec l'objet le plus proche de la position spécifiée dans les paramètres [X début couche](./layer_start_x.md) et [Y début couche](./layer_start_y.md), au lieu de l'objet qui avait été imprimé en dernier dans la couche précédente.

**Le paramètre était caché dans Cura 2.4 et n'a jamais été supprimé correctement, c'est pourquoi ce paramètre existe toujours dans cette liste. Cependant, il n'a aucun effet sur l'impression.**

Le comportement alternatif n'était plus possible après l'implémentation du découpage en plusieurs fils, donc le paramètre a été caché.

L'impression de chaque couche dans le même ordre évite d'empiler deux couches l'une sur l'autre immédiatement après l'autre, s'il y a plusieurs parties à imprimer. Cela permet à la couche précédente de refroidir plus longtemps pendant que la buse est occupée à imprimer les autres parties. Cela améliore le porte-à-faux et réduit le banderolage et l'affaissement. D'autre part, cela permet à l'imprimante de se déplacer un peu plus, ce qui augmente légèrement le temps d'impression.
