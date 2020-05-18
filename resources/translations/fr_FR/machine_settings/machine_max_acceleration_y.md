Accélération maximale Y
====
Ce paramètre indique l'accélération maximale que le moteur et le châssis de votre imprimante peuvent supporter dans la direction Y, selon le microprogramme de l'imprimante.

Ce paramètre n'est utilisé que pour obtenir des estimations de temps correctes. La valeur de l'[accélération](../speed/acceleration_print.md) fixée par Cura n'a pas de limite, mais Cura suppose que votre microprogramme fixe une certaine limite par axe. Si l'accélération sur l'axe Y dépasse ce paramètre, l'estimation du temps de ces mouvements sera ajustée pour supposer que votre microprogramme limite l'accélération. L'accélération totale peut encore être plus importante lorsque l'on accélère en diagonale avec plusieurs axes en même temps.

*Comme il s'agit d'un réglage machine, ce réglage n'est normalement pas visible dans la liste des paramètres.*
