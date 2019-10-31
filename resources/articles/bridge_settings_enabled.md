When your model has some overhang that is supported on both sides, Cura will detect this and modify the skin area that is overhanging in order to print better. If this setting is enabled, you can tune the detection of these bridging areas and the resulting behaviour so that it bridge better.

Normally Cura will use a fairly rudimentary bridging technique. Cura will detect overhanging areas of skin that are supported on multiple sides. The [direction of those skin lines](skin_angles.md) is adjusted to bridge those areas automatically. This ensures that the greatest possible part of the overhanging area is supported on multiple sides and improves print quality.

When this setting is enabled though, you can tune that behaviour more precisely according to your requirements. This allows you to tweak:
* printing speed
* flow rate
* density (like infill density, but with the skin lines)
* fan speed

These settings can be adjusted separately for the skin that bridges a gap as well as for the walls. If [Bridge Has Multiple Layers](bridge_enable_more_layers.md) is enabled, they can also be adjusted separately for the second and third layer above the bridged gap. It also allows tweaking which parts of the print are seen as bridging areas, by tuning [what fraction of an area must be over air](bridge_skin_support_threshold.md) and a [minimal width for the walls](bridge_wall_min_length.md).