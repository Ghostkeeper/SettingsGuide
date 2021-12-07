Unterextrusion
====
Eines der häufigsten Probleme beim 3D-Druck ist, dass der Drucker nicht genug Material extrudiert, um ein schönes, festes Objekt zu produzieren. Wenn dies geschieht, spricht man von "Unterextrusion": Die Düse extrudiert weniger Material als vorgesehen.

![Ein extremer Fall von Unterextrusion, bei dem man sogar das Innere des Objekts sehen kann](../../../articles/images/underextrusion.jpg)

Auch Unterextrusion kann sich auf vielfältige Weise äußern. Im extremsten Fall ist das Objekt sehr spröde und das Innere ist durch die Oberfläche hindurch zu sehen. Manchmal sind die Linienbreiten zu gering, so dass sie sich nicht mit den benachbarten Linien verbinden. Manchmal sind es auch nur kleine Löcher in der Oberfläche oder winzige Risse in den Wänden, die sich zeigen.

Es gibt unzählige mögliche Ursachen für Unterextrusion, was die Fehlersuche sehr erschwert. Der Rest dieses Artikels beschreibt einige der wahrscheinlichsten Ursachen und wie man sie beheben kann.

Verstopfte Düse
----
Wenn Ihr Drucker zuvor einwandfrei druckte und plötzlich eine Unterextrusion aufweist, ohne dass sich das gedruckte Objekt oder die Einstellungen wesentlich verändert haben, liegt das Problem wahrscheinlich irgendwo im Extruderzug. In der Regel ist das schwächste Glied hier die Düse.

Verstopfte Düsen kommen bei allen 3D-Druckern regelmäßig vor. Das kann passieren, wenn das Filament mit Dingen verunreinigt ist, die nicht gut schmelzen und in die Düse gedrückt werden. Es kann auch passieren, wenn das Filament selbst in der Düse verbrannt wird. Das kann passieren, wenn der Kunststoff zu stark erhitzt oder zu lange auf einer hohen Temperatur gehalten wird. Das Material zersetzt sich, die Polymere kristallisieren und es bleibt ein Stück harter Kunststoff zurück, der sich nicht aus der Düse herausschmelzen lässt. Um hier Abhilfe zu schaffen, müssen Sie die Ablagerungen aus der Düse entfernen.

Es gibt verschiedene Techniken, um die Ablagerungen aus der Düse zu entfernen. Wenn Sie eine Akupunkturnadel oder eine andere dünne Metallnadel haben, können Sie sie von unten herausdrücken. Die gebräuchlichste Technik ist jedoch der so genannte "Atomic Pull". Um diese Technik auszuführen, nehmen Sie ein mindestens 50 cm langes Stück Filament, vorzugsweise aus einem Material mit einem hohen Schmelzpunkt. Erhitzen Sie die Düse auf den Schmelzpunkt des Filaments (z. B. 190 °C für PLA), und drücken Sie das Filament mit einer Zange hinein, bis etwas Material aus der Düse austritt. Lassen Sie dann die Düse auf ihre Glasübergangstemperatur abkühlen (z. B. 60 °C bei PLA), während Sie das Filament in die Düse drücken. Kurz bevor die Glasübergangstemperatur erreicht ist, ziehen Sie das Filament schnell heraus. Wenn die Spitze des Filaments mit geschwärztem Kunststoff verschmutzt ist, schneiden Sie die Spitze ab und versuchen Sie es erneut, bis sie sauber ist. Versuchen Sie erneut, etwas zu drucken, und hoffen Sie, dass es jetzt besser extrudiert.

Rutschende Zuführung
----
Manchmal kann der Feeder das Filament nicht fest genug greifen, um es kräftig genug durch die Düse zu drücken. Während des Druckens können Sie dann hören, wie das Filament regelmäßig mit einem leisen Klacken alle paar Sekunden durchrutscht. Das ist der Feeder, der versucht, das Filament hineinzudrücken, aber das Filament rutscht ab und zu wieder heraus.

