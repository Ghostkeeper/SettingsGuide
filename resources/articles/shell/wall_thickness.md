This setting determines how thick the wall around the print will be. Ultimately it adjusts the number of inner walls to achieve the desired thickness.

![0.8mm thick walls](images/wall_thickness_0.8.png)
![1.6mm thick walls](images/wall_thickness_1.6.png)

The wall thickness must be a multiple of the wall line width. If it is not, it will be rounded to be an exact multiple. Keep in mind though that one of the walls will be an outer wall, and the rest will be inner walls. These walls can have different line widths.

The thickness of the walls is a major factor in how strong the print will be. Since the walls are adjacent, they can reinforce each other leading to a stronger part. For larger prints, this can be a much more effective way to get a strong object than adjusting the infill, depending on the shape.

Increasing the wall thickness will:
* Greatly increase the strength of the print.
* Reduce the shine-through effect where the infill pattern is visible on the outside.
* Improve overhangs, because the wall lines are usually more oriented towards their nearest resting point.
* Make the model watertight more easily.
* Greatly increase the printing time and material usage of the print.