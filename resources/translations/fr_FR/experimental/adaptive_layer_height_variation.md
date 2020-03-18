Variation maximale des couches adaptatives
====
Avec ce paramètre, vous pouvez limiter la plage dans laquelle les couches adaptatives sont autorisées à sélectionner une épaisseur de couche. La hauteur de la couche ne doit pas s'écarter de plus de cette variation par rapport à la [Hauteur de la couche](../resolution/layer_height.md) normale.

Par exemple, avec une hauteur de couche normale de 0,15 mm et une variation fixée à 0,1 mm, les couches adaptatives peuvent produire des couches d'une épaisseur comprise entre 0,05 mm et 0,25 mm.

Ce réglage limite la puissance de la fonction "Couches adaptatives". Si la gamme d'épaisseurs de couche est trop étroite, l'épaisseur de la couche sera toujours très proche de l'épaisseur de la couche d'origine telle que définie par le réglage de la hauteur de la couche. Les couches adaptatives ne feront alors pas grand-chose pour gagner du temps ou améliorer la qualité.

Cependant, si la gamme est très large, les couches peuvent devenir très épaisses ou très fines. Les couches très épaisses nécessitent un débit important à la sortie de la buse, ce qui n'est pas toujours possible en raison de la taille limitée de la buse et de la capacité de fusion de la piste chauffante dans la tête d'impression. Les couches très fines ne sont pas non plus toujours possibles en raison de la viscosité du matériau ou de l'imprécision de l'axe Z. Il est donc bon de limiter la plage sur laquelle les couches adaptatives peuvent régler l'épaisseur de la couche. Sinon, l'imprimante aura du mal à atteindre l'épaisseur de couche souhaitée.

L'épaisseur de la couche ne peut jamais descendre en dessous de 0,001 mm, même si la plage le permet.
