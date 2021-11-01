Probleme mit der Betthaftung
====
Eine der häufigsten Fehlerarten bei 3D-Drucken ist, dass sich der Druck von der Bauplatte löst, während er noch gedruckt wird. Dieser Artikel befasst sich mit einigen Einstellungen, die Sie vornehmen können, um dies zu verhindern.

Wenn sich der Druck von der Bauplatte gelöst hat, sehen Sie in der Regel eine große Menge loser Fäden überall auf der Bauplatte. Wenn Sie mehr Glück haben, kann es sich auch nur als eine [Schicht-Verschiebung](layer_shift.md) zeigen (dann gibt es weniger zu bereinigen). So oder so, der Druck ist ruiniert.

Methoden für die Betthaftung
----
Cura bietet mehrere Methoden zur Verbesserung der Betthaftung. Sie können zwischen diesen Methoden mit der Einstellung [Druckplattenhaftungstyp](../platform_adhesion/adhesion_type.md) wählen. Die folgenden Optionen sind verfügbar.
* Brim, die häufigste Technik, fügt einen Rand um die Unterseite des Drucks hinzu, der die Oberfläche vergrößert, so dass der Druck besser auf der Bauplatte haftet.
* Ein Raft ist eine zusätzliche Schicht unter dem gesamten Druck. Diese Schicht erhält ebenfalls eine größere Oberfläche, so dass sie besser haftet. Wenn das Raft mit einem Material bedruckt ist, das gut am Druck haftet (z. B. mit demselben Material), bleibt der Druck auf diese Weise an seinem Platz.
* Ein Skirt ist nicht mit dem Druck verbunden, sondern umschließt ihn nur. Diese Linie sorgt dafür, dass das Material fließt, bevor der eigentliche Druck beginnt, so dass es in der ersten Schicht nicht zu einer Unterextrusion kommt, die die Haftung zerstören könnte.
* Sie können auch ohne Haftung arbeiten, indem Sie "Keine" auswählen. Dies spart Zeit und Material und verhindert andere negative Auswirkungen der oben genannten Methoden. Verwenden Sie dies nur, wenn Ihr Drucker über eine andere Vorbereitungstechnik verfügt, wie z. B. einen purge bucket.

Der Brim und das Raft sind die effektivsten Techniken, um die Haftung zu erhöhen, da sie speziell für diesen Zweck entwickelt wurden. Die meisten Drucke benötigen eine dieser beiden Techniken.

Wenn ein Brim verwendet wird, können Sie die Haftung weiter erhöhen, indem Sie die [Breite des Brim-Elements](../platform_adhesion/brim_width.md) erhöhen. Sie können auch einen Brim an der [Innenseite des Stützstrucktur](../support/support_brim_enable.md) und dem [Einzugsturm](../dual/prime_tower_brim_enable.md) hinzufügen. Der [Brim ersetzt die Stützstruktur](../platform_adhesion/brim_replaces_support.md) oder wird  [ nur an Außenseite](../platform_adhesion/brim_outside_only.md) des Modells hinzugefügt.

Wenn ein Raft verwendet wird, können Sie die Haftung weiter erhöhen, indem Sie die [Breite des Rafts](../platform_adhesion/raft_margin.md) vergrößern. Das Raft wird jedoch immer unter dem gesamten Modell gedruckt, da die Schichten übereinstimmen müssen. Wenn die Haftung zwischen dem Modell und dem Raft zu Problemen führt, können Sie den [Luftspalt](../platform_adhesion/raft_airgap.md) zwischen dem Raft und dem Modell verringern. Außerdem können Sie in Erwägung ziehen, die [Linienbreite der Raft-Basis](../platform_adhesion/raft_base_line_width.md) zu erhöhen.


