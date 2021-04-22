Matelassage
====
L'effet de matelassage est un effet où de petits renflements ou trous apparaissent entre les lignes de remplissage sur la face supérieure du modèle. On l'observe le plus souvent sur les surfaces supérieures planes lors de l'impression à haut débit.

![Forts bombements et petits trous dans la surface](../../../articles/images/pillowing.jpg)

Causes
----
Le matelassage est une combinaison de plusieurs effets qui se combinent pour provoquer un effet de bombement sur la face supérieure de l'impression.

Le bombement reconnaissable de la peau supérieure est en fait une forme de [gauchissement](warping.md) où la peau supérieure est comprimée par les parois environnantes et le remplissage sous-jacent. Comme les parois et le remplissage sont imprimés en premier dans les couches inférieures, ils vont refroidir et se rétracter pendant que la peau est encore en cours d'impression. Pendant le rétrécissement, les parois et le remplissage poussent les lignes de la peau à l'intérieur au point où elles sont bombées.

Un autre facteur important dans le matelassage est l'affaissement des lignes de peau entre les lignes de remplissage. En fonction de la distance entre les lignes de remplissage, les lignes de peau doivent couvrir une certaine distance. Si le refroidissement est insuffisant, le plastique s'affaissera un peu. Les lignes de peau adhèrent alors moins bien les unes aux autres, laissant des espaces entre elles. Il faut quelques couches de peau pour réparer cela.

L'effet de matelassage a tendance à se gonfler vers le haut plutôt que vers le bas. Bien qu'il puisse y avoir un bombement vers le haut et vers le bas, le bombement vers le haut est plus courant car la buse tire sur la face supérieure du plastique lorsqu'elle traverse la peau, ce qui exerce une force de cisaillement vers le haut pendant un court instant. Une fois que les lignes sont bombées vers le haut, l'effet de déformation les maintient vers le haut.

Prévention
----
Il existe plusieurs méthodes pour empêcher le matelassage dans Cura :
* Augmenter l'[Épaisseur du dessus](../top_bottom/top_thickness.md) est la manière la plus efficace d'empêcher le matelassage. Avec plus de [Couches supérieures](../top_bottom/top_layers.md), les couches supérieures peuvent reposer sur les espaces partiellement fermés des couches précédentes. Cela leur donne une meilleure chance de fermer les espaces et de former une couche supérieure solide qui ne s'appuie pas sur ces bombages. En général, plus vos couches sont fines, plus vous aurez besoin de couches supérieures, car ces couches ne sont pas aussi solides.
* Augmenter la [Densité du remplissage](../infill/infill_sparse_density.md) réduit la taille des espaces qui doivent être comblés par la peau supérieure. Il est ainsi plus facile de combler ces lacunes. Si vous combinez cela avec les [Étapes de remplissage progressif](../infill/gradual_infill_steps.md), la plupart des densités de remplissage peuvent rester les mêmes. Seule la partie supérieure aura une densité plus importante pour éviter l'effet de matelassage.
* L'impression à une [Température d’impression par défaut](../material/material_print_temperature.md) plus basse améliore le pontage et le gauchissement en général, également avec la peau supérieure, ce qui réduit l'effet de matelassage.
* De même, il faut veiller à augmenter la vitesse du [refroidissement](../cooling/cool_fan_speed.md) pour améliorer le pontage.
* La réduction de la [Vitesse d'impression du dessus/dessous](../speed/speed_topbottom.md) améliorera directement le pontage. Cela permettra également de mieux pousser les couches supérieures de la peau sur les couches inférieures. Cela permet également de fermer les trous plus rapidement.

