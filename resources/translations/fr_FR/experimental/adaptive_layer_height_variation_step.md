Taille des étapes de variation des couches adaptatives
====
Si l'épaisseur souhaitée d'une couche est très différente de celle d'une couche adjacente, il y aura une grande différence de débit à la sortie de la buse, ce qui peut provoquer une sur ou une sous-extrusion. Ce réglage permet de s'assurer que la différence d'épaisseur de couche est un changement progressif, pour éviter cela. Avec ce paramètre, vous pouvez spécifier la variation maximale de l'épaisseur de la couche entre deux couches adjacentes.

![Une grande taille de pas permet des changements très soudains dans l'épaisseur de la couche](../../../articles/images/adaptive_layer_height_variation_step_0_05.png)
![Une petite taille de pas nécessite des changements d'épaisseur de couche pour être plus lisse](../../../articles/images/adaptive_layer_height_enabled.png)

La réduction de ce paramètre obligera à une transition plus progressive de l'épaisseur de la couche. Cela a un certain nombre d'effets sur l'impression :
* Il y aura moins de surextrusion lors de la transition vers une épaisseur de couche plus faible, car le débit sortant de la buse a un certain temps pour s'adapter à un débit plus faible. Cela permet d'éviter les taches à la surface.
* De même, il y aura moins de sous-extrusion lors de la transition vers une épaisseur de couche plus importante, car le débit sortant de la buse peut s'adapter progressivement à un débit plus important.
* Les bandes seront moins visibles. Même si des zones d'épaisseur de couche différente auront toujours une texture et une couleur différentes, ces zones sont maintenant plus éloignées les unes des autres, ce qui les rend plus difficiles à voir.
* Là où il y a un angle aigu dans le modèle qui devrait provoquer une transition soudaine vers des couches plus fines, l'effet de topographie réapparaîtra. En effet, l'épaisseur de la couche ne pourra pas être ajustée aussi rapidement, et il faudra donc utiliser des couches plus épaisses pour les surfaces peu profondes.
* De même, lorsqu'un angle aigu du modèle devrait provoquer une transition soudaine vers des couches plus épaisses, l'imprimante créera des couches inutilement fines, ce qui fera perdre du temps d'impression là où ce n'est pas nécessaire.

En raison de l'implémentation de l'algorithme des couches adaptatives, la transition progressive vers une épaisseur de couche différente se produira toujours *au-dessus* de l'angle dans le modèle qui provoque la transition.


