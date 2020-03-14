With the Top/Bottom Thickness you can adjust how thick of a solid skin is created on the top and bottom sides of your print.

![Ordinary top/bottom thickness](../images/top_bottom_thickness_0.8.png)
![Much thicker top and bottom sides](../images/top_bottom_thickness_3.png)

This affects both the top and bottom sides of the print. The top and bottom can also be configured individually with the [Top Thickness](top_thickness.md) and [Bottom Thickness](bottom_thickness.md) settings.

If this setting is not a multiple of the layer height, it will get rounded to the nearest multiple. This setting only determines how many top and bottom layers will be generated.

Greater top and bottom thickness will have several effects, beneficial for total quality but detrimental to productivity.
* Your part will be stronger. Greater top and bottom thickness will mean that a smaller part of your print will get filled with the sparse infill pattern. Instead it gets made completely solid.
* The top surface will be smoother. Any pillowing and sagging in the top skin will get smoothed out in the layers put on top.
* It's more likely that your model will be water tight. Both on the top and bottom sides there will be more layers to block water or other fluids from getting in, and to recover from sagging overhangs.
* Your print will use more material, since more layers are filled completely.
* Your print will take longer, since more material must be placed down and these layers are normally printed more slowly than the infill.
