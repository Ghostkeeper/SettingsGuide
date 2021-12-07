Max. Detaillänge
====
Kleine Details des Drucks sind oft sehr maßkritisch. Diese Einstellung bewirkt, dass kleine Löcher im Druck langsamer gedruckt werden, um eine höhere Genauigkeit zu erreichen.

Wenn ein Loch im Druck einen geringeren Umfang hat als durch diese Einstellung angegeben, wird die Geschwindigkeit, mit der der Umfang dieses Lochs gedruckt wird, mit einem Faktor der [Detailgeschwindigkeit](small_feature_speed_factor.md) multipliziert,(normalerweise reduziert). Diese Einstellung ist eine andere Art der Annäherung an die Einstellung [Max. Lochdurchmesser](small_hole_max_size.md), die allgemeiner als nur für kreisförmige Löcher ist.

Ein häufiger Anwendungsfall für diese Funktion ist das Drucken von Schraubenlöchern mit sehr genauen Abmessungen. Beim Drucken von kleinen Löchern neigt der Tropfen dazu, zusammen mit der Düse in die Ecke gezogen zu werden. Wenn die Ecke sehr scharf ist, wie es bei kleinen Löchern der Fall ist, hat dies den Effekt, dass das Loch kleiner wird. Wenn man langsamer druckt, verringert sich dieser Zug, weil das Material mehr Zeit hat, sich zu setzen, weil der mechanische Zug einfach geringer ist.

Eine Erhöhung dieser Einstellung führt dazu, dass mehr Konturen als "kleines Feature" markiert werden. Ein größerer Teil der Löcher im Druck wird langsamer gedruckt. Dies führt dazu, dass diese Löcher genauer gedruckt werden, erhöht aber die Druckzeit.