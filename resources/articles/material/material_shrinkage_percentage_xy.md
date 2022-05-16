Horizontal Scaling Factor Shrinkage Compensation
====
This setting scales the model automatically before slicing, in the horizontal direction. The aim is to compensate for any shrinkage that happens when the print cools down to room temperature. By making the print slightly bigger than desirable, the final result could be more accurate to the original dimensions of the input model. This scaling factor is applied only to the X and Y directions.

Scaling in the horizontal directions is more important because that is the direction where the internal stresses of the print are the greatest. Typically the horizontal shrinkage is bigger than the vertical shrinkage. The lines being printed horizontally causes the lines to contract more in the horizontal direction than in the vertical direction.

The entire scene gets scaled from its centre. When printing multiple models, all of them get scaled from the same origin point. This allows you to position those models very close together, without having them overlap in the final print. The collision areas of the models are scaled along, so that you can see exactly where your print will end up. This will also prevent you from placing models in the scene in locations where they would collide with features of the print or printer, like the prime tower or the clips of the build plate.

A factor of 100% will not cause any scaling. A factor of slightly more than 100% is more appropriate for many engineering materials such as ABS or polypropylene. A scaling factor of less than 100% would indicate that the material grows when cooling, like a foam perhaps.

Purely chemical data on how much a material shrinks between printing temperature and room temperature is not enough to predict a good value for this setting, because the printing process influences shrinkage too. When extruded in a line, the plastic is stretched in the direction of the length of the line, and shrinks more in that axis.