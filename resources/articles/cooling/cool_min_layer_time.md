Minimum Layer Time
====
The Minimum Layer Time configures the shortest duration of printing a layer that is allowed. The printer is not allowed to print layers any faster than this.

This is necessary in order to allow the previous layer to cool down before the next layer gets put on top of it. This ensures that the previous layer has completely solidified, to prevent sagging.

![Which fan speed is used where](../images/cool_fan_speed.svg)

This setting has three effects:
* If a layer prints faster than the [Regular/Maximum Fan Speed Threshold](cool_min_layer_time_fan_speed_max.md) setting indicates, the fan speed will be increased towards the [Maximum Fan Speed](cool_fan_speed_max.md). Once a layer is so small that it takes down to the Minimum Layer Time to print, the Maximum Fan Speed will be used. The fan speed is interpolated between the two.
* If the layer would take less than the Minimum Layer Time to print, the printing speed will be slowed down such that it still takes the Minimum Layer Time.
* If the print head would be slowed down too much (printing slower than the [Minimum Speed](cool_min_speed.md) setting) then the print head will wait at the end of a layer and optionally lift the head up a bit.

There is a trade-off when slowing down the nozzle to allow the layer to cool down better. The Minimum Layer Time is intended to give some time for the material to cool down by slowing down the movement of the print head. During this time, the fans will be blowing at maximum power to cool it down more quickly, but the hot nozzle is also still on the plastic. For very small pieces, the hot nozzle may transfer more heat into the print than what the fans can blow off. This causes the plastic to melt even more than if you were to have no minimum layer time.

When printing relatively cold materials or if the fans on the print head are particularly powerful, the material will tolerate a higher Minimum Layer Time to reduce sagging. If the Minimum Layer Time is set too high, the nozzle will slow down more and more often, which causes blobs and sagging in some places too.