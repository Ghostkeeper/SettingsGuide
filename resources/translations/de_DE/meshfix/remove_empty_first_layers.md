Leere erste Schichten entfernen
====
Wenn diese Funktion aktiviert ist, werden alle leeren Schichten an der Unterseite des Drucks entfernt. Der gesamte Druck wird nach unten verschoben, bis er auf der Bauplatte aufliegt. Anstelle von leeren Schichten, die den Druck zum Scheitern bringen, wird der Druck etwas niedriger sein.

Wenn in Cura die Einstellung "Setzte Modelle automatisch auf der Druckplatte ab" aktiviert ist, wird diese Einstellung wahrscheinlich kaum Auswirkungen haben. Sie kann aber trotzdem eine Rolle spielen. Beim automatischen Ablegen von Modellen auf der Bauplatte werden die Modelle genau an der Bauplatte ausgerichtet. Wenn die erste(n) Schicht(en) jedoch nur Elemente enthält/enthalten, die zu klein sind, um gedruckt zu werden (z. B. weil die Unterseite nicht ganz glatt ist), kann die erste Schicht im endgültigen Druck noch leer sein. Mit dieser Einstellung wird dies verhindert, indem die restlichen Schichten um eine Schicht nach unten verschoben werden.

Nach der Verschiebung des Drucks nach unten werden die Einstellungen, die für die erste Schicht gelten, weiterhin angewendet. Obwohl also die ursprüngliche erste Schicht entfernt wird, werden die [Drucktemperatur erste Schicht](../material/material_print_temperature_layer_0.md) und ähnliche Einstellungen weiterhin auf die neue erste Schicht angewendet.

Normalerweise sollte diese Einstellung immer aktiviert sein, um zu verhindern, dass Drucke fehlschlagen, weil die Unterseite nicht ganz glatt ist oder nicht richtig an der Bauplatte ausgerichtet ist. Sie können diese Einstellung jedoch auch deaktivieren, wenn Sie einen Druckauftrag mit mehreren Stufen durchführen, der in der Luft beginnen muss.

Wenn [Stützstrukturen generieren aktiviert ist](../support/support_enable.md), reicht die Unterstützung bis zur Bauplatte, so dass die ersten Schichten nicht mehr leer sind. Es werden keine Schichten entfernt und der Druck bewegt sich nicht nach unten.

Wenn die Einstellung [Slicing-Toleranz](../experimental/slicing_tolerance.md) auf "Exklusiv" gesetzt ist, wird die erste Schicht immer leer sein. Wenn diese Einstellung nicht aktiviert ist, ist die erste Schicht leer, und der Druck schlägt höchstwahrscheinlich fehl.