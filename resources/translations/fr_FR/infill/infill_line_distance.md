Distance d'écartement de ligne de remplissage
===

Au lieu de définir la [Densité de remplissage](infill_sparse_density.md) en pourcentage, il est également possible de configurer la densité de remplissage en définissant la distance entre les lignes de remplissage adjacentes. Une distance plus grande entre les lignes de remplissage entraînera une densité de remplissage globale plus faible.

La distance entre les lignes de remplissage est une façon différente de considérer cette propriété que la densité. La distance entre les lignes de remplissage donne une indication de la distance que les lignes de surface supérieure doivent parcourir d'une ligne de remplissage à l'autre. La réduction de la distance entre les lignes de remplissage permet donc de réduire la distance de pontage et d'améliorer la qualité des surfaces supérieures.

![4mm de distance entre les lignes, ce qui donne une densité de 20%](../../../articles/images/infill_sparse_density_high.png)
![8mm de distance entre les lignes, ce qui donne une densité de 10%](../../../articles/images/infill_sparse_density_low.png)

Normalement, la distance de la ligne de remplissage est calculée à partir de la densité de remplissage souhaitée, en fonction du modèle de remplissage sélectionné et de la largeur de la ligne. La distance de la ligne de remplissage est en tête.

L'augmentation de la densité de remplissage (en réduisant la distance entre les lignes) a un effet important sur votre impression, à savoir :
* Votre impression sera plus forte.
* La surface supérieure sera mieux soutenue, ce qui la rendra plus lisse et plus étanche.
* L'oreiller sera réduit car les poches de chaleur seront plus petites.
* Votre tirage nécessitera plus de matière et sera donc plus lourd.
* Il faut plus de temps pour imprimer.
