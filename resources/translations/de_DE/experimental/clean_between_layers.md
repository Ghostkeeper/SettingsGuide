Düse zwischen den Schichten abwischen
====
Diese Einstellung aktiviert eine Prozedur, die am Ende jeder Schicht ausgeführt wird, um jegliches Material von der Düsenspitze abzuwischen. Wenn Sie einen Drucker mit einer eingebauten Wischbürste haben, veranlasst die Aktivierung dieser Einstellung Cura, den Drucker anzuweisen, die Düse periodisch mit dieser Bürste abzuwischen.

![Visualisierung der Bewegungen während des Wischvorgangs](../../../articles/images/clean_between_layers.svg)

Dieses Wischverfahren besteht aus einer Reihe von Schritten:
1. Wenn [Abwischen bei Einzug aktiviert ist](wipe_retraction_enable.md), wird das Material eingezogen.
2. Wenn [Z-Sprung beim Abwischen](wipe_hop_enable.md) eingeschaltet ist, wird die Düse nach oben oder die Bauplatte nach unten bewegt.
3. Die Düse wird über die [Position des Pinsels](wipe_brush_pos_x.md) hinaus bewegt.
4. Die Düse wird [eine Anzahl von Malen](wipe_repeat_count.md) auf dem Pinsel abgewischt.
5. Die Düse wird wieder in ihre ursprüngliche Position gebracht.
6. Der Z-Sprung wird beendet, falls er aktiviert war. Das Material wird zurückgeschoben.
7. Der Druck pausiert für eine [bestimmte Zeit](wipe_pause.md).

Ziel dieses Verfahrens ist es, die Düse regelmäßig von Verunreinigungen zu befreien. Einige Materialien neigen dazu, aufgrund der hohen Oberflächenspannung durch Kapillarwirkung zur Düse aufzusteigen. Diese können in den Druckkopf gelangen und sich dort ansammeln, wodurch der Druckkopf beschädigt werden kann. Andere Materialien, die Fasern oder andere Füllungen enthalten, können dazu führen, dass die Füllung beim Drucken auf die Düse gespritzt wird. Dadurch wird dieses Material abgewischt.

Das Wischverfahren ist jetzt allerdings nicht sehr konfigurierbar. Es wird immer in X-Richtung gewischt, wobei die Y-Position der letzten Position im Druck beibehalten wird. Das bedeutet, dass ein Drucker mit einer Bürste in einer Ecke nicht gut mit dieser Funktion arbeiten wird. Man bräuchte einen Pinsel entlang einer ganzen Seite des Bauvolumens.