Die meisten Feeder haben Einstellpunkte, um die Kraft, die sie auf das Filament ausüben, zu regulieren. Versuchen Sie, die Zuführung etwas fester auf das Filament einzustellen. Wenn die Zuführung zu fest auf das Filament drückt, könnte das Filament brechen oder zu viel Reibung verursachen und anfangen zu schleifen. Wenn er zu locker sitzt, kommt es oft zu einer Unterextrusion.

Ungleichmäßiger Filamentdurchmesser
----
Während die meisten Filamente in Ordnung sind, wird manchmal eine Charge produziert, bei der das Filament ein wenig zu dünn ist. Dies kann große Auswirkungen auf die Menge der Extrusion in Ihrem Druck haben. Günstigere Filamente sind oft anfälliger für dieses Problem. Sie können mit einem Messschieber den tatsächlichen Durchmesser Ihres Filaments messen. Achten Sie darauf, dass Sie an mehreren verschiedenen Stellen entlang des Filaments messen und nicht dort, wo der Feeder das Filament abgeschliffen hat.

Wenn der Durchmesser des Filaments zu weit abweicht (ein Unterschied von 50μm wird im Druck sichtbar), können Sie den Durchmesser des Filaments im Materialmanager anpassen. Wenn Sie ein in Cura vorhandenes Material verwenden, müssen Sie dieses Material duplizieren, bevor Sie es bearbeiten. Cura wird dann den neuen Durchmesser kompensieren, indem es die Geschwindigkeit des Vorschubs anpasst.

Material Schmelzen
----
Abgesehen davon, dass Ihr 3D-Drucker in bestem Zustand ist, müssen die Einstellungen, mit denen Sie drucken, auch den Materialeigenschaften des von Ihnen verwendeten Werkstoffs entsprechen. Die wichtigste Einstellung ist die Drucktemperatur.

Wenn die [Drucktemperatur](../material/material_print_temperature.md) zu niedrig ist, kommt es sehr schnell zu Unterextrusion. Wenn das Material zu kalt ist, wird es sehr zähflüssig, was es erschwert, richtig aus der Düse zu fließen. In Kombination mit einer hohen Druckgeschwindigkeit hat das Material nicht genug Zeit, um richtig zu schmelzen und in die richtige Position zu fließen. Einige Materialien, wie PVA oder Nylon, neigen dazu, Feuchtigkeit aus der Luft zu absorbieren. Diese Feuchtigkeit verdunstet, wenn das Material gedruckt wird, wodurch sich der Kunststoff abkühlt. Um diesen Effekt auszugleichen, müssen diese Materialien bei einer höheren Temperatur gedruckt werden, wenn sie eine Zeit lang der Luft ausgesetzt waren.

Wenn die Temperatur zu hoch ist, kann sich das Material sehr schnell zersetzen. Zersetztes Filament schmilzt dann möglicherweise nicht mehr richtig, was die Düse verstopft. Die zusätzliche Wärme kann auch dazu führen, dass das Material weiter oben im Extruderstrang schmilzt. Dies kann zu Reibung im Extruderstrang führen, wodurch es schwieriger wird, das Material herauszudrücken. Schauen Sie sich die Temperaturangaben auf dem Etikett Ihres Filaments genau an, um zu sehen, in welchem Temperaturbereich es gedruckt werden kann.

Anstatt die Temperatur einzustellen, können Sie auch die [Lüftergeschwindigkeit](../cooling/cool_fan_speed.md) einstellen . Wenn das Gebläse zu hoch eingestellt ist, kann die Düse beim Extrudieren von Material schneller abkühlen, so dass sie kälter ist, als der Temperatursensor tatsächlich misst. Vor allem bei Materialien, die von Natur aus mit hoher Temperatur gedruckt werden, wie z. B. Polycarbonat, ist es oft notwendig, die Lüftergeschwindigkeit zu reduzieren, um eine Unterextrusion zu verhindern.

Zu schnelles Drucken führt ebenfalls zu Unterextrusion, da das Material nicht genug Zeit hat, um in der Düsenkammer zu schmelzen. Eine Verringerung der [Druckgeschwindigkeit](../speed/speed_print.md) kann ebenfalls helfen, Unterextrusion zu vermeiden.

