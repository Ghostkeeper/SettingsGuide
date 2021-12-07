Drucken mit Drahtstruktur
====
Diese Einstellung ermöglicht eine völlig andere Art des Druckens, den sogenannten Drahtdruck. Beim Drahtdruck druckt der Drucker kein festes Objekt, sondern nur ein dreieckiges Netz aus dünnen Drähten, das der äußeren Form entspricht.

Diese Technik hat eine Reihe von Vorteilen:
* Sie druckt viel schneller als ein festes Objekt.
* Sie verbraucht nur einen Bruchteil des Materials, das beim normalen Drucken verwendet würde.
* Es sieht so aus, als wäre es mit einem 3D-Druckstift von Hand hergestellt worden.

Das resultierende Objekt ist jedoch nicht funktional. Es hat ungefähr die richtige Größe, was es für Prototypen nützlich macht, um ein Gefühl für den Maßstab des Drucks zu bekommen, obwohl die Größe auch nicht sehr genau ist. Das resultierende Objekt ist extrem zerbrechlich, nicht nur während des Druckens, sondern auch danach. Es ist schwer, es von der Bauplatte zu nehmen, ohne es zu beschädigen. Außerdem verliert das Modell die meisten seiner Details.

Beim Drucken mit Drahtstruktur werden Materialringe mit einem relativ großen vertikalen Abstand von mehreren Millimetern aufgebracht. Zwischen diesen Ringen wird eine Sägezahnform gezeichnet, die es dem nächsten Ring ermöglicht, auf dem vorherigen aufzuliegen. Dort, wo die Oberfläche des Modells horizontal verläuft, wird eine ähnliche Technik verwendet, um die Oberseite zu schließen. Im Dach befinden sich konzentrische Ringe, die durch eine Sägezahnform zusammengehalten werden, die sorgfältig in der Luft schwebt, indem sie von außen (wo sie an einer Wand anliegen kann) nach innen gebaut wird.

Das Drucken mit Drahtstruktur funktioniert nur zuverlässig bei Formen, die fast vollständig vertikal sind, ähnlich der Art von Modellen, die gut mit dem [Spiralisieren](../blackmagic/magic_spiralize.md) funktionieren würden. Wenn die Oberfläche über weite Bereiche horizontal ist, muss die Dachschließtechnik eine extrem große Distanz überbrücken. Dies wird dann höchstwahrscheinlich scheitern. Wenn das Modell dann auf halber Strecke über eine horizontale Fläche nach oben weitergeht, wird es mit ziemlicher Sicherheit in der Luft gedruckt.

**Die Schicht-Ansicht von Cura zeigt das Drucken von Drähten direkt nach dem Slicen nicht korrekt an. Das Ergebnis kann jedoch immer noch in der Vorschau angezeigt werden, indem man den G-Code auf der Festplatte speichert und diesen G-Code erneut mit Cura öffnet.**