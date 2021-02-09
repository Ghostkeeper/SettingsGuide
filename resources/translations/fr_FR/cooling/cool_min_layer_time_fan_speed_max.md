Limite de vitesse régulière/maximale du ventilateur
====
Ce paramètre détermine le temps d'impression de la couche à laquelle il est si court que la vitesse du ventilateur commence à augmenter pour atteindre la [vitesse maximale du ventilateur](cool_fan_speed_max.md). Les couches qui prennent plus de temps à imprimer utiliseront la [vitesse normale du ventilateur](cool_fan_speed_min.md). Pour les couches dont le temps d'impression est plus court, la vitesse du ventilateur sera interpolée entre les paramètres de vitesse normale et de vitesse maximale du ventilateur, jusqu'à la [durée minimale de la couche](cool_min_layer_time.md) où la vitesse du ventilateur sera à la vitesse maximale du ventilateur.

![Quelle vitesse de ventilateur est utilisée](../images/cool_fan_speed_fr.svg)

En effet, en réduisant ce seuil (vers des couches plus courtes), le ventilateur tournera plus souvent à la vitesse normale. En augmentant ce seuil, le ventilateur tournera plus souvent à une vitesse plus élevée, même si les couches ne sont pas très petites.

Il est bon de garder une certaine distance entre le temps minimum de la couche et ce seuil de vitesse régulière/maximum du ventilateur. Si le seuil est réglé sur le temps de couche minimum, le ventilateur s'arrêtera brusquement si les couches deviennent légèrement en dessous du seuil. Cela entraîne la formation de bandes visibles sur la surface de l'impression, car il y a une bordure dure où le ventilateur s'est soudainement mis en marche. Si, au contraire, il y a une différence entre les deux réglages, le changement de vitesse du ventilateur sera plus progressif et les bandes ne seront pas visibles sur l'impression.
