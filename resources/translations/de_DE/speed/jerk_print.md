Ruckfunktion Drucken
====
Der Ruck bestimmt die Geschwindigkeit, mit der die Düse durch Kurven fahren kann. Bei hohen Ruckwerten wird die Düse bei der Annäherung an eine Kurve nicht so stark abgebremst, was zu einer konstanteren Geschwindigkeit, aber auch zu stärkeren Vibrationen führt.

**Ruck im 3D-Druck ist nicht dasselbe wie Ruck in der Physik.** Der Begriff "Ruck" wurde von Marlin eingeführt. Er wurde dort als Abhilfe für das inhärente Problem des Versuchs, einem Pfad perfekt zu folgen, entwickelt. Da die Düse (theoretisch) nicht von der Bahn abweichen darf, müsste sie in jeder Ecke auf 0 mm/s abbremsen. Dies würde Ihren Druck ruinieren, da das Abbremsen auf 0 mm/s in jeder Ecke einen Klecks verursachen würde. Die Düse darf weder Kurven fahren, um die Ecke abzukürzen, noch darf sie überschießen. Stattdessen lässt Marlin eine sofortige Änderung des Geschwindigkeitsvektors in jeder Ecke zu. Das Ausmaß dieser Änderung des Geschwindigkeitsvektors wird als "Ruck" bezeichnet. Der Ruck ist also die maximale augenblickliche Änderung der Geschwindigkeit in jeder Ecke der Bewegung.

Die Erhöhung des Rucks hat einige positive und einige negative Auswirkungen auf Ihren Druck:
* Die Druckzeit wird verkürzt, da die Düse in den Ecken weniger abbremst.
* Da die Düse nicht bis zum Stillstand verlangsamt wird, erhalten Sie weniger Kleckse in den Ecken. Die Düse bewegt sich in einem konstanteren Tempo, so dass sie nicht in der Ecke verweilt, während weiterhin Material aus der Öffnung fließt.
* Der Drucker wird im Allgemeinen bei jeder Ecke stärker vibrieren, da der Druckkopf angewiesen ist, bei theoretisch unendlicher Beschleunigung sofortige Richtungsänderungen vorzunehmen. Diese Vibrationen neigen dazu, Unebenheiten Ihrem Druck zu erzeugen, was zu verminderter Maßgenauigkeit führt.
* Bei extremen Werten besteht die Möglichkeit, dass Ihre Motoren in den Ecken einige Schritte verlieren, was eine Schichtverschiebung verursachen kann.