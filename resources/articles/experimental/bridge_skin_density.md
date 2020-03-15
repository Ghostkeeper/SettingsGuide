Bridge Skin Density
====
This setting controls the density of the bottom side of the print where it bridges a gap. At 100% density, the lines are placed directly adjacent. At lower densities, the lines are spaced further apart.

![At 100% density, the lines are placed directly adjacent to one another](../images/bridge_skin_density_100.png)
![At 50% density, there is some spacing between the lines](../images/bridge_skin_density_50.png)

There are two major effects at play when tuning this setting: Adhesion between lines and cooling.

When spacing the skin lines directly adjacent to each other, they will stick to one another. This will make the bottom side of the bridged gap look nicer, since the surface will be continuous instead of stringing. Additionally, the second line can lean on the first line a bit while bridging, which makes the bridge sag a bit less.

However there is another effect and that is cooling. When the lines are spaced further apart, they will be able to cool down faster and then won't sag as much either. Of course, this only applies when the fan is turned on, so for high temperature materials this strategy is not going to work.

Which of these effects is stronger depends on the viscosity of the material, how fast it solidifies and on the fan speed. Some tuning is always required.

**If the [Bridge Skin Flow](bridge_skin_material_flow.md) is less than 100%, there will also be some spacing between the lines even if the density is 100%, because the lines will be thinner then.**