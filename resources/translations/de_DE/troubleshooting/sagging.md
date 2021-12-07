Sagging
====
Bei FFF-Druckern wird eine Linie aus geschmolzenem Kunststoff gezogen. Diese Linie ist weich, und wenn sie nirgendwo anliegt, sinkt sie nach unten. Dies wird als Sagging bezeichnet.

![Sagging in den überhängenden Teilen](../../../articles/images/sagging.jpg)

Sagging führt dazu, dass überhängende Teile strähnig aussehen. Anstatt der beabsichtigten Oberfläche des Modells gleichmäßig zu folgen, wird sie zu niedrig sein. In extremen Fällen wird die Unterseite einer Fläche so ausgefranst, dass die hohle Innenseite des Drucks zu sehen ist.

Ursachen
----
Sagging wird eigentlich nicht oder kaum durch die Schwerkraft verursacht. Es wird hauptsächlich durch die Kraft des Materials verursacht, das aus der Düse gedrückt wird. Daher tritt dieses Phänomen auch bei Druckern auf, die auf den Kopf gestellt werden oder in der Schwerelosigkeit drucken. Der Druck, mit dem das Material extrudiert wird, drückt das Material nach unten, da die Düse (normalerweise) nach unten gerichtet ist.

Normalerweise ist der Druck in der Düsenkammer notwendig, um das (zähflüssige) Material nach außen zu drücken und es in Form einer breiten und flachen Materiallinie zu glätten, indem es zwischen der Düse und der vorherigen Schicht oder der Bauplatte zusammengepresst wird. Wenn jedoch in der vorherigen Schicht kein Material vorhanden war, gibt es keinen Gegendruck, um den Streifen zu glätten. Stattdessen wird er zu weit nach unten gedrückt.

Bridging
----
Eine Technik zur Verbesserung der Qualität von Überhängen ist die Optimierung der Art und Weise, wie der überhängende Spalt überbrückt wird. Dazu gehört die Verringerung des Drucks, mit dem das Material aus der Düse gedrückt wird, sowie Versuche, die Viskosität des Materials zu erhöhen oder es schneller erstarren zu lassen. Außerdem können die gedruckten Linien neu ausgerichtet werden, um den Abstand zu verringern, über den die Linien nicht gestützt werden. Diese Techniken zusammen werden als Bridging bezeichnet.

Cura bietet eine Reihe von Möglichkeiten, um das Bridging zu verbessern. Es bietet noch mehr, wenn [Brückeneinstellungen](../experimental/bridge_settings_enabled.md) aktiviert ist. Wenn Sie diese Option aktivieren, werden mehr Einstellungen angezeigt und die Druckparameter für die Überbrückungsbereiche werden standardmäßig angepasst.

Wenn Sie die Überbrückung konfigurieren, um das Sagging zu reduzieren, sollten Sie die folgenden Anpassungen berücksichtigen:
* Durch die Verringerung der [Drucktemperatur](../material/material_print_temperature.md) wird der Thermoplast zähflüssiger, wodurch er weniger durchhängt.
* Verringern der [Schichthöhe](../resolution/layer_height.md) oder der [Linienbreite](../resolution/line_width.md) verringert den Druck, mit dem das Material aus der Düse gedrückt wird. Dadurch wird nicht nur das Sagging verringert, sondern diese Linien haben auch eine geringere Wärmekapazität, so dass die Lüfter am Druckkopf effektiver kühlen können.
* Wenn Sie die [Druckgeschwindigkeit](../speed/speed_print.md) reduzieren, verringert sich auch der Druck, mit dem das Material aus der Düse gedrückt wird. In diesem Fall wird die thermische Kapazität nicht reduziert, aber die Lüfter blasen länger auf das Material, was auch ihre Effektivität erhöht und das Sagging reduziert. Wenn die Brückeneinstellungen aktiviert sind, kann die Druckgeschwindigkeit von Brücken separat eingestellt werden. Eine Verringerung der [Druckgeschwindigkeit von Brückenwänden](../experimental/bridge_wall_speed.md) ist wirksam, um schräge Überhänge zu verbessern. Das Verringern der [Druckgeschwindigkeit der Außenhaut](../experimental/bridge_skin_speed.md) verringert das Sagging in völlig horizontalen Überhangbereichen. Es gibt auch eine Variante davon, die die [Geschwindigkeit für überhängende Wände](../experimental/wall_overhang_speed_factor.md) anpasst. Diese Einstellung wird auch dann wirksam, wenn die Oberfläche nicht vollständig horizontal ist, so dass eine bestimmte Druckgeschwindigkeit für Überhänge nur für schräge Wände möglich ist.
* Die Verringerung der [Flussrate](../material/material_flow.md) ist ähnlich wie die Verringerung der Linienbreite. Dadurch wird der Druck, mit dem das Material herausgedrückt wird, sowie die Wärmekapazität verringert, so dass das Material schneller erstarrt. Diese Einstellung kann auch nur für die Überbrückungsbereiche, separat für die [Wände](../experimental/bridge_wall_material_flow.md) oder die [Außenhaut](../experimental/bridge_skin_material_flow.md) angepasst werden. Die Verringerung des Flusses für große Flächen führt allerdings auch zu Lücken in der Oberfläche und zu einem unruhigen Aussehen, so dass der Überhang visuell immer noch schlecht aussehen kann, wenn dies angepasst wird. Allerdings sollte die Maßhaltigkeit verbessert werden.
* Erhöhen Sie die [Lüftergeschwindigkeit](../cooling/cool_fan_speed.md), um das Material schneller abzukühlen. Dadurch verfestigt sich das Material schneller, und es wird verhindert, dass es herunterhängt.
* Drucke die Wände von [innen nach außen](../shell/outer_inset_first.md). Dadurch kann sich die äußere Wand auf die angrenzende innere Wand stützen, was verhindert, dass sie herunterfällt. Dies ist am effektivsten mit einer kleinen [Linienbreite](../resolution/wall_line_width_0.md).

