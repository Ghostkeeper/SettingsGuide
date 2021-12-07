Coasting Brückenwand
====
Beim Überbrücken mit Wandlinien wird kurz vor dem Drucken einer Brücke der Materialvorschub für einen Moment angehalten. Während dieser Zeit kann das restliche Material in der Düsenkammer ausfließen, um den Druck in der Düsenkammer zu verringern. Diese Technik wird als [coasting](coasting_enable.md) bezeichnet. Mit dieser Einstellung kann der Umfang des Nachlaufs gesteuert werden. Damit wird im Wesentlichen gesteuert, wie weit vor einer Brücke das Material aufhört zu fließen.

Nachdem die Brücke fertiggestellt ist, wird das nicht extrudierte Material trotzdem ausgestoßen. Die Gesamtmenge des extrudierten Materials bleibt gleich. Dadurch wird der Druck auf die Düse wiederhergestellt, was eine Unterextrusion verhindert.

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
    "bridge_settings_enabled": true,
    "bridge_skin_density": 100,
    "bridge_skin_material_flow": 100,
    "bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![Keine Extrusion auf einer Seite der Brücke und zusätzliche Extrusion auf der anderen Seite](../../../articles/images/bridge_skin_density_100.png)

Die Einheit dieser Einstellung ist nicht intuitiv zu verstehen. Der Abstand vor der Brücke, bei dem das Material aufhört zu fließen, hängt von einer Reihe von Faktoren ab:
* Die Länge der bisherigen Wand bis zur Brücke. Je länger die Wand ist, desto mehr kann sie auslaufen.
* Die Fließgeschwindigkeit aus der Düse während der normalen Wand, die von der [Geschwindigkeit](../speed/speed_wall.md), der [Linienbreite](../resolution/wall_line_width.md), der [Fließgeschwindigkeit](../material/wall_material_flow.md) und der [Schichthöhe](../resolution/layer_height.md) dieser Wände abhängig ist. Je größer die Fließgeschwindigkeit in normalen Wänden ist, desto länger ist die Auslaufstrecke.
* Die Durchflussrate aus der Düse während der überbrückten Wand, hängt von der [Geschwindigkeit](bridge_wall_speed.md) und [Durchflussrate](bridge_wall_material_flow.md) dieser Wände ab. Je größer die Fließgeschwindigkeit in überbrückten Wänden ist, desto *kürzer* ist die Auslaufstrecke.

Diese Einstellung ist ein Multiplikationsfaktor für die endgültige Länge.

Der Zweck dieses Nachlaufs besteht darin, den Druck in der Düsenkammer zu senken. Dies ist notwendig, da ein verbleibender Druck in der Düsenkammer dazu führt, dass das Material über eine beträchtliche Strecke nach unten gedrückt wird, bevor es erstarrt, sobald der Gegendruck verschwindet. Dieses Herunterdrücken des Materials führt zu einer Durchbiegung. Im Wesentlichen werden die überhängenden Linien durch den Rest des Materials, der sich noch in der Düse befindet, nach unten gedrückt. Wenn der Druck in der Düsenkammer verringert wird, verringert sich auch diese Kraft, und es kommt zu einer geringeren Durchbiegung.

Wird der Nachlauf erhöht, verringert sich der Druck in der Düsenkammer bis zu dem Zeitpunkt, an dem die Brücke gedruckt werden muss, wodurch sich die Durchbiegung verringert. Der Druck ist dann genauer. Erhöht man jedoch die Nachlaufzeit zu stark, kommt es zu einer Phase der Unterextrusion, kurz bevor die Brücke gedruckt wird. Da sich diese Unterextrusion in den Wänden des Drucks befindet, wird sie auf der Seite des Drucks deutlich sichtbar sein.