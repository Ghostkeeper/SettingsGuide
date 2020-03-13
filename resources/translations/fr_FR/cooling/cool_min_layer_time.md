Le temps minimum de couche configure la durée la plus courte autorisée pour l'impression d'une couche. L'imprimante n'est pas autorisée à imprimer des couches plus rapidement que cela.

Ceci est nécessaire pour permettre à la couche précédente de refroidir avant que la couche suivante ne soit mise par-dessus. Cela permet de s'assurer que la couche précédente s'est complètement solidifiée, pour éviter qu'elle ne s'affaisse.

![Quelle vitesse de ventilation est utilisée où](../../../articles/images/cool_fan_speed.svg)

Ce cadre a trois effets :
* Si une couche s'imprime plus vite que ne l'indique le paramètre [Seuil de vitesse normale/maximale du ventilateur] (cool_min_layer_time_fan_speed_max.md), la vitesse du ventilateur sera augmentée pour atteindre la [Vitesse maximale du ventilateur] (cool_fan_speed_max.md). Lorsqu'une couche est si petite qu'il faut moins de temps pour l'imprimer, la vitesse maximale du ventilateur sera utilisée. La vitesse du ventilateur est interpolée entre les deux.
* Si la couche prend moins de temps que le temps minimum de couche pour s'imprimer, la vitesse d'impression sera ralentie de telle sorte qu'elle prendra toujours le temps minimum de couche.
* Si la tête d'impression est trop ralentie (impression plus lente que le paramètre [Vitesse Minimum](cool_min_speed.md)), la tête d'impression attendra à la fin d'une couche et soulèvera éventuellement un peu la tête.
