This setting determines how far before the end of the contour the feeder will stop feeding material. The length of coasting is configured however in a volume of material. It is more closely related to the volume inside the nozzle chamber.

![Coasting 0.2mm³ of material](../../../articles/images/coasting_enable.png)
![Coasting 0.1mm³ of material](../../../articles/images/coasting_volume_0_1.png)

Increasing the coasting volume causes the nozzle to stop extruding farther before it's finished the contour. The result is that it'll have more underextrusion towards the end. The function of coasting is to compensate for the blob when the contour is seamed, so increasing the coasted volume can compensate for bigger blobs.

However increasing the coasted volume too much will cause harsh underextrusion towards the end of the contour. It can even lead to some underextrusion in whatever is printed after the contour, since the pressure on the nozzle is still low then.