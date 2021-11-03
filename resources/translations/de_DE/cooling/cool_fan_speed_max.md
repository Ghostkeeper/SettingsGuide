Maximaldrehzahl des Lüfters
====
Die Geschwindigkeit, mit der sich die Lüfter im Druckkopf drehen, wenn die Schicht bei minimaler Schichtzeit gedruckt wird. Bei der minimalen Schichtzeit wollen Sie die Schicht so schnell wie möglich abkühlen, um die Zeit zu verkürzen, die die Schicht braucht, um abzukühlen, bevor der Drucker die nächste Schicht auflegt.

![Welche Lüfterdrehzahl wird wo verwendet](../../../articles/images/cool_fan_speed.svg)

Wenn der Druck einer Schicht zwischen dem [Grenzwert für Normaldrehzahl/Maximaldrehzahl des Lüfters](cool_min_layer_time_fan_speed_max.md) und der [Mindestzeit für Schicht](cool_min_layer_time.md) liegt, wird die Lüfterdrehzahl zwischen der [Normaldrehzahl des Lüfters](cool_fan_speed_min.md) und der [Maximaldrehzahl des Lüfters](cool_fan_speed_max.md) interpoliert. Sobald die minimale Schichtzeit erreicht ist, wird auch die maximale Lüfterdrehzahl erreicht. Auf diese Weise wird der Druck maximal gekühlt, um ihn so schnell wie möglich abzukühlen, bevor die nächste Schicht aufgetragen wird.