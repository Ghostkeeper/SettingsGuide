Temperaturprüfung der Druckplatte einfügen
====
Diese Einstellung teilt dem Slicing-Back-End mit, ob es vor dem Start-G-Code Befehle für die Temperatur der Bauplatte zu Beginn des Drucks schreiben soll oder nicht. Sie wird automatisch beim Start eines Slice gesetzt.

Für die meisten Operationen während des [Start G-Code](machine_start_gcode.md) ist es sinnvoll, die Bauplatte auf die richtige Temperatur zum Drucken zu bringen. Um es den Entwicklern von Druckerdefinitionen einfacher zu machen, heizt Cura die Bauplatte automatisch auf, bevor der Start-G-Code ausgeführt wird. Enthält der Start-G-Code jedoch einen Verweis auf die Temperatur der Bauplatte, wird die Bauplatte nicht mehr automatisch aufgeheizt.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar. Sie zu ändern hat auch keine Auswirkungen, da sie von Cura automatisch geändert wird.**