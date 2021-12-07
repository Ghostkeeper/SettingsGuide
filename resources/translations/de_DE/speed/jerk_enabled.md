Rucksteuerung aktivieren
====
Der Ruck bestimmt die Geschwindigkeit, mit der die Düse durch Ecken fahren kann. Wenn die Ruckkontrolle aktiviert ist, bestimmt Cura, wie viel Ruck während der verschiedenen Teile des Drucks angewendet werden soll. Wenn sie deaktiviert ist, wählt die Drucker-Firmware einen Ruckwert. Der Ruckwert des Druckers ist in der Regel ziemlich hoch, um dem Slicer mehr Kontrolle zu geben, aber er hat möglicherweise mehr Informationen über seine eigene Hardware als Cura. 

![Die Beziehung zwischen Geschwindigkeit, Beschleunigung und Ruck](../../../articles/images/velocity_acceleration_jerk.svg)

**Ein Ruck im 3D-Druck ist nicht dasselbe wie ein Ruck in der Physik.** Der Begriff "Ruck" wurde von Marlin eingeführt. Er wurde dort als Abhilfe für das inhärente Problem des Versuchs, einer Bahn perfekt zu folgen, entwickelt. Da die Düse (theoretisch) nicht von der Bahn abweichen darf, müsste sie in jeder Ecke auf 0 mm/s abbremsen. Dies würde Ihren Druck ruinieren, da das Abbremsen auf 0 mm/s in jeder Ecke einen Klecks verursachen würde. Die Düse darf weder Kurven fahren, um die Ecke abzukürzen, noch darf sie überschießen. Stattdessen lässt Marlin eine sofortige Änderung des Geschwindigkeitsvektors in jeder Ecke zu. Das Ausmaß dieser Änderung des Geschwindigkeitsvektors wird als "Ruck" bezeichnet.

Der Ruck ist also die maximale momentane Geschwindigkeitsänderung, die an jeder Ecke der Bewegung auftritt.

Firmware, die nicht auf Marlin basiert, wie z.B. die Sailfish-Firmwarefamilie, ignoriert Änderungen in jerk. Diese Einstellung hat dann keine Auswirkung.

Beispiel für die Mathematik des Rucks
----
Nehmen wir als Beispiel einen sehr einfachen Druck: Bewegen Sie zuerst 100 mm nach rechts, dann 100 mm nach unten. Die Druckgeschwindigkeit ist auf 50mm/s eingestellt. Die Beschleunigung ist auf 1000mm/s^2 eingestellt. Der Ruck ist auf 10mm/s eingestellt. Das wird passieren:
1. Zu Beginn eines Druckvorgangs benötigt Marlin die Hälfte des Ruckwertes, um zu starten, so dass er theoretisch sofort auf 5 mm/s beschleunigt.
2. Bei einer Beschleunigung von 1000mm/s^2 benötigt er 0,045s, um von 5mm/s auf die maximale Geschwindigkeit von 50mm/s zu beschleunigen. In dieser Zeit legt die Düse 1,2375 mm zurück.
3. Die Düse fährt eine Zeit lang mit der maximalen Druckgeschwindigkeit 50mm/s.
4. Marlin berechnet, mit welcher Geschwindigkeit die Düse durch die Ecke fahren kann: Die Düse macht eine 90-Grad-Ecke, zuerst nach rechts, dann nach unten. Um diese Geschwindigkeitsänderung zu begrenzen, wird sie mit cos(90/2) * (10/2)mm/s nach rechts in die Ecke einfahren und mit cos(90/2) * (10/2)mm/s nach unten wieder herausfahren. Sie wird also mit etwa 7,07 mm/s durch die Ecke fahren.
5. Es dauert 0,043s, um von einer Geschwindigkeit von 50mm/s auf 7,07mm/s abzubremsen.
6. Die Kurve wird mit einer sofortigen Geschwindigkeitsänderung durchfahren. Der Betrag der Differenz zwischen den Vektoren [7,07, 0] und [0, 7,07] beträgt genau 10 mm/s, so dass die Kurve sofort durchfahren werden kann.
7. Es braucht 0,043s, um von 7,07mm/s auf 50mm/s zu beschleunigen.
8. Die Düse fährt wieder eine Weile mit der maximalen Druckgeschwindigkeit von 50mm/s.
9. Gegen Ende des Druckvorgangs wird die Düse in 0,05s von 50mm/s auf 0mm/s abgebremst.