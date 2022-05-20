Wandübergangslänge
====
Bei dünnen Teilen passen nicht alle Wände innerhalb der Form. Wenn das Teil an einigen Stellen dünner ist als an anderen, muss Cura an einigen Stellen eine andere Anzahl von Wänden verwenden. Diese Einstellung steuert, wie breit der Übergangsbereich sein wird, in dem eine Wand hinzugefügt oder entfernt wird.

<!--screenshot {
"image_path": "wall_transition_length_0_2.png",
"models": [{"script": "wedge.scad"}],
"camera_position": [-7, 0, 75],
"settings": {"wall_transition_length": 0.2},
"colours": 64
}-->
<!--screenshot {
"image_path": "wall_transition_length_1_5.png",
"models": [{"script": "wedge.scad"}],
"camera_position": [-7, 0, 75],
"settings": {"wall_transition_length": 1.5},
"colours": 64
}-->
![Ein sehr kurzer Übergang](../../../articles/images/wall_transition_length_0_2.png)
![Ein längerer Übergang](../../../articles/images/wall_transition_length_1_5.png)

Der Übergangsbereich zwischen einer unterschiedlichen Anzahl von Wänden ist immer etwas problematisch. Am deutlichsten wird dies, wenn eine einzelne Linie in der Mitte endet und die beiden umgebenden Wände die Lücke füllen müssen. Sie füllen den Raum nicht sofort aus, und es bleibt eine Lücke. Dies führt zu winzigen Löchern auf der Ober- und Unterseite der Drucke. Das Gegenteil ist der Fall, wenn sich zwei Wände zu einer vereinigen, so dass sie sich für einen Moment überlappen, bis sie sich zusammengefügt haben. Die Überextrusion kann zu Maßungenauigkeiten führen, vor allem, wenn sie an der Außenwand auftritt. All dies kann verhindert werden, indem der Übergang so kurz wie möglich gehalten wird.

Ein kurzer Übergang führt jedoch auch dazu, dass die Düse einige sehr scharfe Kurven fährt, um diesen Spalt schnell zu füllen. Dies führt zu einem stärkeren Ringing, insbesondere wenn dies beim Drucken der Außenwand auftritt. Ein längerer Übergang verringert die Beschleunigungen in der Düse, insbesondere wenn dadurch die [jerk](../speed/jerk_print.md) Grenze unterschritten wird.

Es ist sinnvoll, diese Länge auf das Ein- oder Zweifache der Zeilenbreite einzustellen. Bei Druckern mit schwächeren Rahmen oder schwereren Druckköpfen muss die Länge möglicherweise erhöht werden, während Drucker, die schnell beschleunigen können, ohne dass es zu Ringing kommt, es sich leisten können, den Übergang zu verkürzen, um die visuelle Qualität zu verbessern.

**Diese Einstellung gilt nicht nur für normale Wände, sondern auch für Wände mit zusätzlicher Außenhaut, Support-Wände, Füllungen und konzentrische Muster.**