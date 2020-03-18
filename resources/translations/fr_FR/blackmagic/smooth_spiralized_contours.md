Lisser les contours spiralisés
====
Si [Spiraliser le contour extérieur](magic_spiralize.md) est activé, ce paramètre active ou désactive la caractéristique la plus distinctive du mode Spiralize: au lieu d'imprimer chaque couche l'une après l'autre à des intervalles de hauteur, la hauteur est progressivement augmentée au cours de la couche.

Étant donné que le mode Spiralize entraîne uniquement l'impression des murs pour la plupart des couches avec un seul contour, ce contour unique prendra la forme d'une spirale, prêtant le nom à la fonction Spiralize. Les première et dernière couches de l'impression voient leur débit progressivement réduit afin d'éviter une surextrusion et d'atteindre la bonne hauteur.

Étant donné que la buse est progressivement déplacée jusqu'à la hauteur de couche suivante tout au long de la couche, il n'y aura plus de couture où la buse se déplace vers la couche suivante. En effet, cela supprime la couture Z.

En revanche, le calque est déplacé vers le haut ou vers le bas d'une demi-hauteur de calque. C'est moins précis. Il peut avoir un effet de flou sur les détails fins de l'impression.

Ce paramètre n'est pas efficace pour supprimer les coutures s'il y a plusieurs contours à imprimer sur un calque. Il faudra encore arrêter l'extrusion après le contour pour passer à la prochaine pièce imprimée. Cela laisse une couture de toute façon.

**Cet effet n'est pas visible dans la vue des calques en raison des limitations de rendu.**
