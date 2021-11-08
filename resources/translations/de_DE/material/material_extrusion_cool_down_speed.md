Geschwindigkeitsregulierer für Abkühlung bei Extrusion
====
Wenn [Automatische Temperatur](../experimental/material_flow_dependent_temperature.md) aktiviert ist, wird die Drucktemperatur je nach der Menge des extrudierten Materials angepasst.

Wenn das Material in der Düsenkammer erhitzt wird, entzieht dies der Düse Wärme. Je schneller das Material extrudiert wird, desto mehr Wärme wird der Düse entzogen. Wenn sich der Temperaturfühler nicht genau an der Düsenspitze befindet, führt dies dazu, dass die Düse beim Extrudieren von Material eine etwas niedrigere Temperatur hat als im Leerlauf, selbst bei einem guten PID-Regler.

Diese Einstellung beschreibt, wie viel Wärme in der Düse während des Drucks verloren geht. Die zusätzliche Wärme, die beim Extrudieren verloren geht, wird dann durch eine Erhöhung der gewünschten Drucktemperatur aus dem G-Code kompensiert. Der Wert der Einstellung hängt von der Düsenkonstruktion, der Wärmekapazität des gedruckten Materials und der Extrusionsrate ab.