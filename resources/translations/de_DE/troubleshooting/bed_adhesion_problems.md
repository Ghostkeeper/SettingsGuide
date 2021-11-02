Probleme mit der (Druck-)Betthaftung
====
Eine der häufigsten Fehlerarten bei 3D-Drucken ist, dass sich der Druck von der Bauplatte löst, während er noch gedruckt wird. Dieser Artikel befasst sich mit einigen Einstellungen, die Sie vornehmen können, um dies zu verhindern.

Wenn sich der Druck von der Bauplatte gelöst hat, werden Sie in der Regel eine Menge loser Drähte überall auf der Bauplatte sehen. Wenn Sie mehr Glück haben, kann es sich auch nur als [Ebenenverschiebung](layer_shift.md) manifestieren (und es gibt weniger zu bereinigen). So oder so, der Druck ist ruiniert.

Methoden der Betthaftung
----
Cura bietet mehrere Methoden, um die Betthaftung zu verbessern. Sie können zwischen diesen Methoden mit der Einstellung [Druckplattenhaftungstyp](../platform_adhesion/adhesion_type.md) wählen. Die folgenden Optionen sind verfügbar.
* Brim, die häufigste Technik, fügt einen Rand um die Unterseite des Drucks hinzu, der die Oberfläche vergrößert, so dass der Druck besser auf der Bauplatte haftet.
* Ein Raft ist eine Platte unter dem gesamten Druck. Diese Platte erhält ebenfalls eine größere Oberfläche, so dass sie gut haftet. Wenn das Raft mit einem Material bedruckt ist, das gut am Druck haftet (z. B. mit dem gleichen Material), dann bleibt der Druck auf diese Weise an seinem Platz.
* Eine Schürze (Skirt) wird nicht am Druck befestigt, sondern umschließt ihn nur. Diese Linie stellt sicher, dass das Material fließt, bevor der eigentliche Druck beginnt, so dass es keine Unterextrusion in der ersten Schicht gibt, die die Haftung ruinieren könnte.
* Sie können auch keine (zusätzliche) Haftung haben, indem Sie "Keine" auswählen. Dies spart Zeit und Material und verhindert andere negative Effekte der oben genannten Methoden. Verwenden Sie dies nur, wenn Ihr Drucker über eine andere Grundierungstechnik verfügt, wie z. B. einen Spüleimer.

Brim und Raft sind die effektivsten Techniken, um die Haftung zu erhöhen, da sie speziell für diesen Zweck entwickelt wurden. Die meisten Drucke von vernünftiger Größe werden eine dieser beiden Techniken benötigen.

Wenn Brim verwendet wird, können Sie die Haftung weiter erhöhen, indem Sie die [Breite des Brim-Elements](../platform_adhesion/brim_width.md) erhöhen. Sie können auch eine Krempe an der [Innenseite der Stützen](../stütze/stütze_krempe_aktivieren.md) und dem [Primärturm](../dual/prime_tower_krempe_aktivieren.md) sowie zwischen [Modell und Stütze](../plattform_haftung/krempe_ersetzt_stütze.md) und den [Innenlöchern](../plattform_haftung/krempe_außen_nur.md) des Modells hinzufügen.

Wenn Raft verwendet wird, können Sie die Haftung weiter erhöhen, indem Sie die [Breite des Raft](../platform_adhesion/raft_margin.md) erhöhen. Das Raft wird aber immer unterhalb von allem gedruckt, da die Schichten zueinander passen müssen. Wenn die Haftung zwischen dem Modell und dem Raft ein Problem darstellt, sollten Sie erwägen, den [Luftspalt für Raft](../platform_adhesion/raft_airgap.md) zwischen dem Raft und dem Modell zu verringern. Außerdem können Sie in Erwägung ziehen, die [Raft-Basislinienbreite](../platform_adhesion/raft_base_line_width.md) zu erhöhen.

Verhindern von Verwerfungen
----
Wenn Ihr Druck unter Verzug leidet, ist die Kontaktfläche zwischen dem Druck und der Bauplatte stark reduziert. Um dies zu verhindern, lesen Sie den Artikel über [Verziehen](warping.md). Zusammengefasst sind dies einige Einstellungen, die Sie vornehmen können, um Verzug zu verhindern.
* Stellen Sie das [Unteres Muster für erste Schicht](../top_bottom/top_bottom_pattern_0.md) auf konzentrisch.
* Reduzieren Sie die [Temperatur Druckplatte](../material/material_bed_temperature.md) und erhöhen Sie die [Temperatur Druckplatte](../material/build_volume_temperature.md).
* Passen Sie das Modell so an, dass es weniger scharfe Außenecken auf der ersten Schicht gibt.

