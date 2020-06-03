Activation de la rétraction d'essuyage
====
Si ce paramètre est activé, la matière sera rétracté tout au long de la procédure d'essuyage. Ce paramètre peut être configuré séparément des [rétractions normales](../travel/retraction_enable.md).

La procédure d'essuyage fait que la buse va jusqu'au côté de l'imprimante, se déplace d'avant en arrière, puis revient à sa position initiale. Il s'agit essentiellement d'un déplacement très long. Comme ce mouvement est plus long que les mouvements moyens de déplacement tout au long de l'impression, vous pouvez souhaiter que la matière soit rétracté pendant cette procédure, même si les rétractions sont normalement désactivées.

La rétraction du matériau réduira la quantité de matériau qui suinte pendant la procédure d'essuyage. Le matériau qui suinte pendant la procédure d'essuyage sera normalement essuyé par la brosse. Cependant, ce matériau est alors perdu. Par conséquent, il y aura une certaine sous-extrusion juste après la fin de l'essuyage, car ce matériau a suinté au lieu d'être placé à son emplacement correct.

D'autre part, la rétraction peut prendre un certain temps et provoquer une usure inutile du filament. Si la sous-extrusion n'est pas un problème, le fait de désactiver la rétraction peut permettre de gagner du temps et d'améliorer la fiabilité. Cela peut fonctionner correctement si, par exemple, le [remplissage est imprimé avant les murs](../infill/infill_before_walls.md), car une certaine sous-extrusion pendant le remplissage n'est pas vraiment un problème. 
