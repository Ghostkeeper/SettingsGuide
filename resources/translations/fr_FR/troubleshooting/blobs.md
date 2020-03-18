Les gouttes (Blobs)
====
Les blobs sont de petites gouttes sur le côté du modèle. Parfois, ce ne sont que des points. Parfois, ce sont des rayures. Ils constituent un défaut de surface visuel et peuvent augmenter la friction entre les surfaces qui doivent glisser les unes sur les autres dans un mécanisme.

![Quelques gouttes sur cette surface](../../../articles/images/blobs.jpg)

Il y a plusieurs causes possibles pour les blobs. C'est l'un des défauts les plus courants dans l'impression 3D. Cet article énumère quelques causes possibles et leurs solutions.

La buse ralentit
----
Si la buse se déplace plus lentement dans un certain parcours que dans d'autres, elle y déposera alors plus de matière. Cette matière s'écoule vers l'extérieur de la surface de la paroi, en formant une goutte.

L'alimentation en matière est probablement destinée à être réduite avec elle. Cependant, même si l'extrudeur se déplace plus lentement, il peut s'écouler quelques secondes avant que le débit sortant de l'ouverture de la buse ne soit réduit en conséquence. Pendant ce temps, une trop grande quantité de matière sera extrudée, ce qui donne ces gouttes.

Pour lutter contre ce phénomène, regardez les réglages suivants :
* Égaliser la vitesse de la [paroi extérieure](../speed/speed_wall_0.md) de manière à ce qu'elle soit identique à celle de ce qui est imprimé avant elle (comme les [parois intérieures](../speed/speed_wall_x.md) ou le [remplissage](../speed/speed_infill.md)). Il n'y aura donc pas de ralentissement.
* Augmenter le [taux de secousse pour la paroi extérieure](../speed/jerk_wall_0.md). Cela empêchera la buse de ralentir dans les coins.
* Vous pouvez réduire la [résolution](../meshfix/meshfix_maximum_resolution.md) et augmenter la [déviation](../meshfix/meshfix_maximum_deviation.md) pour empêcher le contrôleur de ralentir la buse afin de suivre les Codes G qu'il doit traiter.
* Désactivez le paramètre [Compenser les chevauchements des parois extérieures](../shell/travel_compensate_overlapping_walls_0_enabled.md). Ce paramètre permet de créer de nouvelles commandes de déplacement avec des vitesses d'avance différentes. La désactivation de cette fonction réduit le nombre d'ordres de déplacement dans le mur.

La buse s'arrête
----
Si la buse fait de petites pauses pendant l'impression de la paroi extérieure, il est fort probable qu'elle attende que le processeur de votre imprimante 3D traite de nouvelles commandes de mouvement. Le logiciel de planification des mouvements de l'imprimante conserve généralement une mémoire tampon avec des commandes prétraitées prêtes pour de telles occasions, lorsque les commandes de mouvement ont déjà été traitées afin que l'imprimante connaisse précisément les délais d'activation des moteurs pas à pas ou d'autres mouvements. Si cette mémoire tampon s'épuise, on parle de "buffer underrun". Cela provoque l'apparition de taches à la surface.

Pour éviter cela, vous devez réduire la résolution du code g.
* Augmentez le paramètre [Maximum Resolution](../meshfix/meshfix_maximum_resolution.md), ce qui permet à Cura de produire des segments de ligne plus longs.
* Augmenter le paramètre [Maximum Deviation](../meshfix/meshfix_maximum_deviation.md), ce qui permet à Cura de réduire davantage la résolution en s'écartant davantage du chemin d'origine.
* Désactivez le paramètre [Compenser les chevauchements des murs extérieurs](../shell/travel_compensate_overlapping_walls_0_enabled.md). Si le mur extérieur se chevauche avec d'autres murs extérieurs, cela donnerait à une partie du mur une largeur de ligne différente, mais cela nécessite une commande de mouvement supplémentaire. Pour réduire les commandes de mouvement, vous pouvez désactiver ce paramètre. Cependant, cela peut également entraîner une surextrusion dans ces murs, ce qui provoque également des boursouflures.
* Réduisez la [vitesse d'impression du mur extérieur](../speed/speed_wall_0.md). Cela réduit la vitesse d'exécution des commandes de déplacement, ce qui permet au CPU de rattraper le retard.

Le déplacement se fait à travers les murs
----
Bien que Cura évite généralement de traverser le mur extérieur autant que possible, cela est parfois inévitable. Si la buse transporte une matière suintante alors qu'elle traverse une paroi extérieure, cette matière peut être essuyée à cet endroit, laissant une tache.

Il est possible d'éviter cette cause de bavure en réglant les paramètres suivants :
* Assurez-vous que la fonction [peignage](../travel/retraction_combing.md) est activée. Cela permet à la buse de contourner les murs autant que possible, au lieu de les traverser.
* Activer [Z Hops](../travel/retraction_hop_enabled.md). Si les murs sont franchis, la buse se déplacera un peu vers le haut, pour passer par-dessus les murs au lieu de les traverser. Le matériau suintant ne sera probablement pas essuyé sur la paroi, mais à l'endroit où la buse atterrit après le déplacement. Cura essaiera toujours de se poser dans le remblai ou la peau si possible.
* Assurez-vous que [l'ordre d'impression des murs est optimisé](../shell/optimize_wall_printing_order.md). Cela réduit le nombre de mouvements effectués lors de l'impression des murs, ce qui permet des mouvements plus efficaces et réduit le risque que certains de ces mouvements doivent passer à travers un mur extérieur.

Une pression accrue
----
Si la buse est sur-extrudée, l'extrusion peut devenir irrégulière. Celle-ci peut parfois trouver soudainement une issue lorsqu'un coin particulier de votre empreinte est imprimé (en particulier au niveau des débords). Parfois, cette pression refoulée explose, laissant une grosse tache. En général, une bande de pression progressivement décroissante se forme après la goutte.

Pour réduire cet effet, voici quelques paramètres à prendre en compte :
* Réduire la [largeur de la ligne du mur](../resolution/wall_line_width.md). Cela réduit la pression dans la chambre de la buse en général.
* Réduire la [largeur de la paroi extérieure](../shell/wall_0_inset.md). Ce réglage fait que la paroi extérieure chevauche la paroi intérieure adjacente, de sorte que la paroi est poussée plus fortement sur la paroi intérieure, ce qui améliore la résistance. Cependant, cette poussée augmente également la pression à l'intérieur de la chambre de la buse.

Filament humide
----
Si le filament a accumulé de l'humidité alors qu'il était encore sur la bobine, cette eau sera chauffée dans la buse au-delà de son point d'ébullition. La vapeur d'eau explosera hors de la buse lorsqu'elle en sera expulsée. Cette petite explosion peut faire éclater du plastique, ce qui se traduit par une petite tache à la surface.

Coutures
----
Un joint sera créé à l'endroit où le périmètre de la paroi extérieure est démarré et fermé. Ce n'est pas ce que les gens appellent normalement une goutte, bien qu'elle ait un aspect similaire. Voir l'article sur les [coutures](seam.md) pour savoir comment réduire cet effet.

Si le paramètre [Alignement de la jointure en Z](../shell/z_seam_type.md) est réglé sur "Aléatoire", la couture sera répartie autour du modèle, créant ainsi de petites coutures partout. Cela peut ressembler exactement à un blob, même si c'est en fait une couture. Modifiez le paramètre [Alignement de la jointure en Z](../shell/z_seam_type.md) pour masquer ces coutures.
