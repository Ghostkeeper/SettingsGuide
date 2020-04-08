Durée minimale température de veille
====
Ce réglage configure la durée minimale d'une mise en veille pendant laquelle il faudra refroidir la buse à la température de veille. Si la buse est réglée pour une durée plus courte, elle ne sera pas refroidie mais restera à la [Température d'impression finale](../material/material_final_print_temperature.md).

Votre buse est équipée d'un régulateur PID, qui régule la quantité de puissance utilisée pour chauffer votre buse afin d'atteindre les températures correctes. Lorsque la buse est commandée pour se refroidir et se réchauffer avec de grandes différences de température en succession rapide, le régulateur PID a tendance à mal prévoir la quantité de chaleur nécessaire. Cela entraîne de grandes fluctuations de la température réelle de la buse. Vous pouvez ainsi éviter qu'elle n'atteigne la [température d'attente] (../material/material_standby_temperature.md) si la buse est inactive pendant une très courte période.

La valeur optimale de ce réglage dépend du réglage de votre régulateur PID. Certains régulateurs gèrent mieux que d'autres les changements rapides de la température cible, et ceux-là peuvent mieux gérer une brève période de veille. Abaisser ce réglage permettrait alors d'éviter que la matière ne se dégrade à l'intérieur de la buse.

*Comme il s'agit d'un réglage de machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
