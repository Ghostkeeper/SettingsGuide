Overhanging Wall Speed
====
With this setting, the speed can be adjusted at which [overhanging walls](wall_overhang_angle.md) are printed. The speed is set as a ratio of their normal print speed, which is either the [Outer Wall Speed](../speed/speed_wall_0.md) or the [Inner Wall Speed](../speed/speed_wall_x.md).

Printing overhang at lower speeds can be very effective to reduce droop. This has a number of positive effects on your print.
* The walls get more time to attach to adjacent walls in the previous layer. This helps them stay upright better, which reduces droop.
* If your fan speed is set up high, the fans get more time to cool down the filament. This makes it solidify faster. If the printing speed were high, the material gets more time to droop down.
* The material in the overhang is still connected to a bead coming out of the nozzle. When printing slower, the nozzle stays closer during the solidification, meaning that the pull of the nozzle on the material is more effective to keep the bead up high while it's solidifying.

However printing overhang at lower (or different speeds can also have negative effects):
* The print will obviously take longer to complete.
* The border where the print speed is different may be very visible on the outside. This introduces a visible border in your print which may not be desirable.
* When reducing speed, there will briefly be some overextrusion out the nozzle due to high pressure in the nozzle chamber. This can lead to blips or make the overhang quality worse. When increasing speed, there will be some underextrusion. In general this technique works better for large areas of overhang rather than small ones.