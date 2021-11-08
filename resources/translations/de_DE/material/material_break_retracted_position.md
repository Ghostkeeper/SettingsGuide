Einzugsmaß für das Brechen
====
Bei einigen Druckern muss das Material beim Einziehen für einen Filament-Wechsel sauber abgebrochen werden, damit es ohne Verwicklungen durch die Zuführung bewegt werden kann. Diese Einstellung konfiguriert einen Teil des Verfahrens, um es sauber abzubrechen.

Mit dieser Einstellung wird die dritte Position eingestellt, in die das Material eingezogen wird, um das Filament schließlich von dem Stück abzubrechen, das unweigerlich in der Düse zurückbleibt. Während der Stück in der Düse aufgrund seines geschmolzenen Zustands nicht herausgezogen werden kann, sollte der Teil, der herausgezogen wird, keinen dünnen Faden an der Spitze haben, da dieser in der Zuführung stecken bleiben könnte. Bei diesem letzten Einziehen bricht das Filament ab, hoffentlich bricht es aber dank der beiden vorangegangenen Schritte sauber ab.

![Zunächst wird das Material eingezogen, um das Sickern zu reduzieren.](../../../articles/images/filament_switch_anti_ooze.svg)
![Zweitens wird das Filament langsam eingezogen, um einen dünnen Faden zu ziehen, der leicht zu trennen ist, und diesen Faden erstarren zu lassen.](../../../articles/images/filament_switch_break_preparation.svg)
![Drittens wird das Filament schnell weiter eingezogen, um das Filament zutrennen.](../../../articles/images/filament_switch_break.svg)

**Diese Einstellung ist derzeit nicht in Curas Oberfläche sichtbar. Sie kann nur von den Profilen gesetzt werden. Sie wird auch nicht von Cura beim Slicen verwendet. Drucker, die das Materialdateiformat von Cura verstehen, können es jedoch verwenden, um ihre Filament-Wechselprozedur korrekt zu konfigurieren.** 
Durch ein Post-Processing-Skript kann der Befehl `M600` in den Druck eingefügt werden, der einen Filament-Wechsel auslöst.