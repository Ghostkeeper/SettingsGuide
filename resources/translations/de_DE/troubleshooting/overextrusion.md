Überextrusion
====
Überextrusion ist ein Begriff, der verwendet wird, wenn der Drucker zu viel Material an einer Stelle extrudiert. Dadurch fließt das Material zu den Seiten oder nach oben, wodurch die Oberfläche sehr rau und unregelmäßig wird. Es kann auch zu [Stringing](stringing.md) und vielen [Blobs](blobs.md) führen.

![Bei diesem Druck kam es zu einer massiven Überextrusion](../../../articles/images/overextrusion.jpg)

Temperaturkontrolle
----
Die häufigste Ursache für Überextrusion ist zu heißes Drucken. Wenn die [Drucktemperatur](../material/material_print_temperature.md) zu hoch eingestellt ist, hat das Material eine niedrigere Viskosität, wodurch es unkontrolliert aus der Düse fließt. Das Ergebnis ist in der Regel eine Überextrusion in einigen Bereichen wie den Außenwänden, aber eine Unterextrusion in anderen Bereichen wie der Füllung.

Um dies zu beheben, müssen Sie die Temperatur schrittweise senken. Schauen Sie sich das Datenblatt des Materials, mit dem Sie drucken, genau an, um herauszufinden, welcher Temperaturbereich akzeptabel ist, und senken Sie die Drucktemperatur in Richtung des unteren Endes dieses Bereichs.

Durchmesser des Filaments
----
Es gibt mehrere Standards für den Durchmesser von Filamenten. Die gebräuchlichsten sind 1,75 mm und 2,85 mm, aber auch 3,00 mm sind noch im Umlauf. Abgesehen davon produzieren nicht alle Hersteller ihr Filament mit einem einheitlichen Durchmesser. Wenn Ihr Filament breiter ist als von Cura erwartet, werden Sie zu viel Material extrudieren, da Cura den Drucker anweist, eine bestimmte Länge an Filament zu extrudieren, die dann zu viel Volumen hat.

Um dies zu beheben, messen Sie zunächst den tatsächlichen Durchmesser des Filaments mit einem Messschieber. Am besten messen Sie diesen an mehreren Stellen, falls er variiert, und in verschiedenen Winkeln um den Umfang herum. Ermitteln Sie den Durchschnitt dieser Messungen. Dieser Durchschnittswert kann in Cura auf der Seite Materialverwaltung als Eigenschaft des Materials eingegeben werden. Wenn der Durchmesser nicht bearbeitet werden kann, weil es sich um ein vordefiniertes Material handelt, müssen Sie das Material möglicherweise zunächst duplizieren. Dann sollte es möglich sein, den Durchmesser zu bearbeiten.

Extruder-Kalibrierung
----
Manchmal liegt das Problem darin, dass die Hardware nicht mit den Erwartungen der Firmware übereinstimmt. Wenn der Extrudermotor ein Schrittmotor ist (was bei 3D-Druckern üblich ist), muss die Firmware wissen, wie viele Schritte des Motors zu einer bestimmten Strecke führen. Die Firmware hat dafür eine Einstellung, die die Genauigkeit des Vorschubs in Schritten pro Millimeter misst. Wenn diese Einstellung falsch konfiguriert ist, bewegt sich der Förderer möglicherweise zu schnell oder zu langsam. Am besten ist es, diese Einstellung in der Firmware vorzunehmen. Ist dies jedoch nicht möglich, kann der [Fluss](../material/material_flow.md) in Cura angepasst werden, um dies auszugleichen. Sie sollten dann auch den [Einzugsabstand](../travel/retraction_amount.md) und [Geschwindigkeiten](../travel/retraction_speed.md) anpassen.

Wandüberlappungen
----
Normalerweise zeichnet Cura nur die Konturen des Drucks mit einer bestimmten Linienbreite. Wenn die Wände an bestimmten Stellen Ihres Drucks dicht beieinander liegen, führt dies zu überlappenden Linien. Diese Linien werden dick und erzeugen Blobs, weil dort bis zu doppelt so viel Material wie nötig aufgetragen werden kann. Bei einer großen Überlappung wird die zweite Linie am Extrudieren gehindert, so dass der Druck in der Düsenkammer ansteigt, bis sie ausgestoßen wird und einen Blob erzeugt.

Dies kann verhindert werden, indem die [Wandüberlappungen ausgleichen] aktiviert wird (../shell/travel_compensate_overlapping_walls_enabled.md). Die Extrusion der zweiten Linie wird so reduziert, dass nur so viel Material extrudiert wird, wie nötig ist, um den verbleibenden Raum der Wand auszufüllen, was eine Überextrusion verhindert.

Wenn sich die Wände aufgrund der Einstellung [Einfügung Außenwand](../shell/wall_0_inset.md) überlappen, können Sie versuchen, diesen Parameter zu reduzieren, um eine Überlappung zu verhindern. Sie können auch versuchen, die [Außenwand zuerst](../shell/outer_inset_first.md) zu drucken. Das überschüssige Material wird dann in das Innere des Modells geschoben, wo es unsichtbar ist.

Durchflussmenge direkt einstellen
----
Wenn die Ursache für die Überextrusion nicht bekannt ist, können Sie auch direkt die [Flussrate] anpassen (../material/material_flow.md). Verringern Sie die Flussrate, bis Ihre Oberfläche wieder glatt erscheint. Dies kann einige unbekannte Faktoren direkt kompensieren.