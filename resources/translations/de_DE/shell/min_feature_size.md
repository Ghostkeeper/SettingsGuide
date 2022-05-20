Mindestgröße des Merkmals
====
Diese Einstellung steuert die Mindestbreite der Details des Modells, die gedruckt werden sollen. Alles, was dünner als dieser Wert ist, wird nicht gedruckt.

Details, die kleiner als die Düsengröße sind, werden wahrscheinlich nicht gut gedruckt. Dies ist eine Einschränkung des Druckers. Cura kann dennoch versuchen, sie zu drucken, wobei es in Kauf nimmt, dass die Extrusionsrate nicht gut ist oder dass die Details am Ende dicker als modelliert sind.

Wenn Sie die minimale Merkmalgröße verringern, druckt der Drucker kleinere Details des Drucks. Abhängig von der [Minimale Wandlinienstärke](min_bead_width.md) können diese winzigen Details gedruckt werden, indem sehr wenig extrudiert wird (was zu einer [unterextrusion](../troubleshooting/underextrusion.md) führt), oder indem vernünftigere Linienbreiten extrudiert, aber überdimensioniert gedruckt werden. Wenn Sie diesen Wert auf 0 setzen, geht der Drucker bis in die äußersten Spitzen jeder scharfen Ecke.

Wenn Sie die minimale Merkmalgröße erhöhen, braucht sich der Drucker nicht um kleine Details zu kümmern, die ohnehin nicht gut herauskommen würden. Das spart ein wenig Zeit und kann dazu führen, dass der Druck sauberer wird.