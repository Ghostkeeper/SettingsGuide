Accélération maximale du filament
====
Ce paramètre indique l'accélération maximale que les moteurs du chargeur de votre imprimante prennent en charge, selon le microprogramme de l'imprimante.

Ce paramètre n'est utilisé que pour obtenir des estimations de temps correctes. L'[accélération](../speed/acceleration_print.md) définie par Cura n'a pas de limite, mais Cura suppose que votre microprogramme fixe une certaine limite par axe. Si l'accélération du chargeur dépasse ce paramètre, l'estimation du temps de ces mouvements sera ajustée pour supposer que votre microprogramme limite l'accélération. L'accélération totale peut encore être plus importante lorsque l'on accélère en diagonale avec plusieurs axes en même temps.

Il est assez fréquent que les limites d'accélération du chargeur soient atteintes, puisque (selon le microprogramme) l'accélération définie par Cura affecte également le chargeur. Il est donc crucial que ce paramètre soit configuré correctement afin d'obtenir des estimations de temps correctes pour les rétractions.

*Comme il s'agit d'un réglage de la machine, ce réglage n'est normalement pas visible dans la liste des réglages.*
