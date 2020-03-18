Insert en spaghettis
====
Pour permettre au remplissage de spaghetti de se développer dans toutes les directions de manière égale, il faut garder une certaine distance par rapport aux murs. Ce réglage détermine cette distance.

Le comportement de ce paramètre est presque le même que celui du paramètre [Chevauchement du remplissage](../infill/infill_overlap_mm.md). Si le chevauchement de remplissage est réglé à la valeur négative de ce paramètre, la zone que la buse traversera sera la même. Toutefois, la différence est que le volume total extrudé pour le remplissage reste inchangé par ce réglage. Alors que la réduction du chevauchement réduit la quantité de matériau extrudé pour le remplissage, le réglage de ce paramètre ne changera pas le volume total extrudé pour le remplissage.

Lorsque l'on utilise des spaghettis de remplissage comme modèle de remplissage flexible, ce réglage doit être réglé de manière à ce que le matériau ne heurte pas les parois lors de sa descente, avant qu'il ne repose sur le matériau. Si l'encastrement est trop petit, le spaghetti de remplissage collera simplement aux murs et produira de gros blocs de matériau à cet endroit. Par contre, si l'encart est trop grand, toute la matière sera concentrée au milieu au lieu d'ajouter des quantités égales de force de tous les côtés.

Lorsque l'on utilise des spaghettis de remplissage pour le coulage, il faut les régler pour qu'ils soient adaptés aux buses de coulage plus larges, typiques des imprimantes qui sont capables de couler du matériau, de sorte qu'aucun matériau ne s'écoule sur la paroi en dehors du volume de remplissage.
