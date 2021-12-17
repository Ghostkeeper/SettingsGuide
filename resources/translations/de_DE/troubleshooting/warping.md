Warping
====
Warping ist ein Problem mit dem endgültigen Druck, bei dem sich der Druck nach dem Druck aufrollt und das fertige Objekt verformt. Typischerweise rollen sich die Ecken an der Unterseite des Drucks nach oben, oder dünne Teile des Drucks werden wellig.

![Die Spitzen rollen sich auf](../../../articles/images/warping.jpg)

Ursache
----
Die Verformung wird durch eine Kombination von Effekten verursacht, in erster Linie jedoch durch innere Spannungen, die durch das Ziehen der Düse am geschmolzenen Kunststoff entstehen. Während des Glasübergangs verhält sich Kunststoff ein wenig wie Gummi oder Kaugummi. Wenn man daran zieht, dehnt sich das Material, aber wenn man aufhört zu ziehen, kehrt es in seine ursprüngliche Form zurück. Das Gleiche passiert auch beim Drucken. Wenn man eine lange Linie druckt, zieht die Düse an der Kunststofflinie, die sich in der Länge der Linie dehnt. Wenn die Düse wegfährt und aufhört zu ziehen, zieht sich die Kunststofflinie zusammen. Diese Kontraktion verursacht eine Zugkraft auf alles, was an ihr befestigt ist. Wenn genügend Kunststoffleitungen gemeinsam ziehen, können sie den Druck verzerren. Dies ist besonders häufig der Fall, wenn viele Linien parallel verlaufen, wie z. B. bei der Außenhaut.

Ein zweiter Effekt, der zu Verformungen führt, ist die Schrumpfung des Materials beim Abkühlen. Die meisten Materialien neigen zum Schrumpfen, wenn sie abkühlen. Wenn das Objekt ungleichmäßig abkühlt, schrumpfen einige Teile des Drucks stärker als andere Teile des Drucks, wodurch sich das Objekt verzieht. Wenn das Objekt weiter abkühlt, verfestigt es sich weiter und die Verformung bleibt dauerhaft bestehen.

Einige Materialien sind aufgrund ihrer Kristallinität anfälliger für Schrumpfung als andere. Im Folgenden finden Sie einige Schrumpfungskoeffizienten für gängige 3D-Druckmaterialien. Das ist der ungefähre Wert, um den jedes Material schrumpft, wenn es von seiner Glasübergangstemperatur auf Raumtemperatur abkühlt. Zwischen den einzelnen Mischungen gibt es gewisse Abweichungen. Eine stärkere Schrumpfung führt zu einer stärkeren Verformung.
* PLA: 0.21%
* ABS: 0.70%
* TPU: 0.63%
* HIPS: 0.64%
* PETG und CPE: 0.45%
* Nylon: 0.62%
* PC: 0.70%
* PP: 1.2%

Außerdem kann das Warping verhindert werden, wenn anderes Material im Weg ist. Wenn ein Teil des Drucks völlig dicht ist, kann das umgebende Material weniger oder gar nicht schrumpfen. Wenn andere Teile nicht ganz dicht sind, wird der Druck teilweise geschrumpft sein. Der geschrumpfte Teil des Drucks zieht am Rest, was ebenfalls zu Warping führen kann. Dies ist häufig an der Grenze zwischen Außenhaut und Füllung der Fall, da die Außenhaut vollständig dicht ist, die Füllung jedoch nicht.

Warping tritt am häufigsten an der Unterseite des Drucks auf. Hier ist das Temperaturgefälle am größten, da die Unterseite des Drucks oft durch ein Heizbett erwärmt wird, der Rest des Drucks jedoch nicht. Die Unterseite besteht in der Regel auch aus vielen langen Außenhautlinien. Wenn das [Untere Muster](../top_bottom/top_bottom_pattern.md) auf Linien oder Zickzack eingestellt ist, sind diese Linien lang, gerade und parallel, so dass sie gemeinsam in dieselbe Richtung ziehen, um das Objekt zu verziehen.

Vermeidung
----
* Wenn das Warping an der Unterseite des Drucks auftritt, setzen Sie das [Untere Muster für erste Schicht](../top_bottom/top_bottom_pattern_0.md) auf konzentrisch. Auf diese Weise wird die Kontraktion der unteren Außenhautlinien nicht mehr im Gleichschritt erfolgen. Die innere Spannung verteilt sich gleichmäßig auf die Innenseite der unteren Schicht. Wenn dies nicht ausreicht, um Warping zu verhindern, können Sie auch das normale [Unteres/oberes Muster](../top_bottom/top_bottom_pattern.md) auf Concentric stellen.
* Um die Temperaturgradienten innerhalb des Drucks zu reduzieren, verringern Sie die [Temperatur der Druckplatte](../material/material_bed_temperature.md). Das Objekt sollte dann gleichmäßiger abkühlen.
* Abhängig von Ihrer Druckerhardware kann das Drucken in einer geschlossenen, beheizten Kammer auch Warping verhindern. Zum einen wird dadurch der Temperaturunterschied zwischen dem Bauvolumen und der Bauplatte sowie der Unterschied zwischen dem Bauvolumen und der Düse verringert. Außerdem kann der Kunststoff so länger aushärten (https://en.wikipedia.org/wiki/Annealing_%28glass%29), wodurch die inneren Spannungen und damit das Ziehen der gedruckten Linien, das das Warping verursacht, verringert werden. Wenn Ihr Drucker dies unterstützt, sollten Sie die [Temperatur Druckabmessung](../material/build_volume_temperature.md) erhöhen.
* Um zu verhindern, dass sich die Unterseite verzieht, ist eine gute Haftung der Bauplatte hilfreich. Dies erhöht die Kraft, die das Material zum Warping benötigt. Erhöhen Sie zum Beispiel die [Brim-Breite](../platform_adhesion/brim_width.md) oder den [Zusätzlichen Abstand für Raft](../platform_adhesion/raft_margin.md).
* Die Verwendung eines [Raft anstelle eines Brims](../platform_adhesion/adhesion_type.md) entfernt den Druck von der Bauplatte und legt ein stabiles Stück Kunststoff dazwischen, das gegen Warping resistent ist.
* Versuchen Sie, mit einem [Windschutz] zu drucken (../experimental/draft_shield_enabled.md). Dadurch wird eine Schutzkammer um Ihren Druck herum gebildet, die verhindert, dass Zugluft von außen Ihren Druck abkühlt, bevor er fertig ist. Bedenken Sie jedoch, dass auch der Windschutz selbst schrumpfen kann. Wenn der Windschutz versagt, kann es sein, dass Sie in Ihrem Druck viele Stringing oder Spaghetti sehen.
* Drucken Sie mit einem Material, das weniger schrumpft, wie z. B. PLA.
* Wenn Sie die Möglichkeit haben, das gedruckte Modell anzupassen, versuchen Sie, sehr scharfe äußere Ecken auf der Bauplatte zu vermeiden. Sie können bestimmte äußere Ecken abrunden. Dadurch wird verhindert, dass sich die gesamte Kraft der inneren Spannung auf einen Punkt konzentriert, was die Wahrscheinlichkeit eines Warpings verringert.