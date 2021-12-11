Is-Center-Ursprung
====
Wenn diese Einstellung aktiviert ist, befindet sich die 0,0-Koordinate des Druckers in der Mitte des Bauvolumens und nicht in der vorderen linken Ecke.

Bei einigen Druckern geht die Firmware davon aus, dass sich die 0,0-Koordinate in der Mitte des Bauvolumens befindet. Dies ist bei Deltadruckern üblich, die in der Regel zylindrische Bauvolumen und keine Quader haben.

Wenn die Null-Koordinate des Druckers in der Mitte liegt, dann enthält der endgültige g-Code sowohl negative als auch positive Koordinaten. Der Koordinatenursprung befindet sich in der Mitte des Bauvolumens von Cura. Cura zeigt seinen dreifarbigen Koordinatenmarker ebenfalls in der Mitte an. Die Koordinaten von 3MF-Dateien werden jedoch weiterhin so behandelt, als ob der Koordinatenursprung in der vorderen linken Ecke des Druckers liegt, da das 3MF-Dateiformat dies erfordert.

**Da es sich hierbei um eine Geräteeinstellung handelt, wird sie normalerweise nicht in der normalen Liste der Einstellungen aufgeführt. Es gibt jedoch ein Kontrollkästchen für diese Einstellung im Dialogfeld "Druckereinstellungen", das Sie in der Liste der hinzugefügten Drucker im Dialogfeld "Einstellungen" finden.**