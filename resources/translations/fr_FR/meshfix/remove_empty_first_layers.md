When enabled, any empty layers on the bottom side of the print will be removed. The entire print will move down until it rests on the build plate. Instead of having empty layers which cause the print to fail, the print will be slightly lower.

If the Cura preference to "Automatically drop models to the build plate" is enabled, this setting will likely have very little effect. It can still have an effect though. When automatically dropping models down to the build plate, the models are aligned exactly with the build plate. However, if the first layer(s) contain only features that are too small to print (perhaps due to the bottom not being entirely smooth) the first layer may still be empty in the final print. This setting will prevent that by moving the rest of the layers one down.

After moving the print down, the settings that apply to the first layer are still applied. So even though the original first layer is removed, the [Initial Layer Print Temperature](../material/material_print_temperature_layer_0.md) and similar settings are still applied to the new first layer.

Normally this setting should always be enabled to prevent prints from failing due to not being entirely smooth on the bottom or being improperly aligned to the build plate. However you might choose to disable this setting if you're making a print job with multiple stages that needs to start in mid-air.

If [support is enabled](../support/support_enable.md), that support will extend all the way to the build plate, making the first layers not empty any more. No layers will get removed and the print will not move downwards.

If the [Slicing Tolerance](../experimental/slicing_tolerance.md) setting is set to "Exclusive", the first layer will always be empty. If this setting is not enabled then, the first layer will actually be empty and your print will most likely fail.