Normally, Cura will create cross sections of all the triangles in your mesh. These line segments are stitched together to form loops. Any loops that are not closed will be discarded.

This setting controls what will be done with these unclosed loop. If set to "Normal", they are discarded. If set to "Surface", all of the cross sections are printed as outlines. If set to "Both", the closed outlines are printed normally but the unclosed ones are printed separately as extra walls.

![Normal mode leaves out the single unclosed surface on the right](magic_mesh_surface_mode_normal.png)
![Surface mode only prints the surfaces without treating them as closed volumes](magic_mesh_surface_mode_surface.png)
![Printing both the volumes and the extra unclosed surface on the right](magic_mesh_surface_mode_both.png)

The extra surfaces that get printed will only include the vertical surfaces as single lines. There is no filling technique for horizontal surfaces, since the surfaces are not closed polygons. They cannot be filled since there is no inside. There can be no tops, bottoms, infill or supports. Only single lines.

The extra surfaces will be printed as if they are outer walls, so they will be affected by the outer wall printing speed, line width, and so on.

*If printing both the normal volumes and the extra surfaces, keep in mind that the volumes will be printed with the outer wall completely inside the volume. The extra surfaces are printed with the line centred on the surface, with half of the line's width on either side. If an extra surface is aligned to the surface of a closed volume, as in the pictures above, the surface will be shifted by half a line width. After all, the extra surface has no inside to move towards.*