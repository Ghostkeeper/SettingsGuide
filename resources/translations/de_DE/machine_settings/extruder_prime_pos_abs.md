Extruder absolute Einzugsposition
====
Wenn der [Einzugstropfen](../platform_adhesion/prime_blob_enable.md) verwendet wird, kann die Position dieses Einzug-Verfahrens mit einer [X](../platform_adhesion/extruder_prime_pos_x.md) und [Y](../platform_adhesion/extruder_prime_pos_y.md) Position eingestellt werden. Diese Einstellung legt fest, ob es sich um die Position auf der Bauplatte oder um eine Position relativ zur aktuellen Druckerposition handelt.

Wenn diese Einstellung aktiviert ist, beziehen sich die X- und Y-Koordinaten auf eine bestimmte feste Position auf der Bauplatte. Der Extruder wird sich immer dorthin bewegen, um einen Einzugstropfen zu erzeugen.

Wenn diese Einstellung deaktiviert ist, beziehen sich die X- und Y-Koordinaten auf die Position, die die Düse zufällig hat, wenn sie zum ersten Mal auf diesen Extruder umschaltet. Für den ersten Extruder wäre das die Koordinate [0,0]. Für die anderen Extruder wäre dies ihre Startposition, wie sie in der Definitionsdatei des Extruders definiert ist. Diese Startposition kann auch relativ sein.

Es wird dringend empfohlen, eine absolute Startposition zu verwenden. Eine absolute Startposition ist garantiert frei von Kollisionen mit anderen Teilen des Drucks, da Sie keine Objekte an dieser Stelle auf der Bauplatte platzieren können. Eine relative Einzugsposition kann sich an jeder beliebigen Stelle der Bauplatte befinden, was dazu führen kann, dass Sie irgendwo auf der ersten Schicht beginnen. Die Verwendung einer relativen Einzugsposition könnte etwas Zeit sparen, aber das ist das Risiko nicht wert.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**