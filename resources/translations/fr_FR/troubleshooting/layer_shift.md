A layer shift occurs when the layers of a print are not properly stacked up on top of each other. If the print head gets shifted during the printing of a layer for some reason, the printer continues printing with an offset. As a result the top side of the print is shifted in relation to the bottom side.

![A single layer shift due to an obstruction](../../../articles/images/layer_shift_single.jpg)

Causes
----
Layer shifts come in two flavours.

One type of layer shift is caused by the print head being obstructed somewhere along the way. This then causes a layer shift in one spot halfway through the print. This could happen due to the user placing something inside the gantry while printing, or when the print head hits another object while printing in [one at a time mode](../blackmagic/print_sequence.md). If the print head collides with something and is unable to move, the motors will skip some steps. If the printer is unable to detect that this happened, it will just continue without that movement, shifting the rest of the print.

Another type of layer shift occurs when the print job itself imposes too much force on the print head, causing the stepper motors of the printer to lose steps. Each time steps are lost, the print is shifted from there on. Typically the lost steps happen in the same place at every layer due to a particularly sharp corner. The result is that the entire print or a certain part of it appears skewed.

Prevention
----
The first type of layer shift is not normally prevented by adjusting Cura. Cura is designed to prevent hitting the sides of the print volume. If the size of the print volume is entered correctly in Cura, it should not generate any g-code that moves outside of the printable volume. If it does generate such g-code, then the Machine Settings dialogue under printer management will allow you to adjust the size of the print volume to make a correction. You should also make sure that there are no obstructions in the print volume that the print head or motion system could hit while printing. Printers can't usually detect that this happens, so they will continue printing from a shifted position. Look for cables that are in the way, and make sure that all cables are long enough to allow the printer's full range of motion. Also see if the stepper drivers on the printer's circuit board are not overheating, which could cause them to stop working temporarily.

The other type of layer shift, the one that happens continuously throughout the print, is likely caused by having too much force on your motion system. There are several possible solutions.

You should first look into your hardware. Are the belts tightened? If not, you can look for a way to tighten them. Some printers have adjustable motor positions that allow you to tighten the belts. Are the pulleys slipping? Tighten the bolts on the pulleys just to be sure. Lastly, a common electrical problem is that the motors don't get sufficient current to generate strong enough forces to make a sharp turn. In that case, check if the power supply is sufficient.

If the hardware is performing well, you can also adjust Cura go a bit easier on the hardware. These are a few settings you can adjust:
* Lower the [jerk rates](../speed/jerk_print.md). This will cause the print head to slow down before making corners. That makes the corner softer, easing into the corner instead of making a hard turn.
* Lower the [acceleration rates](../speed/acceleration_print.md). This will cause the print head to slow down more carefully and longer before making a corner (though the speed at which the print head will go through the apex of the corner will be unaffected; that is the jerk setting's purpose).
* Lower the [travel speed](../speed/speed_travel.md). This reduces the force with which the nozzle skids over previously printed parts.
* Enable [z hops](../travel/retraction_hop_enabled.md). This prevents the print head from hitting previously printed parts if they protrude a bit upwards due to blobs or warping.