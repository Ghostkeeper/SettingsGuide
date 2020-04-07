Gantry Height
====
This setting measures the distance between the build plate and the gantry system to which the print head is suspended. This height is a ceiling when you're printing [one object at a time](../blackmagic/print_sequence.md), since previously printed object could collide against the gantry.

![Dimensions of the print head](../images/head_dimensions.svg)

Most 3D printers have their print head hanging on a cross bar or two. The shape of this gantry is not modelled by Cura: whether it's two crossing bars, a single arm coming in from one direction or a single crossbar along which the print head can move in one direction. Cura sees this gantry as a hard ceiling when printing one at a time, regardless of which order the models are printed in. When printing one at a time, the height of the build volume is lowered to this gantry height, to indicate that no models higher than the gantry height are allowed.

One exception is when only one object is loaded on the build plate. This object is allowed to be higher than the gantry height since there will be nothing else on the build plate that can collide with the gantry then.

*Since this is a machine setting, it will not normally be listed in the normal list of settings. The gantry height can be changed in the printer settings dialogue, which can be found in the list of added printers in the preferences dialogue.*