Spiralisieren der äußeren Konturen
====
Spiralisieren der Außenkontur ist ein Spezialfall.

Wenn Sie Schicht für Schicht drucken, muss sich die Düse normalerweise von einer Schicht zur nächsten bewegen. Diese Bewegung führt dazu, dass die Düse für den Bruchteil einer Sekunde fast stillsteht, was eine Naht auf der Oberfläche hinterlässt, die so genannte Z-Naht. Diese Einstellung soll dies und mehr verhindern. Sie vereinfacht den Druckprozess erheblich, indem sie viele Aspekte des Prozesses ausspart.

Bei der Spiralisierung des Modells erhält das Modell keine Füllung oder Oberseiten. Es wird nur eine Wand und einen Boden erhalten. Wenn die Option [Spiralisieren der äußeren Konturen glätten](smooth_spiralized_contours.md) aktiviert ist, wird die Höhe der Düse allmählich über die Höhe einer Schicht erhöht. Auf diese Weise wird eine Spirale erzeugt, die der Kontur des Modells folgt. Es findet keine Bewegung von einer Schicht zur nächsten statt, da sich die Düse bereits allmählich zur nächsten Schicht bewegt hat.

Der Modus Spiralisieren ist bei vielen Slicern üblich. Er wird manchmal auch als "Vasenmodus" bezeichnet, da er sich gut zum Drucken von Vasen eignet. Einige weitere Eigenschaften sind:
* Druckt extrem schnell.
* Die Oberfläche wird sehr glatt. Es gibt keine [Z-Naht](../../../articles/troubleshooting/seam.md) mehr, die sie sich zur nächsten Ebene bewegt, wenn [Spiralisieren der äußeren Konturen glätten](smooth_spiralized_contours.md) aktiviert ist.
* Der Druck wird nicht sehr stabiel sein. Wenn das Modell zu groß ist, neigt es aufgrund der dünnen Wand dazu [zu brechen](../../../articles/troubleshooting/layer_splitting.md).
* Während das Entfernen der Naht dazu beiträgt, den Druck wasserdicht zu machen, ist es schwierig, den Druck wasserdicht zu bekommen, wenn er eine bestimmte Größe hat. Deshalb ist es ratsam, mindestens 2 Wände zu haben. Das Spiralisieren der Außenkontur ist dann nicht mehr möglich.

**Spiralisieren funktioniert nicht gut bei Drucken mit vielen horizontalen Flächen. Es verarbeitet keine Überhänge und druckt keine Oberseiten, so dass sich nichts an eine horizontale Fläche auflegen kann. Es funktioniert auch nicht gut, wenn es mehrere Teile auf einer Ebene gibt.**