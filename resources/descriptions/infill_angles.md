Infill lines are usually directed at a 45 degree angle as much as possible. At this angle, both the X and Y motor work together to obtain maximum acceleration of the print head, when using a printer with the common Cartesian gantry mechanism.

With this setting, you can adjust this angle. You can specialise it to create greater strength for your specific model, or achieve greater acceleration for your specific gantry system (such as for delta printers).
![Lines infill with default angles of 45 and 135 degrees](infill_angles_45_135.png)
![Lines infill with customised angles of 0 and 30 degrees](infill_angles_0_30.png)
The value of this setting needs to be a comma-separated list of angles with brackets around it. An angle of 0 degrees will result in a line parallel with the Y axis. The list of angles will be alternated over the layers.
* The final print will be strongest in the directions of the infill lines. If you need the print to carry a specific force in a horizontal direction, it is useful to orient the infill lines around that direction.
* Leave the setting an empty list to use the default.
* The default depends on the infill pattern:
  * For Cross and Cross 3D infill patterns, the default is [22]. This orients as many lines as possible close to the diagonals.
  * For Lines and Zigzag infill patterns, the default is [45,135]. This causes the orientation to alternate layer by layer between the two diagonals.
  * All other patterns use a default of [45]. This orients as many lines as possible close to the diagonals.