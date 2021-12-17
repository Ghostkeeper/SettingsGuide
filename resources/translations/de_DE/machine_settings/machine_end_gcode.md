Ende G-Code
====
Mit dieser Einstellung kann ein Stück g-Code geschrieben werden, das am Ende jedes Drucks ausgeführt wird. Mit diesem g-Code kann der Drucker seine Komponenten abschalten und nach dem Drucken aufräumen.

Einige Beispiele für Dinge, die üblicherweise im End-G-Code ausgeführt werden, sind:

* Einziehen des Materials.
* Abkühlung der Düse(n).
* Abkühlung der Bauplatte.
* Ausschalten der Lüfter.

Eine einigermaßen umfassende Liste der verfügbaren g-Codes, die Sie hier schreiben können, finden Sie in der [RepRap Wiki](https://reprap.org/wiki/G-code).

Verweise auf Einstellungen
----
Bei der Bearbeitung des End-G-Codes können Sie auf die Werte anderer Einstellungen verweisen. Dazu wird eine bestimmte Syntax verwendet. Einstellungen werden durch ihren *Schlüssel* referenziert. Dieser Schlüssel ist ein interner Name in Cura. Er ist in der Benutzeroberfläche nicht sichtbar. Eine vollständige Liste aller Schlüssel finden Sie in [diesem Dokument](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) im Quellcode von Cura.

Die Syntax, um den Wert einer globalen Einstellung zu ermitteln, lautet wie folgt:

`{setting_key}`

Mit anderen Worten: Schreiben Sie den Schlüssel der Einstellung in geschweifte Klammern. Auf diese Weise wird der globale Wert einer Einstellung ermittelt. Viele Einstellungen können jedoch für jeden Extruder unterschiedlich sein. Diese sollten wie folgt referenziert werden:

`{setting_key, #}`

Hier sollten Sie anstelle des Symbols "#" die Nummer des Extruders schreiben, von dem Sie die Einstellung erhalten möchten. Extruder fangen bei 0 an zu zählen. Globale Einstellungen können auch durch die Angabe eines Extruders erhalten werden, aber sie werden für alle Extruder gleich sein. Wenn Sie versuchen, eine extruderspezifische Temperatur zu erhalten, ohne die Extrudernummer anzugeben, erhalten Sie den Wert für den ersten Extruder, der nicht deaktiviert ist.

Sie können diese Referenzen z. B. zum Abkühlen auf eine Standby-Temperatur oder zum Wiederherstellen der Standardbeschleunigung und des Rucks des Druckers verwenden. Hier sind einige Beispiele:

`M104 T0 S{material_standby_temperature, 0} ;stand-by for the next print`

`M104 T1 S{material_standby_temperature, 1}`

`M204 P{machine_acceleration} T{machine_acceleration}`

Seien Sie vorsichtig mit den Geschwindigkeitsangaben. Der G-Code akzeptiert normalerweise Vorschubgeschwindigkeiten in Millimetern pro *Minute*, während die Einstellungen in Millimetern pro *Sekunde* angegeben sind. Es gibt derzeit keine Möglichkeit, die richtige Vorschubgeschwindigkeit auszuwählen. Es ist unmöglich, Berechnungen mit diesen Referenzen durchzuführen.

Andere Informationen
----
Über die gleiche Syntax wie bei den Verweisen auf Einstellungen sind auch einige Zusatzinformationen verfügbar:

* `{time}` bezieht sich auf die aktuelle Ortszeit des Tages, an dem es gesliced wurde.
* `{date}` bezieht sich auf das Datum, an dem es gesliced wurde.
* `{day}` bezieht sich auf den Wochentag, an dem es gesliced wurde.
* `{initial_extruder_nr}` bezieht sich auf den Extruder, mit dem der Druckvorgang beginnt.
<!--if cura_version>=4.12-->
* `{material_id}` bezieht sich auf einen eindeutigen Bezeichner für das aktive Material. Geben Sie den Extruder ähnlich wie bei anderen Einstellungen an.
* `{material_name}` bezieht sich auf den Namen des aktiven Materials. Dies ist in der Regel der Name, den Sie auf einer Website finden, auf der das Material verkauft wird.
* `{material_type}` bezieht sich auf die Klasse des aktiven Materials, wie PLA oder ABS.
* `{material_brand}` verweist auf den Hersteller des Werkstoffs.
<!--endif-->

**Diese Einstellung ist eine Geräteeinstellung und wird daher nicht in der normalen Liste der Einstellungen angezeigt. Sie kann geändert werden, indem Sie in der Liste der Drucker im Einstellungsbildschirm auf "Geräteeinstellungen" klicken.**