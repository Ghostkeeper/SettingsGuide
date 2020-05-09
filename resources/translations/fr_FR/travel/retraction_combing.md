Mode de détours
====
Le détour est un mode de calcul des trajectoires qui consiste à éviter de traverser les murs de l'empreinte lors d'un déplacement d'un endroit à un autre. Le croisement des parois tend à laisser une cicatrice sur la surface où une buse chaude est sortie ou est entrée dans le volume de l'impression, ce qui est généralement indésirable.

Le détour seul fait que la buse évite les parois lorsqu'elle traverse l'intérieur du remplissage. Cependant, cela permet également d'utiliser la fonction [Eviter les pièces imprimés lors du déplacement](travel_avoid_other_parts.md), qui permet à la buse d'éviter les objets lorsqu'elle se trouve à l'extérieur du volume imprimé.

![Détour désactivé, le mouvement de déplacement traverse les parois de l'impression](../../../articles/images/retraction_combing_off.png)
![Détour activé, un détour est fait pour éviter de traverser les murs](../../../articles/images/retraction_combing_on.png)

S'il existe un chemin à travers l'objet du début à la fin sans heurter aucun mur, ce chemin sera emprunté sans faire de rétractation. Si les emplacements de départ et d'arrivée sont situés sur des trajectoires complètement séparées, la buse se déplacera d'abord vers la position où les deux parties sont les plus proches l'une de l'autre, puis se rétractera éventuellement (si [les rétractions sont activées](retraction_enable.md)), se déplacera vers la trajectoire cible, se rétractera éventuellement, puis se déplacera à travers la nouvelle partie jusqu'à sa destination finale. Dans les deux parties, il évitera de heurter les murs lors de son déplacement à l'intérieur. Lors d'un déplacement d'une pièce à l'autre, il n'évitera les pièces que si le paramètre [Eviter les pièces imprimés lors du déplacment](travel_avoid_other_parts.md) est activé.

L'objectif du mode de détour est d'éviter de passer à travers les parois de l'objet, en réduisant la quantité de cicatrices à la surface. Il réduira également la filasse visible à l'extérieur, car pendant le déplacement, elle suintera toujours, mais ce suintage est placée à l'intérieur du modèle. Cependant, le mode de détour augmentera également la longueur du mouvement de déplacement. Parfois, il faut faire un grand détour.

Il y a quatre options dans le menu déroulant pour ce réglage :
* **Désactivé** : Le mode de détour est désactivé. Les déplacements se feront toujours directement vers leur destination. S'il ne touche aucun mur, il ne se rétractera pas.
* **Tout** : La buse ne touche aucun mur lorsqu'elle se déplace à l'intérieur de l'empreinte, comme décrit ci-dessus.
* **Pas dans la couche extérieure** : La buse évitera également de toucher la peau, si possible. Cela peut réduire les cicatrices sur la face supérieure de l'impression en faisant en sorte que la buse longe les parois plutôt que de couper à travers la peau. Toutefois, dans certains cas, la buse ne pourra pas s'échapper et devra se rétracter, sinon elle aurait coupé la peau.
* **A l'intérieur du remplissage** : Le mode le plus strict de tous, qui ne permet que le détour à travers le remplissage. Cela permet d'éviter de marquer les parois intérieures aussi bien que les parois extérieures, et évite également de marquer la peau. Si la buse touche les parois intérieures, elle peut parfois être encore visible de l'extérieur, car son rayon extérieur peut être plus large que les parois. Cela permet d'éviter cet effet. Cependant, il faudra faire encore plus de rétractions car souvent, il n'y aura pas de passage.
