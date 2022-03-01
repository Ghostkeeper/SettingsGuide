Regular/Maximum Fan Speed Threshold
====
This setting determines the printing time of the layer at which it is so short that the fan speed will start increasing towards the [Maximum Fan Speed](cool_fan_speed_max.md). Layers that take longer to print than this will use the [Regular Fan Speed](cool_fan_speed_min.md). Layers that take shorter to print will have their fan speed interpolated between the Regular and the Maximum Fan Speed settings, up towards the [Minimum Layer Time](cool_min_layer_time.md) where the fan speed will be at the Maximum Fan Speed.

![Which fan speed is used where](../images/cool_fan_speed.svg)

Effectively, reducing this threshold (towards shorter layers) will cause the fan to spin at the regular fan speed more often. Increasing this threshold will cause the fan to spin at greater speeds more often, even if the layers aren't very small.

It is good to keep some distance between the Minimum Layer Time and this Regular/Maximum Fan Speed Threshold. If the threshold is set to be at the Minimum Layer Time, the fan will abruptly stop if the layers become slightly below the threshold. This causes visible banding across the surface of the print, since there is a hard border where the fan suddenly flared up. If instead there is some difference between the two settings, the change in fan speed will be more gradual and the banding won't be visible in the print.