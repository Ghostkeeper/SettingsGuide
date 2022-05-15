Flow Equalization Ratio
====
This feature allows you to change the way that your printer will use to adjust the line width: Instead of changing the flow rate of material through the nozzle, the printer will change the speed at which the nozzle moves.

FFF printers are notoriously bad at changing the rate at which material flows out of the nozzle. If the printer changes the speed of the feeder, it takes a fraction of a second before this actually translates into a change of flow rate. By that time, depending on the print speed, the nozzle may already be several millimetres beyond the point where the flow rate should've been adjusted. This is even worse if your printer has the feeder removed from the print head with a Bowden tube in between.

Instead of changing the feed rate, the printer can also change the movement speed of the print head. The print head can accelerate much faster and so could get better control over the width of the line. If the print head speeds up while the flow rate is kept the same, the same amount of material gets stretched over a greater length, which reduces the line width. If the print head slows down, the same amount of material is bunched up in a smaller space, increasing the line width.

This setting is a ratio. It could adjust the flow rate (0%) or the print speed (100%) or a combination of the two. The ratio can even exceed 100%, which means that the flow rate is reduced in order to produce thicker lines, but the speed is reduced even more to compensate.

Increasing this ratio towards 100% means that it uses the speed instead of the flow rate to change the line width, which has the following effects on the print:
* The line width is likely more accurate, improving the dimensional accuracy of the print.
* The flow rate will be kept equal, which makes the print more reliable, especially with exotic materials.
* In some places the print head moves faster, which results in ringing.

This setting only applies to the variations in line width caused by fitting the lines into the width of thin parts and sharp corners. Changes in flow rate due to settings such as different line widths for infill vs. wall will not be compensated for, nor features like bridging or ironing. Printers that implement Linear Advance or similar compensation features should still use those, even if this setting is set to 100%, because flow changes can still occur due to those settings.