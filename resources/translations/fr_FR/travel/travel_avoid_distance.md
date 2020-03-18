Distance d'évitement du déplacement
====
Lorsque [Eviter les pièces imprimées lors du déplacement](travel_avoid_other_parts.md) est actif, ce paramètre définit l'espace libre que la buse garde par rapport aux autres objets qu'elle doit éviter.

N'oubliez pas que ce paramètre définit la distance entre les autres objets et l'axe du mouvement de translation. Le mouvement de déplacement n'a pas d'épaisseur. Il est conseillé de donner une valeur à ce paramètre qui soit au moins suffisamment grande pour que l'extrémité de la buse ne touche pas les autres parties.

En augmentant la valeur de ce réglage, on réduit le risque que la buse ne touche des objets déjà imprimés lorsqu'elle les contourne. Cependant, augmenter la valeur de ce réglage augmentera aussi légèrement la longueur des mouvements de déplacement, puisque la buse doit faire un plus grand détour. Cela augmente le temps d'impression et la quantité de suintement légèrement. Ce qui est peut-être plus important, c'est que cela réduit les chances de trouver un chemin valable qui ne s'approche pas trop des pièces précédemment imprimées. Si aucun chemin valable n'est trouvé, la buse se rétractera (peut-être) et se déplacera en ligne droite à la place, se résignant à ce que les autres parties soient touchées de toute façon. Une augmentation trop importante de ce réglage peut donc également nuire à la qualité de la surface.
