交叉填充密度图象（支撑）
====
在此设置中，可以提供一个图像，用于指定整个支撑上各个位置的密度。支撑密度在某些地方会有所不同，具体取决于图像的亮度。这仅适用于[交叉图案](../support/support_pattern.md)，因为该图案能够调整其密度而不会截断线条，这将导致流量中断和强度降低。

<!--screenshot {
"image_path": "cross_support_density_image.png",
"models": [{"script": "wide_bridge.scad"}],
"camera_position": [0, 0, 120],
"layer": 79,
"settings": {
"support_enable": true,
"support_pattern": "cross",
"support_infill_rate": 100,
"cross_support_density_image": "{root}/resources/articles/images/cross_support_density_image_mask.png"
},
"colours": 32
}-->
![两侧的支撑密度更大](../images/cross_support_density_image.png)
![用于创建该图案的图像文件](../images/cross_support_density_image_mask.png)

图像的路径以本地路径的形式提供，例如Windows上的"C:\Projects\3D Printing\support_density.png"或Unix上的"/home/ghostkeeper/3d_printing/support_density.png"。支持的文件格式包括JPG、PNG、TGA、BMP、PSD、GIF、HDR和PIC。图像将在打印上进行缩放，使其完全适合打印场景的边界框。图像中的亮度决定了支撑的密度：
* 如果图像为黑色，则使用[支撑密度](../support/support_infill_rate.md)。
* 在图像为白色的情况下，支撑密度将接近0%。

支撑密度永远不会超过由[支撑走线距离](../support/support_line_distance.md)指定的值。它只能被减少。该图案还受限于其可以降低其密度的地方。虽然它试图尽可能接近所需的支撑密度，但这并不总是可能的。如果支撑密度真的很低，则调整支撑密度的机会特别少，从而导致印刷品非常松散地跟随图像。在支撑密度高的地方，图像将被非常紧密地跟随。所选择的密度也被大量量化。密度只能加倍或减半，但Cura将[抖动图案](https://en.wikipedia.org/wiki/Dither)，以实现更高的有效精度。

使用此设置，您可以非常有效的自定义您的支撑。如果打印的某些部分容易下垂或需要非常精确地打印，您可以局部增加密度以更好地支撑它们，而不必在打印时间内承受很大的冲击或使其更难拉下支撑。

** 此设置不能很好地通过Cura项目文件进行传输。项目文件将把图像的路径存储为设置值，但不存储图像。如果在其他计算机上打开项目文件，密度图像可能无法恢复。**
