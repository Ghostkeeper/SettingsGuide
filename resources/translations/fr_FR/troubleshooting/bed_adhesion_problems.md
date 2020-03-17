Problèmes d'adhérence au plateau
===

L'un des modes de défaillance les plus courants pour les impressions 3D est que l'empreinte s'est détachée de la plaque de construction alors qu'elle était encore en cours d'impression. Cet article passe en revue certains ajustements que vous pouvez apporter pour éviter que cela ne se produise.

Si l'impression s'est perdue de la plaque de montage, vous verrez généralement beaucoup de fils détachés sur la plaque de montage. Si vous avez plus de chance, cela peut aussi se manifester par un simple [décalage de couche](./layer_shift.md) (et il y aura moins à nettoyer). Dans tous les cas, l'impression est gâchée.

Méthodes d'adhérence au plateau
----
Cura propose plusieurs méthodes pour améliorer l'adhérence au lit. Vous pouvez choisir entre ces méthodes avec le paramètre [Build Plate Adhesion Type](../platform_adhesion/adhesion_type.md). Les options suivantes sont disponibles.
* Bord, la technique la plus courante, ajoute un bord autour de la face inférieure de l'impression, ce qui augmente la surface de l'impression de sorte que celle-ci adhère mieux à la plaque de montage.
* Un radeau est une plaque située sous l'ensemble de l'impression. Cette plaque obtient également une plus grande surface, de sorte qu'elle adhère bien. Si le radeau est imprimé avec un matériau qui adhère bien à l'empreinte (comme avec le même matériau), l'empreinte restera à sa place de cette façon.
* Une jupe n'est pas attachée à l'empreinte, mais l'encercle simplement. Cette ligne garantit que le matériau s'écoule avant que l'impression proprement dite ne commence, de sorte qu'il n'y a pas de sous-extrusion dans la première couche qui pourrait ruiner l'adhérence.
* Vous pouvez également ne pas avoir d'adhérence en sélectionnant "Aucune". Cela permet d'économiser du temps et du matériel et d'éviter les autres effets négatifs des méthodes susmentionnées. N'utilisez cette option que si votre imprimante dispose d'une autre technique d'impression, par exemple un seau de purge.

Le bord et le radeau sont les techniques les plus efficaces pour augmenter l'adhérence, car ils sont conçus expressément à cet effet. La plupart des impressions de taille raisonnable auront besoin de l'une ou l'autre de ces techniques.

Si un bord est utilisé, vous pouvez augmenter encore l'adhérence en augmentant la [largeur du bord](../platform_adhesion/brim_width.md). Vous pouvez également ajouter un rebord à [l'intérieur des supports](../support/support_brim_enable.md) et à la [tour principale](../dual/prime_tower_brim_enable.md) ainsi qu'entre le [modèle et support](../platform_adhesion/brim_replaces_support.md) et les [trous intérieurs](../platform_adhesion/brim_outside_only.md) du modèle.

De même, si un radeau est utilisé, vous pouvez augmenter l'adhérence en augmentant la [largeur du radeau](../platform_adhesion/raft_margin.md). Le radeau sera toujours imprimé en dessous de tout, car les couches doivent correspondre. Si l'adhérence entre la maquette et le radeau pose problème, pensez à réduire l'[entrefer](../platform_adhesion/raft_airgap.md) entre le radeau et la maquette. De plus, vous pouvez envisager d'augmenter la [largeur de la ligne de base du radeau](../platform_adhesion/raft_base_line_width.md).

Prévention du gauchissement
----
Si votre impression souffre de déformation, la zone de contact entre l'impression et la plaque de montage est fortement réduite. Pour éviter cela, consultez l'article sur [le décollement](./warping.md). En résumé, voici quelques ajustements à apporter pour éviter le gauchissement.
* Réglez le [Modèle de couche initiale du bas](../resolution/layer_height_0.md) sur concentrique.
* Réduisez la [température de la plaque de construction](../material/material_bed_temperature.md) et augmentez la [température du volume de construction](../material/build_volume_temperature.md).
* Ajustez le modèle de manière à ce qu'il y ait moins de coins extérieurs tranchants sur la première couche.

