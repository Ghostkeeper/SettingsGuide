Regular Fan Speed at Height
====
The fan speed will start at the value of the [Initial Fan Speed](cool_fan_speed_0.md) setting at the beginning of the print. During the first few layers of the print up until it has reached the height specified in this setting, the fan speed will gradually be increased to the [Regular Fan Speed](cool_fan_speed_min.md).

![Which fan speed is used where](../images/cool_fan_speed.svg)

Normally the Initial Fan Speed is lowered considerably because the initial layer needs to stay hot during the print. If the initial layer cools down, the material will start to [warp](../troubleshooting/warping.md). This pulls the first layer off the build plate, which makes the print fail. However if the second layer cools down too quickly, it'll still shrink and through shear friction pull the first layer up, warping the print as well. The purpose of this setting is to allow printing multiple layers with a lower fan speed. This way, the warping can be prevented until the print has sufficient stiffness to resist the warping.

Simply reducing the fan speed during the first few layers would create a sharp change in fan speed which would be visible in the surface quality of the final print. This creates banding. Instead, the fan speed is gradually changed towards the regular fan speed.

* Increasing this setting can improve [bed adhesion](../troubleshooting/bed_adhesion_problems.md).
* If your build plate is heated to a high temperature, you might need to reduce this setting in order to prevent [elephant's foot](../troubleshooting/elephants_foot.md) or oozing.