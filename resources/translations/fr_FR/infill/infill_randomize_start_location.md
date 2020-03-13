Si ce paramètre est activé, la position où l'imprimante commencera à imprimer le remplissage sur une couche sera aléatoire.

Le début de la piste de remplissage est généralement un peu plus faible que le reste du remplissage. Cela se produit lorsque le remplissage est imprimé plus rapidement, avec des lignes plus épaisses ou une hauteur de couche plus importante. Le flux de matériau doit soudainement s'accélérer, et cela ne se produit pas instantanément, de sorte qu'il y aura une sous-extrusion pendant un court moment. Si cela se produit au même endroit à chaque couche, cela affaiblit la structure de remplissage. L'endroit où cela se produit sera le maillon le plus faible, et le matériau de remplissage qui l'entoure sera soumis à plus de contraintes. Si l'empreinte est soumise à une force, c'est à cet endroit qu'elle risque le plus de se rompre.

Normalement, le remplissage commence par la ligne qui est la plus proche de la position où se trouvait la buse au moment du remplissage, afin de réduire le temps de parcours. Si ce réglage est activé, l'emplacement de départ est plutôt aléatoire. Cela permet d'étaler les points faibles. Il n'y aura plus un seul maillon faible dans la chaîne, et le remplissage sera donc plus fort à la fin.

Toutefois, cela augmente légèrement le temps de parcours et entraîne une augmentation du suintement à l'intérieur du modèle, puisque la distance jusqu'au point de départ du remplissage n'est plus réduite.

**Bien que l'emplacement de départ soit réparti de manière aléatoire, il reste déterministe. Répéter la même tranche deux fois devrait aboutir aux mêmes emplacements de départ.**
