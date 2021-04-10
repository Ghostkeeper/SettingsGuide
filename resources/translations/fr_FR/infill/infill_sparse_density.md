Densité du remplissage
====
Ce paramètre configure la densité du volume à l'intérieur de l'impression, qui est un facteur majeur de la solidité de l'impression finale ainsi que de la qualité de la surface supérieure. Plus la densité de remplissage est élevée, plus les lignes de remplissage seront rapprochées. Vous pouvez même dépasser la densité de 100 %, mais cela entraînera une surextrusion.

![20% de densité](../../../articles/images/infill_pattern_grid.png)
![10% de densité](../../../articles/images/infill_sparse_density_low.png)

Des densités différentes fonctionnent mieux avec des modèles de remplissage différents. Les modèles de remplissage avec beaucoup de coins et de croisements ne fonctionneront pas bien avec de grandes densités de remplissage. Les coins posent un problème car le filament a tendance à glisser vers l'intérieur dans les angles, créant des poches d'air à l'extérieur du coin où le matériau aurait dû être déposé. Les croisements sont un problème encore plus important, car lorsqu'une ligne en croise une autre, son flux est interrompu, ce qui provoque une sous-extrusion juste après le croisement.

Augmenter la densité de remplissage (en réduisant la distance entre les lignes) a un effet important sur votre impression, à savoir :
* Votre impression sera plus forte.
* La surface supérieure sera mieux soutenue, ce qui la rendra plus lisse et plus étanche.
* L'effet matelassage sera réduit car les poches de chaleur seront plus petites.
* Votre impression nécessitera plus de matière et sera donc plus lourd.
* Il faut plus de temps pour imprimer.
