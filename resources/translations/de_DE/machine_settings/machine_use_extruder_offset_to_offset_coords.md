Versatz mit Extruder
====
Diese Einstellung entscheidet, ob Cura Koordinaten für den Druckkopf oder für die Düse schreiben, zu denen er sich bewegen soll.

Wenn Ihr Drucker nur eine einzige Düse hat, ist das Koordinatensystem Ihres Druckers höchstwahrscheinlich auf die Düse ausgerichtet. Das bedeutet, dass das Anfahren der Position [50,50] die Düsenspitze tatsächlich an diese Position verschiebt. Wenn Ihr Drucker jedoch mehrere Düsen hat und diese Düsen im Druckkopf nebeneinander liegen, spielt dies eine Rolle.

Bei einigen Druckern wird der Druckkopf an dieselbe Stelle bewegt, unabhängig davon, welche Düse gerade aktiviert ist. Während der G-Code dem Drucker befehlen könnte, die Position [50,50] anzufahren, könnte die Spitze der gerade aktiven Düse stattdessen an die Position [68,50] bewegt werden, da sie sich beispielsweise 18 mm rechts von der ersten Düse befindet. Ist dies der Fall, sollte diese Einstellung aktiviert werden.

Andere Drucker stellen die Position des Druckkopfs automatisch so ein, dass die aktive Düse an die im G-Code angegebene Position verschoben wird. Das heißt, wenn der G-Code dem Drucker befiehlt, sich zur Position [50,50] zu bewegen, würde sich der derzeit aktive Extruder zu dieser Position bewegen. Der Druckkopf selbst würde sich ein wenig zur Seite bewegen, um den aktiven Extruder dort zu positionieren. Wenn sich Ihr Drucker auf diese Weise verhält, sollte diese Einstellung deaktiviert werden.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**