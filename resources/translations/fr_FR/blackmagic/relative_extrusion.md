Cura écrit des instructions pour que l'imprimante imprime votre objet en g-code. Ces instructions déplacent la tête d'impression dans certaines positions et l'engage dans le chargeur. Cura enregistre normalement les coordonnées de la tête d'impression et la rotation du chargeur comme coordonnées absolues. Toutefois, si ce paramètre est activé, les coordonnées du chargeur seront enregistrées de manière relative.

Si ce paramètre est désactivé (c'est-à-dire si l'extrusion est absolue), la position du filament au début de l'impression est conservée comme coordonnée zéro. La position du filament augmentera tout au long du fichier à mesure que de la matière sera extrudée et que le filament devra s'éloigner de plus en plus du point de départ au début de l'impression.

Toutefois, si cette fonction est activée, chaque ligne du code g aura son extrusion écrite séparément, par rapport à la position de la ligne précédente. Chaque ligne ne contient alors que la quantité de matière extrudée pour cette ligne particulière.

L'extrusion relative facilite l'édition du code g après sa génération. Si de la matière supplémentaire doit être extrudée quelque part entre les deux (pour ajouter ou supprimer des segments de ligne ou pour ajuster les débits), la nouvelle extrusion doit simplement être écrite dans la partie qui est éditée. Si une extrusion absolue est utilisée, la position de l'alimentateur doit être réinitialisée en utilisant "G92" par la suite pour s'assurer que toutes les commandes ultérieures sont correctes.

Cependant, si des erreurs d'arrondi sont introduites à un moment quelconque du traitement du code g (dans Cura, le firmware ou le mouvement), l'extrusion absolue le corrigera automatiquement à la ligne suivante. Dans l'extrusion relative, cela entraînera une sur-extrusion ou une sous-extrusion, bien qu'extrêmement mineure.

Tous les microprogrammes d'imprimante ne prennent pas en charge l'extrusion relative.

**Lorsque l'extrusion absolue est utilisée, Cura réinitialisera toujours la position du filament tous les 10 mètres afin d'éviter les erreurs d'arrondi en virgule flottante dans le firmware.**


