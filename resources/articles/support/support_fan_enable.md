Fan Speed Override
====
This setting causes the fans on the print head to spin at a different rate while the skin that rests on top of support is printed. The speed at which the fans spin is determined by the [Supported Skin Fan Speed](support_supported_skin_fan_speed.md) setting.

Where the model has overhangs, you'll want that to be supported. The part that gets supported should rest on the support but should not stick to it. If the material is too hot, it'll sag a lot and really lean into the support. This makes it stick too much to the support, and reduces the accuracy of the overhang as well. With this setting, you can increase the fan speed for parts where the model is resting on the support. This cools down the material faster, which makes the model stick less to the support and improves the quality of overhangs.

For parts of overhang that do not get supported, there is a similar feature available when the [bridge settings](../experimental/bridge_settings_enabled.md) are enabled.