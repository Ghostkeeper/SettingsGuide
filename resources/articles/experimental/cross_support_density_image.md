Cross Fill Density Image for Support
====
In this setting, you can provide an image that specifies the density in various places across the support. The support density will vary in certain places depending on the brightness of the image. This only works for the [Cross pattern](../support/support_pattern.md), since that pattern is able to adjust its density without chopping up lines, which would result in interrupted flow and reduced strength.

![The support density is greater at the sides](../images/cross_support_density_image.png)
![The image file used to create that pattern](../images/cross_support_density_image_mask.png)

The path to the image is provided as a local path, for instance `C:\Projects\3D Printing\support_density.png` on Windows or `/home/ghostkeeper/3d_printing/support_density.png` on Unix. Supported file formats are JPG, PNG, TGA, BMP, PSD, GIF, HDR and PIC. Image is scaled over the print such that it fits the bounding box of the printed scene exactly. The brightness in the image determines the support density:
* Where the image is black, the [support density](../support/support_infill_rate.md) is used.
* Where the image is white, the support density will approach 0%.

The support density will never exceed the value specified by the [support line distance](../support/support_line_distance.md). It can only be reduced. The pattern is also limited in where it can reduce its density. While it tries to approximate the desired support density as closely as possible, this is not always possible. If the support density is really low, there will be particularly few opportunities to adjust the support density, causing the print to follow the image very loosely. In places where the support density is high, the image will be followed very closely. The chosen density is heavily quantised as well. The density can only be doubled or halved, but Cura will [dither](https://en.wikipedia.org/wiki/Dither) the pattern in order to achieve a greater effective accuracy.

With this setting, you can customise your support very far. If certain parts of your print are prone to sagging or need to be printed very accurately, you can locally increase the density there to support them better, without having to take a big hit in printing time or making it harder to pull the support off.  

**This setting will not transfer well through Cura project files. The project file will store the path to the image as the setting value, but will not store the image. If the project file is opened on a different computer, the density image will likely not be restored.**