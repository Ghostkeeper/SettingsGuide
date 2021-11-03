Mindestzeit für Schicht
====
Mit der Mindestzeit für die Schicht wird die kürzeste zulässige Druckdauer für eine Schicht festgelegt. Der Drucker darf keine schnelleren Schichten drucken als diese.

Dies ist notwendig, damit die vorherige Schicht abkühlen kann, bevor die nächste Schicht darauf gelegt wird. Dadurch wird sichergestellt, dass die vorherige Schicht vollständig ausgehärtet ist, um ein Absacken zu verhindern.

![Welche Lüfterdrehzahl wird wo verwendet](../../../articles/images/cool_fan_speed.svg)

Diese Einstellung hat drei Auswirkungen:
* Wenn eine Schicht schneller druckt, als es die Einstellung [Grenzwert für Normaldrehzahl/Maximaldrehzahl des Lüfters](cool_min_layer_time_fan_speed_max.md) angibt, wird die Lüfterdrehzahl in Richtung der [Maximaldrehzahl des Lüfters](cool_fan_speed_max.md) erhöht. Sobald eine Schicht so klein ist, dass sie die minimale Schichtzeit zum Drucken benötigt, wird die maximale Lüfterdrehzahl verwendet. Die Lüfterdrehzahl wird zwischen diesen beiden Werten interpoliert.
* Wenn die Schicht weniger als die Minimale Schichtzeit zum Drucken benötigt, wird die Druckgeschwindigkeit so verlangsamt, dass sie immer noch die Minimale Schichtzeit benötigt.
* Wenn der Druckkopf zu sehr verlangsamt würde (langsamer als die Einstellung [Mindestgeschwindigkeit](cool_min_speed.md)), dann wartet der Druckkopf am Ende einer Schicht und hebt optional den Druckkopf etwas an.

Es gibt einen Kompromiss, wenn die Düse verlangsamt wird, damit die Schicht besser abkühlen kann. Die Mindestschichtzeit soll dem Material etwas Zeit zum Abkühlen geben, indem die Bewegung des Druckkopfs verlangsamt wird. Während dieser Zeit blasen die Lüfter mit maximaler Leistung, um das Material schneller abzukühlen, aber die heiße Düse ist immer noch auf dem Kunststoff. Bei sehr kleinen Teilen kann die heiße Düse mehr Wärme in den Druck übertragen, als die Lüfter abblasen können. Dies führt dazu, dass der Kunststoff noch stärker schmilzt, als wenn Sie keine Mindestschichtzeit einhalten würden.

Wenn Sie relativ kalte Materialien drucken oder wenn die Lüfter am Druckkopf besonders stark sind, kann das Material eine höhere Mindestschichtzeit vertragen, um das Absacken zu verringern. Wenn die Mindestschichtzeit zu hoch eingestellt ist, verlangsamt sich die Düse immer häufiger, was an manchen Stellen ebenfalls zu Stellen zu Klümpchen und Durchhängen führt.