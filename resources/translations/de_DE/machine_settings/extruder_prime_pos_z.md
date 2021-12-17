Z-Position Extruder-Einzug
====
Wenn der [Einzugstropfen](../platform_adhesion/prime_blob_enable.md) aktiviert ist, gibt diese Einstellung die Z-Koordinate an, an der die Bewegung des Einzugstropfens beginnt. Cura wird sich zu dieser Position bewegen, bevor der Einzugstropfen ausgeführt wird.

Anders als die X- und Y-Koordinate ist dies eine Maschineneinstellung. Der Grund dafür ist, dass man davon ausgeht, dass der Vorgang eine feste Z-Koordinate hat. Um einen Einzugstropfen zu erzeugen, muss sich die Düse zur Bauplatte bewegen und sich vielleicht ein wenig auf und ab bewegen. [X](../platform_adhesion/extruder_prime_pos_x.md) und [Y](../platform_adhesion/extruder_prime_pos_y.md)  können mit den normalen Einstellungen gewählt werden, um die Position des Einzugstropfen zu verschieben, falls der Platz auf der Bauplatte begrenzt ist, die Z-Koordinate jedoch nicht.

Das Einzige, was sich dadurch ändert, ist die Z-Koordinate, zu der Cura die Düse bewegt, bevor der Einzugstropfen-Befehl ausgeführt wird.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**