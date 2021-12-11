Immer aktives Tools schreiben
====
Diese Einstellung gibt an, wie bestimmte G-Code-Befehle mit einem Werkzeugparameter vom Drucker interpretiert werden. Einige G-Code-Befehle können einen Parameter enthalten, der angibt, für welchen Extruder er gilt. Manche Firmware interpretiert diesen Parameter als einen Befehl, zu diesem Werkzeug zu wechseln und dann den G-Code auszuführen, während manche Firmware diesen Parameter als einen Befehl interpretiert, den G-Code auf einen anderen Extruder als den derzeit aktiven anzuwenden.

Die einzigen Befehle, auf die dies zutrifft und die für den 3D-Druck relevant sind, sind die Befehle zum Heizen der Düsen, `M104` und `M109`. Nehmen wir das folgende Beispiel eines Heizbefehls, der ausgeführt wird, während der erste Extruder (`T0`) druckt:

`M104 S210 T1`

Es gibt zwei mögliche Interpretationen dieses Befehls:
* Während der erste Extruder weiter druckt, beginnen Sie, den zweiten Extruder auf 210°C aufzuheizen. Dies ist die Interpretation, die von Marlin, Reprap, Sailfish und ihren abgeleiteten Firmware-Paketen vertreten wird.
* Erst auf den zweiten Extruder umschalten, dann den zweiten Extruder auf 210°C aufheizen. Dies ist die Interpretation von Smoothieware und seiner abgeleiteten Firmware.

Aufgrund der Temperaturregelungsstrategie von Cura ist es nie nötig, die zweite Interpretation auszuführen. Wenn der Drucker den g-code Befehl auf die zweite Weise interpretiert, schreibt Cura stattdessen den folgenden g-code:

`M104 S210 T1`

`T0`

Im Wesentlichen weiß er, dass der Drucker aufgrund dieses Befehls auf den zweiten Extruder umschalten wird, und muss daher auf den ersten Extruder zurückschalten, um dort weiter zu drucken.

**Da es sich um eine Maschineneinstellung handelt, wird sie normalerweise nicht in der normalen Liste der Einstellungen aufgeführt.**