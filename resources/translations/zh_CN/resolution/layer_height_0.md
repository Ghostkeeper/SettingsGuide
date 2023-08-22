起始层高
====
该设置定义第一层的层高。通常第一层会打印的较厚些，以便更好的粘附在构造板上。调节这个设置不会影响其他层的高度。

<!--screenshot {
"image_path": "layer_height_0.png",
"models": [
{
"script": "rolling_blind_spacer.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [39, 28, 5],
"settings": {"layer_height_0": 0.3},
"colours": 32
}-->
![起始层高比其他层更厚](../images/layer_height_0.png)

增加起始层高，喷头在同样距离下挤出更多材料。这会带来格外的压力，使得材料在填充线宽时向两边分散。这种压力会让材料和构造板粘得更牢。此外还可以弥补热床的不平整。构造板的轻微弯曲可以被起始层的厚度吸收，否则喷嘴可能会在第二层中将其刮掉。

太厚的首层会导致“象脚”问题（首层过分压扁）。 将[起始层水平扩展](../shell/xy_offset_layer_0.md) 设为一个小负值可以防止这种情况。
