Abstandspriorität der Stützstruktur
====
Sowohl der [X/Y-Abstand](support_xy_distance.md) als auch der [Z-Abstand](support_z_distance.md) des Supports sollten genau eingehalten werden, nicht mehr und nicht weniger. Dies ist eine Beschränkung, so dass es eine Präferenz zwischen den beiden geben muss. Diese Einstellung legt diese Präferenz fest.

X/Y hat Vorrang vor Z
----
![X/Y hat Vorrang vor Z](../../../articles/images/support_xy_overrides_z.svg)

Wenn der X/Y-Abstand Vorrang vor dem Z-Abstand hat, dann wird der X/Y-Abstand immer konstant gehalten, auch wenn das bedeutet, dass der Z-Abstand größer als gewünscht ist. Der Z-Abstand wird jedoch immer noch als Mindestabstand beibehalten. Wenn der Überhang also sehr horizontal ist, wirkt sich der Z-Abstand trotzdem aus und macht den X/Y-Abstand größer als gewünscht.

Z hat Vorrang vor X/Y
----
![Z hat Vorrang vor X/Y](../../../articles/images/support_z_overrides_xy.svg)

Wenn der Z-Abstand Vorrang vor dem X/Y-Abstand hat, dann wird der Z-Abstand immer konstant gehalten, auch wenn das bedeutet, dass der X/Y-Abstand kleiner als gewünscht ist. Der X/Y-Abstand hat dann nur dort Einfluss auf den Druck, wo der Z-Abstand nicht ins Spiel kommt, also nicht oben auf den Support-Strukturen, sondern nur an den Seiten.

Ein minimaler X/Y-Abstand wird aber immer noch eingehalten. Wenn der Überhang sehr vertikal ist, würde der X/Y-Abstand so klein werden, dass der Support mit den Seiten des Modells verschmelzen könnte. Der [Minimale X/Y-Abstand](support_xy_distance_overhang.md) verhindert dies.