Das Material zum Fließen bringen
----
Es gibt immer eine gewisse Latenzzeit zwischen dem Vorschub des Materials durch den Drucker und dem tatsächlichen Beginn der Extrusion. Diese Latenzzeit kann zu Unterextrusion führen, wenn sie nicht berücksichtigt wird. Wenn der Drucker das Material vorschiebt, steigt der Druck in der Düsenkammer allmählich an, bis er ausreicht, um das geschmolzene Material am anderen Ende herauszudrücken. Es kann bis zu einer Sekunde dauern, bis das Material seine normale Fließgeschwindigkeit erreicht hat. Wenn der Drucker über einen Bowdenschlauch zwischen Zuführung und Düse verfügt, kann diese Verzögerung sogar noch um ein Vielfaches größer sein, etwa 10 Sekunden oder so.

Wenn der Drucker mehr Material als zuvor extrudieren muss, wird er das Material schneller zuführen, aber es dauert eine Weile, bis es an der Düsenspitze ankommt. In der Zwischenzeit versucht die Düse, eine Linie zu ziehen, aber diese Linie wird unterextrudiert. Vor allem wenn der Druck sehr detailliert ist, kann dies zu einer erheblichen Unterextrusion führen.

Um dies zu beheben, können Sie zwei Einstellungen vornehmen: Vorbereiten und Geschwindigkeitsanpassung.

Das Vorbereiten des Materials bedeutet, dass ein wenig Material herausgedrückt wird, bevor der wichtige Teil des Drucks beginnt. Häufig wird dies zu Beginn des Drucks in einer separaten Routine durchgeführt, indem eine kleine Linie oder ein Tropfen Kunststoff in eine Ecke der Bauplatte gedruckt wird. Alternativ können Sie einen [Skirt oder Brim](../platform_adhesion/adhesion_type.md) verwenden, der eine Reihe von Linien um den Druck selbst druckt. Wenn das Material richtig fließt und alle Luft aus der Düsenkammer entwichen ist, wird es gleichmäßiger extrudiert.

Wenn das Material eingezogen wird, wird der Materialfluss unterbrochen. Wenn das Material in die Düse zurückgeschoben wird, kann es eine Weile dauern, bis es wieder fließt. Wenn Sie die [Einzugsgeschwindigkeit (Zurückschieben)](../travel/retraction_prime_speed.md) verringern, kann das Material besser schmelzen, bevor es extrudiert wird, was ein wenig hilft. Ansonsten kann man auch versuchen, das Material etwas weiter zu schieben als vor dem Einziehen, indem man die [Zusätzliche Zurückschiebemenge nach Einzug](../travel/retraction_extra_prime_amount.md) anpasst, um die Unterextrusion zu kompensieren. Diese Einstellung ist allerdings sehr heikel.

Ausgleich des Filamentflusses
----
Wenn die Unterextrusion nur in bestimmten Strukturen des Drucks auftritt, z. B. in der Füllung und im Support, sollten Sie die Fließgeschwindigkeit Ihres Drucks stärker angleichen. Es gibt immer eine Verzögerung zwischen der Zuführung des Materials und dem tatsächlichen Ausfließen des Materials aus der Düse. Wenn die Druckgeschwindigkeit für einen Teil des Drucks erhöht wird, beschleunigt der Druckkopf relativ schnell, aber der Materialfluss hinkt hinterher, bis der Druck in der Düsenkammer erhöht wird, um die höhere Extrusionsrate zu bewältigen. Dies führt ebenfalls zu einer Unterextrusion. Wenn man die Extrusionsrate verlangsamt, kommt es immer zu einer Überextrusion.

