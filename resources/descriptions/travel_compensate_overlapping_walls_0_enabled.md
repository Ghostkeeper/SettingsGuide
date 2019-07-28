When printing very thin parts, opposite outer walls may come close enough together that they overlap. When printing both walls with their normal line width they would overextrude. This setting prevents that overextrusion by reducing the width of one of the lines, preventing this overextrusion and achieving a better dimensional accuracy.

![All lines are extruded with their full width, creating a part that will be too wide](travel_compensate_overlapping_walls_enabled_disabled.png)
![Half of the lines have reduced their width, resulting in a more accurate print](travel_compensate_overlapping_walls_enabled_enabled.png)

The line width of the outer wall that overlaps another outer wall is reduced by the overlapping area. This compensates for the overextrusion.

As described above, this feature tends to improve dimensional accuracy. However, the disadvantage is that the flow rate becomes less even, which causes underextrusion in some places and overextrusion in others. Also, the flow rate can be reduced below the minimum flow rate of the nozzle and extruder set-up, leading to inconsistent flow and beading. To reduce this effect, you can set the [Minimum Wall Flow](wall_min_flow) which will turn some of the thinnest walls into travel moves at the cost of dimensional accuracy.