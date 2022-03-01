Wipe Nozzle Between Layers
====
This setting enables a procedure that gets executed at the end of every layer to wipe off any material from the nozzle tip. If you have a printer with a built-in wiping brush, enabling this setting will cause Cura to instruct the printer to periodically wipe the nozzle off on that brush.

![Visualisation of the movements in the wiping procedure](../images/clean_between_layers.svg)

This wiping procedure consists of a number of steps:
1. If [retraction is enabled](wipe_retraction_enable.md), the material is retracted.
2. If [Z-hop is enabled](wipe_hop_enable.md), the nozzle is moved up or the build plate down.
3. The nozzle is moved beyond the [position of the brush](wipe_brush_pos_x.md).
4. The nozzle is wiped [a number of times](wipe_repeat_count.md) on the brush.
5. The nozzle is moved back to its original position.
6. The Z hop is ended, if it was enabled. The material unretracts.
7. The print pauses for a [certain period](wipe_pause.md).

The aim of this procedure is to clean the nozzle periodically of any debris. Some materials tend to creep up to the nozzle with capillary action due to high surface tension. This can creep into the print head and collect there, which may break the print head apart. Other materials containing fibres or other fillings may cause the filling to be sprayed onto the nozzle during printing. This will wipe that material off.

The wipe procedure is not very configurable now though. It always wipes in the X direction, keeping the Y position of the last position in the print. This means that a printer with a brush in a corner is not going to work well with this function. You'd need a brush along an entire side of the build volume.