<!--screenshot {
"image_path": "support_enable.png",
"models": [{"script": "pipe_corner.scad"}],
"camera_position": [77, 197, 40],
"settings": {"support_enable": true},
"colours": 64
}-->
Support
----
![Eine Support-Struktur unterstützt das Modell](../../../articles/images/support_enable.png)

Die gebräuchlichste und zuverlässigste Methode zur Verbesserung überhängender Teile besteht darin, sie während des Druckens mit einer Support-Struktur zu unterstützen. Diese Support-Struktur wird später entfernt, nachdem sich das Material verfestigt hat. Das Drucken von Support ist unabhängig von der Größe des überhängenden Bereichs sehr effektiv, um ein Durchhängen zu verhindern, aber es erfordert zusätzlichen Zeit- und Materialaufwand und hinterlässt eine Narbe an der Stelle, an der der Support angebracht war.

<!--if cura_version >= 4.7-->Cura verfügt über zwei Techniken zur Erzeugung von Support, die mit der Einstellung [Stützstruktur](../support/support_structure.md) angegeben werden. Es gibt eine "normale" Methode und eine "Baum"-Methode. Die normale Methode ist im Allgemeinen effektiver, um das Durchhängen zu verringern, führt aber manchmal auch zu einer ungleichmäßigen Unterseite. Der "Baum Support" führt dazu, dass die Stränge etwas weiter aber auch gleichmäßiger durchhängen.<!--endif-->
<!--if cura_version < 4.7:Cura hat zwei Techniken, um Support zu erzeugen. Es gibt eine Standardmethode, die erzeugt wird, wenn [Stützstruktur generieren](../support/support_enable.md) aktiviert ist. Alternativ wird eine Baumstützstruktur generiert, wenn [Baumstützstruktur](../experimental/support_tree_enable.md) ausgewählt wurde. Die normale Methode ist im Allgemeinen effektiver, um das Sagging zu reduzieren, führt aber manchmal auch zu einer ungleichmäßigen Unterseite. Der "Baum Support" führt dazu, dass die Stränge etwas weiter aber auch gleichmäßiger durchhängen.-->

Curas Support-Generierung entscheidet automatisch, wo Stützen platziert werden sollen. In den meisten Fällen funktioniert das gut, aber bei manchen Modellen kann es zu wenig oder zu viel Support geben. Glücklicherweise bietet Cura auch viele Methoden, um die Platzierung der Stützen anzupassen.
* Das Anpassen des [Überhangwinkels](../support/support_angle.md) ist die einfachste Methode, um zu bestimmen, wie viel Support-Material platziert wird. Sie sollten diesen Parameter so einstellen, dass alle Ihre überhängenden Bereiche unterstützt werden. Diese Einstellung bestimmt auch, welche Bereiche in der Vorbereitungsphase rot gezeichnet werden. Eine Verringerung des Überhangwinkels führt dazu, dass mehr Support gedruckt wird, was das Sagging in mehr Teilen des Drucks reduziert, aber auch mehr Zeit und Material benötigt und mehr Narben verursacht.
* Sie können überhängende Teile über anderen Teilen entfernen, indem Sie die Einstellung [Platzierung Stützstruktur](../support/support_type.md) auf "Druckbett berühren" setzen. Wenn Sie stattdessen "Überall" einstellen, können Sie schlechte Überhänge vermeiden.
* Stellen Sie sicher, dass die Einstellung [Mindestbereich Stützstruktur](../support/minimum_support_area.md) keine dünnen Teile des Supports auslöscht.
* Mit dem Support-Blocker-Werkzeug können Sie Würfel in Ihrer Szene platzieren, um zu verhindern, dass dort Support erzeugt wird. Sie können diese Blöcke auch markieren und Cura in den Einstellungen pro Modell anweisen, sie als Support zu drucken. Sie werden dann als ein neues Stück Support gedruckt. Auf diese Weise können Sie genau festlegen, wo der Support platziert werden soll. Sie können sogar ein komplettes 3D-Modell mit der exakten Form Ihres Supports in Cura laden und Cura über das Werkzeug "Pro Modell Einstellungen" anweisen, es als Support zu drucken.

