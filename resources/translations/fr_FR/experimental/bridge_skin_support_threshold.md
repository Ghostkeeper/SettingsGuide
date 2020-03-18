Limite de support de la couche extérieure du pont
====
Ce paramètre vous permet d'ajuster la sensibilité de la détection des zones de transition. Les zones de pontage sont détectées en vertu de la partie de la peau qui est soutenue par quelque chose dans la couche précédente.

Pour chaque région disjointe de la peau, ce paramètre permet de déterminer la proportion de la peau qui est soutenue par un élément de la couche inférieure. Si la région est trop peu soutenue, la technique de pontage sera appliquée aux régions de la peau qui ne sont pas soutenues.

L'application de la technique de pontage sur la peau entraîne des modifications du débit et de la vitesse d'impression. Ces derniers tentent d'ajuster la vitesse à laquelle le matériau est versé par la buse, mais cela a tendance à être difficile à modifier. Par conséquent, il y aura une surextrusion dans certaines parties de l'impression et une sous-extrusion dans d'autres, car le débit tente de s'ajuster de lui-même. Ainsi, le réglage du débit pour un très petit morceau de surplomb réduira très probablement la qualité d'impression au lieu de l'améliorer.

En augmentant ce réglage, la technique de pontage sera appliquée à des parties plus petites du surplomb, où le pontage est moins efficace mais où le débit est toujours interrompu. Si l'on réduit ce réglage, la technique de pontage ne sera appliquée que sur de très grandes surfaces en surplomb. Cela n'entraînera pas autant de changements de débit, mais peut réduire la qualité du surplomb pour les zones de surplomb plus petites.
