Expansion horizontale des supports
====
Ce réglage fait que le support devient légèrement plus large, s'étendant horizontalement dans toutes les directions.

![Le support est plus large que nécessaire pour supporter le modèle](../../../articles/images/support_offset.png)

Ce cadre a de multiples usages, selon la matière utilisé pour le soutien et le type de modèle qui a besoin d'être soutenu :
* Augmenter ce paramètre rendra le support plus large et donc plus solide. Ceci est utile pour les modèles hauts avec de petites zones de surplomb, puisque le surplomb serait autrement soutenu par un pilier de soutien très haut et mince. Avec un peu d'expansion horizontale, il devient un pilier de soutien très haut mais légèrement plus large.
* L'augmentation de ce paramètre est également une mesure de sécurité pour s'assurer que les zones de soutien ont une certaine surface minimale. Ceci est nécessaire pour les matériaux difficiles à extruder, comme le PVA.
* Réduire ce paramètre permet de réduire l'utilisation de matériaux et le temps d'impression du support. En l'augmentant, on augmentera bien sûr le matériau nécessaire et le temps d'impression. Voir également la fonction [support conique](support_conical_enabled.md), qui réduit la largeur du support sans compromettre la surface qu'il supporte.
* Le réglage de ce paramètre sur une valeur négative peut également supprimer complètement les piliers minces de support. Si ce support ne s'imprime pas de toute façon, il peut être préférable de le laisser complètement en dehors. Une méthode pour supprimer le support sans compromettre la qualité du surplomb du reste du modèle est l'outil Support Blocker.
