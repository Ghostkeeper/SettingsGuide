Brückenwandfluss
====
Diese Einstellung passt die Materialmenge an, die extrudiert wird, um überbrückende Wände zu drucken.

Durch die Reduzierung der Materialmenge wird die Linienbreite der Wände, die einen Spalt überbrücken, effektiv verringert. Bei verringerter Linienbreite ist das Verhältnis von Oberfläche zu Masse der Linien größer, so dass sie schneller abkühlen können und nicht so stark durchhängen.

Eine zu starke Verringerung der Fließgeschwindigkeit führt jedoch zu einer starken Veränderung der Fließgeschwindigkeit, insbesondere in Verbindung mit einer [langsameren Druckgeschwindigkeit](bridge_wall_speed.md). In der Realität kann das Material seine Fließgeschwindigkeit nicht sehr schnell ändern, was dazu führt, dass die Linien etwas dicker als beabsichtigt sind, wenn die Fließgeschwindigkeit verlangsamt wird, und etwas dünner als beabsichtigt, wenn die Fließgeschwindigkeit beschleunigt wird. Der erste dieser Effekte kann durch ein gewisses [coasting](bridge_wall_coast.md) kompensiert werden, was jedoch eine sorgfältige Feineinstellung erfordert.