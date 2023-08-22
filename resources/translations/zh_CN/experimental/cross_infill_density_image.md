交叉填充密度图像
====
在此设置中，可以提供一个图像，用于指定填充中各个位置的密度。填充密度在某些地方会有所不同，具体取决于图像的亮度。该设置仅用于 [交叉3D](../infill/infill_pattern.md)填充图案，因为该填充图案能够在不截断线条的情况下调整其密度，而截断线条将导致流量中断和强度降低。

<!--screenshot {
"image_path": "cross_infill_density_image.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cross_3d",
"infill_sparse_density": 101,
"cross_infill_density_image": "{root}/resources/articles/images/cross_infill_density_image_mask.png"
},
"colours": 32
}-->
![对象内的填充密度各异](../images/cross_infill_density_image.png)
![用于创建该图案的图像文件](../images/cross_infill_density_image_mask.png)

图像的路径以本地路径的形式提供, 例如在windows下的"C:\Projects\3D Printing\infill_density.png" 或 Unix下的"/home/ghostkeeper/3d_printing/infill_density.png"。支持的文件格式包括JPG、PNG、TGA、BMP、PSD、GIF、HDR和PIC。图像将在整个对象上缩放，使其完全适合对象的边界框。图像中的亮度决定填充密度：
* 如果图像为黑色，则使用 [填充密度](../infill/infill_sparse_density.md)。
* 如果图像为白色，填充密度将接近0%。

填充密度永远不会超过由[填充走线距离](../infill/infill_line_distance.md)指定的值。它只能被减少。该图案还受限于其可以降低其密度的地方。虽然它试图尽可能接近所需的填充密度，但这并不总是可能的。如果填充密度真的很低，则调整填充密度的机会特别少，从而导致打印件非常松散地跟随图像。在填充密度高的地方，图像将被非常紧密地跟随。所选择的密度也被大量量化。密度只能加倍或减半，但Cura将[抖动图案](https://en.wikipedia.org/wiki/Dither)，以实现更高的有效精度。

使用此设置，您可以更好的定制填充。由于十字填充图案大多数用于柔性材质，因此该设置用于实现非常特定的柔度或硬度约束。例如，人们可以打印一个鞋底，定制柔软度，以更好地适合脚，或一个机械装置，必须在特定的部分弯曲。

** 此设置不能很好地通过Cura项目文件进行传输。项目文件将把图像的路径存储为设置值，但不存储图像本身。如果在其他计算机上打开项目文件，密度图像可能无法恢复。**
