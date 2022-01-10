Problèmes d'adhérence au plateau
====
L'un des modes de défaillance les plus courants pour les impressions 3D est que la pièce se décolle du plateau alors qu'elle était encore en cours d'impression. Cet article passe en revue certains ajustements que vous pouvez apporter pour éviter que cela ne se produise.

Si l'impression s'est décollée du plateau, vous verrez généralement beaucoup de fils éparpillés sur le plateau. Si vous avez plus de chance, cela peut aussi se manifester par un simple [décalage de couche](layer_shift.md) (et il y aura moins à nettoyer). Dans tous les cas, l'impression est gâchée.

Méthodes d'adhérence au plateau
----
Cura propose plusieurs méthodes pour améliorer l'adhérence au plateau. Vous pouvez choisir entre ces méthodes avec le paramètre [Type d'adhérence du plateau](../platform_adhesion/adhesion_type.md). Les options suivantes sont disponibles.
* Bordure, la technique la plus courante, ajoute une bordure autour de la face inférieure de l'impression, ce qui augmente la surface de l'impression de sorte que celle-ci adhère mieux à la plaque de montage.
* Un radeau est une plaque située sous l'ensemble de l'impression. Cette plaque occupe également une plus grande surface, de sorte qu'elle adhère bien. Si le radeau est imprimé avec un matériau qui adhère bien à l'empreinte (ou avec le même matériau), l'empreinte restera à sa place de cette façon.
* Une jupe n'est pas attachée à l'empreinte, mais l'encercle simplement. Cette ligne garantit que le matériau s'écoule avant que l'impression proprement dite ne commence, de sorte qu'il n'y a pas de sous-extrusion dans la première couche qui pourrait ruiner l'adhérence.
* Vous pouvez également ne pas avoir d'adhérence en sélectionnant "Aucune". Cela permet d'économiser du temps et de la matière et d'éviter les autres effets négatifs des méthodes susmentionnées. N'utilisez cette option que si votre imprimante dispose d'une autre technique d'impression, par exemple un seau de purge.

La bordure et le radeau sont les techniques les plus efficaces pour augmenter l'adhérence, car ils sont conçus expressément à cet effet. La plupart des impressions de taille raisonnable auront besoin de l'une ou l'autre de ces techniques.

