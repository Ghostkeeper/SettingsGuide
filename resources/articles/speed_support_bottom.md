This setting configures the speed at which the bottom side of the support is printed, if [Support Floor is enabled](support_bottom_enable.md).

![Various structures printed at different speeds](images/speed_difference.png)

A higher speed can save some printing time.

The effect of this setting greatly depends on circumstances. With some materials, in particular materials that cool quickly and with a large [Support Bottom Distance](support_bottom_distance.md), greater speed will increase the adhesion between the support and the model. The effect is similar to bridging: At greater speeds, the material is less carefully suspended and doesn't get time to get cooled by the fans on the print head. This is something you don't normally want, because it will cause the support to leave a greater mark on your surface.

With other materials, greater speed reduces the force with which the material is put down and doesn't allow it to flow out much. This effect is similar to bed adhesion. The greater speed is then only advantageous until you start reaching the limits of the change in flow rate that occurs at the start and end of the support floors.

If the support floor is very close to the model, such as for PVA or other soluble support materials, increasing the support floor speed can also cause the nozzle to overshoot into the model, marring the surface slightly.