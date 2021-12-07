Blobs
====
Blobs sind kleine Flecken an der Seite des Modells. Manchmal sind es nur Punkte. Manchmal sind es auch Streifen. Sie sind ein optischer Oberflächenfehler und können die Reibung zwischen Oberflächen, die in einem Mechanismus übereinander gleiten müssen, erhöhen.

![Einige Blobs auf dieser Oberfläche](../../../articles/images/blobs.jpg)

Es gibt mehrere mögliche Ursachen für Blobs. Es ist einer der häufigsten Fehler beim 3D-Drucken. Dieser Artikel listet einige mögliche Ursachen und ihre Lösungen auf.

Düse verlangsamt
----
Wenn sich die Düse in einer bestimmten Spur langsamer bewegt als in anderen, kann sich dort mehr Material ablagern. Dieses Material fließt an der Wandoberfläche nach außen und bildet einen Blob.

Die Materialzufuhr sollte damit wahrscheinlich reduziert werden. Doch selbst wenn sich der Feeder langsamer bewegt, kann es einige Sekunden dauern, bis die Durchflussmenge aus der Düsenöffnung entsprechend reduziert ist. In dieser Zeit wird zu viel Material extrudiert, was zu Blobs führt.

Um dies zu verhindern, sollten Sie die folgenden Einstellungen vornehmen:
* Gleichen Sie die Geschwindigkeit für die [Außenwand](../speed/speed_wall_0.md) so an, dass sie die gleiche ist wie das, was vor ihr gedruckt wird (wie die [Innenwände](../speed/speed_wall_x.md) oder [Füllung](../speed/speed_infill.md)). Es kommt dann nicht zu einer Verlangsamung.
* Erhöhen Sie die [Ruckfunktion Außenwand](../speed/jerk_wall_0.md). Dadurch wird verhindert, dass die Düse in Kurven langsamer wird.
* Reduzieren Sie die [Maximale Auflösung](../meshfix/meshfix_maximum_resolution.md) und erhöhen Sie die [Maximale Abweichung](../meshfix/meshfix_maximum_deviation.md), um zu verhindern, dass die Bewegungssteuerung die Düse verlangsamt, um mit den zu verarbeitenden g-Codes Schritt zu halten.
* Deaktivieren Sie die Einstellung [Außenwandüberlappungen ausgleichen](../shell/travel_compensate_overlapping_walls_0_enabled.md). Diese Einstellung kann neue Bewegungsbefehle mit unterschiedlichen Vorschubgeschwindigkeiten erzeugen. Die Deaktivierung dieser Funktion reduziert die Anzahl der Bewegungsbefehle in der Wand.

Düse steht still
----
Wenn die Düse während des Druckens der Außenwand kleine Pausen macht, wartet sie höchstwahrscheinlich darauf, dass der Prozessor in Ihrem 3D-Drucker neue Bewegungsbefehle verarbeitet. Die Bewegungsplanungssoftware des Druckers hält für solche Fälle in der Regel einen Puffer mit vorverarbeiteten Befehlen parat, in dem die Bewegungsbefehle bereits verarbeitet wurden, so dass der Drucker die Zeitpunkte für die Aktivierung der Schrittmotoren oder anderer Bewegungen genau kennt. Wenn dieser Puffer erschöpft ist, spricht man von einem "buffer underrun". Dies führt dazu, dass Kleckse auf der Oberfläche erscheinen.

Um dies zu verhindern, müssen Sie die Auflösung des G-Codes verringern.
* Erhöhen Sie die Einstellung [Maximale Auflösung](../meshfix/meshfix_maximum_resolution.md), wodurch Cura längere Liniensegmente ausgibt.
* Erhöhen Sie die Einstellung [Maximale Abweichung](../meshfix/meshfix_maximum_deviation.md), wodurch Cura die Auflösung weiter reduzieren kann, indem es weiter vom ursprünglichen Pfad abweicht.
* Deaktivieren Sie die Einstellung [Wandüberlappungen ausgleichen](../shell/travel_compensate_overlapping_walls_0_enabled.md). Wenn sich die Außenwand mit anderen Außenwänden überlappt, würde ein Teil der Wand eine andere Linienstärke erhalten, was jedoch einen zusätzlichen Bewegungsbefehl erfordert. Um die Anzahl der Bewegungsbefehle zu verringern, können Sie diese Funktion deaktivieren. Allerdings kann dies auch zu einer Überextrusion in diesen Wänden führen, was ebenfalls Blobs verursacht.
* Reduzieren Sie die [Geschwindigkeit der Außenwand](../speed/speed_wall_0.md). Dadurch wird die Geschwindigkeit, mit der die Bewegungsbefehle ausgeführt werden müssen, verringert, so dass die CPU aufholen kann.