Auch wenn der Überhang durch einen Support gestützt wird, kann er noch etwas durchhängen. Damit die Stütze entfernt werden kann, wird ein bestimmter [vertikaler Abstand](../support/support_z_distance.md) zwischen dem Modell und der Stütze eingehalten. Das Modell wird bis zu diesem Abstand durchhängen, bevor die Stütze wirksam wird. Eine Verringerung des Z-Abstands verringert das Durchhängen (macht die Stütze aber schwieriger zu entfernen). Einige Materialien sind so konzipiert, dass sie sich leichter entfernen lassen, weil sie sich nicht chemisch mit dem Material verbinden oder sich auflösen lassen. Diese Materialien können es sich leisten, den Z-Abstand zu verkleinern, wodurch das Sagging weiter reduziert wird, während es immer noch möglich ist, den Support anschließend zu entfernen. Der Druck kann auch zwischen den Support-Linien durchhängen, so dass eine Verringerung des [Abstandes zwischen den Support-Linien](../support/support_line_distance.md) das Durchhängen ebenfalls verringert (aber die Druckzeit verlängert und die Entfernung des Supports erschwert).

Einstellen des Modells
----
Wenn Sie die Freiheit haben, das zu druckende Modell anzupassen, kann dies zu einem viel saubereren Ergebnis führen, als wenn Sie versuchen, die Überhänge zu überbrücken oder sie zu unterstützen. Anstatt das Material in den Überhängen durchhängen zu lassen, sollten Sie Ihr Modell so gestalten und ausrichten, dass es keine Überhänge gibt.

<!--screenshot {
"image_path": "support_minimise_overhang.png",
"models": [
    {
        "script": "dowel.scad",
        "transformation": ["rotateY(127)"]
    }
],
"settings": {"support_angle": 55},
"camera_position": [21, -104, -30],
"layer": -1
}-->
![Diese Ausrichtung ermöglicht es, das Objekt mit sehr wenig Support zu drucken](../../../articles/images/support_minimise_overhang.png)

Der einfachste Trick, um dies zu erreichen, besteht darin, das Modell zu drehen. Wenn Ihr Drucker in der Lage ist, 45-Grad-Winkel ohne Sagging zu drucken, können Sie ein Modell mit einem vertikalen und einem horizontalen Teil so drehen, dass sie zwei 45-Grad-Schrägen bilden, was die Qualität der vertikalen Wand leicht verringert, aber ein Sagging im horizontalen Teil verhindert. Achten Sie jedoch darauf, dass die Kontaktfläche mit der Bauplatte nicht zu klein ist, sonst könnte sich der Druck von der Bauplatte lösen und noch ruiniert werden.

Das Hinzufügen von Fasen kann auch dazu beitragen, die Anzahl der Überhänge im Modell mit relativ wenig zusätzlichem Material zu reduzieren. Cura bietet eine automatische Methode, um Fasen zu Ihrem Modell hinzuzufügen, und zwar über die Einstellung [Überhänge druckbar machen](../experimental/conical_overhang_enabled.md). Durch das Hinzufügen von Fasen wird die Support-Struktur zum eigentlichen Modell hinzugefügt. Sie werden dann nahtlos in das Modell gedruckt, was hübscher aussieht. Außerdem wird im Vergleich zum Drucken von Support Material gespart, da das Support-Material die Kräfte schnell auf den Rest des Modells überträgt. Und am Ende wird Ihr Objekt stärker sein.

Im Allgemeinen ist es beim Entwerfen von Objekten für den 3D-Druck am besten, Überhänge ganz zu vermeiden. Wenn die Geometrie des Objekts dies nicht zulässt, sollten Sie überlegen, ob Sie das Modell in mehrere Teile aufteilen und diese anschließend zusammensetzen.