G-Code-Variante
====
Obwohl G-Code ein standardisiertes Format für die Übermittlung von Anweisungen an CNC-Maschinen wie 3D-Drucker ist, gibt es immer noch einige Unterschiede darin, welche G-Codes von den einzelnen Druckern unterstützt werden, wie ihr Ausgangszustand ist und manchmal auch darin, wie sie die Befehle interpretieren. Mit der G-Code-Variante können Sie weitgehend angeben, welchen Satz von Befehlen Ihr Drucker akzeptiert.

Der Unterschied zwischen den verschiedenen G-Code-Varianten ist im Allgemeinen recht gering. Die wichtigsten Befehle, wie die Bewegung und das Aufheizen der Düse, sind im Allgemeinen gleich.

Um die richtige G-Code Variante auszuwählen, lesen Sie die Dokumentation der Firmware Ihres Druckers. Dort sollten Sie erfahren, welche Funktionen unterstützt werden und welche nicht. Dies sind die verfügbaren Varianten in Cura und ihre Unterschiede.

Marlin
----
Marlin gilt als die Standard-G-Code-Variante. Er ist für die Hauptversion der [Marlin-Firmware](https://marlinfw.org/) gedacht, die die beliebteste 3D-Druck-Firmware ist und die Grundlage der meisten alternativen Firmwares da draußen bildet.

Marlin (Volumetrisch)
----
Dies ist eine Variante von Marlin, bei der die Extrusionsbefehle die Extrusionsmenge in Kubikmillimetern und nicht in Filamentlängen angeben werden. Dies sind die bemerkenswerten Änderungen:
* Der `E`-Parameter des `G1`-Befehls wird in Kubikmillimetern berechnet, dem Volumen des zugeführten Kunststoffs, anstatt der Länge des Filaments, das während dieser Bewegung zugeführt wird.
* In der Statistik am Anfang des G-Codes wird auch das verwendete Filament in Kubikmillimetern angegeben.

RepRap
----
Dies ist eine Variante, die sich auf den Support von Druckern konzentriert und aus dem [RepRap-Projekt](https://reprap.org/wiki/RepRap) hervorgegangen ist. Sie hat eine Reihe von bemerkenswerten Ausnahmen:
* Erwähnen Sie immer den Extruder, wenn Sie die Anfangstemperatur der Schicht einstellen, auch wenn es nur einen Extruder gibt.
* Kehren Sie nach dem Drucken zur relativen Extrusion zurück.
* Ändern Sie die Beschleunigung mit den Parametern `P` und `T` des Befehls `M204`, für die Druck- bzw. Fahrbeschleunigung, anstatt mit dem Parameter `S`.
* Ändern Sie den Ruck mit dem Befehl `M566`, anstatt mit dem Befehl `M205`.

Ultimaker 2
----
Diese G-Code-Variante ist für die Ultimaker 2-Familie gedacht. Die Firmware dieser Familie hatte die merkwürdige Idee, dass der Drucker die materialbezogenen Einstellungen steuern sollte und nicht der Slicer. Dies sind die Ausnahmen:
* Es wird keine Befehle für die Drucktemperatur im G-Code geben.
* Es wird keine Befehle für die Temperatur der Bauplatte im G-Code geben.
* Im G-Code wird es keine Befehle für die Temperatur des Bauvolumens geben.
* Es wird angenommen, dass ersten Düse die [Drucktemperatur für die erste Schicht](../material/material_print_temperature_layer_0.md) hat, wenn der Druck beginnt.
* Es wird angenommen, dass die Bauplatte die [Temperatur der ersten Schicht](../material/material_bed_temperature_layer_0.md) hat, wenn der Druck beginnt.
* Der Parameter `E` des Befehls `G1` wird in Kubikmillimetern berechnet, dem Volumen des zugeführten Kunststoffs, und nicht der Länge des Filaments, das während dieser Bewegung zugeführt wird.
* In der Statistik am Anfang des G-Codes wird das verwendete Filament in Kubikmillimetern angegeben.


Griffin
----
Dies ist die G-Code-Variante für moderne Ultimaker-Drucker, den Ultimaker 3 und neuere Modelle. Diese Drucker erfordern eine Reihe von Metadaten in einem bestimmten Format am Anfang des G-Codes. Die Unterschiede in dieser G-Code Variante sind:
* Am Anfang des G-Codes befindet sich eine große Kopfzeile, die Metadaten wie die Dauer des Drucks, den Namen des Druckauftrags und einige praktische Informationen wie die Starttemperatur und den Begrenzungsrahmen des Drucks enthält.
* Im G-Code sind keine Befehle für die Temperatur des Bauvolumens enthalten.
* Bei der ersten Düse wird davon ausgegangen, dass sie zu Beginn des Druckvorgangs die [Drucktemperatur der ersten Schicht](../material/material_print_temperature_layer_0.md) hat.
* Es wird davon ausgegangen, dass die Bauplatte die [Temperatur der ersten Schicht der Bauplatte](../material/material_bed_temperature_layer_0.md) hat, wenn der Druck beginnt.
* Es wird nicht davon ausgegangen, dass der Drucker mit dem ersten Extruder startet, so dass er zu Beginn des Druckvorgangs mit einem `T`-Befehl immer zum Startextruder wechselt.
* Für jeden Extruder wird beim ersten Druckstart ein Einzugstropfen mit `G280` gedruckt, anstatt eines Einzugs.

Makerbot
----
Dies ist eine G-Code-Variante, die für [Sailfish](https://www.sailfishfirmware.com/) basierte Firmware gedacht ist. Diese Firmware wird in Nachfolgern der ursprünglichen Makerbot-Drucker verwendet. Einige bemerkenswerte Unterschiede sind:
* Beim Ändern der Drucktemperatur wird `M109` (Temperatur einstellen und warten) nicht unterstützt. Es wird stattdessen `M104` ausgegeben, welcher nicht wartet, bis die Temperatur erreicht ist. Es verwendet dann `M116`, um dem Drucker zu befehlen, zu warten, bis diese Temperatur erreicht ist.
* Die `E`-Abmessung des `G1`-Extrusionsbefehls wird während des Drucks nicht zurückgesetzt. Bei anderen Varianten wird dieser Parameter nach jeweils 10 Metern Filament mit einem `G92 E0`-Befehl zurückgesetzt, um Fließkomma-Rundungsfehler in der Firmware zu vermeiden, aber nicht bei dieser Variante.
* Das Umschalten der Extruder erfolgt mit dem Befehl `M135`" und nicht mit den `T`-Befehlen.
* Die Drehzahl des Lüfters wird nicht ausgegeben. Der Lüfter ist entweder komplett ein- oder ausgeschaltet. Cura befiehlt dem Drucker, den Lüfter einzuschalten, wenn er sonst eine Lüftergeschwindigkeit von 50% oder mehr wünscht.

Bits von Bytes
----
Dies ist eine G-Code-Variante für die Bits from Bytes-Drucker, die über eine eigene Firmware verfügen. Deren G-Code-Variante unterscheidet sich erheblich von anderen. Die folgenden Änderungen werden von Cura vorgenommen:
* Extrusionsmengen werden mit der Drehzahl der Zuführung geschrieben und nicht mit dem Parameter `E`.
* Einzüge werden mit `M101` oder `M201`" geschrieben, je nach aktivem Extruder.
* Die Einzugsgeschwindigkeit wird mit einem separaten Befehl `M108` angegeben.
* Fahrbewegungen werden mit einem `M103`-Befehl angegeben, anstatt `G1` für `G0` auszuschalten. Es werden keine `G0`-Befehle gegeben.
* Der Drucker ist so eingestellt, dass er den automatischen Rückzug mit dem Befehl `M227` verwendet.
* Cura wird Zeilenumbrüche im Windows-Stil mit vorangestelltem Wagenrücklauf ausgeben, anstatt nur ein Zeilenumbruchssymbol.
* Die `E`-Abmessung des `G1`-Extrusionsbefehls wird während des Drucks nicht zurückgesetzt. Bei anderen Flavours wird dieser Parameter nach jeweils 10 Metern Filament mit einem `G92 E0`-Befehl zurückgesetzt, um Fließkomma-Rundungsfehler in der Firmware zu vermeiden, aber nicht bei diesem.

Mach3
----
Dies ist eine G-Code-Variante, die näher an der Art und Weise bleibt, wie CNC-Fräsen den G-Code erwarten. Es gibt nur einen bemerkenswerten Unterschied:
* Die Extrusionsmengen werden mit dem Parameter `A` des Befehls `G1` und nicht mit dem Parameter `E` geschrieben.

Repetier
----
Dies ist eine G-Code-Variante für die 3D-Drucker von Repetier. Sie ahmt die Ausgabe des Repetier-Slicers nach. Dies sind die bemerkenswerten Unterschiede bei dieser G-Code-Variante:
* Wenn Firmware-Einzüge aktiviert sind, verwenden die Einzüge für einen Extruderschalter `G10 S1`, um anzuzeigen, dass es sich um einen Einzug für einen Extruderschalter handelt.
* Beschleunigungsänderungen werden mit den Befehlen `M201` und `M202` (zum Drucken der Beschleunigung bzw. der Verfahrbeschleunigung) und nicht mit `M204` vorgenommen.
* Ruckänderungen werden mit dem Befehl `M207` und nicht mit dem Befehl `M205` vorgenommen.

**Da es sich hierbei um eine Geräteeinstellung handelt, wird sie normalerweise nicht in der normalen Liste der Einstellungen aufgeführt. Es gibt jedoch ein Auswahlmenü für diese Einstellung im Dialog "Druckereinstellungen", der in der Liste der hinzugefügten Drucker im Einstellungsdialog zu finden ist.**