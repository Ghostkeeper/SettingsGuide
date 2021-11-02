Spiralisieren der äußeren Konturen glätten
====
Wenn [Spiralisieren der äußeren Konturen](magic_spiralize.md) aktiviert ist, aktiviert bzw. deaktiviert diese Einstellung das charakteristischste Merkmal des Spiralisierungsmodus: Anstatt jede Schicht nacheinander in Höhenintervallen zu drucken, wird die Höhe im Verlauf der Schicht schrittweise erhöht.

Da der Spiralisierungsmodus bewirkt, dass bei den meisten Schichten nur die Wände mit einer einzigen Kontur gedruckt werden, nimmt diese einzige Kontur die Form einer Spirale an, was der Spiralisierungsfunktion ihren Namen gibt. Bei den ersten und letzten Schichten des Drucks wird die Durchflussrate schrittweise reduziert, um eine Überextrusion zu verhindern und die richtige Höhe zu erreichen.

Da die Düse während der gesamten Schicht allmählich auf die nächste Schichthöhe angehoben wird, gibt es an der Stelle, an der die Düse auf die nächste Schicht übergeht, keine Naht mehr. Dadurch wird die Z-Naht effektiv beseitigt.

Andererseits wird die Schicht um eine halbe Schichthöhe nach oben oder unten verschoben. Dies ist weniger genau. Es kann zu Unschärfen bei feinen Details im Druck kommen.

Diese Einstellung entfernt die Nähte nicht, wenn mehr als eine Kontur auf einer Ebene zu drucken ist. Das Extrudieren muss immer noch nach der Kontur unterbrochen werden, um zum nächsten gedruckten Teil zu gelangen. Dadurch bleibt trotzdem eine Naht zurück.

**Dieser Effekt ist in der Ebenenansicht aufgrund von Rendering-Einschränkungen nicht sichtbar.**