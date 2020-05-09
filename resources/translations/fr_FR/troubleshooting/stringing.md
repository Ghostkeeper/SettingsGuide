Filasse
====
Lorsque l'imprimante a fini d'imprimer une partie d'une couche et doit passer à une autre partie, elle doit temporairement arrêter l'extrusion. Si le matériau continue à couler pendant qu'il se déplace, un fin fil de plastique est tiré entre les deux parties. C'est ce qu'on appelle le fil ou la filasse (Stringing en Anglais).

![De fines lignes de plastique sont visibles à l'endroit où la buse s'est déplacée d'une partie à l'autre](../../../articles/images/stringing.jpg)

Souvent, les fils sont alignés les unes sur les autres, car la buse termine une pièce au même endroit sur chaque couche. Cela crée une bande verticale. Le plastique supplémentaire peut également s'accumuler sur les fils des couches précédentes, ce qui donne des boules de plastique partout.

La filasse est parfois accompagnée d'une sous-extrusion. Le trancheur part généralement du principe qu'aucun matériau n'est perdu pendant les déplacements et demande donc à l'imprimante d'extruder juste assez de matériau pour imprimer sa prochaine partie. Si du matériau s'échappe de la buse pendant un déplacement (ce qui donne un fil), ce matériau ne sera pas utilisé pour l'impression de la partie suivante, ce qui entraîne une sous-extrusion à cet endroit. La filasse n'est normalement pas un problème s'il se produit à l'intérieur du remplissage, mais si la filasse est trop extrême, elle peut poser un problème même à cet endroit car elle entraîne une sous-extrusion par la suite.

Causes
----
La filasse se produit parce que la matière suinte de la buse lors d'un mouvement de déplacement. Bien que l'imprimante n'alimente pas de nouveau matériau pendant un déplacement, le flux de matériau ne s'arrête pas immédiatement. Pendant l'impression, il y a une certaine pression à l'intérieur de la chambre de la buse causée par le filament qui accumule une certaine force comme un ressort. Lorsque la buse se déplace dans l'air, cette pression peut se relâcher, poussant involontairement le matériau hors de la buse.

Même si la matière est rétractée avant le déplacement, il y aura encore de la matière à l'intérieur de la chambre de la buse. Cela se produit parce que la matière dans cette buse est en fusion. Le fait de la retirer d'un côté ne fait pas reculer le liquide. À moins qu'il ne soit solidifié, un cordon de matière fondue reste dans la buse. Lors d'un déplacement, cette bille suinte de la buse si elle est suffisamment liquide.

Prévention
----
La rétraction est la principale technique permettant d'éviter la filasse. Si vous voyez des traces de fils dans vos empreintes, voici quelques trucs que vous pourriez essayer :
* Assurez-vous que [la rétraction est activée](../travel/retraction_enable.md). Cela prend un peu plus de temps d'impression, mais réduit considérablement le nombre de fils.
* Réduisez la [température d'impression](../material/material_print_temperature.md). Cela rend le matériau moins liquide, ce qui le fait moins suinter de la buse. Cela permet également des rétractions plus efficaces, car une plus grande partie du matériau sera aspirée hors de la chambre de la buse.
* Si votre matériau est visqueux, l'augmentation de la [vitesse de rétraction](../travel/retraction_speed.md) réduira généralement la filasse pour les mouvements courts en exerçant une dépression sur la chambre de la buse. Cette pression réduite maintient la matière aspirée à l'intérieur, de sorte qu'elle ne suinte pas à l'extérieur.
* Pour les déplacements longs, l'augmentation de la [distance de rétraction](../travel/retraction_amount.md) maintient le matériau dans un endroit plus froid pendant le déplacement, réduisant ainsi la vitesse à laquelle le matériau fond et suinte de la buse.
* Parfois, Cura essaie de prévenir l'usure du filament en limitant le nombre de rétractions sur une certaine longueur de filament. Comme il n'y a pas de rétractions à ce moment-là, il produira udu fil comme un mal nécessaire plutôt que l'impression défaillante. Si votre extrudeur n'use pas trop le matériau, vous pouvez augmenter le [nombre de rétractions autorisées](../travel/retraction_count_max.md) ou réduire la [longueur du filament](../travel/retraction_extrusion_window.md) le long de laquelle il compte ces rétractions.
* Si l'on autorise le [Mode de détours](../travel/retraction_combing.md) à l'intérieur du remplissage, la buse passera à l'intérieur du modèle plutôt qu'à l'extérieur. Cela n'empêche pas réellement la filasse, mais la rendra invisible en la plaçant à l'intérieur du modèle.
* Si l'on a [Optimiser l'ordre d'impression des parois](../shell/optimize_wall_printing_order.md), la buse se déplacera moins souvent d'une pièce à l'autre, ce qui réduira la quantité de filasse.
* L'augmentation de la [vitesse de déplacement](../speed/speed_travel.md) permet généralement d'amincir les fils lors des déplacements plus longs. Pour les déplacements courts, cela ne fait pas vraiment de différence, puisque les limites d'accélération des imprimantes empêchent de toute façon la buse d'atteindre ces vitesses.
* L'impression avec une buse plus petite réduira aussi normalement le nombre de fils. Il est plus facile pour le plastique de suinter d'une buse plus grosse.
