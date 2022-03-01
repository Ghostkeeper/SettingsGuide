Scaling Factor Shrinkage Compensation
====
<!--if cura_version >= 4.8-->This setting effectively scales the model before slicing automatically. The aim is to compensate for any shrinkage that happens when the print cools down to room temperature. By making the print slightly bigger than desirable, the final result could be more accurate to the original dimensions of the input model. This scaling factor is applied equally to all dimensions (X, Y and Z).

The entire scene gets scaled from its centre. When printing multiple models, all of them get scaled from the same origin point. This allows you to position those models very close together, without having them overlap in the final print. The collision areas of the models are scaled along, so that you can see exactly where your print will end up. This will also prevent you from placing models in the scene in locations where they would collide with features of the print or the printer, like the prime tower or the clips of the build plate.

A factor of 100% will not cause any scaling. A scaling factor of slightly more than 100% is appropriate for many engineering materials such as ABS or polypropylene. A scaling factor of less than 100% would indicate that the material grows when cooling, like a foam perhaps.

Purely chemical data on how much a material shrinks between printing temperature and room temperature is not enough to predict a good value for this setting, because the printing process influences shrinkage too. When extruded in a line, the plastic is stretched in the direction of the length of the line, and shrinks more in that axis. The shrinkage is not uniform, but this setting only applies a uniform scale factor in all directions. To get accurate results, you need to apply the scaling factor on the axis that is most important to your application. If there are a lot of long, straight lines along the dimension that is most important, the scaling factor will need to be bigger.

If the scaling factor is greater than 100.5% and you are printing something big, Cura will display a warning that you might start to experience [warping](../troubleshooting/warping.md).<!--endif-->

<!--if cura_version < 4.8:This is a descriptive setting, letting Cura know how much the material shrinks when it cools down from the printing temperature to room temperature.

This setting is currently not used for slicing. It is currently only used to display a warning to the user when printing large things if the shrinkage ratio is larger than 0.5%.
-->
**This setting is not visible in the list of settings. It is only an internal setting to be overwritten by the material profile.**