Preventing warping
----
If your print suffers from warping, the contact area between the print and the build plate is greatly reduced. To prevent this, refer to the article on [warping](warping.md). To summarise, these are a few adjustments to make to prevent warping.
* Set the [Initial Layer Bottom Pattern](../top_bottom/top_bottom_pattern_0.md) to concentric.
* Reduce the [Build Plate Temperature](../material/material_bed_temperature.md) and increase the [Build Volume Temperature](../material/build_volume_temperature.md).
* Adjust the model such that there are fewer sharp outer corners on the first layer.

Miscellaneous adjustments
----
These settings can also be adjusted if the normal bed adhesion methods are not sufficient.
* Increase the [Initial Layer Height](../resolution/layer_height_0.md). This offers a bit more room for error, if the build plate is not perfectly level. It also increases the force with which the material is pushed out of the nozzle and onto the build plate.
* Increase the [Initial Layer Line Width](../resolution/initial_layer_line_width_factor.md). Similarly, this pushes the material out with more force, sticking it well to the build plate.
* Increasing the [Printing Temperature Initial Layer](../material/material_print_temperature_layer_0.md) makes the material flow out more onto the build plate, increasing contact area.
* Like increasing the temperature, you can also reduce the [Initial Layer Fan Speed](../cooling/cool_fan_speed_0.md) or increase the [duration of that setting](../cooling/cool_fan_full_at_height.md) to keep the material fluid for longer.
* Similarly, reduce the [Initial Layer Speed](../speed/speed_layer_0.md). Reducing the [Initial Layer Print Speed](../speed/speed_print_layer_0.md) makes the material flow out more again, as the material is kept fluid for longer by the hot nozzle. Reducing the [Initial Layer Travel Speed](../speed/speed_travel_layer_0.md) reduces the chance that a travel move pulls previously printed lines off the build plate. Likewise, consider adjusting the [Initial Layer Acceleration](../speed/acceleration_layer_0.md) and [Initial Layer Jerk](../speed/jerk_layer_0.md) as well. 
* Increase the [Number of Slower Layers](../speed/speed_slowdown_layers.md). This reduces the chance that fast movements pull off the previous layers.

Build plates
----
Aside from a good print, a good build plate is important for adhesion as well. A good build plate should be:
* ...clean! It's very important that the build plate contains no grease (such as from your fingers) and no dust. Cleaning it under a hot tap is very effective. Using some rubbing alcohol and a microfibre cloth is ideal.
* ...level! If the build plate is too close, the flow out the nozzle will be inconsistent, resulting in bumps that the nozzle will tear off when it comes around next time. If the build plate is too far, the material is not pushed well onto the build plate, which reduces surface area greatly. Most printers allow adjusting the build plate with some thumb screws, so make sure that it is perfectly level and spaced correctly from the nozzle.
* ...rough! With a slightly roughened build plate, the contact area between the build plate and the print is greatly increased as opposed to a perfectly smooth build plate. Some printers come with frosted glass or anodised metal for this reason.

The material of the build plate also has a big impact on the adhesive properties. This can differ greatly with different print materials. Common build plate materials are glass, acrylic, aluminium, steel or anodised aluminium. Each of these stick to different materials. Plastic build plates may stick chemically to your material. Other materials rely on a rough surface to increase the contact area.

There are also add-on bed adhesion methods you can apply to any build plate:
* Generic paper glue sticks work very well. Although the glue dries up quickly, it produces a rough surface with increased surface area for the print to stick to.
* Masking tape has a similar effect, since it has a rough surface made of paper, but unlike paper it stays perfectly flat on the build plate. The thicker types of masking tape made for outdoor use are most effective.
* Hair spray works similar to glue in that it leaves a finely grained rough surface on the build plate. It's very easy to apply this evenly.
* Apply some sandpaper to the build plate to roughen it up and increase the contact area. Don't roughen it up too much though, or you'll have an uneven surface to print on. Use very fine-grained sand paper to do this, of grit 500 or more.
* Specialised "adhesion sheets" are sold by many 3D printer vendors, which can be stretched over the build plate. They function similarly to masking tape, but are made to last longer. Some are made out of a plastic that bonds chemically to the printed material as well.