Fahrbewegungen gehen durch Wände
----
Obwohl Cura im Allgemeinen das Überqueren der Außenwand so weit wie möglich vermeidet, ist dies manchmal unvermeidlich. Wenn die Düse beim Überqueren einer Außenwand etwas gesickertes Material mit sich führt, kann dieses Material dort abgewischt werden und einen Klecks hinterlassen.

Diese Ursache von Blobs kann durch die folgenden Einstellungen verhindert werden:
* Stellen Sie sicher, dass [Combing-Modus](../travel/retraction_combing.md) aktiviert ist. Dies bewirkt, dass die Düse so viel wie möglich um Wände herumfährt, anstatt durch sie hindurch.
* Aktivieren Sie [Z-Sprung beim Einziehen](../travel/retraction_hop_enabled.md). Wenn die Wände gekreuzt werden, bewegt sich die Düse ein wenig nach oben, um über die Wand zu fahren, anstatt durch sie hindurch. Das gesickerte Material wird höchstwahrscheinlich nicht an der Wand abgewischt, sondern dort, wo die Düse nach der Fahrbewegung landet. Cura wird immer versuchen, in der Füllung oder Außenhaut zu landen, wenn dies möglich ist.
* Stellen Sie sicher, dass die [Reihenfolge des Wanddrucks optimieren](../shell/optimize_wall_printing_order.md) ist. Dadurch wird die Anzahl der Bewegungen beim Drucken von Wänden reduziert, was effizientere Bewegungen ermöglicht und die Wahrscheinlichkeit verringert, dass einige dieser Bewegungen durch eine Außenwand führen müssen.

Aufgebauter Druck
----
Wenn die Düse überextrudiert, kann die Extrusion unregelmäßig werden. Dieser Druck kann sich plötzlich entladen, wenn eine bestimmte Ecke Ihres Drucks gedruckt wird (vor allem an Überhängen). Manchmal entlädt sich dieser aufgestaute Druck und hinterlässt einen großen Klecks. In der Regel folgt auf den Klecks dann ein Streifen mit allmählich abnehmendem Druck in der Düse.

Um diesen Effekt zu verringern, sollten Sie einige Einstellungen in Betracht ziehen:
* Verringern Sie die [Breite der Wandlinien](../resolution/wall_line_width.md). Dadurch wird der Druck in der Düsenkammer im Allgemeinen reduziert.
* Verringern Sie den Wert [Einfügung Außenwand](../shell/wall_0_inset.md). Diese Einstellung bewirkt, dass die Außenwand mit der angrenzenden Innenwand überlappt, so dass die Wand stärker an die Innenwand gedrückt wird, was die Festigkeit erhöht. Allerdings erhöht sich dadurch auch der Druck im Inneren der Düsenkammer.

Feuchtes Filament
----
Wenn sich im Filament Feuchtigkeit angesammelt hat, während es sich noch auf der Spule befand, wird diese Feuchtigkeit in der Düse über ihren Siedepunkt hinaus erhitzt. Der Wasserdampf entweicht schlagartig aus der Düse. Diese kleine Explosion kann etwas Kunststoff aus dem Weg sprengen, was zu einem kleinen Blob auf Ihrer Oberfläche führt.

Nähte
----
Dort, wo der Umfang der Außenwand beginnt und geschlossen wird, entsteht eine Naht. Dies ist nicht das, was man normalerweise einen Blob nennt, obwohl es ähnlich aussieht. Lesen Sie den Artikel über [Nähte](seam.md), wie Sie diesen Effekt reduzieren können.

Wenn die [Justierung der Z-Naht](../shell/z_seam_type.md) auf "Zufall" eingestellt ist, wird die Naht über das Modell verteilt und erzeugt überall kleine Nähte. Dies kann wie ein Klecks aussehen, auch wenn es sich tatsächlich um eine Naht handelt. Ändern Sie die Einstellung für die Justierung der Z-Naht, um diese Nähte zu verbergen.