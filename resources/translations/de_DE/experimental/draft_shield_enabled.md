Windschutz aktivieren
====
Wenn diese Einstellung aktiviert ist, baut der Drucker eine Hülle um Ihren Druck auf, die den Druck vor Luftströmungen aus der Umgebung schützt.

<!--screenshot {
"image_path": "draft_shield_enabled.png",
"models": [{"script": "headphone_hook.scad"}],
"camera_position": [-56, 139, 305],
"settings": {
    "draft_shield_enabled": true
},
"colours": 32
}-->
![Ein Windschutz wird um das Modell gedruckt](../../../articles/images/draft_shield_enabled.png)

Einige Drucker und Druckmaterialien sind sehr empfindlich gegenüber der Umgebung, in der sie gedruckt werden. Das Drucken an verschiedenen Stellen der Bauplatte kann zu unterschiedlichen Ergebnissen führen, da sie anfälliger für Luftströmungen von außen sind. Wenn der Druck über Nacht läuft und der Raum kälter wird, kann sich dies erheblich auf den Druck auswirken. Der Windschutz soll diesen Effekt verringern, indem er ein kleines, isoliertes Volumen um den Druck herum schafft. Dieser dient als behelfsmäßige "Heizkammer", um den Druck warm zu halten und ihn vor kalten Luftzügen von außen zu schützen.

Die Abschirmung wird während des Druckens des Modells gedruckt. Wenn mehrere Extruder am Druck beteiligt sind, wird der Windschutz mit dem Extruder gedruckt, der die Schicht beginnt. Dies geschieht abwechselnd von Schicht zu Schicht.

Der Windschutz hat mehrere wichtige Auswirkungen auf den Druck:
* Er hält die Temperatur des Drucks konstanter. Dies ist die beabsichtigte Wirkung des Windschutzes. Infolgedessen sollte die Streifenbildung aufgrund von Temperaturschwankungen im Raum reduziert werden.
* Im Allgemeinen ist die Temperatur im Inneren des Windschutzes höher als ohne Windschutz. Das liegt daran, dass die Wärme schwerer entweichen kann und keine Konvektionsströme mit der heißen Luft vom Druck aufsteigen können. Dies wirkt sich auf alle Aspekte des Drucks aus. Insbesondere kommt es zu mehr Fadenbildung und Durchhängen.
* Die Lüfter am Druckkopf werden weniger effektiv. Die Abschirmung stört auch dort den Luftstrom. Um die Wirksamkeit der Lüfter am Druckkopf zu erhöhen, kann der [X/Y-Abstand des Windschutzes](draft_shield_dist.md) vergrößert werden.
* Der Windschutz kann als [Sickerschutz](../dual/ooze_shield_enabled.md) fungieren. Wenn Fahrbewegungen in Richtung eines Objekts ausgeführt werden, das durch einen Windschutz geschützt ist, wird der an der Düse verbliebene Ooze auf dem Schild abgewischt.
* Der Windschutz kann als [Einzugsturm](../dual/prime_tower_enable.md) dienen. Da er vor dem Objekt gedruckt wird, ist der Druck des Windschutzes eine Möglichkeit, das Material zu spülen und richtig fließen zu lassen. Dies ist jedoch nur bei 2 Extrudern wirksam, da bei mehr als 2 Extrudern nicht alle gespült werden.