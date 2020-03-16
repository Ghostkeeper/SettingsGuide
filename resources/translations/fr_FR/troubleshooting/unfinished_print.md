Impression non terminée
===

Parfois, une impression ne se termine pas complètement. Plusieurs raisons peuvent expliquer ce phénomène, dont certaines peuvent être résolues en ajustant les paramètres de Cura.

![Le filament a cessé de couler à mi-chemin de cette impression](../../../articles/images/unfinished_print.jpg)

Défaillances des imprimantes
----
Parfois, la cause d'une impression inachevée est une panne d'imprimante, lorsque l'imprimante ne fait pas ce qu'on attend d'elle. En général, Cura ne peut pas faire grand-chose pour remédier à ces problèmes. Voici quelques causes courantes.
* Panne de courant. Cura ne peut pas faire grand-chose à ce sujet, si ce n'est imprimer plus vite pour réduire les risques de panne de courant pendant l'impression.
* Panne d'alimentation électrique. Si l'une des températures (soit le [plateau](../material/material_bed_temperature.md) ou la [buse](../material/material_print_temperature.md)) est trop élevée, certaines imprimantes ont un mode de défaillance où l'alimentation électrique brûle ou les capteurs de température donnent des erreurs. L'imprimante s'éteint alors et ne termine pas l'impression.
* Le microprogramme se fige. En raison de bogues dans le microprogramme, l'imprimante peut ne plus répondre. Si vous pouvez déterminer où dans le code G il se fige (le plus souvent au début ou à la fin de l'impression), vous pourrez peut-être voir quel code G en est la cause. Il est possible que le g-code de début ou de fin doive être ajusté.
* La bobine de filament est emmêlée. C'est une bonne idée de *toujours* tenir le bout du filament s'il n'est pas bien fixé dans l'extrudeuse ou engagé dans un des trous du filament (si votre bobine a de tels trous). Si vous lâchez et que l'extrémité du filament saute à nouveau sur la bobine, il pourrait glisser sous l'un des autres enroulements et s'emmêler. Comme le filament fait généralement des centaines de mètres de long, ce nœud peut être très difficile à dérouler s'il entre.

Broyage du filament
----
L'alimentateur pousse parfois très fort sur le filament pour le faire passer dans le train de l'extrudeuse. Cela endommage le filament. Lorsque le dispositif d'alimentation pousse et tire très souvent sur le même bout de filament, cela peut l'endommager à tel point que le dispositif d'alimentation ne peut plus avoir de prise sur le filament. Le matériau s'arrête alors de couler et le reste de l'impression est imprimé à l'air plutôt qu'en plastique.

![Le filament a été broyé par le margeur](../../../articles/images/grinding.jpg)

Vous pouvez sentir que cela se produit pendant l'impression en plaçant un doigt à l'ouverture où le filament va dans le chargeur. Pendant l'impression, vous devez sentir le filament bouger. Si elle ne bouge pas, c'est probablement qu'elle a broyé le matériau et qu'elle n'a pas de prise sur lui. Vous pouvez également tirer le filament hors de l'imprimante et voir où il est endommagé.

Pour éviter ce problème, vous pouvez effectuer les réglages suivants dans les paramètres de Cura :
* Réduire le [retrait maximal](../travel/retraction_count_max.md) ou augmenter la [Fenêtre de distance d'extrusion minimale](../travel/retraction_extrusion_window.md). Cela limitera le nombre de rétractions effectuées pendant l'extrusion d'une longueur donnée de filament. En fait, cela limite la fréquence à laquelle le dispositif d'alimentation peut rouler en avant et en arrière sur chaque morceau de filament.
* Réduire la [Distance de rétraction](../travel/retraction_amount.md). Cela limitera à nouveau le nombre de fois que le chargeur fera des allers-retours sur le même morceau de filament.
* Réduisez la [Vitesse de rétraction](../travel/retraction_speed.md)). Si le matériau se déplace rapidement mais qu'il est obstrué à un endroit quelconque du chemin, le chargeur broiera le matériau. Si le matériau se déplace plus lentement, il y a moins de chances que cela se produise.
* Imprimez plus lentement en réduisant la [Hauteur de la couche](../resolution/layer_height.md), la [Largeur de la ligne](../resolution/line_width.md) ou les [vitesses](../speed/speed_print.md)). Cela permet de réduire la force que le chargeur doit exercer sur le filament, ce qui réduit les risques de broyage.

