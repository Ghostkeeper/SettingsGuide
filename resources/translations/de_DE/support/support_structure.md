Stützstruktur
====
Mit dieser Einstellung können Sie wählen, welcher Algorithmus für die Konstruktion der Stützstruktur verwendet werden soll. Diese Konstruktionen haben sehr unterschiedliche Eigenschaften, so dass die Wahl eines Algorithmus einen großen Einfluss darauf hat, wie gut Ihr Druck unterstützt wird. Es sind zwei Optionen verfügbar.

<!--screenshot {
"image_path": "support_type_everywhere.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
    "support_enable": true,
    "support_type": "everywhere"
},
"colours": 32
}-->
Normale Stützstruktur
----
![Normale Stützstruktur](../../../articles/images/support_type_everywhere.png)

Dies ist die traditionelle Support-Struktur, an welche die meisten Menschen gewöhnt sind. Die Struktur wird unterhalb der überhängenden Bereiche erzeugt und normalerweise mit einem Muster gefüllt, das die überhängenden Bereiche direkt unterstützt. Von dort wird sie gerade nach unten fallen gelassen, bis sie die Bauplatte oder einen Teil des Modells erreicht, der sie stützt.

Die normale Support-Konstruktion war für den größten Teil der Geschichte des 3D-Drucks der Standard und funktioniert in allen Slicern ähnlich. Dies ist der goldene Standard, und das nicht ohne Grund:
* Aufgrund seiner stabilen Struktur mit großen Kontaktflächen auf dem Modell und der Bauplatte ist er sehr zuverlässig. Er verzeiht sehr gut schlechte Einstellungen oder einen schlecht eingestellten Drucker.
* Da die Form einfach ist, lässt sie sich schnell slicen.
* Die gerade Support-Struktur ist für den Benutzer leicht anzupassen, da sofort klar ist, welche Ränder unterstützt werden und welche nicht.

Die wichtigsten Nachteile ergeben sich aus denselben Eigenschaften:
* Aufgrund der großen Kontaktflächen ist der Support oft schwer zu entfernen und kann auf der Oberfläche, die er berührt hat, erhebliche Narben hinterlassen.
* Obwohl sie stabil ist, kann sie viel Material verbrauchen und viel Zeit zum Drucken benötigen. Dem kann bis zu einem gewissen Grad durch die Verwendung von, [Überhänge druckbar machen](../experimental/conical_overhang_enabled.md), entgegengewirkt werden.

Da der Support in der Regel groß und breit ist, wird ein [Füllmuster](support_pattern.md) benötigt, um die Oberfläche richtig zu unterstützen. Die zickzackförmige Füllung kann verwendet werden, um den Support größtenteils aus einer einzigen Linie zu drucken und um das Entfernen zu erleichtern. Andere Muster können mit einer zusätzlichen [Anzahl von Stützstrukturwandlinien](support_wall_count.md) kombiniert werden, um den Support besonders stabil zu machen.

<!--screenshot {
"image_path": "support_structure_tree.png",
"models": [{"script": "duct.scad"}],
"camera_position": [56, 127, 60],
"settings": {
    "support_enable": true,
    "support_structure": "tree",
    "support_tree_collision_resolution": 0.05
},
"colours": 32
}-->
Baumstützstruktur
----
![Baumstützstruktur](../../../articles/images/support_structure_tree.png)

Beim baumförmigen Support beginnt die Support-Struktur klein auf der Bauplatte und wächst dann in Richtung der Teile des Drucks, die unterstützt werden müssen.

Die Baumstützstruktur kann Hindernisse vermeiden, wenn sie in Richtung der überhängenden Bereiche wächst, da die Stützstruktur nicht gerade nach unten fallen muss. Wenn es möglich ist, wird der Support nur auf der Bauplatte aufliegen, um die Oberfläche, auf der der Support aufliegt, nicht zu beschädigen. Wenn es keinen Weg von der Bauplatte zum Überhang gibt, wird die Stütze auf einer Fläche aufliegen, die so nah wie möglich am Überhang liegt, um den Materialverbrauch zu minimieren. Die Äste der Baumstützstruktur werden durch den [Astwinkel der Baumstützstruktur](support_tree_angle.md) begrenzt, damit sie nicht selbst einen zu steilen Überhang erzeugen. Dies schränkt die Fähigkeit ein, um Hindernisse herumzuwachsen und bestimmt auch die Höhe, in der die Stämme anfangen, sich zu verzweigen.

Die Baumstützstruktur hat eine Reihe von großen Vorteilen gegenüber normalen Stützstruktur:
* Die Baumstützstruktur verbrauchen oft viel weniger Material als normale Stützstruktur. Zwischen 25% und 50% des Materialverbrauchs sind üblich. Das spart eine Menge Zeit und senkt die Kosten des Drucks.
* Aufgrund der kleinen Kontaktfläche sieht der Überhang bei der Verwendung von der Baumstützstruktur tendenziell besser aus.
* Aufgrund der kleinen Kontaktfläche lässt sich der Support auch leichter entfernen.
* Er hinterlässt weniger Narben auf der Oberfläche als normaler Support, da er von der Bauplatte aus um das Modell herum in Richtung des Überhangs greifen kann.

Die Hauptnachteile sind jedoch:
* Das Sliceing dauert deutlich länger als beim normalen Support. Vor allem bei großen Modellen ist Geduld gefragt.
* Es gibt viele Unterbrechungen im Fluss, wenn die kleinsten Äste gedruckt werden, was die Baumstützstruktur ungeeignet macht, um Materialien zu drucken, die schwer zu extrudieren sind, wie PVA oder flexible Materialien.
* Die Baumstützstruktur eignet sich nicht gut für den Support einiger mechanischer Modelle. Insbesondere neigt sie dazu, zu wenige Äste zu platzieren, um flache, schräge Überhänge zu unterstützen.

Die Baumstützstruktur ist standardmäßig hohl. Die Äste haben eine kleine Spitze, so dass ein Füllmuster keine zusätzliche Unterstützung für die überhängende Oberfläche des gedruckten Objekts bietet. Aufgrund seiner gezackten Form ist der Baum-Support normalerweise recht stabil. Die normalen Support-Einstellungen gelten jedoch weiterhin für den Bereich, der von den Ästen des Baums umschlossen wird. Die [Dichte der Stützstruktur](support_infill_rate.md) kann verwendet werden, um dem Support mehr strukturelle Festigkeit zu verleihen.