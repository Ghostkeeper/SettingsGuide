Z Hop Speed
====
This setting configures the movement rate at which the vertical movements are made in a Z Hop. The horizontal movements of a Z Hop are unaffected, since those are configured by the [Travel Speed](speed_travel.md).

![The vertical movement is made at the Z Hop Speed](../images/speed_z_hop.svg)

<!--if cura_version >= 4.2-->The Z Hop Speed is also used as the speed of the travel move between layers. In practice, this speed matters very little since the movement of a single layer thickness is so short that it is almost always limited by acceleration, not the maximum cruise speed.<!--endif-->

For most printers, the Z axis is built to be sturdy but slow. Increasing the Z Hop Speed will test the limits of the Z movement, which can cause the Z motor to skip some steps. As a result, the nozzle could end up at a different height after the Z hop. Reducing this speed reduces the chances of that happening.

On the other hand, a greater Z Hop Speed will make the nozzle move away from the printed surface more quickly. This can reduce the size of blobs.

Due to low Z-axis acceleration rates, it is uncommon that the desired Z Hop Speed is reached unless the Z Hop height is very high or the speed very low.