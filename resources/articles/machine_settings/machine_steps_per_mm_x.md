Steps per Millimeter (X)
====
Most 3D printers use stepper motors to move the print head around the build volume. These motors rotate in steps, and have difficulty staying between two positions of the steps. The steps are essentially the resolution of the printer. This setting indicates that resolution: How many steps of the motor would result in one millimetre of movement in the X direction?

This does not apply for printers that don't control motion in the X direction with a separate motor (such as delta-style printers) or that don't use stepper motors to move the print head in the X direction.

This setting is not used in Cura at all. However it is used by the X3Gwriter plug-in to output X3G files with correct step sizes.

**Since this is a machine setting, this setting is not normally visible in the settings list.**