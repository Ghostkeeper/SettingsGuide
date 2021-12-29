Konische Stützstruktur aktivieren
====
Wenn diese Einstellung aktiviert ist, ist die Support-Struktur an den Seiten nicht mehr vollständig senkrecht. Der Support erhält eine konische Form, die nach unten hin entweder kleiner oder größer wird.

<!--screenshot {
"image_path": "support_conical_enabled.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": 30
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_conical_angle_neg10.png",
"models": [
    {
        "script": "wide_overhang.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [91, -95, 19],
"settings": {
    "support_enable": true,
    "support_conical_enabled": true,
    "support_conical_angle": -10
},
"colours": 64
}-->
![Der Support wird nach unten hin kleiner](../../../articles/images/support_conical_enabled.png)
![Der Support wird nach unten hin größer](../../../articles/images/support_conical_angle_neg10.png)

Der Support selbst neigt sich mit einem bestimmten [Winkel](support_conical_angle.md). Bei negativen Winkeln wird die Stütze nach unten hin größer, was die Stütze deutlich stabiler macht. Bei positiven Winkeln wird sie nach unten hin kleiner. Das spart eine Menge Material und Druckzeit. Um zu verhindern, dass der Support instabil wird, kann auch eine [Mindestbreite](support_conical_min_width.md) für den Support definiert werden.

Der konische Support ist der wichtigste Parameter für die Abwägung zwischen Druckzeit und Stabilität des Supports. Es gibt zwei Hauptanwendungsfälle für konischen Support:
* Einsparung von Material und Druckzeit. Mit einem konischen Support können Sie leicht die Hälfte des Materials einsparen, das für den Support benötigt wird, und damit auch die Hälfte der Zeit, die Sie zum Drucken benötigen. Dies ist besonders bei großen Mengen an Support für große und hohe Drucke von Vorteil.
* Um den Support stabiler zu machen, verwenden Sie einen negativen Winkel. Wenn Ihr Druck winzige, weit oben liegende Elemente enthält, die unterstützt werden müssen, entstehen normalerweise sehr hohe [Pfeiler](../support/support_use_towers.md), die während des Drucks leicht umfallen können. Mit der konischen Stütze können diese hohen, dünnen Support-Strukturen unten breiter gemacht werden. Das gibt ihnen zusätzliche Stabilität. Allerdings dauert es länger, diese Supports zu drucken, da mehr Material benötigt wird.

Wenn die [Platzierung der Stützstruktur](../support/support_type.md) so eingestellt ist, dass der Support nur auf der Bauplatte platziert wird, ermöglicht der konische Support das Umfassen des Modells, um das Modell auch an Stellen zu stützen, die über anderen Teilen des Modells liegen. Der Support liegt weiterhin nur auf der Bauplatte auf, kann aber aufgrund seiner Form nun auch die überhängenden Bereiche in den Ecken erreichen, die sonst nicht abgestützt werden würden.

Diese Funktion ist eine etwas einfachere und weniger extreme Version von der <!--if cura_version >= 4.7-->[Baumstützstruktur](../support/support_structure.md)<!--endif--><!--if cura_version < 4.7:[Baumstützstruktur](support_tree_enable.md)-->. Die Baumstützstruktur hat viele der gleichen Vorteile wie die konische Unterstützung. Die Baumstützstruktur verwendet jedoch einen völlig anderen Algorithmus und lässt mehr Freiheiten bei der Konstruktion des Supports, während die konische Unterstützung eher dem Algorithmus zur Erzeugung des gewöhnlichen Supports folgt. Das bedeutet, dass die Einstellungen für die normale Unterstützung in der Regel besser funktionieren, wenn sie mit der konischen Unterstützung verwendet werden, aber für die Baumstützstruktur müssen sie erheblich angepasst werden. Die Baumstützstruktur spart in der Regel mehr Material und Druckzeit, während die Zuverlässigkeit des Drucks erhalten bleibt.