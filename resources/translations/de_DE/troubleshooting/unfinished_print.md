Unvollendeter Druck
====
Manchmal wird ein Druck nicht vollständig beendet. Dafür kann es eine Reihe von Gründen geben, und einige davon lassen sich durch Anpassung der Einstellungen von Cura beheben.

![Das Filament hat nach der Hälfte des Druckvorgangs aufgehört zu fließen.](../../../articles/images/unfinished_print.jpg)

Drucker-Fehler
----
Manchmal ist die Ursache für einen unvollendeten Druck ein Druckerfehler, bei dem der Drucker nicht das tut, was er tun soll. In der Regel kann Cura nur sehr wenig gegen diese Probleme tun. Hier sind einige häufige Ursachen.
* Stromausfall. Es gibt sehr wenig, was Cura dagegen tun kann, außer schneller zu drucken, um die Wahrscheinlichkeit eines Stromausfalls während des Drucks zu verringern.
* Ausfall der Stromversorgung. Wenn eine der Temperaturen (entweder der [Bauplatte](../material/material_bed_temperature.md) oder der [Düse](../material/material_print_temperature.md)) zu hoch ist, haben einige Drucker einen Fehlermodus, wenn die Stromversorgung überhitzt oder die Temperatursensoren Fehler ausgeben. Dies führt dazu, dass sich der Drucker abschaltet und den Druck nicht beendet.
* Firmware friert ein. Aufgrund von Fehlern in der Firmware kann es vorkommen, dass der Drucker nicht mehr reagiert. Wenn Sie nachvollziehen können, an welcher Stelle im g-Code der Drucker einfriert (meistens am Anfang oder am Ende des Druckvorgangs), können Sie vielleicht herausfinden, welcher g-Code die Ursache ist. Vielleicht muss der Start-G-Code oder der End-G-Code angepasst werden.
* Die Filamentspule hat sich verheddert. Es ist eine gute Idee, das Ende des Filaments *immer* festzuhalten, wenn es nicht sicher in der Zuführung oder in einem der Löcher in der Spule steckt (falls Ihre Spule solche Löcher hat). Wenn Sie loslassen und das Ende des Filaments zurück auf die Rolle springt, könnte es unter eine der anderen Wicklungen rutschen und sich verheddern. Da der Faden in der Regel Hunderte von Metern lang ist, lässt sich dieser Knoten nur sehr schwer wieder lösen, wenn er sich verheddert hat.

Schleifen von Filamenten
----
Der Feeder drückt manchmal sehr stark auf das Filament, um es durch den Extruderstrang zu schieben. Dadurch wird das Filament beschädigt. Wenn die Zuführung sehr oft auf dasselbe Stück Filament drückt und zieht, kann es so stark beschädigt werden, dass die Zuführung das Filament nicht mehr greifen kann. Das Material hört dann auf zu fließen, und der Rest des Drucks wird mit Luft und nicht mit Kunststoff gedruckt.

![Das Filament wurde von der Zuführung ausgeschliffen](../../../articles/images/grinding.jpg)

Sie können dies während des Drucks feststellen, indem Sie einen Finger auf die Öffnung legen, durch die das Filament in die Zuführung gelangt. Während des Drucks sollten Sie spüren, wie sich der Finger bewegt. Wenn es sich nicht bewegt, hat es das Material höchstwahrscheinlich zermahlen und bekommt keinen Halt darauf. Sie können das Filament auch aus dem Drucker ziehen und sehen, wo es beschädigt ist.

Um dieses Problem zu vermeiden, können Sie die folgenden Anpassungen in den Einstellungen von Cura vornehmen:
* Verringern Sie die [Maximale Anzahl von Einzügen](../travel/retraction_count_max.md) oder erhöhen Sie das [Fenster „Minimaler Extrusionsabstand“](../travel/retraction_extrusion_window.md). Dadurch wird die Anzahl der Einzüge, die während der Extrusion einer bestimmten Filamentlänge durchgeführt werden, begrenzt. Dadurch wird begrenzt, wie oft der Feeder über jedes Stück Filament hin und her rollen kann.
* Verringern Sie den [Einzugsabstand](../travel/retraction_amount.md). Auch hierdurch wird die Anzahl der Vorwärts- und Rückwärtsbewegungen der Zuführung über dasselbe Stück Filament begrenzt.
* Reduzieren Sie die [inzugsgeschwindigkeit](../travel/retraction_speed.md). Wenn sich das Material schnell bewegt, aber irgendwo auf dem Weg behindert wird, schleift die Zuführung das Material. Wenn sich das Material langsamer bewegt, ist die Wahrscheinlichkeit, dass dies geschieht, geringer.
* Drucken Sie langsamer, indem Sie die [Schichthöhe](../resolution/layer_height.md), die [Linienbreite](../resolution/line_width.md) oder die [Geschwindigkeiten](../speed/speed_print.md) verringern. Dadurch wird die Kraft, die die Zuführung auf das Filament ausüben muss, verringert, wodurch die Gefahr des Schleifens reduziert wird.