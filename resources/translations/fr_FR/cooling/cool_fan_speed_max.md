La vitesse à laquelle les ventilateurs de la tête d'impression tournent lorsque la couche est imprimée en un temps minimum.

![Quelle vitesse de ventilateur est utilisée où](../images/cool_fan_speed_fr.svg)

Si l'impression d'une couche se situe entre les paramètres [Limite de vitesse régulière/maximale du ventilateur
](./cool_min_layer_time_fan_speed_max.md) et [Durée minimale d’une couche](./cool_min_layer_time.md), la vitesse du ventilateur sera interpolée entre la [Vitesse normale du ventilateur](./cool_fan_speed_min.md) et la [Vitesse maximale du ventilateur](./cool_fan_speed_max.md). Une fois que le temps de couche minimum est atteint, la vitesse maximale du ventilateur sera également atteinte. De cette façon, l'impression sera refroidie au maximum afin de la refroidir le plus rapidement possible avant que la couche suivante ne soit mise sur le dessus.
