Abkühlgeschwindigkeit
====
Diese Einstellung teilt Cura mit, wie schnell Ihre Düse abkühlt, wenn sie nicht beheizt wird. Sie wird verwendet, um vorherzusagen, wann die Düse vor dem Umschalten des Extruders abgekühlt werden soll.

![Die Düsen werden vor dem Umschalten des Extruders aufgeheizt.](../../../articles/images/temperature_regulation.svg)

Wenn der Extruder gewechselt wird, beginnt Cura mit der Vorkühlung der aktiven Düse, kurz bevor diese fertig ist, so dass sie während der Wartezeit etwas weniger sickert. Cura versucht auch vorherzusagen, wie stark die Düse abgekühlt ist, während sie inaktiv war. Auf diese Weise weiß er, wie stark er sie danach wieder aufheizen muss.

Wenn die Düse tatsächlich schneller abkühlt, als diese Einstellung angibt, wird die Düse schneller auf die Bereitschaftstemperatur kommen, als Cura vorhersagt. Infolgedessen kann es länger dauern, die Düse aufzuheizen, als Cura vorhersagt, und der Drucker wird am Düsenschalter darauf warten, dass sich die Düse weiter aufheizt.

Wenn die Düse tatsächlich langsamer abkühlt, als diese Einstellung angibt, kann es sein, dass die Düse noch warm ist, wenn Cura einen Befehl zum Vorheizen der Düse sendet, was dazu führt, dass sie sich zu schnell erwärmt. Die Düse wird eine Zeit lang auf Drucktemperatur sein, bevor sie an der Reihe ist zu drucken. Während dieser Zeit tropft es ein wenig und der Kunststoff zersetzt sich ein wenig mehr.

Die tatsächliche Abkühlgeschwindigkeit ist keine konstante Rate in Grad pro Sekunde. Vielmehr hängt sie von der Differenz zwischen der aktuellen Düsentemperatur und der Temperatur des Bauvolumens ab. Wenn die Düse heiß ist, kühlt sie schneller ab, und wenn sie sich der Bereitschaftstemperatur nähert, kühlt sie langsamer ab. Wenn Sie dies einstellen, versuchen Sie es, indem Sie die Zeit messen, die es braucht, um von der [endgültigen Drucktemperatur](../material/material_final_print_temperature.md) auf die [Standby-Temperatur](../material/material_standby_temperature.md) abzukühlen. Dies ist die wichtigste Angabe, die Cura versucht, vorherzusagen. Wenn Sie kleine Drucke machen, könnten Sie die Abkühlgeschwindigkeit etwas erhöhen, um auszugleichen, dass es öfter heiß bleibt.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**