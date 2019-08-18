This setting allows you to change the direction in which the lines of the top and bottom are printed. You can specify a comma-separated list of angles (in degrees), and the lines will alternate directions per layer.

![Lines pattern with 0°, 60° and 120° angles alternating](images/skin_angles.gif)

By default, the lines pattern prints in the two diagonal directions. For Cartesian gantry systems this is the most accurate, because the printer can use both the X and Y motors to accelerate the nozzle when turning around for the next line.

There can be several reasons to change these directions:
* To achieve an optical effect.
* To optimise strength. The print will normally be tougher when subjected to push and pull parallel to the skin (and infill) lines.
* To reduce overhang. If a print is very thin in one direction, making the skin bridge that direction can be an effective way to save material on infill. No infill will be necessary to bridge the gap. Similarly, you can also choose a direction that is perpendicular to the infill in order to minimise overhang over infill. This can achieve a better top surface quality.
* To optimise accuracy if your printer does not have one motor for the X direction and one for the Y direction, such as a printer with an H-bridge gantry or a delta printer.

Multiple numbers can be entered to change the direction in each layer. For example, entering `[0, 30, 60]` makes it alternate between 0 degrees away from the X axis, 30 degrees away and 60 degrees away.