Si une bordure est utilisée, vous pouvez augmenter encore l'adhérence en augmentant la [largeur de la bordure](../platform_adhesion/brim_width.md). Vous pouvez également ajouter une bordure à [l'intérieur des supports](../support/support_brim_enable.md) et à la [tour d'amorçage](../dual/prime_tower_brim_enable.md) ainsi qu'entre le [modèle et support](../platform_adhesion/brim_replaces_support.md) et les [trous intérieurs](../platform_adhesion/brim_outside_only.md) du modèle.

De même, si un radeau est utilisé, vous pouvez augmenter l'adhérence en augmentant la [largeur du radeau](../platform_adhesion/raft_margin.md). Le radeau sera toujours imprimé en dessous de tout, car les couches doivent correspondre. Si l'adhérence entre la maquette et le radeau pose problème, pensez à réduire la [lame d'air](../platform_adhesion/raft_airgap.md) entre le radeau et la maquette. De plus, vous pouvez envisager d'augmenter la [largeur de la ligne de base du radeau](../platform_adhesion/raft_base_line_width.md).

Prévention du gauchissement
----
Si votre impression souffre de déformation, la zone de contact entre l'impression et le plateau est fortement réduite. Pour éviter cela, consultez l'article sur [le décollement](warping.md). En résumé, voici quelques ajustements à apporter pour éviter le gauchissement.
* Réglez la [Couche initiale du motif du dessous](../top_bottom/top_bottom_pattern_0.md) sur concentrique.
* Réduisez la [température du plateau](../material/material_bed_temperature.md) et augmentez la [température du volume de construction](../material/build_volume_temperature.md).
* Ajustez le modèle de manière à ce qu'il y ait moins de coins extérieurs tranchants sur la première couche.

Réglage du plateau d'impression
----
Une autre source fréquente de problèmes d'adhérence est que le plateau d'impression n'est pas de niveau. Cura suppose que la buse touche le plateau lors du déplacement vers la coordonnée Z 0, mais c'est rarement le cas. Les plateaux d'impression s'inclinent, sont déplacées vers le haut et vers le bas, et peuvent même se plier. Si le plateau d'impression n'est pas partout à la coordonnée 0, Cura extrudera plus de matière que ne le permet l'espace entre la buse et le plateau, et vous obtiendrez soit une surextrusion, soit une sous-extrusion. Lorsque le plateau est trop proche, la surextrusion peut entraîner la formation de bulles, ce qui peut amener la buse à arracher l'impression du  plateau d'impression lors d'un déplacement. Lorsque le plateau est trop éloigné, la sous-extrusion empêche le matériau d'être poussé sur le plateau d'impression, ce qui l'empêche de s'y coller correctement. Dans les deux cas, l'impression n'est pas fiable.

Certaines imprimantes sont équipées de capteurs capables de mesurer la position du plateau d'impression et de la compenser dans le micrologiciel. Pour ces imprimantes, déplacer la buse à la coordonnée Z 0 fera en sorte que la buse touche le plateau. Cependant, cela présente l'inconvénient de déformer le modèle. Pour compenser un plateau d'impression incliné, vous aurez un côté inférieur incliné, ou l'impression entière peut s'incliner, être tournée ou déformée. Si votre imprimante n'est pas en mesure de compenser un plateau qui n'est pas de niveau, il y a quelques choses qui peuvent être faites du côté de Cura aussi :

Augmentez la [hauteur initiale de la première couche](../resolution/layer_height_0.md). Cela offre un peu plus de marge d'erreur. Cela augmente également la force avec laquelle le matériau est poussé hors de la buse et sur le plateau d'impression.
Réduisez la [vitesse de déplacement de la couche initiale](../speed/speed_layer_0.md). Vous éviterez ainsi qu'un déplacement n'entraîne des lignes déjà imprimées sur le plateau d'impression.
De même, pensez à ajuster [l'accélération de la couche initiale](../speed/acceleration_layer_0.md) et les [secousses de la couche initiale](../speed/jerk_layer_0.md). Cela permet de réduire les vibrations, qui peuvent provoquer une sous-extrusion et une surextrusion périodiques.
Augmentez le [nombre de couches plus lentes](../speed/speed_slowdown_layers.md). Cela réduit le risque que des mouvements rapides arrachent les couches précédentes.

Ajustements divers
----
Ces paramètres peuvent également être ajustés si les méthodes normales d'adhérence au plateau ne sont pas suffisantes.
* Augmenter la [Hauteur de la couche initiale](../resolution/layer_height_0.md). Cela offre un peu plus de marge d'erreur, si le plateau n'est pas parfaitement de niveau. Cela augmente également la force avec laquelle le matériau est poussé hors de la buse et sur le plateau.
* Augmenter la [Largeur de la ligne de la couche initiale](../resolution/initial_layer_line_width_factor.md). De même, cela pousse le matériau avec plus de force, en le collant bien au plateau.
* L'augmentation de la [couche initiale de la température d'impression](../material/material_print_temperature_layer_0.md) permet au matériau de s'écouler davantage sur la plaque de montage, ce qui augmente la surface de contact.
* Comme pour l'augmentation de la température, vous pouvez également réduire la [vitesse du ventilateur de la couche initiale](../cooling/cool_fan_speed_0.md) pour garder le matériau fluide plus longtemps.
* De même, réduisez la [vitesse de la couche initiale](../speed/speed_print_layer_0.md). La réduction de la [vitesse d'impression de la couche initiale](../speed/speed_print_layer_0.md) permet au matériau de s'écouler à nouveau davantage, car le matériau est maintenu fluide plus longtemps par la buse chaude. La réduction de la [vitesse de déplacement de la couche initiale](../speed/speed_travel_layer_0.md) réduit le risque qu'un mouvement de déplacement arrache les lignes précédemment imprimées du plateau. De même, il faut envisager d'ajuster les paramètres [Accélération de la couche initiale](../speed/acceleration_layer_0.md) et [Saccade de la couche initiale](../speed/jerk_layer_0.md). 
* Augmenter le [nombre de couches plus lentes](../speed/speed_slowdown_layers.md). Cela réduit les risques que des mouvements rapides ne fassent disparaître les couches précédentes.

Plateau d'impression
----
En plus d'une bonne impression, un bon plateau d'impression est également important pour l'adhérence. Un bon plateau d'impression devrait être :
* ...propre ! Il est très important que le plateau ne contienne pas de graisse (comme celle de vos doigts) et pas de poussière. Il est très efficace de la nettoyer sous un robinet chaud. L'idéal est d'utiliser de l'alcool isopropylique et un chiffon en microfibre.
* ...de niveau ! Si le plateau est trop proche, le flux sortant de la buse sera irrégulier, ce qui entraînera des bosses que la buse arrachera lors de sa prochaine utilisation. Si le plateau est trop loin, le matériau n'est pas bien plaqué sur le plateau, ce qui réduit considérablement la surface. La plupart des imprimantes permettent d'ajuster le plateau d'impression à l'aide de quelques vis à molettes, il faut donc s'assurer qu'elle est parfaitement de niveau et correctement espacée de la buse.
* ...rugeux ! Avec un plateau légèrement rugueux,la surface de contact sur le plateau et l'impression est considérablement augmentée, contrairement à un plateau parfaitement lisse. Pour cette raison, certaines imprimantes sont équipées de verre dépoli ou de métal anodisé.

Le matériau du plateau d'impression a également un impact important sur les propriétés adhésives. Celles-ci peuvent varier considérablement en fonction des matériaux d'impression. Les matériaux les plus courants sont le verre, l'acrylique, l'aluminium, l'acier ou l'aluminium anodisé. Chacun d'eux adhère à des matériaux différents. Les plateaux d'impression en plastique peuvent adhérer chimiquement à votre matériau. D'autres matériaux se caractérisent par une surface rugueuse qui augmente la surface de contact.

Il existe également des méthodes d'adhérence par couche supplémentaire que vous pouvez appliquer à n'importe quel plateau d'impression :
* Les bâtons de colle à papier génériques fonctionnent très bien. Bien que la colle sèche rapidement, elle produit une surface rugueuse avec une surface accrue pour que l'impression y adhère.
* Le ruban de masquage a un effet similaire, puisqu'il a une surface rugueuse faite de papier, mais contrairement au papier, il reste parfaitement plat sur la plaque de montage. Les types de rubans de masquage plus épais, conçus pour une utilisation extérieure, sont les plus efficaces.
* La laque pour cheveux fonctionne de la même manière que la colle, en ce sens qu'elle laisse une surface rugueuse à grain fin sur le plateau. Il est très facile de l'appliquer uniformément.
* Utilisez du papier de verre sur le plateau d'impression pour le rendre plus rugueux et augmenter la surface de contact. Ne le rendez pas trop rugueux, sinon vous aurez une surface inégale pour imprimer. Pour ce faire, utilisez un papier de verre à grain très fin, comme un grain de 500 ou plus.
* Des "feuilles d'adhérence" spécialisées sont vendues par de nombreux vendeurs d'imprimantes 3D, qui peuvent être tendues sur le plateau. Elles fonctionnent de la même manière que le ruban adhésif, mais sont conçues pour durer plus longtemps. Certaines sont faites d'un plastique qui adhère chimiquement au matériau imprimé également.