Einige Firmwareprogramme sind in der Lage, diesen Effekt zu kompensieren. Marlin verfügt über eine Funktion namens [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html), die den Druck in der Düsenkammer im Voraus erhöht, so dass das Material früher aus der Düse fließen kann. Sailfish verfügt über eine [ähnliche Funktion](https://www.sailfishfirmware.com/doc/tuning-jkn-advance.html), die JKN Advance genannt wird. Um die Parameter dieser Funktionen einzustellen, müssen Sie den g-code im Start-g-code nachsehen.

Wenn solche Funktionen nicht verfügbar oder unwirksam sind, müssen Sie sicherstellen, dass es beim Drucken keine plötzlichen, großen Flussänderungen gibt. Verringern Sie die [Füllschichtdicke](../infill/infill_sparse_thickness.md) und die [Stützstruktur Füllschichtdicke](../support/support_infill_sparse_thickness.md). Mit diesen Einstellungen wird die Extrusionsrate multipliziert, um eine größere Schichthöhe zu erreichen.

Noch wichtiger ist, dass Sie sicherstellen, dass Füllung, Innenwände, Außenhaut und Support mit einer ähnlichen Extrusionsrate gedruckt werden. Die Extrusionsgeschwindigkeit einer Linie ist das Produkt aus Linienbreite, Schichthöhe, Fluss und (durchschnittlicher) Geschwindigkeit. Multiplizieren Sie diese vier Faktoren miteinander, und stellen Sie sicher, dass das Ergebnis für die Füllung ungefähr gleich ist ([Füllschichtdicke](../infill/infill_sparse_thickness.md), [Breite der Fülllinien](../resolution/infill_line_width.md), [Fluss der Füllung](../material/infill_material_flow.md) und [Füllgeschwindigkeit](../speed/speed_infill.md)), Außenhaut ([Breite der Linie](../resolution/skin_line_width.md), [Fluss oben/unten](../material/skin_material_flow.md) und [Geschwindigkeit obere/untere Schicht](../speed/speed_topbottom.md)), Außenwand ([Breite der äußeren Wandlinien](../resolution/wall_line_width_0.md), [Wandfluss außen](../material/wall_0_material_flow.md) und [Geschwindigkeit Außenwand](../speed/speed_wall_0.md)), Innenwand ([Breite der inneren Wandlinien](../resolution/wall_line_width_x.md), [Wandfluss innen](../material/wall_x_material_flow.md) und [Geschwindigkeit Innenwand](../speed/speed_wall_x.md)) und Support ([Stützstruktur Füllschichtdicke](../support/support_infill_sparse_thickness.md), [Breite der Stützstrukturlinien](../resolution/support_line_width.md), [Stützstruktur-Fluss](../material/support_material_flow.md) und [Stützstrukturgeschwindigkeit](../speed/speed_support.md)). Wenn [Wandüberlappungen ausgleichen](../shell/travel_compensate_overlapping_walls_enabled.md) eingeschaltet ist, stellen Sie sicher, dass Sie [Ausgleich des Filamentflusses](../speed/speed_equalize_flow_enabled.md) aktivieren, damit die Geschwindigkeit und nicht der Fluss angepasst wird.

Grenzwerte für Düsen
----
Wird zu viel Material durch eine kleine Düse extrudiert, kann es auch zu einer Unterextrusion kommen. Wenn mit einer kleinen Düse große Schichthöhen, Linienbreiten oder Geschwindigkeiten gedruckt werden, kann das Material physikalisch gesehen nicht rechtzeitig aus der Düse fließen. Eine Erhöhung der Temperatur kann dazu beitragen, dass das Material bis zu einem gewissen Grad fließfähiger wird, aber es gibt immer noch Grenzen, bis zu denen eine Düse extrudieren kann. Wenn diese Grenze überschritten wird, sollten Sie eine größere Düse kaufen.

Auf der anderen Seite kann das Extrudieren von zu wenig Material auch zu einer Unterextrusion führen. Wenn der Druck in der Düsenkammer sehr niedrig ist, kann die Oberflächenspannung des flüssigen Kunststoffs das Material in der Düsenkammer halten. Gelegentlich wird es mit einem großen Tropfen herausgedrückt, wobei an anderen Stellen Luft zurückbleibt. Dies kann zu einem ähnlichen Effekt wie bei der Unterextrusion führen.

Direktes Einstellen des Durchflusses
----
Wenn alles andere versagt, hat Cura auch eine Einstellung, um den [Fluss](../material/material_flow.md) direkt anzupassen. Diese Notlösung kann einen unbekannten Fehler irgendwo im System kompensieren.

Sie funktioniert nicht, wenn das Material physisch daran gehindert wird, schneller zu fließen (z. B. wegen einer verstopften Düse). In anderen Fällen wird es wahrscheinlich zu einer Überextrusion an einigen Stellen führen. Es ist jedoch eine einfache Möglichkeit, den Druck nach Bedarf anzupassen.