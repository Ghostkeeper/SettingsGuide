Regular Fan Speed at Height
====
The fan speed will start at the value of the [Initial Fan Speed](cool_fan_speed_0.md) setting at the beginning of the print. During the first few layers of the print up until it has reached the height specified in this setting, the fan speed will gradually be increased to the [Regular Fan Speed](cool_fan_speed_min.md).

![Which fan speed is used where](../images/cool_fan_speed.svg)

Normally the Initial Fan Speed is lowered considerably because the initial layer needs to stay hot during the print. If the initial layer cools down, the material will start to [warp](../troubleshooting/warping.md). This pulls the first layer off the build plate, which makes the print fail. However if the second layer cools down too quickly, it'll still shrink and through shear friction pull the first layer up, warping the print as well. The purpose of this setting is to allow printing multiple layers with a lower fan speed. This way, the warping can be prevented until the print has sufficient stiffness to resist the warping.

* Increasing this setting can improve bed adhesion.
* Reduce this setting if you find issues with elephant feet or oozing.
* If your build plate is heated to a high temperature, you might need to reduce this setting in order to prevent elephant feet or oozing.