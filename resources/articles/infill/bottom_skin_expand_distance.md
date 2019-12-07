Make the solid layers on the bottom of your print wider or thinner in a horizontal direction. Normally the solid layers are only generated above parts where there is air beneath them, but with this setting you can expand it horizontally a bit further, improving strength by making the skin attach better to adjacent walls and closing gaps in the skin.

![How skins (the yellow parts) normally look](images/expand_skins_expand_distance_original.png)
![Skins expanded by 1mm](images/expand_skins_expand_distance_1mm.png)

* If you have small holes in the bottom layers of the skin (holes that are filled with the infill pattern), setting this a bit higher will close them. This allows the printer to continuously print bottom lines, greatly improving strength.
* If you have a bottom side that is not directly on the build plate there will be walls beneath the skin. This will enhance the adhesion between the bottom layers and its nearby walls because the bottom layers will be printed directly on top of the walls.
* Setting this setting to a negative value will reduce the width of the bottom layers, replacing it with infill. This can save some printing time, at the cost of strength.

**Due to technical limitations, you can't reduce this setting negatively below the value of [Bottom Skin Removal Width](bottom_skin_preshrink.md). Increase the Bottom Skin Removal Width setting in order to remove more skin.**