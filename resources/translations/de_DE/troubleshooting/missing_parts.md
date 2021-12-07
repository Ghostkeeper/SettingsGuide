Fehlende Teile
====
Manchmal sieht es bei der Überprüfung der Schichtansicht (oder, wenn Sie Pech haben, beim Drucken) so aus, als ob einige Teile des Drucks fehlen würden. Dies kann verschiedene Gründe haben. Dieser Artikel nennt ein paar Möglichkeiten.

Nicht-geschlossene Netze
----
Manche Netze haben Löcher in ihrer Oberfläche oder zusätzliche Geometrie im Inneren. Das verwirrt Cura, weil es nicht mehr klar ist, welche Teile des Volumens zum Inneren gehören und welche nicht. Wenn Sie einen Querschnitt des Modells betrachten, zählt Cura von außen nach innen. Die erste Fläche, die es durchquert, bedeutet, dass es ins Innere des Modells geht. Die zweite Fläche bedeutet, dass es wieder nach außen geht. Die dritte Fläche, die er kreuzt, bedeutet, dass er wieder nach innen geht, und so weiter. Wenn Teile der Flächen fehlen oder wenn es in der Mitte zusätzliche lose Flächen gibt, wird das Innere mehrdeutig, je nachdem, von welcher Seite man es betrachtet.

![Bei geschlossenen Netzen ist es klar, wo das Innere des Modells liegt](../../../articles/images/manifold_correct.svg)
![Bei nicht-geschlossenen Netzen ist das Volumen des Netzes nicht eindeutig](../../../articles/images/manifold_incorrect.svg)

Netze, die solche fehlenden Flächen oder zusätzlichen Teile haben, werden als Non-Manifold bezeichnet, da sie in der realen Welt nicht existieren können. Cura versucht, sie zu ergänzen, indem es kleine Lücken schließt, aber wenn eine Fläche nicht ergänzt werden kann, wird sie nicht gedruckt (es sei denn, der [Oberflächenmodus](../blackmagic/magic_mesh_surface_mode.md) ist so eingestellt, dass sie mit einbezogen wird). Die fehlende oder zusätzliche Geometrie wird auch in der 3D-Szene mit einem gepunkteten Muster angezeigt, oder in der Vorbereitungsphase in Rot, wenn die Röntgenansicht verwendet wird. Dabei wird die Fläche anders eingefärbt, wenn sie zu einer ungeraden Anzahl von Flächen gehört, was nur der Fall ist, wenn das Netz nicht vielfältig ist. So können Sie Probleme mit Ihrem Netz erkennen. Sie müssen diese Netze dann in einer CAD- oder Modellierungsanwendung reparieren.

![In der Röntgenansicht werden nicht-geschlossene Netze mit roten Teilen angezeigt.](../../../articles/images/x_ray.png)

Während Cura normalerweise davon ausgeht, dass das Netz vielfältig ist, kann es in einigen Fällen das Modell korrigieren. Dies sind einige Dinge, die Sie versuchen können:
* [Extensives Stitching](../meshfix/meshfix_extensive_stitching.md) behandelt Fälle besser, in denen zusätzliche Geometrie an der Außenseite eines Modells angebracht ist, obwohl es etwas mehr Zeit zum Slicen benötigt.
* [Unterbrochene Flächen beibehalten](../meshfix/meshfix_keep_open_polygons.md) schließt alle offenen Schleifen mit einer geraden Linie. Dadurch werden kleine Lücken sehr gut geschlossen. Allerdings kann das Modell dadurch auch sehr seltsam aussehen, wenn es große Lücken enthält.
* Als letzter Ausweg kann der [Oberflächenmodus](../blackmagic/magic_mesh_surface_mode.md) verwendet werden, um Teile mit Löchern nur als eine einzige Wand zu drucken, ohne jeglichen Inhalt. Da nicht bekannt ist, wo sich das Innere dieses Teils befindet, wird es keine Füllung oder Außenhaut geben, aber zumindest die Umrisse können gezeichnet werden. In einigen Fällen kann dies dazu führen, dass der Druck noch passabel aussieht.

Wenn diese Optionen nicht zu dem gewünschten Druck führen, müssen Sie sie manuell mit 3D-Modellieranwendungen reparieren.

Dünne Teile
----
Wenn das Modell sehr feine Details hat, kann nicht alles mit den dicken Linien gezeichnet werden, die aus Ihrem 3D-Drucker kommen. Cura passt die Linien in die Form ein, die durch Ihr Netz umrissen wird. Wenn dies nicht möglich ist, wird nichts gedruckt. In diesem Fall kann es so aussehen, als ob Teile des Drucks fehlen würden.

Es gibt einige Möglichkeiten, um dies zu ändern:
* Verringern Sie die [Linienbreite](../resolution/line_width.md). Wenn Sie etwas drucken, das dünne Wände oder Stege hat, stellen Sie sicher, dass die Linienbreite etwas kleiner ist als die Mindestbreite des betreffenden Teils. Wenn Sie die Linienbreite jedoch zu stark reduzieren, kann es zu [underextrusion](underextrusion.md) aufgrund von unzureichendem Fluss kommen. Um die Linienbreite weiter zu verringern, müssen Sie eine kleinere Düse verwenden.
* Fügen Sie dem Druck eine [horizontale Erweiterung](../shell/xy_offset.md) hinzu. Dadurch wird das gesamte Modell an allen Seiten breiter, auch die dünnen Teile. Sie werden dadurch weniger dünn, so dass sie nun gedruckt werden können. Dies ruiniert natürlich auch jegliche Massgenauigkeit und Detailtreue des Drucks, da alles dicker wird.
* Aktivieren Sie die Einstellung [Drucken von dünnen Wänden](../shell/fill_outline_gaps.md). Damit wird versucht, die dünnen Teile mit sehr kleinen Linien zu füllen, ohne die Linienbreite des restlichen Modells zu verringern. Dies führt jedoch zu großen Veränderungen in der Fließgeschwindigkeit des Materials und füllt die Wände möglicherweise nicht immer mit schönen, gleichmäßigen Linien.
* Denken Sie daran, das Modell an den Druck anzupassen, indem Sie jedes Teil mindestens so dick wie Ihre Linienbreite machen.