Start G-Code
====
Mit dieser Einstellung kann ein bisschen G-Code geschrieben werden, der zu Beginn eines jeden Drucks ausgeführt wird. Mit diesem G-Code kann der Drucker so eingestellt werden, dass er zum Drucken bereit ist.

Einige Beispiele für Dinge, die üblicherweise im Start-G-Code ausgeführt werden, sind:
* Vorfüllen der Düse(n).
* Aufheizen der Bauplatte.
* Aufheizen der Düse(n).
* Sicherstellen, dass der richtige Extruder ausgewählt ist.
* Konfigurieren der Lüfter, der Beschleunigung oder des Rucks.
* Automatische Bettnivellierung.
* Konfigurieren des linearen Vorschubs.

Eine einigermaßen umfassende Liste der verfügbaren g-Codes, die Sie hier schreiben können, finden Sie im [RepRap Wiki](https://reprap.org/wiki/G-code).

Verweise auf Einstellungen
----
Bei der Bearbeitung des Start-G-Codes können Sie auf die Werte anderer Einstellungen verweisen. Dazu wird eine bestimmte Syntax verwendet. Einstellungen werden durch ihren *Schlüssel* referenziert. Dieser Schlüssel ist ein interner Name in Cura. Er ist in der Benutzeroberfläche nicht sichtbar. Eine vollständige Liste aller Schlüssel finden Sie im Quellcode von Cura in [diesem Dokument](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json).

Die Syntax, um den Wert einer globalen Einstellung zu ermitteln, lautet wie folgt:

`{setting_key}`

Mit anderen Worten: Schreiben Sie den Schlüssel der Einstellung in geschweifte Klammern. Auf diese Weise wird der globale Wert einer Einstellung ermittelt. Viele Einstellungen können jedoch für jeden Extruder unterschiedlich sein. Diese sollten wie folgt referenziert werden:

`{setting_key, #}`

Hier sollten Sie anstelle des Symbols "#" die Nummer des Extruders schreiben, von dem Sie die Einstellung erhalten möchten. Extruder beginnen bei 0 zu zählen. Globale Einstellungen können auch durch Angabe eines Extruders erhalten werden, aber sie sind für alle Extruder gleich. Wenn Sie versuchen, eine extruderspezifische Temperatur zu erhalten, ohne die Extrudernummer anzugeben, erhalten Sie den Wert für den ersten Extruder, der nicht deaktiviert ist.

Sie können diese Referenzen zum Beispiel zum Vorheizen auf die richtige Temperatur oder zum Einstellen der Beschleunigungen verwenden. Hier sind einige Beispiele:

`M104 S{material_print_temperature_layer_0, 0} ;pre-heat`

`M140 S{material_bed_temperature_layer_0} ;heat bed`

`M204 P{acceleration_print, 0} T{acceleration_travel, 0}`

`M205 X{jerk_print, 0}`

Seien Sie vorsichtig mit den Geschwindigkeitsangaben. Der G-Code akzeptiert normalerweise Vorschubgeschwindigkeiten in Millimetern pro *Minute*, während die Einstellungen in Millimetern pro *Sekunde* angegeben sind. Es gibt derzeit keine Möglichkeit, die richtige Vorschubgeschwindigkeit auszuwählen. Es ist nicht möglich, Berechnungen mit diesen Referenzen durchzuführen.

Andere Informationen
----
Über die gleiche Syntax wie die Verweise auf die Einstellungen sind auch einige Zusatzinformationen verfügbar:

* `{time}` bezieht sich auf die aktuelle Ortszeit des Tages, an dem es gesliced wurde.
* `{date}` bezieht sich auf das Datum, an dem es gesliced wurde.
* `{day}` bezieht sich auf den Wochentag, an dem es gesliced wurde.
* `{initial_extruder_nr}` bezieht sich auf den Extruder, mit dem der Druckvorgang beginnt.
<!--if cura_version>=4.12-->
* `{material_id}` bezieht sich auf einen eindeutigen Bezeichner für das aktive Material. Geben Sie den Extruder ähnlich wie bei den anderen Einstellungen an.
* `{material_name}` bezieht sich auf den Namen des aktiven Materials. Dies ist in der Regel der Name, den Sie auf einer Website finden, auf der das Material verkauft wird.
* `{material_type}` bezieht sich auf die Klasse des aktiven Materials, wie PLA oder ABS.
* `{material_brand}` verweist auf den Hersteller des Materials.
<!--endif-->

Heizen vor dem Start G-Code
----
Cura gibt automatisch Heizbefehle aus, bevor Ihr Start-G-Code beginnt. Auf diese Weise muss der Start-G-Code nicht berücksichtigen, dass die Düse aufgeheizt werden muss. Sie können sofort mit der Beheizung der Düse beginnen. Wenn Ihr Start-G-Code einen Verweis auf eine beliebige Temperatur (für die Düse oder das Bett) enthält, wird diese deaktiviert (für die Düse bzw. das Bett).

**Diese Einstellung ist eine Geräteeinstellung, d. h. sie wird nicht in der normalen Liste der Einstellungen angezeigt. Sie kann geändert werden, indem Sie in der Liste der Drucker im Einstellungsbildschirm auf "Geräteeinstellungen" klicken.**