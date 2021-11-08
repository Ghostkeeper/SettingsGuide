Standardtemperatur Druckplatte
====
Einige Drucker verfügen über eine beheizte Bauplatte. Diese Einstellung bestimmt, wie warm die Bauplatte wird.

Durch die Erwärmung der Bauplatte bleibt das Material leicht flüssig und klebrig. Einige Materialien kristallisieren beim Erstarren, was dazu führt, dass das Material stark schrumpft. Das beheizte Bett hält das Material knapp über dieser Temperatur, um diese Schrumpfung zu verhindern und die Klebkraft des flüssigen Kunststoffs zu erhalten. Dies alles dient dazu, die Haftung des Drucks auf der Bauplatte zu verbessern.

Wenn die Bauplatte jedoch zu heiß gehalten wird, ist der Druck dort, wo er die Bauplatte berührt, sehr flüssig. Dies führt dazu, dass das Material ein wenig nachgibt, was einen [Elefantenfuß](../troubleshooting/elephants_foot.md) an der Unterseite des Drucks verursacht. Dies kann mit der Einstellung [Horizontale Erweiterung erste Schicht](../shell/xy_offset_layer_0.md) kompensiert werden, beeinträchtigt aber die Maßgenauigkeit. Durch die Erwärmung der Bauplatte entsteht auch ein Temperaturunterschied zwischen dem Material, das auf der Bauplatte liegt, und dem Material weiter oben im Modell, was zu [Warping](../troubleshooting/warping.md) führt, wenn das Material weiter oben zu schrumpfen beginnt.

Wenn diese Einstellung auf 0 Grad gesetzt ist, wird Cura keine Anweisungen zur Änderung der Temperatur der Bauplatte ausgeben, was bei der Firmware zu Problemen führen kann, wenn keine beheizte Bauplatte vorhanden ist.

**Wenn Sie die Temperatur der Bauplatte in einem Materialprofil anpassen, wird die Einstellung [Standardtemperatur Druckplatte](default_material_bed_temperature.md) angepasst. Normalerweise ist die Temperatur der Bauplatte gleich der Standardtemperatur der Bauplatte, aber manchmal kann die Wahl einer anderen Qualität zu leichten Anpassungen der Temperatur der Bauplatte führen. Diese Einstellung für die Temperatur der Bauplatte ist diejenige, die tatsächlich für den Druck verwendet wird.**