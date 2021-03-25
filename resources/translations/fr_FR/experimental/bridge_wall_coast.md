Roue libre pour paroi du pont
====
Lors de l'impression d'un pont avec des lignes murales, juste avant qu'un pont ne soit imprimé, l'alimentation en matériau est interrompue pendant un moment. Pendant ce temps, le matériau restant à l'intérieur de la chambre de la buse est laissé s'écouler, afin de réduire la pression à l'intérieur de la chambre de la buse. Cette technique est appelée [Roue libre](coasting_enable.md). Ce réglage permet de contrôler la quantité de roue libre. Il s'agit essentiellement de contrôler la distance à laquelle le matériau cessera de s'écouler devant un pont.

Une fois le pont terminé, le matériau qui n'a pas été extrudé sera de toute façon expulsé. La quantité totale de matériau extrudé restera la même. Cela rétablit la pression sur la buse, ce qui empêche la sous-extrusion.

![Pas d'extrusion d'un côté du pont, et extrusion supplémentaire de l'autre](../../../articles/images/bridge_skin_density_100.png)

L'unité de ce réglage n'est pas censée être intuitive. La distance devant le pont à laquelle le matériau s'arrêtera de couler dépend d'un certain nombre de facteurs :
* La longueur du mur jusqu'au pont. Plus le mur est long, plus il peut se déplacer en roue libre.
* Le débit de la buse pendant la paroi normale, qui dépend de la [vitesse](../speed/speed_wall.md), [largeur de ligne](../resolution/wall_line_width.md), [débit](../material/wall_material_flow.md) et [hauteur_couche](../resolution/layer_height.md) de ces parois. Plus le débit est important dans les murs normaux, plus la distance parcourue est longue.
* Le débit de sortie de la buse pendant la paroi en pont, qui dépend de la [vitesse](bridge_wall_speed.md) et du [débit](bridge_wall_material_flow.md) de ces parois. Plus le débit est important dans les parois pontées, plus la distance de franchissement est courte.

Ce paramètre est un facteur multiplicateur de la longueur finale.

L'objectif de cette roue libre est d'abaisser la pression à l'intérieur de la chambre de la buse. Ceci est nécessaire, car toute pression restante dans la chambre de la buse fera gicler la matière sur une distance considérable avant de se solidifier dès que la contre-pression disparaîtra. Ce jet de matière entraîne un affaissement. En fait, les lignes en surplomb sont poussées vers le bas par le reste de la matière qui se trouve encore à l'intérieur de la buse. Si la pression à l'intérieur de la chambre de la buse diminue, cette force sera également réduite et il y aura moins d'affaissement.

L'augmentation de la course en roue libre réduira la pression à l'intérieur de la chambre de la buse au moment où le pont doit être imprimé, ce qui réduira l'affaissement. L'impression sera plus précise. Cependant, si l'on augmente trop le cambrage, il y aura une période de sous-extrusion juste avant l'impression du pont. Comme cette sous-extrusion se trouve dans les parois de l'empreinte, elle sera très visible sur le côté de l'empreinte.
