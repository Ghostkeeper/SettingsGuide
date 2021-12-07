Herunterfallen bei Drucken mit Drahtstruktur
====
Beim Drucken des Drahtrahmens ist damit zu rechnen, dass das Material aufgrund der latenten Wärme durchhängt, bevor es sich verfestigen kann. Dadurch würde das Sägezahnmuster zu kurz werden. Während sich die horizontalen Ringe aufgrund der kontinuierlichen horizontalen Bewegung überbrücken können, ist dies beim Sägezahnmuster nicht möglich. Diese Einstellung gleicht die kurze Statur des Sägezahnmusters aus, indem sie das Muster etwas höher macht, so dass der nächste horizontale Ring richtig auf ihm aufliegt.

![Wie die Höhe des Sägezahnmusters kompensiert wird](../../../articles/images/wireframe_fall_down.svg)

Der Wert der Einstellung wird zur Höhe der Sägezähne addiert. Dadurch wird hoffentlich das Durchhängen beim Drucken dieser Sägezähne kompensiert. Wenn die Einstellung richtig ist, wird der horizontale Ring fest auf dem Sägezahnmuster gedruckt, anstatt tiefer als die beabsichtigte Druckhöhe zu fallen.

In Kombination mit [Nachziehen](wireframe_drag_along.md) wird die Höhe des Sägezahnmusters zur normalen [Höhe](wireframe_height.md) plus dem Wert der Einstellung Nachziehen plus dem Wert dieser Einstellung.