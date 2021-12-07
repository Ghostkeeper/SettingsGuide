Schicht Verschiebung
====
Eine Schichtverschiebung tritt auf, wenn die Schichten eines Drucks nicht richtig übereinander gestapelt sind. Wenn der Druckkopf aus irgendeinem Grund während des Drucks einer Schicht verschoben wird, druckt der Drucker mit einem Versatz weiter. Infolgedessen wird die Oberseite des Drucks gegenüber der Unterseite verschoben.

![Eine Schichtverschiebung aufgrund eines Hindernisses](../../../articles/images/layer_shift_single.jpg)

Ursachen
----
Es gibt zwei Arten von Schichtverschiebungen.

Die eine Art der Schichtverschiebung wird dadurch verursacht, dass der Druckkopf irgendwo auf dem Weg behindert wird. Dadurch verschiebt sich die Schicht an einer Stelle in der Mitte des Druckvorgangs. Dies kann passieren, wenn der Benutzer während des Drucks etwas in das Druckportal stellt oder wenn der Druckkopf beim Drucken im [Modus Druckreihenfolge Nacheinander](../blackmagic/print_sequence.md) auf ein anderes Objekt trifft. Wenn der Druckkopf mit etwas kollidiert und sich nicht bewegen kann, überspringen die Motoren einige Schritte. Wenn der Drucker nicht in der Lage ist, dies zu erkennen, wird er einfach ohne diese Bewegung fortfahren und den Rest des Drucks verschieben.

Eine andere Art der Schichtverschiebung tritt auf, wenn der Druckauftrag selbst zu viel Kraft auf den Druckkopf ausübt, wodurch die Schrittmotoren des Druckers Schritte verlieren. Jedes Mal, wenn Schritte verloren gehen, wird der Druck von da an verschoben. Typischerweise treten die verlorenen Schritte in jeder Schicht an der gleichen Stelle auf, weil eine besonders scharfe Ecke vorhanden ist. Das Ergebnis ist, dass der gesamte Druck oder ein bestimmter Teil davon schief erscheint.

Vorbeugung
----
Die erste Art der Schichtverschiebung wird normalerweise nicht durch die Einstellung von Cura verhindert. Cura ist so konzipiert, dass es ein Anschlagen an den Seiten des Druckvolumens verhindert. Wenn die Größe des Druckvolumens korrekt in Cura eingegeben wurde, sollte es keinen g-code erzeugen, der sich außerhalb des druckbaren Volumens bewegt. Sollte dies dennoch der Fall sein, können Sie im Dialog Maschineneinstellungen unter Druckerverwaltung die Größe des Druckvolumens anpassen, um eine Korrektur vorzunehmen. Sie sollten auch sicherstellen, dass sich im Druckvolumen keine Hindernisse befinden, auf die der Druckkopf oder das Bewegungssystem beim Drucken stoßen könnte. Drucker können dies in der Regel nicht erkennen und drucken daher aus einer verschobenen Position weiter. Suchen Sie nach Kabeln, die im Weg sind, und vergewissern Sie sich, dass alle Kabel lang genug sind, um den vollen Bewegungsbereich des Druckers zu ermöglichen. Vergewissern Sie sich auch, dass die Stepper-Treiber auf der Platine des Druckers nicht überhitzt sind, was zu einem vorübergehenden Ausfall führen könnte.

Die andere Art der Schichtverschiebung, die kontinuierlich während des Drucks auftritt, wird wahrscheinlich durch eine zu hohe Kraft auf Ihr Bewegungssystem verursacht. Hier gibt es mehrere mögliche Lösungen.

Zunächst sollten Sie sich Ihre Hardware ansehen. Sind die Riemen fest angezogen? Wenn nicht, können Sie nach einer Möglichkeit suchen, sie zu spannen. Einige Drucker haben einstellbare Motorpositionen, mit denen Sie die Riemen spannen können. Rutschen die Riemenscheiben durch? Ziehen Sie die Schrauben an den Riemenscheiben sicherheitshalber nach. Ein häufiges elektrisches Problem besteht darin, dass die Motoren nicht genügend Strom erhalten, um genügend Kraft für eine scharfe Bewegung zu erzeugen. Prüfen Sie in diesem Fall, ob die Stromversorgung ausreichend ist.

Wenn die Hardware gut funktioniert, können Sie Cura auch so einstellen, dass es die Hardware ein wenig schont. Hier sind einige Einstellungen, die Sie anpassen können:
* Senken Sie die [Ruckraten](../speed/jerk_print.md). Dies führt dazu, dass der Druckkopf langsamer wird, bevor er eine Ecke druckt. Dadurch wird die Kurve weicher, er geht sanft in die Kurve hinein, anstatt hart abzubiegen.
* Verringern Sie die [Beschleunigungsraten](../speed/acceleration_print.md). Dies führt dazu, dass der Druckkopf vor einer Kurve vorsichtiger und länger abbremst (obwohl die Geschwindigkeit, mit der der Druckkopf den Scheitelpunkt der Kurve durchfährt, davon unberührt bleibt; das ist der Zweck der Ruck-Einstellung).
* Verringern Sie die [Fahrgeschwindigkeit](../speed/speed_travel.md). Dadurch wird die Kraft reduziert, mit der die Düse über bereits gedruckte Teile rutscht.
* Aktivieren Sie [Z-Sprung](../travel/retraction_hop_enabled.md). Dadurch wird verhindert, dass der Druckkopf auf zuvor gedruckte Teile auftrifft, wenn diese aufgrund von Blobs oder Warping ein wenig nach oben ragen.