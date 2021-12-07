Druckgeschwindigkeit für Raft-Basis
====
Mit dieser Einstellung wird die Geschwindigkeit konfiguriert, mit der die unterste Schicht des Rafts gedruckt wird. Die Geschwindigkeit der unteren Schicht kann getrennt von der Geschwindigkeit der oberen und mittleren Schicht konfiguriert werden.

![Wo sich die unterste Schicht im Raft befindet](../../../articles/images/raft_dimensions_simplified.svg)

Wenn die Basisschicht langsamer gedruckt wird, kann das Material besser fließen. Dadurch vergrößert sich die Kontaktfläche zwischen dem Raft und der Bauplatte, so dass es besser an der Bauplatte haften kann. Wenn das Material länger heiß bleibt, wird der Kunststoff auch getempert, was die inneren Spannungen verringert. Beide Effekte verringern den Verzug. Die Basisschicht wird in der Regel langsamer gedruckt als die anderen Schichten. Wenn man die Druckgeschwindigkeit der Basisschicht zu sehr reduziert, dauert der Druck natürlich länger.

Wenn das Raft verwendet wird, gilt die [Druckgeschwindigkeit für die erste Schicht](../speed/speed_print_layer_0.md) des Modells und nicht für die erste Schicht des Rafts. Die Fahrtbewegungenn innerhalb des Rafts werden mit der normalen [Bewegungsgeschwindigkeit](../speed/speed_travel.md) durchgeführt.