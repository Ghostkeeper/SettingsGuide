Build Plate Adhesion Extruder
====
If you are printing extra build plate adhesion structures, such as a brim or raft, this setting determines with which extruder those structures are printed.

* When printing with a material that doesn't stick well to your build plate, it could be useful to use a raft printed with a material that does stick well.
* If you are using only one extruder for your print and it's not the first extruder, this setting will not automatically adjust to using the same extruder as your model. Your print will then still use multiple extruders.

When using the skirt or brim, the [Skirt/Brim Extruder](skirt_brim_extruder_nr.md) completely overrides this setting, although they should be the same by default. When using a raft, the individual components of the raft can get different extruders assigned with the [Raft Base Extruder](raft_base_extruder_nr.md), [Raft Middle Extruder](raft_interface_extruder_nr.md) and [Raft Top Extruder](raft_surface_extruder_nr.md).