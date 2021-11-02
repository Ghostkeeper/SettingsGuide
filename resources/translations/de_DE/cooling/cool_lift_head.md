Druckkopf anheben
====
Wenn die [Mindestzeit für Schicht](cool_min_layer_time.md) erreicht ist, wird der Druckkopf verlangsamt, um zu verhindern, dass schneller als die Mindestschichtzeit gedruckt wird. Auf diese Weise erhält die vorherige Schicht genügend Zeit zum Abkühlen und Aushärten, bevor die nächste Schicht aufgetragen wird. Der Druckkopf wird so lange verlangsamt, bis die [Mindestgeschwindigkeit](cool_min_speed.md) erreicht ist.

Wenn diese Einstellung aktiviert ist und der Druckkopf sich langsamer als die Mindestgeschwindigkeit bewegen soll, um die Mindestschichtzeit einzuhalten, bewegt sich der Druckkopf nach dem Drucken der Schicht leicht nach oben. Er wartet dann eine Weile, bis die Mindestzeit für die Schicht erreicht ist, bevor er mit der nächsten Schicht beginnt.

Wenn diese Einstellung deaktiviert ist, fährt der Drucker sofort mit der nächsten Schicht fort. Er wartet nicht auf die Mindestschichtzeit, so dass Schichten über Schichten gedruckt werden, die möglicherweise noch nicht vollständig ausgehärtet sind.

![Wenn die Mindestschichtzeit erreicht ist, kann sich der Kopf anheben](../images/cool_fan_speed.svg)

Der Druckkopf wird immer um 3 mm angehoben. Zurzeit gibt es keine Möglichkeit um dies zu konfigurieren.

Kompromisse
----
Es gibt einen Kompromiss, wenn die Düse verlangsamt wird, damit die Schicht besser abkühlen kann. Die Mindestschichtzeit soll dem Material etwas Zeit zum Abkühlen geben, indem die Bewegung des Druckkopfs verlangsamt wird. Während dieser Zeit blasen die Lüfter mit maximaler Leistung, um das Material schneller abzukühlen, aber die heiße Düse ist immer noch auf dem Kunststoff. Bei sehr kleinen Teilen kann die heiße Düse mehr Wärme in den Druck übertragen, als die Lüfter abblasen können. Dies führt dazu, dass der Kunststoff noch stärker schmilzt, als wenn Sie keine Mindestschichtzeit hätten.

Mit Druckkopf anheben wird dieser Kompromiss gelöst. Sie können immer noch bis zu einem gewissen Punkt verlangsamen, aber bei sehr kleinen Schichten wird die heiße Düse wegbewegt, so dass sie keine Wärme mehr in den Druck überträgt. Der Druckkopf bleibt dabei so nah, dass etwaige Lüfter am Druckkopf weiterhin auf den Druck blasen.

Der Nachteil dieses Verfahrens ist, dass es effektiv einen [Z-Sprung](../travel/retraction_hop.md) ausführt, was wiederum zu [stringing](../troubleshooting/stringing.md) führt. Das Anheben des Kopfes kann es zwar das Durchhängen und das Blobing verbessern, verursacht aber eine andere Art von Problemen. Ein wenig manuelle Nachbearbeitung mit einem Messer kann die dadurch verursachten Fäden beseitigen.