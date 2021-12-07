Max. Lochdurchmesser
====
Kleine Details des Drucks sind oft sehr maßkritisch. Diese Einstellung bewirkt, dass kleine Löcher im Druck langsamer gedruckt werden, um eine höhere Genauigkeit zu erreichen.

Wenn ein kreisförmiges Loch einen Durchmesser hat, der unter dem Wert dieser Einstellung liegt, wird die Geschwindigkeit, mit der der Umfang dieses Lochs gedruckt wird, mit einem Faktor der [Detailgeschwindigkeit](small_feature_speed_factor.md) multipliziert (normalerweise reduziert). Für Löcher, die nicht kreisförmig sind, werden sie mit einer anderen Geschwindigkeit gedruckt, wenn der Umfang kleiner als ein Kreis mit dem hier angegebenen Durchmesser ist. Siehe auch [Max. Detaillänge](small_feature_max_length.md); dies ist die Einstellung, die tatsächlich für das Slicing verwendet wird.

Ein häufiger Anwendungsfall für diese Funktion ist das Drucken von Schraubenlöchern mit sehr genauen Abmessungen. Beim Drucken kleiner Löcher neigt die Wulst dazu, zusammen mit der Düse in die Ecke gezogen zu werden. Wenn die Ecke sehr scharf ist, wie bei kleinen Löchern, hat dies den Effekt, dass das Loch kleiner wird. Wenn man langsamer druckt, verringert sich dieser Zug, weil das Material mehr Zeit hat, sich zu setzen und weil der mechanische Zug einfach geringer ist.

Eine Erhöhung dieser Einstellung führt dazu, dass mehr Konturen als "kleines Feature" markiert werden. Ein größerer Teil der Löcher im Druck wird langsamer gedruckt. Dies führt dazu, dass diese Löcher genauer gedruckt werden, erhöht aber die Druckzeit.