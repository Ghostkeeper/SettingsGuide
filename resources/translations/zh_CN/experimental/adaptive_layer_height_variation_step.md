自适应图层变化步长
====
如果一个层的所需层厚度与相邻层的所需层厚度相差很大，则喷嘴的流量速率将有很大的差异，这会导致挤出过度或挤出不足。此设置可确保图层厚度的差异是逐渐变化的，以防止出现上述情况。使用此设定，您可以指定两个相邻图层之间图层厚度的最大变幅。

<!--screenshot {
"image_path": "adaptive_layer_height_variation_step_0_05.png",
"models": [{"script": "barn.scad"}],
"camera_position": [-108, -229, 118],
"settings": {
"adaptive_layer_height_enabled": true,
"adaptive_layer_height_variation_step": 0.05,
"layer_height": 0.2
},
"colour_scheme": "layer_thickness",
"colours": 128
}-->
<!--screenshot {
"image_path": "adaptive_layer_height_enabled.png",
"models": [{"script": "barn.scad"}],
"camera_position": [-108, -229, 118],
"settings": {
"adaptive_layer_height_enabled": true,
"layer_height": 0.2
},
"colour_scheme": "layer_thickness",
"colours": 128
}-->
![较大的步长允许非常突然地更改图层厚度](../images/adaptive_layer_height_variation_step_0_05.png)
![较小的步长要求图层厚度的变化更平滑](../images/adaptive_layer_height_enabled.png)

减小此设置将强制层厚度更平缓地过渡。这会对打印产生许多影响：
* 当过渡到较低的层厚度时，将存在较少的挤出过度，因为从喷嘴流出的流量具有一些时间来调节到较低的流率。这样可以防止曲面上出现斑点。
* 类似地，当过渡到更大的层厚度时，将存在更少的挤出不足，因为从喷嘴流出的流量可逐渐调节到更大的流率。
* 条带将不太明显。即使具有不同层厚度的区域仍将具有不同的纹理和颜色，但这些区域现在相距较远，这使得更难看到。
* 如果模型中有一个锐角会导致突然过渡到更薄的层，地貌效应将再次出现。这是因为不允许对层厚度进行那么快的调整，因此必须对浅表面使用较厚的层。
* 同样地，如果模型中有一个锐角会导致突然过渡到较厚的层，打印机将创建不必要的薄层，从而在不必要的地方浪费打印时间。

由于"自适应图层"算法的实现，渐变到不同图层厚度将始终发生在引发转换的模型角度 *之上*。
