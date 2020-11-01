Maximum Fan Speed
====
The speed at which the fans in the print head will spin when the layer is printed at minimum layer time. At the minimum layer time, you'll want to cool down the layer as fast as possible to reduce the time it takes for the layer to cool down before your printer puts the next layer on top.

![Which fan speed is used where](../images/cool_fan_speed.svg)

If printing a layer takes somewhere between the [Regular/Maximum Fan Speed Threshold](cool_min_layer_time_fan_speed_max.md) and the [Minimum Layer Time](cool_min_layer_time.md) settings, then the fan speed will be interpolated between the [Regular Fan Speed](cool_fan_speed_min.md) and the [Maximum Fan Speed](cool_fan_speed_max.md). Once the Minimum Layer Time is reached, the Maximum Fan Speed will also be reached. This way the print will be cooled maximally to cool it down as quickly as possible before the next layer gets put on top.