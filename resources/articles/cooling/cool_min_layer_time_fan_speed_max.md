Regular/Maximum Fan Speed Threshold
====
This setting determines the printing time of the layer at which it is so short that the fan speed will start increasing towards the [Maximum Fan Speed](cool_fan_speed_max.md). Layers that take longer to print than this will use the [Regular Fan Speed](cool_fan_speed_min.md). Layers that take shorter to print will have their fan speed interpolated between the Regular and the Maximum Fan Speed settings, up towards the [Minimum Layer Time](cool_min_layer_time.md) where the fan speed will be at the Maximum Fan Speed.

![Which fan speed is used where](../images/cool_fan_speed.svg)