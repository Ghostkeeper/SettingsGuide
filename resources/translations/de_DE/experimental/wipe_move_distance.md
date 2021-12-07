Abstand Wischbewegung
====
Mit dieser Einstellung können Sie festlegen, wie breit die Abwischbewegungen sein müssen. Die Düse bewegt sich bei [jeder Abwischbewegung](wipe_repeat_count.md) um diese Distanz.

Anfänglich wird die Düse direkt hinter dem Abwischen in einer [bestimmten X-Koordinate](wipe_brush_pos_x.md) platziert. Der in dieser Einstellung angegebene Abstand muss so gewählt werden, dass die Düse auf der anderen Seite des Pinsels platziert wird, wenn sie um diesen Abstand verschoben wird. Ein zu großer Abstand führt zu unnötigen Bewegungen und kann dazu führen, dass sich die Düse in das Bauvolumen zurückbewegt, was dazu führen kann, dass sie unnötigerweise auf das Modell trifft, wenn [Z-Sprünge nicht aktiviert sind](wipe_hop_enable.md). Wenn sie sich nicht weit genug bewegt, kann sie den Pinsel nicht richtig treffen.

Der Abstand kann auch negativ sein. Die Düse wird dann in die andere Richtung abwischen. Je nach Wahl der [X-Koordinate](wipe_brush_pos_x.md) kann dies notwendig sein, um in die richtige Richtung abzuwischen.