Normaldrehzahl des Lüfters bei Schicht
====
Die Lüfterdrehzahl beginnt zu Beginn des Druckvorgangs mit dem Wert der Einstellung [Anfängliche Lüfterdrehzahl](cool_fan_speed_0.md). Während der ersten Schichten des Drucks wird die Lüfterdrehzahl entsprechend dieser Einstellung schrittweise auf die [Normaldrehzahl des Lüfters](cool_fan_speed_min.md) erhöht.

![Welche Lüfterdrehzahl wird wo verwendet](../../../articles/images/cool_fan_speed.svg)

Normalerweise wird die anfängliche Lüfterdrehzahl deutlich verringert, da die erste Schicht während des Drucks heiß bleiben muss. Wenn die erste Schicht abkühlt, beginnt sich das Material zu [Warpen](../troubleshooting/warping.md). Dadurch wird die erste Schicht von der Druckplatte abgezogen, was zum Scheitern des Drucks führt. Wenn die zweite Schicht jedoch zu schnell abkühlt, schrumpft sie immer noch und zieht durch Scherreibung die erste Schicht nach oben, wodurch sich der Druck ebenfalls verzieht. Der Zweck dieser Einstellung ist es, den Druck mehrerer Schichten mit einer niedrigeren Lüfterdrehzahl zu ermöglichen. Auf diese Weise kann das Verziehen verhindert werden, bis der Druck eine ausreichende Steifigkeit aufweist, um dem Verziehen zu widerstehen.

* Eine Erhöhung dieser Einstellung kann die [Druckplattenhaftung](../troubleshooting/bed_adhesion_problems.md) verbessern.
* Wenn Ihre Druckplatte auf eine hohe Temperatur erhitzt wird, müssen Sie diese Einstellung möglicherweise verringern, um das Entstehen vom [Elephant's foot](../troubleshooting/elephants_foot.md) oder Oozing zu vermeiden.