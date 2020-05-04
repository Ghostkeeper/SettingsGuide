Zones interdites
====
Ce réglage indique les zones de votre plaque de construction où la tête d'impression n'est pas autorisée à aller. L'utilisateur n'est pas autorisé à placer des objets dans ces zones ou à proximité de celles-ci au point d'y permettre l'impression de quelque chose (comme une bordure).

Ces zones interdites sont nécessaires pour éviter que la tête d'impression n'entre en collision avec des objets. Par exemple, il peut y avoir une brosse d'essuyage à portée de la tête d'impression quelque part, ou une caméra qui dépasse légèrement trop à l'intérieur du volume de construction. Si l'utilisateur devait imprimer trop près de ces objets, la tête d'impression entrerait en collision avec eux. Au mieux, vous obtiendrez un [décalage des couches](../troubleshooting/layer_shift.md). Au pire, vous endommageriez la tête d'impression ou tout autre objet avec lequel la tête d'impression entre en collision.

Les zones interdites sont représentées par une ombre grise sur la plaque de construction, indiquant à l'utilisateur qu'il ne peut y placer aucun objet. Ces ombres peuvent être étendues dans toutes les directions pour éviter que la bordure ou la jupe ne la touche et pour diverses autres raisons. Il existe également d'autres zones grisées sur le plateau d'impression, par exemple pour limiter l'amplitude de mouvement si les buses sont décalées.

Si seule la buse active devait entrer en collision avec les obstacles, le réglage similaire [Zones interdites aux buses d'impression](nozzle_disallowed_areas.md) peut empêcher la buse d'entrer en collision avec elle tout en permettant à la tête d'impression de se déplacer au-dessus.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
