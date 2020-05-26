Is Center Origin
====
If this setting is enabled, the 0,0 coordinate of the printer is set to be in the middle of the build volume, rather than the front left corner.

In some printer the firmware considers the 0,0 coordinate to be in the centre of the build volume. This is common for delta-style printers, which generally have cylindrical build volumes rather than cuboids.

If the zero coordinate of the printer is in the centre, then the final g-code will contain negative coordinates as well as positive coordinates. The coordinate origin will be in the middle of Cura's build volume. Cura will also show its tricolor coordinate marker in the centre. However the coordinates of 3MF files will still be treated as if the coordinate origin is in the front-left corner of the printer, since the 3MF file format requires this.

**Since this is a machine setting, it will not normally be listed in the normal list of settings. There is a checkbox for this setting though in the printer settings dialogue, which can be found in the list of added printers in the preferences dialogue.**