Verschiedene Anpassungen
----
Diese Einstellungen können auch angepasst werden, wenn die normalen Bett-Haftungsmethoden nicht ausreichen.
* Erhöhen Sie die [Initiale Schichthöhe](../resolution/layer_height_0.md). Dies bietet ein wenig mehr Spielraum für Fehler, wenn die Bauplatte nicht perfekt eben ist. Es erhöht auch die Kraft, mit der das Material aus der Düse und auf die Bauplatte gedrückt wird.
* Erhöhen Sie die [Dicke der ertsen Schicht](../resolution/initial_layer_line_width_factor.md). Dadurch wird das Material ebenfalls mit mehr Kraft herausgedrückt und bleibt gut auf der Bauplatte haften.
* Das Erhöhen der [Drucktemperatur erste Schicht](../material/material_print_temperature_layer_0.md) lässt das Material mehr auf die Bauplatte ausfließen und vergrößert die Kontaktfläche.
* Wie bei der Erhöhung der Temperatur können Sie auch die [Anfängliche Lüfterdrehzahl](../cooling/cool_fan_speed_0.md) reduzieren oder die [Normaldrehzahl bei Höhe](../cooling/cool_fan_full_at_height.md) erhöhen, um das Material länger flüssig zu halten.
* Verringern Sie in ähnlicher Weise die [Geschwindigkeit erste Schicht](../speed/speed_layer_0.md). Eine Reduzierung der [Druckgeschwindigkeit für die erste Schicht](../speed/speed_print_layer_0.md) lässt das Material wieder mehr ausfließen, da das Material durch die heiße Düse länger flüssig gehalten wird. Eine Verringerung der [Bewegungsgeschwindigkeit für die erste Schicht](../speed/speed_travel_layer_0.md) verringert die Wahrscheinlichkeit, dass eine Verfahrbewegung zuvor gedruckte Linien von der Bauplatte abzieht. Ebenso sollten Sie die [Druckbeschleunigung für die erste Schicht](../speed/acceleration_layer_0.md) und [Rückfunktion der ersten Schicht](../speed/jerk_layer_0.md) anpassen. 
* Erhöhen Sie die [Anzahl der langsameren Schichten](../speed/speed_slowdown_layers.md). Dies verringert die Wahrscheinlichkeit, dass schnelle Bewegungen die vorherigen Schichten abziehen.

Platten bauen
----
Abgesehen von einem guten Druck ist eine gute Bauplatte auch für die Haftung wichtig. Eine gute Bauplatte sollte sein:
* ...sauber sein! Es ist sehr wichtig, dass die Bauplatte kein Fett (z. B. von Ihren Fingern) und keinen Staub enthält. Die Reinigung unter einem heißen Wasserhahn ist sehr effektiv. Ideal ist die Verwendung von etwas Franzbranntwein, Isopropanol und einem Mikrofasertuch.
* ...eben! Wenn die Bauplatte zu nah an der Düse ist, fließt der Filament-Strom aus der Düse ungleichmäßig, was zu Unebenheiten führt, die die Düse beim nächsten Mal abreißen wird. Wenn die Bauplatte zu weit von der Düse entfernt ist, wird das Material nicht gut auf die Bauplatte gedrückt, was die Oberfläche stark reduziert. Bei den meisten Druckern kann die Bauplatte mit einigen Rändelschrauben eingestellt werden. Stellen Sie also sicher, dass sie perfekt eben ist und den richtigen Abstand zur Düse hat.
* ...rau! Mit einer leicht aufgerauten Bauplatte wird die Kontaktfläche zwischen der Bauplatte und dem Druck im Gegensatz zu einer perfekt glatten Bauplatte stark vergrößert. Einige Drucker sind aus diesem Grund mit mattiertem Glas oder eloxiertem Metall ausgestattet.

Auch das Material der Bauplatte hat einen großen Einfluss auf die Klebeeigenschaften. Dies kann bei verschiedenen Druckmaterialien sehr unterschiedlich sein. Gängige Bauplattenmaterialien sind Glas, Acryl, Aluminium, Stahl oder eloxiertes Aluminium. Jedes dieser Materialien haftet auf anderen Materialien. Kunststoff-Bauplatten können chemisch an Ihrem Material haften. Andere Materialien setzen auf eine raue Oberfläche, um die Kontaktfläche zu vergrößern.

Es gibt auch zusätzliche Bett-Haftungsmethoden, die Sie auf jede Bauplatte anwenden können:
* Allgemeine Papierklebestifte funktionieren sehr gut. Obwohl der Kleber schnell trocknet, erzeugt er eine raue Oberfläche mit einer vergrößerten Auflagefläche für den Druck.
* Abdeckband hat einen ähnlichen Effekt, da es eine raue Oberfläche aus Papier hat, aber im Gegensatz zu Papier bleibt es perfekt flach auf der Bauplatte. Die dickeren Arten von Abdeckband, die für den Außeneinsatz hergestellt werden, sind am effektivsten.
* Haarspray funktioniert ähnlich wie Kleber, da es eine feinkörnige raue Oberfläche auf der Bauplatte hinterlässt. Es ist sehr einfach, dieses gleichmäßig aufzutragen.
* Tragen Sie vorsichtig etwas Schleifpapier auf die Bauplatte auf, um sie aufzurauen und die Kontaktfläche zu vergrößern. Rauen Sie sie aber nicht zu sehr auf, sonst haben Sie eine unebene Oberfläche zum Drucken. Verwenden Sie dazu sehr feinkörniges Schleifpapier mit einer Körnung von 500 oder mehr.
* Viele 3D-Druckerhersteller bieten spezielle "Klebefolien" an, die über die Bauplatte gespannt werden können. Sie funktionieren ähnlich wie Abdeckband, sind aber für eine längere Lebensdauer ausgelegt. Einige bestehen aus einem Kunststoff, der sich auch chemisch mit dem gedruckten Material verbindet.