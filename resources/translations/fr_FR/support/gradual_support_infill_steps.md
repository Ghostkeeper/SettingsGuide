Le soutien progressif réduit la quantité de matériau de soutien utilisé, en réduisant la densité de soutien dans les couches inférieures. Cela permet d'économiser du temps et du matériel d'impression, tout en ne réduisant pas beaucoup la qualité du surplomb. Le but premier du support est de soutenir les zones en surplomb. Cette caractéristique permet de concentrer le support à cette seule fin.

Ce paramètre indique en combien d'étapes la densité du support est réduite. À chaque étape, la densité du support est réduite de moitié. Par exemple, à partir d'une densité de 20 % et de deux étapes de soutien progressives, la densité de soutien des parties inférieures sera respectivement de 10 % et de 5 %.

![Le support est réduit à une densité inférieure en 3 étapes](../../../articles/images/gradual_support_infill_step_height_1mm.png)

L'augmentation du nombre de marches entraîne une réduction de plus en plus importante de la densité, ce qui se traduit par une diminution du soutien de la densité. Cela permet d'économiser beaucoup de matériel et de temps d'impression, mais rend le support plus faible.

Une partie du support flottera dans l'air. Cependant, dans la pratique, avec la plupart des modèles de support, cela se réparera rapidement car les couches peuvent s'accumuler correctement même sur les couches inférieures affaiblies. L'objectif de la [Hauteur d'étape de remplissage graduel du support](./gradual_support_infill_step_height.md) est de laisser suffisamment de temps aux couches pour se réparer avant que la prochaine étape de support graduel ne soit empilée sur le dessus.

Ce paramètre est à combiner avec au moins un [Nombre de lignes de la paroi du support](./support_wall_count.md). Cela donne aux lignes de support quelque chose à quoi s'accrocher, plutôt que d'être suspendues en l'air.
