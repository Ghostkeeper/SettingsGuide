Pillowing
====
Pillowing ist ein Effekt, bei dem kleine Beulen oder Löcher zwischen den Füllungslinien auf der Oberseite des Modells entstehen. Dieser Effekt tritt am häufigsten bei (ansonsten) flachen Oberseiten auf, wenn mit hohen Durchflussraten gedruckt wird.

![Starke Beulen und kleine Löcher in der Oberfläche](../../../articles/images/pillowing.jpg)

Ursache
----
Pillowing ist eine Kombination aus mehreren Effekten, die zusammenwirken, um einen Wölbungseffekt auf der Oberseite des Drucks zu verursachen.

Die erkennbare Wölbung der Außenhaut ist eigentlich eine Form des [warping](warping.md), bei der die Außenhaut durch die umgebenden Wände und die darunter liegende Füllung zusammengedrückt wird. Da die Wände und Füllungen in den unteren Schichten zuerst gedruckt werden, kühlen sie ab und schrumpfen, während die Außenhaut noch gedruckt wird. Während sie schrumpfen, drücken die Wände und die Füllung die Linien der Außenhaut nach innen, bis sie sich ausbeulen.

Ein weiterer wichtiger Faktor beim Pillowing ist das Absacken der Außenhaut zwischen den Fülllinien. Je nach Abstand zwischen den Füllungslinien müssen die Außenhautlinien eine gewisse Strecke überbrücken. Wenn die Kühlung unzureichend ist, wird der Kunststoff etwas durchhängen. Dadurch haften die Außenhäute nicht mehr so gut aneinander, und es entstehen Lücken zwischen ihnen. Es bedarf einiger Schichten Außenhaut, um dies zu beheben.

Der Pillow-Effekt wölbt sich eher nach oben als nach unten. Es kann zwar sowohl nach oben als auch nach unten gehen, aber die Ausbuchtung nach oben ist häufiger, da die Düse beim Überfahren der Außenhaut an der Oberseite des Kunststoffs zieht, was für einen kurzen Moment eine Scherkraft nach oben ausübt. Sobald sich die Linien nach oben wölben, werden sie durch den Warping-Effekt in der Höhe gehalten.

Prävention
----
Es gibt mehrere Methoden, um Pillowing in Cura zu verhindern:
* Die Erhöhung der [Obere Dicke](../top_bottom/top_thickness.md) ist die effektivste Methode, um Pillowing zu verhindern. Mit mehr [Oberen Schichten](../top_bottom/top_layers.md) können die höheren Schichten auf den teilweise geschlossenen Lücken der vorherigen Schichten aufliegen. Dadurch haben sie eine bessere Chance, die Lücken zu schließen und eine starke obere Schicht zu bilden, die nicht durchhängt. Im Allgemeinen gilt: Je dünner die Schichten sind, desto mehr obere Schichten werden benötigt, da diese Schichten nicht so stark sind.
* Durch Erhöhen der [Fülldichte](../infill/infill_sparse_density.md) wird die Größe der Lücken, die von der Außenhaut überbrückt werden müssen, verringert. Dadurch lassen sich diese Lücken leichter schließen. Wenn Sie dies mit [Stufenweise Füllungsschritte](../infill/gradual_infill_steps.md) kombinieren, kann der größte Teil der Fülldichte gleich bleiben. Nur die Oberseite wird eine höhere Dichte haben, um Pillowing zu verhindern.
* Das Drucken bei einer niedrigerer [Temperatur](../material/material_print_temperature.md) verbessert die Brückenbildung und das Warping im Allgemeinen, auch bei der oberen Außenhaut, was den Pillowing-Effekt reduziert.
* Erhöhen Sie auch die [Kühlung](../cooling/cool_fan_speed.md), um ebenfalls die Brückenbildung zu verbessern.
* Eine Verringerung der [Druckgeschwindigkeit der Außenhaut](../speed/speed_topbottom.md) verbessert die Überbrückung direkt. Außerdem werden dadurch die höheren Schichten der Außenhaut besser auf die unteren Schichten gedrückt. Dadurch werden auch die Löcher schneller geschlossen.