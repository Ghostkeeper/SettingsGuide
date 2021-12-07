Elefantenfuß
====
Manchmal ist die Unterseite des Drucks etwas breiter als der Rest des Drucks, so dass dort eine kleine Lippe entsteht. Dies wird als "Elefantenfuß" bezeichnet, da es den Beinen eines Elefanten ähnelt, bei denen die Zehen etwas breiter sind als der Rest des Beins.

Es gibt mehrere Effekte, die als Elefantenfuß bezeichnet werden und völlig unterschiedliche Ursachen haben. Diese erfordern auch völlig unterschiedliche Lösungen. Dieser Artikel wird Ihnen helfen, die Ursache zu finden.

![Durch die Stärke der Außenhaut verursachte Elefantenfüße](../../../articles/images/elephants_foot.jpg)

Brim
----
Manchmal ist der Elefantenfuß wirklich nur ein Teil des Brim, der nicht richtig entfernt wurde. Wenn Sie den Brim mit der Hand entfernt haben, können Sie das daran erkennen, dass die Brim-Linie vollständig an die normale Wandlinie angrenzt, und die normale Wandlinie liegt direkt unter dem Rest der Wand. Um den Rand vollständig zu entfernen, ritzen Sie am besten mit einem scharfen Messer an der Unterseite Ihres Drucks entlang.

Wenn das Modell keine große Unterseite hat, sollten Sie den [Druckplattenhaftungstyp](../platform_adhesion/adhesion_type.md) stattdessen auf Skirt einstellen. Wenn dies zu große Probleme mit der Haftung des Bettes verursacht, können Sie alternative Methoden zur Verbesserung der Haftung ausprobieren, wie z.B. die Einstellung des [Musters für die erste untere Schicht](../top_bottom/top_bottom_pattern_0.md) auf "Konzentrisch" stellen.

Warping
----
Die wohl häufigste Ursache für einen echten Elefantenfuß ist das Verziehen. Wenn das Material abkühlt, schrumpft es ein wenig. Das Material der unteren Schicht(en) kann manchmal nicht schrumpfen. Es behält seine ursprüngliche Größe, aber die darüber liegenden Schichten schrumpfen ein wenig. Es gibt mehrere Gründe, warum die unteren Schichten nicht schrumpfen können:
* Sie klebt an der Bauplatte, die nicht schrumpft.
* Sie wird von der Bauplatte erwärmt, wodurch sie nicht schrumpfen kann.
* Es befindet sich eine Außenhaut daneben, die das Schrumpfen verhindert. (In höheren Schichten kann es stattdessen eine Füllung geben).

Um das Warping zu verhindern, werfen Sie einen Blick in den [Artikel Fehlerbehebung Warping](warping.md). Speziell für diese Art des Warping gibt es ein paar Dinge, die Sie versuchen können:
* Erhöhen Sie die [Wandstärke](../shell/wall_thickness.md), um zu verhindern, dass die Wände neben der Füllung schrumpfen.
* Verringern Sie die [Temperatur der Druckplatte](../material/material_bed_temperature.md), damit die erste Schicht genauso stark schrumpft wie die anderen Schichten. Wenn die Betttemperatur sehr hoch war, kann sie auch dazu führen, dass das Material ein wenig nachgibt, wodurch es unten breiter wird. Dieser Effekt ist in der Regel gering, lässt sich aber auch durch eine Verringerung der Betttemperatur verhindern.
* Erhöhen Sie die [Dicke der unteren Schicht](../top_bottom/bottom_thickness.md), um allmählich zu einer schrumpfenden Größe überzugehen. Sie können sogar in Erwägung ziehen, das Modell komplett massiv zu drucken (vorzugsweise, indem Sie die Bodendicke extrem hoch einstellen), um den Unterschied in der Schrumpfung vollständig zu beseitigen.

Druckbett Justierung
----
Der Elefantenfuß kann auch dadurch verursacht werden, dass die Bauplatte beim Drucken der ersten Schicht zu nahe an der Düse liegt. Dadurch wird die erste Schicht überextrudiert und nach außen gedrückt.

Um die Bauplatte zu justieren, sehen Sie im Handbuch Ihres 3D-Druckers nach. Die meisten Drucker verfügen über Einstellschrauben im Bett oder im Portal, um den Höhenunterschied der Bauplatte während der ersten Schicht einzustellen. Passen Sie die Bauplatte während des Druckens an (vorzugsweise während des Brims, Skirt oder Rafts), bis die erste Schicht schön glatt und nicht dünner als die anderen Schichten ist.

