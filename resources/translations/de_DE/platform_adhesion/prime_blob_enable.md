Einzugstropfen aktivieren
====
Wenn diese Option aktiviert ist, gibt Cura einen Befehl zum Vorbereiten des Druckers aus, kurz bevor der Extruder zum ersten Mal benutzt wird. Der Drucker wird sich vorbereiten, indem er einen kleinen Klecks Material auf der Bauplatte erzeugt.

Das Vorbereiten dient dazu, dass das Material richtig fließt. Wenn der Einzugstropfen nicht aktiviert ist, wird der Drucker stattdessen während des Skirts oder Brims vorbereiten. Das ist der Hauptanwendungsfall für den Skirt, aber bei einem Brim wird dadurch die Haftkraft des Brims etwas verringert.

Die Auswirkung dieser Einstellung auf den G-Code ist, dass Cura den M280-Befehl an eine bestimmte Stelle setzt. **Dies funktioniert derzeit nur auf Ultimaker-Druckern seit dem Ultimaker 3**, da sie die einzigen sind, die den M280-Befehl implementiert haben. Bei anderen Druckern wird die Einstellung nicht sichtbar sein.