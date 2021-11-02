Lexikon
====
Auf dieser Seite werden einige der von Cura verwendeten Fachbegriffe erklärt. Cura ist nicht immer konsequent, wenn es um die Verwendung von Begriffen geht, daher sind einige Begriffe Synonyme.

* **Adaptive Schichten:** Eine Technik, bei der die Schichthöhe über den gesamten Druck variiert wird, um die Sichtbarkeit der Struktur zu verringern und trotzdem relativ schnell zu drucken.
* **Aliasing:** Ein Druckfehler, bei dem die Auflösungsgrenze der Schrittmotoren an der Außenseite des Drucks sichtbar ist.
* **Anti-overhang mesh:** Ein Modell, das verhindert, dass eine Stützstruktur zur Unterstützung eines Überhangs erzeugt wird, mit dem sich das Modell überschneidet. Synonym für "Stützstrukturblocker".
* **Bead:** Ein Filamentstrangs, der vom Extruder abgelegt worden ist. Der Begriff "bead" wird in der Wissenschaft verwendet, wo es wichtig ist, die tatsächliche Beschaffenheit des Fadenstrangs nach seiner Aushärtung zu betrachten. Ähnlich wie "Linie".
* **Blob:** Ein Tropfen überschüssiges Material an der Außenseite des Drucks.
* **Bowden tube:** Ein hohler, flexibler Schlauch, der das Filament durch den Extruder führt.
* **Bridging:** Eine Technik, um überhängende Linien in der Luft zu drucken, indem gerade Linien zwischen zwei Ruhepunkten gezogen werden. Cura kann die Parameter der überbrückenden Linien einstellen und passt die Richtung einiger Linien an, um Brücken zu erzeugen.
* **Brim:** Ein am Druck befestigter Materialrand, der wie ein skirt wirkt, aber auch den Druck besser an der Bauplatte befestigt, indem er dem Material eine größere Oberfläche bietet, an der es haften kann.
* **Build plate:** Die Platte, auf der der Druck platziert wird, während er erstellt wird. Einige Bauplatten werden geheizt, damit das Material besser haftet, während der Druckvorgang läuft.
* **Build volume:** Der 3D-Raum, den der Drucker nutzen kann, um Material zu extrudieren.
* **Coasting:** Eine Technik, bei der der letzte Teil eines Extrusionsweges mit 0 % Durchfluss gedruckt wird, wodurch die Düse von ihrem Überdruck befreit wird.
* **Combing:** Eine Bewegung, bei der versucht wird, das Überqueren von Wänden während der Fahrt zu vermeiden, um zu verhindern, dass eine sichtbare Kratzspur auf der Außenseite des Abdrucks entsteht.
* **Coordinate origin:** Die Stelle auf der Bauplatte, wohin sich eine Düse bewegen würde, wenn sie aufgefordert würde, sich zu den Koordinaten [0, 0, 0] zu bewegen.
* **CuraEngine:** Ein Programm, das Cura verwendet, um die aufwändigen Prozesse des Slicings zu erledigen. Konvertiert 3D-Modelle in G-Code.
* **Cutting mesh:** Ein Modell auf der Bauplatte, das Änderungen an den Einstellungen für den Teil seines Volumens vornehmen kann, der sich mit tatsächlich gedruckten Modellen überschneidet. Das Modell selbst wird nicht gedruckt, aber es schneidet Teile anderer Modelle aus und kann dann die Einstellungen oder den Extruder ändern, mit dem diese Teile gedruckt werden.
* **Disallowed area:** Ein Bereich auf der Bauplatte, in dem Sie kein Modell zum Drucken platzieren dürfen. Zum Beispiel, weil es gegen Clips stoßen würde, die das Bett festhalten, oder weil Ihr Druck Zusatzteile enthalten würde, die aus dem Bauvolumen herausfallen würden.
* **Draft shield:** Eine Materialschicht, die um das Objekt herum gedruckt wird und die Temperatur um den Druck herum konstant hält.
* **Elephant's foot:** Ein Druckfehler, bei dem die Unterseite des Drucks etwas breiter als gewünscht ist.
* **Extruder:** Feeder, optional Bowden tube, Heizzone, hot end und Düse zusammen. Einige Drucker verfügen über mehrere Extruder oder haben mehr als einen Teil des Extrudersystems. Kurzform für Extrudersystem
* **Extruder switch:** Normalerweise ist immer nur einer der Extruder aktiv. Bei einem Extruderwechsel wird der aktive Extruder gewechselt, d. h. von einem Extruder zum anderen.
* **Extruder train:** Feeder, optional Bowden tube, Heizzone, hot end und Düse zusammen. Einige Drucker verfügen über mehrere Extruder oder haben mehr als einen Teil des Extrudersystems.
* **Extrusion:** Der Vorgang, bei dem Filament durch das Extrudersystem gedrückt wird, so dass das Material aus der Düse austritt und hoffentlich an der richtigen Stelle abgelegt wird, um den Druck zu erstellen.
* **Face:** Eine flache Oberfläche eines 3D-Netzes. Bei dreieckigen Netzen (die einzige Art, die Cura verarbeiten kann), sind alle Flächen Dreiecke im 3D-Raum.
* **Fan:** Dabei handelt es sich nicht um einen beliebigen Lüfter des Druckers, sondern speziell um den/die am Druckkopf angebrachten Lüfter, die den Druck abkühlen, nachdem das Material extrudiert wurde.
* **FDM printing:** Fused Deposition Modeling. Eine Art des 3D-Drucks, bei dem Linien aus Kunststoff in einer bestimmten Form extrudiert werden. Dies ist die einzige Technik des 3D-Drucks, die Cura unterstützt. Synonym für "FFF-Druck".
* **Feeder:** Ein Motor und ein Getriebe, die das Filament durch das Extrusionssystem schieben oder ziehen.
* **Feedrate:** Die Geschwindigkeit, mit der das Filament dem Extrusionssystem zugeführt wird.
* **FFF printing:** Fused Filament Fabrication. Eine Art des 3D-Drucks, bei dem Linien aus Kunststoff in einer bestimmten Form extrudiert werden. Dies ist die einzige Technik des 3D-Drucks, die Cura unterstützt. Synonym für "FDM-Druck".
* **Filament:** Ein Kunststoffstrang, der in den 3D-Drucker eingeführt wird. Es wird auf Spulen geliefert. Sobald es extrudiert wurde, ist es kein Filament mehr, sondern nur noch Material.
* **Flow:** Die Durchflussrate des extrudierten Materials im Verhältnis zu seiner normalen Durchflussrate. Bei einem Durchfluss von mehr als 100 % wird theoretisch mehr Material extrudiert, als in das zugewiesene Volumen passen würde. Bei weniger als 100 % Durchfluss wird theoretisch zu wenig Material extrudiert.
* **Gantry:** Der mechanische Rahmen, der den Druckkopf um das Bauvolumen bewegt.
* **Gap filling:** Eine Technik, die von Cura verwendet wird, um kleine Lücken im Druck mit Material zu füllen, indem sehr kleine Liniensegmente verwendet werden.
* **Gradual infill:** Eine Technik, bei der die Materialmenge in den unteren Teilen eines Volumens reduziert wird, in den höheren Teilen aber weiterhin hoch ist, um das darüber liegende Material angemessen zu unterstützen. Diese Technik wird nicht nur für das Material, sondern auch für den Support verwendet.
* **Hardness:** Ein Maß für die Widerstandsfähigkeit eines Drucks gegen elastische Verformung oder Durchstoßung.
* **Heater:** Ein Heizelement, das das Filament auf die für den 3D-Druck erforderliche Temperatur bringt.
* **Heat zone:** Die Zone, in der sich das Filament auf dem Weg zur Düse erwärmt. Am Anfang der Heizzone hat das Filament Raumtemperatur. Am Ende ist es auf Drucktemperatur.
* **Hop:** Eine Technik, bei der die Düse nach oben bewegt wird (+Z), um mit etwas Spiel über den Druck zu fahren. Synonym für "Z-Sprung".
* **Hot end:** Der Metall- oder Keramikeinsatz, der die Düse, das Heizelement und den Temperaturfühler enthält.
* **Infill:** Eine auf der Innenseite eines Drucks erzeugte Struktur, die die Außenhaut hält und dem Druck zusätzliche Festigkeit verleiht.
* **Infill mesh:** Ähnlich wie "cutting mesh", aber nur dort anwendbar, wo es sich mit dem Füllvolumen eines anderen Modells überschneidet. Dies ist ein Modell, das die Einstellungen für die Füllung eines anderen Modells anpasst.
* **Inner walls:** Alle Wände mit Ausnahme der äußersten Wand. Während ein Teil in einer Schicht nur eine Außenwand hat, kann es eine beliebige Anzahl von Innenwänden haben.
* **Inset:** Eine Funktion für Polygone, die ein kleineres/dünneres Polygon erzeugt, dessen Kontur einen bestimmten Abstand von der Kontur des ursprünglichen Polygons einhält. Eine Inset mit einem negativen Abstand wird als "Offset" bezeichnet.
* **Ironing:** Eine Technik, bei der die Oberfläche ein weiteres Mal überarbeitet wird, um sie besonders glatt zu machen.
* **Jerk:** Eine Begrenzung des Wertes der momentanen Geschwindigkeitsänderung, die zu Beginn jeder Bewegung angewendet wird. Dies ist nicht dasselbe wie die gängige Definition von "jerk" in der Physik!
* **Layer:** Der 3D-Druck erfolgt in dünnen Schichten von Material. Diese Schichten sind 2D-Formen mit einer bestimmten Dicke, die, wenn sie vertikal aufeinander geschichtet werden, einen 3D-Druck ergeben.
* **Layer shift:** Ein Druckfehler, bei dem die horizontale Position einer Schicht ungewollt verschoben wird, wodurch sich in der Regel auch der Rest des Drucks verschiebt.
* **Layer split:** Ein Druckfehler, bei dem die Schichten nicht gut genug miteinander verbunden sind und aufbrechen.
* **Line:** Ein Materialstrang, nachdem er vom Extruderzug abgelegt worden ist. In Cura werden die Linien als rechteckige Blöcke mit einer bestimmten Breite, Dicke (Schichthöhe) und Länge modelliert. Vergleichbar mit "bead".
* **Line segment:** Um mit dem 3D-Druck-Begriff "Linie" nicht zu verwechseln, wird Cura, wenn es sich um ein Liniensegment im mathematischen Sinne handelt, immer den vollen Begriff "Liniensegment" verwenden, um eine gerade geometrische Linie von begrenzter Länge zu bezeichnen.
* **Material:** Das Material, aus dem Ihr 3D-Druck besteht. Beim FFF-Druck in der Regel ein Thermoplast.
* **Mesh:** Eine Sammlung von Dreiecken, die zusammen ein Modell bilden. Obwohl dies manchmal als Synonym für "Objekt" und "Modell" verwendet wird, wird es in der Regel im Zusammenhang mit Daten und nicht mit etwas, das man drucken möchte, verwendet.
* **Model:** Ein 3D-Modell, das in die 3D-Szene von Cura geladen wird (vor dem Schneiden). Synonym von "Objekt".
* **Nozzle:** Die Öffnung, durch die das Druckmaterial das Extrudersystem verlässt.
* **Object:** Ein 3D-Modell, das in die 3D-Szene von Cura geladen wird (vor dem Schneiden). Synonym von "Modell".
* **Offset:** Eine Verarbeitung von Polygonen, die ein größeres/dickeres Polygon erzeugt, dessen Kontur einen bestimmten Abstand von der Kontur des ursprünglichen Polygons einhält. Ein Versatz mit negativem Abstand wird als "Inset" bezeichnet.
* **One-at-a-time mode:** Ein Verfahren zum Drucken mehrerer Objekte, bei dem jedes Objekt vollständig gedruckt wird, bevor mit dem nächsten Objekt fortgefahren wird, während normalerweise für jedes Objekt eine Schicht gedruckt wird, bevor mit der nächsten Schicht fortgefahren wird.
* **Ooze shield:** Eine Schicht aus Material, die um den Druck herum gedruckt wird und das austretende Material auffängt, wenn ein Fahrweg die Düse in Richtung des Drucks bewegt.
* **Oozing:** Aus der Düse tritt Material aus, obwohl dies nicht beabsichtigt ist. Dies hinterlässt in der Regel einen Materialstrang entlang des Verfahrwegs.
* **Outer wall:** Die äußerste Wand. Pro Teil und Schicht gibt es nur eine Außenwand.
* **Overextrusion:** Es wird zu viel Material in einem begrenzten Volumen extrudiert, so dass das Material dorthin gelangt, wo es nicht hingehört.
* **Overhang:** Ein Teil des Drucks, der nicht (oder nicht vollständig) durch Material in den darunter liegenden Schichten unterstützt wird. Wenn der Überhang zu extrem ist, um ihn gut zu drucken, ist ein Support oder eine Brücke erforderlich.
* **Overpressure:** Während des Drucks wird die Düsenkammer unter hohem Druck gehalten, um sicherzustellen, dass das Material gleichmäßig extrudiert wird.
* **Parking:** Der Vorgang, bei dem der Druck für einen Moment unterbrochen wird, während die Düse vom Druck entfernt ist, um dem Material etwas Zeit zum Abkühlen zu geben.
* **Part:** Eine zusammenhängende Form (Polygon) auf einer einzigen Schicht. Ein einzelnes Modell kann auf bestimmten Schichten in mehrere Teile aufgeteilt werden, wenn es gesliced wird.
* **Pattern:** Eine Technik zum Füllen eines Volumens mit Material, wenn auch nicht unbedingt mit 100%iger Dichte. Cura bietet die Wahl zwischen verschiedenen Mustern wie Linien, Gitter, konzentrisch etc.
* **Pillowing:** Ein Druckfehler, bei dem sich die Außenhaut an den Stellen, an denen sie auf den darunter liegenden Fülllinien aufliegt, wölbt oder aufbricht.
* **Polygon:** Eine 2D-Form oder geschlossene Schleife, die aus einer Reihe von Punkten mit geraden Liniensegmenten zwischen ihnen besteht.
* **Prime blob:** Ein Materialtropfen, der zu Beginn eines Druckvorgangs ausgestoßen wird, um einen Extruder vorzubereiten.
* **Prime tower:** Eine neben dem Druck erzeugte Struktur, die es dem Drucker ermöglicht, seine Düsen in höheren Schichten zu füllen, ohne dass das überschüssige Material an der Seite des eigentlichen Drucks landet. Wird für Drucke verwendet, an denen mehrere Extruder beteiligt sind, um einen Extruder zu befüllen, nachdem er eine Zeit lang im Standby-Modus war.
* **Priming:** Der Vorgang des Ablassens von Material, um sicherzustellen, dass das Filament an der Düsenspitze ausgerichtet ist und die Düsenkammer korrekt gefüllt und unter Druck steht. Wird in der Regel zu Beginn eines Druckvorgangs oder nach einem Extruderwechsel durchgeführt.
* **Purging:** Der Vorgang des Extrudierens eines Materials als Abfall. Ein häufiger Grund für das Purging ist das "Priming".
* **Raft:** Eine Technik zur Verbesserung der Haftung der Bauplatte, bei der eine feste Unterlage unter den Druck gedruckt wird, die später entsorgt wird. Die Unterlage hat eine große Oberfläche und ist mit dicken Linien bedruckt, die gut haften und alle Unregelmäßigkeiten in der Ebenheit der Bauplatte auffangen.
* **Retraction:** Das Zurückziehen des Materials in die Düsenkammer mit dem Feeder. In der Regel wird dies getan, um das Material vorübergehend daran zu hindern, aus der Düse zu fließen, um einen sauberen Verfahrweg zu erhalten.
* **Ringing:** Ein Druckfehler, bei dem die Oberfläche aufgrund von ungleichmäßiger Extrusion oder Wackeln der Düse unruhig wird. Dies geschieht in der Regel, wenn scharfe Ecken zu schnell gedruckt werden.
* **Scar:** Eine Schadstelle an der Außenseite des Drucks, wo die Düse das Material im Vorbeigehen eingeschmolzen hat.
* **Seam:** Die Stelle, an der eine geschlossene Schleife beginnt und endet. Diese Stelle ist in der Regel auf dem endgültigen Druck sichtbar, daher sollten Sie sie an einer Stelle platzieren, an der sie nicht sehr gut sichtbar ist.
* **Shell:** Sowohl die Wände als auch die Außenhaut.
* **Skin:** Die Ober- und Unterseite des Drucks. Sie werden immer mit 100 % Dichte gedruckt, in der Regel mit dem Linienmuster. Synonym für "oben/unten".
* **Skirt:** Eine Kontur, die auf der ersten Schicht um den Druck herum gezeichnet wird, um sowohl das Material zu vorzubereiten als auch dem Benutzer zu zeigen, ob die Bauplatte vollständig eben ist.
* **Slicing:** Der Prozess der Umwandlung eines 3D-Modells in Befehle für einen 3D-Drucker, um es zu drucken. Im Kontext von CuraEngine wird dies manchmal auch für den Prozess der Erstellung von Querschnitten des Modells verwendet, was eine der Stufen des kompletten Slicing-Prozesses ist.
* **Spiralise mode:** Ein Modus, in dem nur die Umrisse der Modelle gedruckt werden, wobei die Z-Koordinate in der Schicht allmählich erhöht wird, um die Z-Naht zu eliminieren, indem das Modell in einer großen Spirale gedruckt wird. Außerhalb von Cura ist dies auch als "Vasenmodus" bekannt.
* **Stand-by:** Beim Druck mit mehreren Extrudern ist in der Regel nur einer der Extruder gleichzeitig aktiv. Die anderen Extruder befinden sich im Standby-Modus.
* **Stitching:** Ein Teil des Slicing-Prozesses. Die Erstellung von Querschnitten einer Gruppe von Dreiecken führt zu einem Bündel von Liniensegmenten auf jeder Schicht. Beim Zusammenfügen werden diese Liniensegmente zu Polygonen kombiniert und das Innere der Schicht bestimmt.
* **Strength:** Umfassender Begriff, der verschiedene Maße des Widerstandes gegen Bewegung angibt, einschließlich Härte, Steifigkeit und Zähigkeit, wenn verschiedene Arten von Kraft angewendet werden.
* **Stringing:** Bei Fahrwegen, während Material ausläuft, entstehen dünne Materialstränge, die als "Stringing" bezeichnet werden. Die Stränge erstrecken sich nicht unbedingt über die gesamte Länge eines Fahrwegs. Eine weniger extreme Form dieses Phänomens führt zu "Klecksen".
* **Support:** Ein Teil des Drucks, der nach dem Druck entfernt wird, aber notwendig war, um Teile des Drucks an Ort und Stelle zu halten, während der Druck noch im Gange war, um zu verhindern, dass Material herunterfällt oder zu sehr wackelt.
* **Support blocker:** Ein Modell, das verhindert, dass Support erzeugt wird, um einen Überhang zu stützen, mit dem sich das Modell überschneidet. Synonym für "Anti-Überhang-Netz".
* **Support floor:** Die Unterseite des Supports, die dort verwendet wird, wo der Support auf dem Modell aufliegt. Dieser Teil des Supports kann optional mit verschiedenen Einstellungen gedruckt werden. Dort, wo der Support auf der Bauplatte aufliegt, gibt es keinen Support-Boden.
* **Support infill:** Der Hauptbestandteil des Supports. Wenn es keine Support-Schnittstelle gibt, besteht der Support nur aus der Support-Füllung.
* **Support interface:** Das Dach und der Boden des Supports, wo das Modell auf dem Support aufliegt und wo der Support auf dem Modell aufliegt. Die Unterseite der Stütze, wo die Stütze auf der Bauplatte aufliegt, erhält keine Stützschnittstelle.
* **Support mesh:** Ein Modell, das mit einer Support-Struktur gefüllt wird, anstatt es als normalen Druck zu drucken. Kann verwendet werden, um die Form Ihres Supports anzupassen.
* **Support roof:** Die Oberseite des Supports, die verwendet wird, wenn das Modell auf dem Support ruht. Dieser Teil des Supports kann optional mit verschiedenen Einstellungen gedruckt werden.
* **Support towers:** Eine Technik zum Support von sehr dünnen oder kleinen Teilen des Drucks. Das Teil wird von der Spitze eines Turms gestützt, der nach unten hin breiter wird, damit der Support während des Drucks nicht umkippt.
* **Thermoplastic:** Eine Art von Kunststoff, der beim Schmelzen weich wird. Für den FFF-Druck können nur Thermoplaste verwendet werden.
* **Thickness:** Die Dicke einer Struktur in Eckpunktrichtung (Z). Vergleiche mit "Breite".
* **Top/bottom:** Die Ober- und Unterseite des Drucks. Sie werden immer mit 100 % Dichte gedruckt, in der Regel mit dem Linienmuster. Synonym für "Außenhaut".
* **Top surface:** Der oberste Teil der Außenhaut. Selten mehr als 1 Schicht, kann diese Oberseite mit separaten Einstellungen gedruckt werden, um eine höhere Qualität zu erreichen, ohne viel zusätzliche Druckzeit zu kosten.
* **Topography:** Der Effekt, bei dem die begrenzte Höhe der Schichten eine fast ebene Fläche in etwas verwandelt, das einer geografischen Höhenkarte mit Ringen an den Enden der Schichten ähnelt.
* **Toughness:** Ein Maß für die Widerstandsfähigkeit eines Drucks gegen plastische Verformung.
* **Travel (move):** Bewegen der Düse von einem Ort zum anderen, ohne Material zu extrudieren.
* **Underextrusion:** Es wird zu wenig Material extrudiert, um ein Volumen richtig auszufüllen oder um starke und kontinuierliche Tropfen zu erzeugen.
* **Underpressure:** Während des Einziehens wird in der Düsenkammer ein Unterdruck erzeugt, der das Material ansaugt und ein Auslaufen verhindert.
* **Vase mode:** Ein Verfahren, bei dem nur die Umrisse der Modelle gedruckt werden, wobei die Z-Koordinate in der Schicht schrittweise erhöht wird, um die Z-Naht zu eliminieren. Cura nennt dies immer den "Spiralisieren-Modus".
* **Walls:** Die Seiten des Drucks. Sie legen sich waagerecht um das Modell.
* **Warping:** Verformung des Drucks nach dem Druck durch Schrumpfung des Materials oder durch innere Spannungen, die am noch nicht verfestigten Material ziehen.
* **Width:** Die Größe einer Struktur in horizontaler Richtung (X/Y). Vergleiche mit "Dicke".
* **Winding order:** Die Reihenfolge der Punkte, die ein Polygon bilden. Entweder im Uhrzeigersinn oder gegen den Uhrzeigersinn. In Cura bedeutet eine gegen den Uhrzeigersinn gewundene Anordnung eine positive Form, während eine im Uhrzeigersinn gewundene Anordnung ein Loch bedeutet. Die eingegebenen 3D-Modelle müssen Dreiecke haben, die von außen gesehen gegen den Uhrzeigersinn angeordnet sind.
* **Wiping:** Eine Technik, bei der die Düse absichtlich eine zuvor gedruckte Struktur kreuzt, um herabhängendes Material von der Düsenspitze abzuwischen, damit dieses Material nicht auf die Außenseite des Drucks gelangt.
* **Wire printing:** Eine Technik zum Drucken eines Modells, bei der nur ein Drahtgitter um die Hülle herum gedruckt wird. Äußerst experimentell.
* **Z seam:** Eine sichtbare Stelle an der Außenwand, an der sich die Düse von einer Schicht zur nächsten bewegt hat. Wird oft fälschlicherweise anstelle von "Naht" verwendet.
* **Z hop:** Eine Technik, bei der die Düse nach oben bewegt wird (+Z), um mit etwas Spiel über den Druck zu fahren. Synonym für " Sprung".