Sie können auch direkt den [Fluss der ersten Schicht](../material/material_flow_layer_0.md) in Cura anpassen, um eine eventuelle Überextrusion auszugleichen. Alternativ kann auch eine Reduzierung der [Linienbreite in der ersten Schicht](../resolution/initial_layer_line_width_factor.md) die Extrusion soweit normalisieren, dass der Elefantenfuß verhindert wird.

Verformung oberhalb des Glasübergangs
----

Bei sehr kleinen Drucken besteht die Möglichkeit, dass die vorherige Schicht noch nicht ausgehärtet ist, wenn die nächste Schicht auf sie aufgebracht wird. Das Material wird mit beträchtlicher Kraft aus der Düse gedrückt. Wenn die vorherige Schicht noch nicht ausgehärtet ist, wird diese Schicht zusammengedrückt und dehnt sich horizontal aus. Dies äußert sich in Form eines Elefantenfußes. Die Lösung für dieses Problem besteht darin, dafür zu sorgen, dass das Material zu dem Zeitpunkt, an dem die nächste Schicht darauf aufgebracht wird, ausgehärtet ist. Versuchen Sie, die folgenden Einstellungen zu ändern:

* Reduzieren Sie die [Drucktemperatur für die erste Schicht](../material/material_print_temperature_layer_0.md), so dass das Material nicht so stark abkühlen muss.
* Reduzieren Sie die [Druckbetttemperatur für die erste Schicht](../material/material_bed_temperature_layer_0.md), damit die erste Schicht schneller abkühlt, indem mehr Wärme an die Bauplatte abgegeben wird. Kunststoffe für den 3D-Druck sind so konstruiert, dass sie bei einem bestimmten Temperaturpunkt, der [Glasübergangstemperatur](https://en.wikipedia.org/wiki/Glass_transition#Transition_temperature_Tg), sehr schnell erstarren. Um Verformungen zu vermeiden, sollten Sie die Glasübergangstemperatur Ihres Filaments im Datenblatt nachschlagen und sicherstellen, dass die Temperatur des Druckbetts nicht zu weit über diese Übergangstemperatur steigt.
* Erhöhen Sie die [Lüftergeschwindigkeit während der ersten Schichten](../cooling/cool_fan_speed_0.md), um das Material schneller abzukühlen. Erwägen Sie auch die Erhöhung der Einstellung [Normaldrehzahl des Lüfters bei Höhe](../cooling/cool_fan_full_at_height.md), um die ersten Schichten weiter abzukühlen.
* Reduzieren Sie die [Geschwindigkeit der ersten Schicht](../speed/speed_layer_0.md). Dadurch hat die erste Schicht mehr Zeit, um nach dem Drucken abzukühlen.
* Erhöhen Sie die [Mindestzeit für Schicht](../cooling/cool_min_layer_time.md). Damit soll sichergestellt werden, dass jede Schicht eine gewisse Zeit abkühlen kann, bevor die nächste Schicht darauf gelegt wird, und außerdem wird die [Maximaldrehzahl des Lüfters](../cooling/cool_fan_speed_max.md) verwendet. Auf diese Weise lassen sich die oben genannten Anpassungen für die anfängliche Geschwindigkeit der Schicht und die Lüftergeschwindigkeit einfacher kombinieren. Beachten Sie jedoch, dass dies für den gesamten Druck gilt, nicht nur für die erste Schicht. 

Allgemeine Lösungen
----
Hier sind ein paar Lösungen, die Sie ausprobieren können, um jede Art von Elefantenfuß zu beseitigen, unabhängig von seiner Ursache:
* Mit einem [Raft](../platform_adhesion/adhesion_type.md) wird der gesamte Druck von der Bauplatte wegbewegt, wodurch durch die Bauplatte verursachte Effekte wie ihre Temperatur und ein zu starkes Anhaften an der Bauplatte verhindert werden, und auch die Notwendigkeit eines Brim wird so vermieden.
* Reduzieren Sie die [Horizontale Erweiterung für die erste Schicht](../shell/xy_offset_layer_0.md) (möglicherweise auf einen negativen Wert). Dies kompensiert den Elefantenfuß in der ersten Schicht.