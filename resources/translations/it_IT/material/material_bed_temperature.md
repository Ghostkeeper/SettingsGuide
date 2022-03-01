Build Plate Temperature
====
Some printers have a heated build plate. This setting determines how warm the build plate will become.

Heating the build plate will keep the material slightly fluid and sticky. Some materials will form crystals upon freezing, which causes the material to shrink significantly upon freezing. The heated bed keeps the material just above freezing temperature to prevent this shrinkage and to maintain the stickiness of the liquid plastic. This is all meant to improve the adhesion of the print to the build plate.

However if the build plate is kept too hot, the print will be very fluid where it touches the build plate. This causes the material to sag a bit, causing [elephant's foot](../troubleshooting/elephants_foot.md) on the bottom side of the print. This can be compensated for with the [Initial Layer Horizontal Expansion](../shell/xy_offset_layer_0.md) setting, but affects dimensional accuracy. Heating the build plate will also create a temperature difference between the material which is resting on the build plate, and the material higher up in the model, which causes [warping](../troubleshooting/warping.md) when the higher up material starts to shrink.

If this setting is set to 0 degrees, Cura will not output any commands to change the build plate's temperature, which could confuse the firmware if there is no build plate.

**When you adjust the build plate temperature in a material profile, this will adjust the [Default Build Plate Temperature](default_material_bed_temperature.md) setting. Normally the Build Plate Temperature will be equal to the Default Build Plate temperature, but sometimes choosing a different quality can make slight adjustments to the build plate temperature. This Build Plate Temperature setting is the one that actually gets used for the print.**