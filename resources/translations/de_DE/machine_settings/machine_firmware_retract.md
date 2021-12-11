Firmware-Einzug
====
Normalerweise bewirkt Cura einen Einzug, indem es die Bewegung des Feeders steuert und ihm befiehlt, das Filament ein Stück einzuziehen. Wenn diese Einstellung aktiviert ist, wird stattdessen ein `G10`-Befehl geschrieben, der bedeutet, dass der Drucker das Filament einziehen muss, oder ein `G11`-Befehl zum vorschieben.

Wenn Sie sich für die Verwendung von Firmware-Einzugen entscheiden, steuert die Firmware des Druckers, wie weit und wie schnell das Filament eingezogen werden soll. Der Drucker weiß möglicherweise mehr über seine eigene Geometrie als Cura, so dass er besser entscheiden kann, wie das Filament eingezogen werden soll. Dies bedeutet jedoch, dass Cura nicht mehr die Kontrolle über diese Einzüge hat und Cura mehr über den Druck selbst weiß. Im Grunde haben der Slicer und die Firmware unterschiedliche Informationen, und diese Einstellung entscheidet, wer von beiden die Wahl hat.

**Da es sich um eine Maschineneinstellung handelt, ist diese Einstellung normalerweise nicht in der Einstellungsliste sichtbar.**