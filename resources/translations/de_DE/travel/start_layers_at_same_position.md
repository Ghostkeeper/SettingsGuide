Startet Schichten mit demselben Teil
====
Ursprünglich bewirkte diese Einstellung, dass der Drucker jede Schicht mit dem Objekt begann, das der in den Einstellungen [Schichtstart X](layer_start_x.md) und [Schichtstart Y](layer_start_y.md) angegebenen Position am nächsten lag, anstatt mit dem Objekt, das in der vorherigen Schicht zuletzt gedruckt wurde.

**Die Einstellung wurde in Cura 2.4 ausgeblendet und nie richtig entfernt, weshalb diese Einstellung in dieser Liste noch vorhanden ist. Sie hat jedoch keine Auswirkung auf den Druck.**

Das alternative Verfahren war nicht mehr möglich, nachdem das Multi-Threaded-Slicing eingeführt wurde, daher wurde die Einstellung ausgeblendet.

Das Drucken aller Schichten in der gleichen Reihenfolge verhindert, dass zwei Schichten unmittelbar nacheinander übereinander gestapelt werden, wenn mehrere Teile zu drucken sind. Dadurch kann die vorherige Schicht länger abkühlen, während die Düse mit dem Druck der anderen Teile beschäftigt ist. Dies verbessert den Überhang und verringert die Streifenbildung und das Durchhängen. Andererseits wird der Drucker dadurch etwas mehr bewegt, was die Druckzeit leicht verlängert.