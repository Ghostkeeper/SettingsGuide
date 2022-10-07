Largeur de ligne de couche extérieure de la surface supérieure
====
Avec le paramètre [couches extérieures de la surface supérieure](../top_bottom/roofing_layer_count.md), un certain nombre de couches situées tout en haut peuvent se voir attribuer une largeur de ligne différente de celle des couches supérieures plus profondes.

La peau sur la face supérieure de l'impression remplit plusieurs fonctions. Elle doit notamment fermer les trous laissés par le remplissage sur la face supérieure et elle confère une grande solidité à la pièce. En dehors de cela, l'idéal serait qu'elle soit encore belle et lisse. La réduction de la [largeur de la ligne du dessus/dessous](../resolution/skin_line_width.md) peut servir à créer une surface plus lisse, mais fera prendre beaucoup plus de temps à l'impression. Ce paramètre permet de créer une surface supérieure lisse avec des lignes très fines sans avoir besoin d'imprimer le reste du haut et du bas avec la même largeur de ligne. Le temps d'impression est ainsi moins pénalisé.

Réduisez la largeur du trait de la surface supérieure pour obtenir une surface plus lisse sur la face supérieure de votre impression. L'impression sera cependant un peu plus longue.

Une réduction excessive de la largeur du trait peut entraîner des interruptions du flux si celui-ci devient inférieur au débit minimum de la buse. La matière forme alors des perles lorsqu'elle sort de la buse et la surface supérieure est alors empochée et sous-extrudée.

Cette technique est similaire à celle de [l'étirage](../top_bottom/ironing_enabled.md). Cependant, avec l'étirage, un passage supplémentaire est effectué sur la même couche avec des lignes très fines et en n'extrudant que des quantités infimes. Avec ce réglage, les lignes fines seront tracées dans sa propre couche au lieu de la peau supérieure. L'étirage provoque une surextrusion (volontairement). Ce réglage ne le fera pas.
