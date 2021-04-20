Activer la rétraction
====
Si une imprimante 3D arrêtait de pousser le matériau, le matériau ne cesserait pas immédiatement de couler par l'extrémité de la buse. Il y a des résidus de matière dans la buse et elle est pressurisée, ce qui fait qu'elle continue à couler pendant un certain temps encore. Pour empêcher le matériau de s'écouler, l'imprimante doit le retirer de l'ouverture de la buse. Cela est nécessaire pour effectuer des mouvements de déplacement propres sans fil.

![Rétractations désactivées](../../../articles/images/retraction_enable_disabled.png)
![Les mouvements de déplacement rétractés apparaissent en bleu plus clair](../../../articles/images/retraction_enable_enabled.png)

Les rétractions sont effectuées lors d'un déplacement particulièrement sensible à la génération de fils. Les mouvements de déplacement qui ne font que passer par un remplissage ou un déplacement de support à support ne sont normalement pas rétractés. Il existe également une limite à la fréquence de rétraction du matériau, par le biais des paramètres [Nombre maximal de rétractions](retraction_count_max.md) et [Intervalle de distance minimale d'extrusion](retraction_extrusion_window.md).

La rétraction présente des avantages importants, mais aussi des inconvénients :
* Il réduit considérablement le nombre de fils. Plus de filasse entre les différentes parties de l'impression.
* Cela réduira de manière significative la quantité et la taille des marques sur la surface où la buse pénètre dans le périmètre d'une pièce.
* Il faut un peu de temps pour se rétracter.
* Le flux de matière est interrompu lorsqu'il y a rétraction. Cela a des conséquences négatives sur la précision dimensionnelle, les rayures et la sous-extrusion.
* Le filament peut s'user quand il y a trop de rétractions, ce qui empêche le dispositif d'alimentation de pousser le matériau.

**Les matériaux flexibles sont plus difficiles à rétracter, car le fait de tirer sur le filament le fait s'étirer au lieu de le sortir de la buse. Il peut être très long et relativement inefficace de permettre la rétraction avec de tels matériaux.**


