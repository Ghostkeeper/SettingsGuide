Skin Removal Width
====
This setting will remove very thin strips of skin, replacing them with infill instead.

The skin will only be removed if there is infill next to it, so it won't normally remove the skin at the very top or bottom of your print, even if that is very thin.

![Not removing any skin](../images/skin_preshrink_original.png)
![Thin strips are removed](../images/skin_preshrink_shrunk.png)

Skin will normally get generated anywhere that is vertically close to the top or bottom of the object. This is not necessary everywhere. Vertical walls are usually strong enough, so while there should normally be skin next to vertical the vertical walls, this setting allows you to omit that. This saves on printing time and material.

If the setting is increased too much, gaps can appear in the top and bottom surface where infill gets exposed. In particular, take good care with models that have thin ledges that should get a thin strip of skin.