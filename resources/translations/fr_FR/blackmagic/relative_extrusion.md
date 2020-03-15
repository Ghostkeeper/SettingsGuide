Extrusion relative
===

Cura écrit des instructions pour que l'imprimante imprime votre objet en g-code. Ces instructions déplacent la tête d'impression dans certaines positions et le pilotage de l'extrudeur. Cura enregistre normalement les coordonnées de la tête d'impression et la rotation de l'extrudeur comme coordonnées absolues. Toutefois, si ce paramètre est activé, les coordonnées de l'extrudeur seront enregistrées de manière relative.

Si ce paramètre est désactivé (c'est-à-dire si l'extrusion est absolue), la position du filament au début de l'impression est définie comme coordonnée zéro. La position du filament augmentera tout au long du fichier à mesure que de la matière sera extrudée et que le filament devra s'éloigner de plus en plus du point de départ au début de l'impression.

Toutefois, si cette fonction est activée, chaque ligne du Code-G aura son extrusion écrite relativement par rapport à la position de la ligne précédente. Chaque ligne ne contient alors que la quantité de matière extrudée pour cette ligne particulière.

L'extrusion relative facilite l'édition du code g après sa génération. Si de la matière supplémentaire doit être extrudée quelque part entre les deux (pour ajouter ou supprimer des segments de ligne ou pour ajuster les débits), la nouvelle extrusion doit simplement être écrite dans la partie qui est éditée. Si une extrusion absolue est utilisée, la position de l'extrudeur doit être réinitialisée en utilisant "G92" par la suite pour s'assurer que toutes les commandes ultérieures sont correctes.

Cependant, si des erreurs d'arrondi sont introduites à un moment quelconque du traitement du Code-G (dans Cura, le firmware ou le mouvement), l'extrusion absolue le corrigera automatiquement à la ligne suivante. Dans l'extrusion relative, cela entraînera une sur-extrusion ou une sous-extrusion, bien qu'extrêmement mineure.

Tous les microprogrammes d'imprimante ne prennent pas en charge l'extrusion relative.

**Lorsque l'extrusion absolue est utilisée, Cura réinitialisera toujours la position du filament tous les 10 mètres afin d'éviter les erreurs d'arrondi en virgule flottante dans le firmware.**


