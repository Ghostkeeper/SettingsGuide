Baumstützstruktur
====
Die Baumstützstruktur bietet einen alternativen Ansatz für die Unterstützung des Modells im Vergleich zur herkömmlichen Unterstützungstechnik. Bei der Baumstützstruktur wird eine verzweigte Struktur erzeugt, die auf der Bauplatte mit einer kleinen Basis beginnt, aber in Richtung der Teile wächst, die gestützt werden müssen.

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
![Eine baumartige Struktur stützt den Überhang](../../../articles/images/support_structure_tree.png)

Die Baumstützstruktur können Hindernisse vermeiden, wenn sie in Richtung der Überhangbereiche wachsen. Wenn es möglich ist, wird der Baum von der Bauplatte nach oben wachsen, um die Oberfläche, auf der der Support ruht, nicht zu beschädigen. Wenn dies nicht möglich ist, wird der Baum auf der Oberfläche des Modells so nahe wie möglich am Überhang aufliegen, um den Zeit- und Materialverbrauch zu minimieren. Die Äste der Baumstützstruktur werden durch den [Astwinkel der Baumstützstruktur](../support/support_tree_angle.md) begrenzt, damit sie nicht selbst einen zu steilen Überhang erzeugen. Dies schränkt die Fähigkeit ein, um Hindernisse herumzuwachsen und bestimmt auch die Höhe, in der die Äste beginnen, sich zu verzweigen.

Die Baumstützstruktur ist standardmäßig hohl. Die normalen Support-Einstellungen gelten jedoch weiterhin für den Bereich, der von den Ästen des Baums umschlossen wird. Insbesondere kann die [Dichte der Stützstruktur](../support/support_infill_rate.md) verwendet werden, um dem Support mehr strukturelle Festigkeit zu verleihen. Da die Baumstützstruktur von Natur aus sehr verwinkelt ist, verfügt sie normalerweise über eine ausreichende Festigkeit für ihren Zweck.

Die Baumstützstruktur bietet eine Reihe von Vorteilen gegenüber der normalen Stützstruktur, um nur einige zu nennen:
* Die Baumstützstruktur benötigt im Allgemeinen viel weniger Material als eine normale Stützstruktur. In der Regel werden zwischen 25 % und 50 % des Materialverbrauchs eingespart. Das spart eine Menge Zeit und Materialkosten.
* Wenn mit dem gleichen Material wie der Druck gedruckt wird, sieht der Überhang bei der Verwendung der Baumstützstruktur in der Regel besser aus.
* Die Baumstützstruktur lässt sich leichter entfernen als eine normale Stützstruktur.
* Die Baumstützstruktur hinterlässt weniger Narben auf der Oberfläche als normaler Support, da er um das Modell herum in Richtung Bauplatte reichen kann.

Dies bringt jedoch auch einige Nachteile mit sich:
* Die Baumstützstruktur benötigt wesentlich mehr Zeit zum Slicen. Vor allem bei großen Modellen ist also Geduld gefragt.
* Es gibt viele Unterbrechungen im Fluss, wenn die kleinsten Äste gedruckt werden, was die Baumstützstruktur ungeeignet macht, um Materialien zu drucken, die schwer zu extrudieren sind, wie PVA oder flexible Materialien.
* Die Baumstützstruktur eignet sich nicht sehr gut für den Support einiger mechanischer Modelle. Insbesondere neigt sie dazu, zu wenige Äste zu platzieren, um flache, schräge Überhänge zu unterstützen.

Obwohl die Baumstützstruktur gleichzeitig mit der normalen Stütze aktiviert werden kann, ist dies im Allgemeinen nicht wünschenswert. Die beiden Arten des Supports überschneiden sich und führen zu einer übermäßigen Ausdehnung.