Le décalage des couches
====
Un décalage de couches se produit lorsque les couches d'une impression ne sont pas correctement empilées les unes sur les autres. Si la tête d'impression est déplacée pendant l'impression d'une couche pour une raison quelconque, l'imprimante continue d'imprimer avec un décalage. La face supérieure de l'impression est alors décalée par rapport à la face inférieure.

![Un décalage d'une seule couche dû à une obstruction](../../../articles/images/layer_shift_single.jpg)

Causes
----
Les changements de couches se présentent sous deux formes.

Le premier type de décalage de couche est causé par l'obstruction de la tête d'impression quelque part sur le chemin. Cela provoque alors un décalage de couche à un endroit situé en cours d''impression. Cela peut être dû au fait que l'utilisateur place quelque chose à l'intérieur du portique pendant l'impression, ou lorsque la tête d'impression heurte un autre objet pendant l'impression en [mode un à la fois](../blackmagic/print_sequence.md). Si la tête d'impression entre en collision avec un objet et est incapable de se déplacer, les moteurs sautent certains pas. Si l'imprimante n'est pas en mesure de détecter que cela s'est produit, elle continuera simplement sans connaissance de cet erreur, en décalant le reste de l'impression.

Un autre type de décalage de couche se produit lorsque la tâche d'impression elle-même impose une force trop importante à la tête d'impression, ce qui fait que les moteurs pas à pas de l'imprimante perdent des pas. Chaque fois que des pas sont perdus, l'impression est décalée à partir de là. En général, les pas perdus se produisent au même endroit à chaque couche en raison d'un coin particulièrement pointu. Le résultat est que l'impression entière ou une certaine partie de celle-ci semble biaisée.

Prévention
----
Le premier type de déplacement de couche n'est normalement pas corrigeable par des réglages Cura. Cura est conçu pour éviter de heurter les côtés du volume d'impression. Si la taille du volume d'impression est saisie correctement dans Cura, elle ne devrait pas générer de G-Code qui se déplace en dehors du volume imprimable. S'il génère un tel G-Code, la boîte de dialogue Paramètres machine sous la gestion de l'imprimante vous permettra d'ajuster la taille du volume d'impression pour effectuer une correction. Vous devez également vous assurer qu'il n'y a pas d'obstruction dans le volume d'impression que la tête d'impression ou le système de mouvement pourrait toucher pendant l'impression. Les imprimantes ne peuvent généralement pas détecter ce genre de problème, et elles continueront donc à imprimer à partir d'une position décalée. Recherchez si il y a des câbles qui gênent et assurez-vous que tous les câbles sont suffisamment longs pour permettre à l'imprimante de se déplacer dans toute sa plage de mouvement. Vérifiez également si les pilotes pas à pas de la carte de circuit imprimé de l'imprimante ne sont pas en surchauffe, ce qui pourrait entraîner un arrêt temporaire de leur fonctionnement.

L'autre type de décalage de couche, celui qui se produit continuellement tout au long de l'impression, est probablement dû à une force trop importante exercée sur votre système de mouvement. Il existe plusieurs solutions possibles.

Vous devriez d'abord examiner votre matériel. Les courroies sont-elles bien tendues ? Si ce n'est pas le cas, vous pouvez chercher un moyen de les resserrer. Certaines imprimantes ont des moteurs à position réglable qui vous permettent de serrer les courroies. Les poulies glissent-elles ? Serrez les boulons des poulies pour être sûr. Enfin, un problème électrique courant est que les moteurs ne reçoivent pas suffisamment de courant pour générer des forces assez fortes pour effectuer un virage serré. Dans ce cas, vérifiez si l'alimentation électrique est suffisante.

Si le matériel fonctionne bien, vous pouvez également régler Cura  pour que les déplacements matériel soit plus facile. Voici quelques paramètres que vous pouvez ajuster :
* Diminuer les [taux de secousse](../speed/jerk_print.md). Cela ralentira la tête d'impression avant de faire les coins. Cela rend le passage dans les coins plus souple, en lissant le coin au lieu de faire un virage serré.
* Diminuez les [taux d'accélération](../speed/acceleration_print.md). La tête d'impression ralentira ainsi plus et plus longtemps avant de faire un virage ( la vitesse à laquelle la tête d'impression passera par le sommet du virage ne sera pas affectée ; c'est le but du réglage de l'accélération).
* Diminuez la [vitesse de déplacement](../speed/speed_travel.md). Cela réduit la force avec laquelle la buse frotte sur les pièces déjà imprimées.
* Activer le [décalage en Z lors d’une rétraction](../travel/retraction_hop_enabled.md). Cela évite que la tête d'impression ne heurte les pièces précédemment imprimées si elles dépassent un peu vers le haut en raison de taches ou de déformations.

