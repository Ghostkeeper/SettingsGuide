Normaldrehzahl des Lüfters bei Höhe
====
Die Lüfterdrehzahl beginnt zu Beginn des Drucks mit dem Wert der Einstellung [Anfängliche Lüfterdrehzahl](cool_fan_speed_0.md). Während der ersten Schichten des Drucks bis zum Erreichen der in dieser Einstellung angegebenen Höhe, wird die Lüfterdrehzahl allmählich auf die [Normaldrehzahl des Lüfters](cool_fan_speed_min.md) erhöht.

![Welche Lüfterdrehzahl wird wo verwendet](../../../articles/images/cool_fan_speed.svg)

Normalerweise wird die anfängliche Lüfterdrehzahl deutlich verringert, da die erste Schicht während des Drucks heiß bleiben muss. Wenn die erste Schicht abkühlt, beginnt sich das Material zu [verziehen](../troubleshooting/warping.md). Dadurch wird die erste Schicht von der Druckplatte abgezogen, was zum Scheitern des Drucks führt. Wenn die zweite Schicht jedoch zu schnell abkühlt, schrumpft sie immer noch und zieht durch Scherreibung die erste Schicht nach oben, wodurch sich der Druck ebenfalls verzieht. Der Zweck dieser Einstellung ist es, den Druck mehrerer Schichten mit einer niedrigeren Lüfterdrehzahl zu ermöglichen. Auf diese Weise kann das Verziehen verhindert werden, bis der Druck eine ausreichende Steifigkeit aufweist, um dem Verziehen zu widerstehen.

Eine einfache Verringerung der Geschwindigkeit des Lüfters während der ersten Schichten würde zu einer starken Änderung der Lüfterdrehzahl führen, die sich in der Oberflächenqualität des endgültigen Drucks bemerkbar machen würde. Dies führt zu Streifenbildung. Stattdessen wird die Lüfterdrehzahl allmählich in Richtung der normalen Lüfterdrehzahl verändert.

* Eine Erhöhung dieser Einstellung kann die [Druckplattenhaftung](../troubleshooting/bed_adhesion_problems.md) verbessern .
* Wenn Ihre Druckplatte auf eine hohe Temperatur erhitzt wird, müssen Sie diese Einstellung möglicherweise verringern, um das Entstehen vom [Elephant's foot](../troubleshooting/elephants_foot.md) oder Oozing zu vermeiden.