Ajustements divers
----
Ces paramètres peuvent également être ajustés si les méthodes normales d'adhésion au lit ne sont pas suffisantes.
* Augmenter la [Hauteur de la couche initiale](../resolution/layer_height_0.md). Cela offre un peu plus de marge d'erreur, si la plaque de construction n'est pas parfaitement de niveau. Cela augmente également la force avec laquelle le matériau est poussé hors de la buse et sur la plaque de montage.
* Augmenter la [Largeur de la ligne de la couche initiale](../resolution/initial_layer_line_width_factor.md). De même, cela pousse le matériau avec plus de force, en le collant bien à la plaque de montage.
* L'augmentation de la [couche initiale de la température d'impression](../material/material_print_temperature_layer_0.md) permet au matériau de s'écouler davantage sur la plaque de montage, ce qui augmente la surface de contact.
* Comme pour l'augmentation de la température, vous pouvez également réduire la [vitesse du ventilateur de la couche initiale](../cooling/cool_fan_speed_0.md) pour garder le matériau fluide plus longtemps.
* De même, réduisez la [vitesse de la couche initiale] (../speed/speed_print_layer_0.md). La réduction de la [vitesse d'impression de la couche initiale] (../speed/speed_print_layer_0.md) permet au matériau de s'écouler à nouveau davantage, car le matériau est maintenu fluide plus longtemps par la buse chaude. La réduction de la [vitesse de déplacement de la couche initiale] (../speed/speed_travel_layer_0.md) réduit le risque qu'un mouvement de déplacement arrache les lignes précédemment imprimées de la plaque de montage. De même, il faut envisager d'ajuster les paramètres [Accélération de la couche initiale](../speed/acceleration_layer_0.md) et [Accélération de la couche initiale](../speed/jerk_layer_0.md). 
* Augmenter le [nombre de couches plus lentes](../speed/speed_slowdown_layers.md). Cela réduit les risques que des mouvements rapides ne fassent disparaître les couches précédentes.

Plateau de construction
----
En plus d'une bonne impression, une bonne plaque de construction est également importante pour l'adhérence. Un bon plateau d'impression devrait être :
* ...propre ! Il est très important que la plaque de montage ne contienne pas de graisse (comme celle de vos doigts) et pas de poussière. Il est très efficace de la nettoyer sous un robinet chaud. L'idéal est d'utiliser de l'alcool à friction et un chiffon en microfibre.
* ...niveau ! Si la plaque de montage est trop proche, le flux sortant de la buse sera irrégulier, ce qui entraînera des bosses que la buse arrachera lors de sa prochaine utilisation. Si la plaque de montage est trop loin, le matériau n'est pas bien poussé sur la plaque de montage, ce qui réduit considérablement la surface. La plupart des imprimantes permettent d'ajuster la plaque de montage à l'aide de quelques vis à oreilles, il faut donc s'assurer qu'elle est parfaitement de niveau et correctement espacée de la buse.
* ...grossier ! Avec une plaque de montage légèrement rugueuse, la surface de contact entre la plaque de montage et l'impression est considérablement augmentée, contrairement à une plaque de montage parfaitement lisse. Pour cette raison, certaines imprimantes sont équipées de verre dépoli ou de métal anodisé.

Le matériau de la plaque de montage a également un impact important sur les propriétés adhésives. Celles-ci peuvent varier considérablement en fonction des matériaux d'impression. Les matériaux les plus courants sont le verre, l'acrylique, l'aluminium, l'acier ou l'aluminium anodisé. Chacun d'eux adhère à des matériaux différents. Les plaques de montage en plastique peuvent adhérer chimiquement à votre matériau. D'autres matériaux se caractérisent par une surface rugueuse qui augmente la surface de contact.

Il existe également des méthodes d'adhésion par lit supplémentaire que vous pouvez appliquer à n'importe quelle plaque de construction :
* Les bâtons de colle à papier génériques fonctionnent très bien. Bien que la colle sèche rapidement, elle produit une surface rugueuse avec une surface accrue pour que l'impression y adhère.
* Le ruban de masquage a un effet similaire, puisqu'il a une surface rugueuse faite de papier, mais contrairement au papier, il reste parfaitement plat sur la plaque de montage. Les types de rubans de masquage plus épais, conçus pour une utilisation extérieure, sont les plus efficaces.
* La laque pour cheveux fonctionne de la même manière que la colle, en ce sens qu'elle laisse une surface rugueuse à grain fin sur la plaque de construction. Il est très facile de l'appliquer uniformément.
* Appliquez du papier de verre sur la plaque de montage pour la rendre plus rugueuse et augmenter la surface de contact. Ne la rendez pas trop rugueuse, sinon vous aurez une surface inégale pour imprimer. Pour ce faire, utilisez un papier de verre à grain très fin, d'un grain de 500 ou plus.
* Des "feuilles d'adhérence" spécialisées sont vendues par de nombreux vendeurs d'imprimantes 3D, qui peuvent être tendues sur la plaque de construction. Elles fonctionnent de la même manière que le ruban adhésif, mais sont conçues pour durer plus longtemps. Certaines sont faites d'un plastique qui adhère chimiquement au matériau imprimé également.
