Mindest-Vorschub
====
Die Marlin-Firmware für 3D-Drucker, von der die meisten Drucker-Firmwares abgeleitet sind, hat eine Mindestgeschwindigkeit für alle ihre Bewegungen. Diese Einstellung gibt an, wie hoch diese Mindestgeschwindigkeit für die Firmware Ihres Druckers ist.

Die Mindestgeschwindigkeit ist eine Anpassung, um Fehler in der Firmware aufgrund von Divisionen durch Null zu vermeiden. Die Firmware muss die Zeitintervalle zwischen den Schritten berechnen, um ein Signal mit dem richtigen Timing an die Motoren zu senden. Wenn sich der Motor mit einer Geschwindigkeit von 0 bewegen muss (d. h. stillsteht), wäre dies ein unendliches Zeitintervall, das die Firmware nicht gut handhaben kann. Dies gilt jedoch nur, wenn sich keiner der Motoren des Druckers tatsächlich dreht. Bei der Bewegung in X-Richtung dreht sich z.B. der Motor der Y-Achse noch nicht, aber aufgrund der Feinheiten von Schrittmotoren gilt der Mindestvorschub hier nicht.

Cura verwendet diesen Mindestvorschub, um korrekte Zeitschätzungen zu erstellen. Er wird angewandt, wenn zu Beginn des Drucks oder nach einer Pause beschleunigt wird, und wenn am Ende eines Drucks oder vor einer Pause bis zum Stillstand abgebremst wird.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**