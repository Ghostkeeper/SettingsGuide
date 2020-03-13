The Minimum Layer Time configures the shortest duration of printing a layer that is allowed. The printer is not allowed to print layers any faster than this.

This is necessary in order to allow the previous layer to cool down before the next layer gets put on top of it. This ensures that the previous layer has completely solidified, to prevent sagging.

![Which fan speed is used where](../../../articles/images/cool_fan_speed.svg)

This setting has three effects:
* If a layer prints faster than the [Regular/Maximum Fan Speed Threshold](cool_min_layer_time_fan_speed_max.md) setting indicates, the fan speed will be increased towards the [Maximum Fan Speed](cool_fan_speed_max.md). Once a layer is so small that it takes down to the Minimum Layer Time to print, the Maximum Fan Speed will be used. The fan speed is interpolated between the two.
* If the layer would take less than the Minimum Layer Time to print, the printing speed will be slowed down such that it still takes the Minimum Layer Time.
* If the print head would be slowed down too much (printing slower than the [Minimum Speed](cool_min_speed.md) setting) then the print head will wait at the end of a layer and optionally lift the head up a bit.